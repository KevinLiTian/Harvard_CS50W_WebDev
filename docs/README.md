# Guide

Welcome to learning Web Development!

## Setting Python Environment

It is recommended that [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is used to manage Python packages. First install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), update your `conda` environment, and then create a new `conda` environment with Python 3.9 using the command:

```shell
conda update conda -y
conda create -n AI python=3.9
conda activate webdev
```

where `webdev` is the preferred name of your new environment. You can name it whatever you want. You can turn off the `conda` environment using the command:

`conda deactivate`

## Install Dependencies

Then use `pip` to install all the packages needed which are specified in the `requirements.txt`. It is recommanded to use the command below to install all the packages at once:

`pip install -r requirements.txt --upgrade`

Check out [Sass](https://sass-lang.com/) official website to learn more about its installation

## Clone Repo

Next step is to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository to your local device. [Github Desktop](https://desktop.github.com/) is recommanded, [Git](https://git-scm.com/) command line also works if you are comfortable with it

## What to Learn?

Recommanded to learn in the order of the lectures, from `0.Introduction` to `5.Scale_Secure`. For each lecture:

1. Read and understand the notes, search online for additional information if needed
2. In the `example` directory of each lecture, read, run and understand the code of each program
3. Check the completed projects, read the descriptions, and run them to see what they do. It is recommanded to DIY the projects afterwards, the specifications and release materials of each project are in the `DIY` directory

Learning Web Development is a long road and this is just a beginning, it is normal if you have any difficulties understanding the notes, example codes or the projects. Feel free to contact me if needed through my emails <kevintian.li@mail.utoronto.ca> or <kevin.li20021106@gmail.com>

## Troubleshoot

When you are building your web application, if modifying the CSS or JavaScript then refresh the webpage does not seem to be working, it might be that your browser is **Caching** static CSS and JavaScript, you can solve this by using an incognito window to develop your web application

Learn more about [caching](https://github.com/KevinLiTian/Harvard_CS50W_WebDev/tree/main/5.Scale_Secure#caching)
