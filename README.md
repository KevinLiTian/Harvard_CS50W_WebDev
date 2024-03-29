# Harvard University's CS50W - Web Programming

In the summer after my sophomore year, in order to gain more knowledge and continue programming, I chose to study Harvard's online web programming course, [CS50W](https://cs50.harvard.edu/web/2020/), which I found through the online learning platform, [edX](https://www.edx.org/). Here's my [certificate](https://certificates.cs50.io/d581ea9c-a42f-4f31-85d4-64869276a9ea) after completing the course

In this repository, I am putting my notes and my work on course projects. For each lecture, I will list the objectives of the lecture and corresponding projects. Detailed notes and in-class examples regarding each lecture can be accessed through the link of the corresponding lecture below

Please <strong>DO NOT</strong> directly use the source code, they are <strong>ONLY</strong> for reference. Plagiarism is strictly prohibited by both the Harvard University and the edX platform. See [academic honesty](https://cs50.harvard.edu/college/2021/fall/syllabus/#academic-honesty) and [license](https://cs50.harvard.edu/web/2020/license/) for details

## Course Overview

This course dive deeply into the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap. Topics include database design, scalability, security, and user experience. Through hands-on projects, students learn to write and use APIs, create interactive UIs, and leverage cloud services like GitHub and Heroku. By semester’s end, students emerge with knowledge and experience in principles, languages, and tools that empower them to design and deploy applications on the Internet

### Web Programming

Web programming/development involves front-end development and back-end development. Front-end is the presentation layer, or the user interface (UI), which can be generally summarized by three languages, HTML, CSS and Javascript, where each one plays an important role in the UI. Back-end is the data access layer, or the database where the data is stored and interacted. This course will discuss thoroughly both the front-end and back-end development of web apps and will also introduce framework and database

- **[HTML & CSS](#lecture-0---introduction)**: A markup language used to outline a webpage, and a procedure for making websites more visually appealing
- **[Git](#lecture-0---introduction)**: Used for version control and collaboration
- **[Python](#lecture-0---introduction)**: A widely-used programming language to make websites more dynamic
- **[Django](#lecture-1---django)**: A popular web framework for the backend of websites
- **[SQL](#lecture-2---sql)**: A language used for storing and retrieving data
- **[JavaScript](#lecture-3---js--ui)**: A programming language used to make websites faster and more interactive
- **[UI](#lecture-3---js--ui)**: Methods used to make a website as easy to use as possible
- **[Testing & CI/CD](#lecture-4---testing--cicd)**: Learning about different methods used to make sure updates to web pages proceed smoothly
- **[Scalability & Security](#lecture-5---scalability--security)**: Making sure websites can be accessed by many users at once, and that they are safe from malicious intent

## Get Started

- To setup the environment on your device, please follow the guide in [docs](docs/)
- To practice doing projects, check all the projects with their specifications in [DIY](DIY/)

## Lecture 0 - Introduction

HTML is a markup language that defines the structure of a web page. CSS is used to customize the appearance of a website. They are interpreted by web browsers (Safari, Google Chrome, Firefox, etc.) in order to display content on the screen. Git is a version control tool to help programmers to have better workflows. Python is a popular programming language that has a variety of uses

### Objectives

- [HTML & CSS](0.Introduction/HTML_CSS/)
- [Git](0.Introduction/git/)
- [Python](0.Introduction/python/)

### Projects

- [Search](0.Introduction/search/)

## Lecture 1 - [Django](1.Django/)

Django is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that a lot of code is already written for us that we can take advantage of

### Objectives

- HTTP
- Django Features
- TODO List

### Projects

- [Wiki](1.Django/wiki/)

## Lecture 2 - [SQL](2.SQL/)

[SQL](https://www.w3schools.com/sql/), or Structured Query Language, is a programming language that allows us to update and query database. Django models is an abstraction layer on top of SQL that allows us to only interact with Django without writing SQL commands ourselves. We will also discuss how users can log in/log out of the website

### Objectives

- SQLite
- Django Models
- Users

### Projects

- [Commerce](2.SQL/commerce/)

## Lecture 3 - JS & UI

JavaScript (JS) makes it possible to do client side data processing. Moreover, recall the HTML Document Object Model (DOM) structure, JS gives us the ability to modify the DOM structure and dynamically changing the webpage without communicating with the server. We'll also see how to create an interactive user interface with animation CSS and ReactJS

### Objectives

- [JavaScript](3.JS_UI/JavaScript/)
- [User Interface](3.JS_UI/UserInterface)

### Projects

- [Mail](3.JS_UI/mail/)

## Lecture 4 - [Testing & CI/CD](4.Testing_CI_CD/)

One important part of the software development process is the act of Testing the code we’ve written to make sure everything runs as we expect it to. CI/CD, which stands for Continuous Integration and Continuous Delivery, is a set of software development best practices that dictate how code is written by a team of people, and how that code is later delivered to users of the application

### Objectives

- General Testing
- Web Testing
- Continuous Integration/Delivery

### Projects

- [Network](4.Testing_CI_CD/network/)

## Lecture 5 - [Scalability & Security](5.Scale_Secure/)

As web applications gets larger, and run not only on local machines, but on the internet, scalability and security issues arises. This lecture will discuss some of the common issues and best practices

### Objectives

- Scalability
- Security
- What's Next?

## Final Project

Designing and implementing a web application of your own with Python and JavaScript. The final project is your opportunity to design and implement a dynamic website of your own

- [Requirements](DIY/capstone/)
- [Example](https://github.com/KevinLiTian/EverLove)

## Contact ME

If you have any questions regarding the course material or any of the projects, please feel free to contact me through my email <kevintian.li@mail.utoronto.ca> or <kevin.li20021106@gmail.com>
