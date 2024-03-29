""" Views """
# pylint: disable=no-member

import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Follow, Like


def index(request):
    """ Index View """

    # POST
    if request.method == "POST":
        owner = User.objects.get(id=request.user.id)
        content = request.POST['content']
        Post.objects.create(owner=owner, content=content)
        return redirect('index')

    # Anti-Chronological order
    posts = Post.objects.order_by("-timestamp")

    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Current User Liked Posts
    likes = []
    if request.user.is_authenticated:
        usr = User.objects.get(username=request.user)
        likes = [like_obj.post for like_obj in usr.liking.all()]

    return render(request, "network/index.html", {
        "posts": page_obj,
        "likes": likes
    })


def login_view(request):
    """ Login View """

    # POST
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("index")

        return render(request, "network/login.html", {
            "message": "Invalid username and/or password."
        })

    # GET
    return render(request, "network/login.html")


def logout_view(request):
    """ Logout View """

    logout(request)
    return redirect("index")


def register(request):
    """ Register View """

    # POST
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect("index")

    # GET
    return render(request, "network/register.html")


def profile(request, username):
    """ User Profile """

    # Query the user profile to visit
    try:
        usr = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    # If the requesting user is following the query user
    is_following = (Follow.objects.filter(user1=request.user, user2=usr)
                    if request.user.is_authenticated
                    else None)

    # Anti-Chronological order
    posts = usr.posts.order_by("-timestamp")

    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Current User Liked Posts
    likes = [like_obj.post for like_obj in usr.liking.all()]

    return render(request, "network/profile.html", {
        "owner": username,
        "posts": page_obj,
        "following": usr.following_others.count(),
        "follower": usr.being_followed.count(),
        "is_following": is_following,
        "likes": likes
    })


@login_required(login_url="login")
def follow(request, username):
    """ Follow Other User """

    try:
        usr = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.user != usr:
        follow_obj = Follow.objects.create(user1=request.user, user2=usr)
        assert follow_obj.valid_follow()

    return redirect('profile', username)


@login_required(login_url="login")
def unfollow(request, username):
    """ Unfollow a User """

    try:
        usr = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    follow_obj = Follow.objects.filter(user1=request.user, user2=usr)

    if follow_obj:
        follow_obj.delete()

    return redirect('profile', username)


@login_required(login_url="login")
def following(request):
    """ Show Posts by Followings """

    usr = User.objects.get(username=request.user)
    followed_users = [followed.user2 for followed in usr.following_others.all()]

    # Anti-Chronological order
    posts = Post.objects.filter(owner__in=followed_users).order_by('-timestamp')

    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Current User Liked Posts
    likes = [like_obj.post for like_obj in usr.liking.all()]

    return render(request, 'network/following.html', {
        "posts": page_obj,
        "likes": likes
    })


@csrf_exempt
@login_required(login_url="login")
def edit(request, post_id):
    """ Edit API """

    # Query for requested post
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    # Check Data
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("content") is not None:
            content = data["content"]
            post = Post.objects.get(id=post_id)
            post.content = content
            post.save()

            return JsonResponse({"success": "Done"}, status=200)

        return JsonResponse({"error": "Body needed"}, status=400)

    return JsonResponse({"error": "PUT request required."}, status=400)


@csrf_exempt
@login_required(login_url="login")
def like(request, post_id):
    """ Like API """

    # Query for requested usr and post
    usr = User.objects.get(username=request.user)

    # Query for requested post
    try:
        post_obj = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    # Check Data
    if request.method == "PUT":
        data = json.loads(request.body)
        like_bool = data.get('like')
        if like_bool is not None:

            # Create Like
            if like_bool:
                Like.objects.create(usr=usr, post=post_obj)
                post_obj.likes += 1
                post_obj.save()

            # Destroy Like
            else:
                like_obj = Like.objects.get(usr=usr, post=post_obj)
                like_obj.delete()
                post_obj.likes -= 1
                post_obj.save()
                assert post_obj.valid_like()

            return JsonResponse({"success": "Done"}, status=200)

        return JsonResponse({"error": "Body needed"}, status=400)

    return JsonResponse({"error": "PUT request required."}, status=400)
