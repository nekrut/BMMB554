---
date: "2020-01-14"
tags: ["jupyter", "github", "python"]
title: "Lecture 1: Basic machinery = Jupyter + GitHub"
---

[![](https://imgs.xkcd.com/comics/python.png)](https://xkcd.com/353/)

# Welcome to Notebooks 

<div class="alert alert-danger" role="alert">
  An important assumption for this lecture is that (1) you have a Google account, (2) know how to use Google Drive, and (3) also have an active GitHub account.
</div>

When you start an analysis, you don't really know how it will go. Maybe data is bad and there is no real reason to analyze anything at all. Maybe data data outliers that need to be dealt with. Maybe data is too sparse and cannot be analyzed using standard approaches. Whatever is the case there are multiple steps that depend on each other. Because real analyses contain many such steps it is easy to end up with tangled mess of little scripts that cannot be comprehended even by their own author. As Steven Skiena points out in his book ["The data science design manual"](http://www.data-manual.com/):


{{< bootstrap-blockquote author="Steven Skiena" >}}
The primary deliverable for a data science project should not be a program. It should not be a data set. It should not be the results of running the program on your data. It should not just be a written report. The deliverable result of every data science project should be a computable notebook tying together the code, data, computational results, and written analysis of what you have learned in the process.
{{< /bootstrap-blockquote >}}

<br>

## Get your first notebook

We will start by using [Colaboratory](https://colab.research.google.com) to start a [Jupyter](http://jupyter.org) notebook that is stored on [GitHub](https://github.com/nekrut/BMMB554). 

Go to http://collab.research.google.com:

------

![](/BMMB554/img/colab1.png)

<small>Default Colaboratory interface.</small>

------


Select "Upload notebook" (you will be prompted for Google sign-in):

------

![](/BMMB554/img/colab2.png)

<small>Select "Upload notebook".</small>

------

Use `https://github.com/nekrut/BMMB554` as the source URL and select `intro_jupyter.ipynb`:

-----

![](/BMMB554/img/colab3.png)

<small>Select <tt>intro_jupyter.ipynb</tt>.</small>

------

You will see something like this:

-----

![](/BMMB554/img/colab4.png)

<small>A freshly rendered notebook.</small>

------


## Make a copy of this notebook

The notebook you just uploaded is immutable - you cannot make any changes to it. To claim it as your own use "Save a copy in Drive..." option:

----

![](/BMMB554/img/colab5.png)

<small>Make a copy!</small>

------

## Commit a copy to your GitHub account

Once you are dony playing with the notebook - save a copy to your GitHub account by using "Save a copy in GitHub" and following the prompts. Before you can actually do this, you will need to initialize a new repository on GitHub as I will show you during this lecture.

----

![](/BMMB554/img/colab6.png)

<small>Save to GitHub!</small>

------

## Jupyter ecosystem is **HUGE**

We will use Jupyter for virtually everything in this course. It is worth noting that anything is indeed possible in Jupyter as highlighted by this [very large list](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks) of known tutorials.

