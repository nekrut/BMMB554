+++
categories = []
date = "2018-02-21"
#draft = true
menu = ""
tags = ['docker','conda','mapping','variant calling','bwa','freebayes']
title = "Diving into analyses"
+++

# Setting up Jupyter

For our analyses we will be using [Jupyter](http://jupyter.org/). The problem is that everyone in this class has a different computer setup, which may cause issues with running Jupyter. We will solve this using [Docker](https://www.docker.com/) - a lightweight virtualization solution that run equally well on Mac, Windows, and Linux:

>Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allow you to run many containers simultaneously on a given host. Containers are lightweight because they don’t need the extra load of a hypervisor, but run directly within the host machine’s kernel. This means you can run more containers on a given hardware combination than if you were using virtual machines. You can even run Docker containers within host machines that are actually virtual machines!

This tutorial uses MacOS as an example, but other platforms should have similar logic.

## 1. Download and Install Docker

First, we need to download and install application that will allow us to instantiate Docker containers.

 - Go to [Docker Community Edition](https://www.docker.com/community-edition) and download Docker CE for your OS.  
 - Double click on `Docker.dmg` file


|          |
|----------|
|![](/img/docker_install.png)|
|<small>Drag docker to you Applications folder</small>|

- Go to "Applications", start it, and go through all prompts
- You know it is running because you will have Docker icon 

|          |
|----------|
|![](/img/docker_menu_bar.png)|
|<small>It's running</small>|

## 2. Start Kitematic

Kitematic is a GUI for Docker.

- start Kitematic by clicking on Docker icon on the menu bar:

|          |
|----------|
|![](/img/start_kitematic.png)|
|<small>Start Kitematic</small>|

- you will see something like this:

|          |
|----------|
|![](/img/kitematic_window.png)|
|<small>Kitematic is running</small>|

## 3. Download Jupyter 

We will use special "flavor" of Jupyter - a Docker image containing Jupyter and many popular data analysis tools - [Jupyter Notebook Data Science Stack](https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook). To do this type `jupyter/datascience-notebook` in your Kitematic window:

|          |
|----------|
|![](/img/getting_jp.png)|
|<small>Finding `jupyter/datascience-notebook` image</small>|

and then click **CREATE** button by `datascience-notebook`:

|          |
|----------|
|![](/img/getting_jp1.png)|
|<small>Downloading `jupyter/datascience-notebook` image</small>|

wait for it to download! It will take some time.

## 4. Start Jupyter Notebook

After Jupyter image is downloaded, the container will start automatically:

|          |
|----------|
|![](/img/running_jp1.png)|
|<small>Downloading `jupyter/datascience-notebook` image</small>|

This is, however, something we <font color="red">**DO NOT WANT**</font>! This is because we want to configure the container to have access to the filesystem of your computer. 

So first go ahead and create a directory somewhere on your filesystem. This is important because you will store your data and notebook copies in that place:

```
$ cd
$ pwd
/Users/anton
$ mkdir bmmb554_sandbox
$ cd bmmb554_sandbox
```

Next, stop the running container using Kitematic interface:

|          |
|----------|
|![](/img/stop_jp.png)|
|<small>Stop running container</small>|

Then click **DOCKER CLI** (stands for Docker Command Line Interface) at the bottom of Kitematic window:

|          |
|----------|
|![](/img/docker_cli.png)|
|<small>Open DOCKER shell</small>|

in the shell type (obviously omit `$` as these simply indicate shell prompt and replace `/Users/anton/bmmb554_sandbox` with directory you created above):

```
$ docker run -v /Users/anton/bmmb554_sandbox:/home/jovyan/work -it --rm -p 8888:8888 jupyter/datascience-notebook
```

when Container starts it will spit something like this:

```
[I 17:47:18.891 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 17:47:18.891 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=90e426ee66686351a303a030093d9fd094bd700f41e07d94
```

just copy this URL into your browser and you will get a running Jupyter server:

|          |
|----------|
|![](/img/its_running.png)|
|<small>Jupyter is now running</small>|

you will notice that the image above simply shows a file browser interface. If you click on `work` you will see an empty directory. However, because we started our Docker container with `-v /Users/anton/bmmb554_sandbox:/home/jovyan/work` flag, we are actually looking inside `/Users/anton/bmmb554_sandbox` directory on my machine. But from the standpoint of Docker container it is in `/home/jovyan/work`. (If you wonder what `jovyan` means [look here](https://github.com/jupyter/docker-stacks/issues/358)).

# Setting up GitHub

## Create a GitHub account

Don't call it anything stupid. You will likely use GitHub a lot in the future!

## Create a new repository

|          |
|----------|
|![](/img/create_repo.png)|
|<small>Create new repository on GitHub</small>|

## Copy repo link

|          |
|----------|
|![](/img/copy_repo_link.png)|
|<small>Copy link to your newly minted repo</small>|

## Get back to Kitematic

Open Shell within your running container:

|          |
|----------|
|![](/img/start_container_shell.png)|
|<small>Click **EXEC** button</small>|

within that shell type:

```
jovyan@5373fde36475:~$ ls
work
jovyan@5373fde36475:~$ cd work/
jovyan@5373fde36475:~/work$ git clone https://github.com/nekrut/bmmb554_notebooks.git
Cloning into 'bmmb554_notebooks'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
jovyan@5373fde36475:~/work$ 

```

Now create a directory for your data, where you will be storing actual datasets. <font color="red">It must be outside of your git repo as you don't want to commit these large files:</font>

```
jovyan@5373fde36475:~/work$ mkdir data
```

Now, you have the following structure for your filesystem:

```
.
├── bmmb554_notebooks
│   └── README.md
└── data
```

Your notebooks will go to `bmmb554_notebooks` and data will do `data`.








