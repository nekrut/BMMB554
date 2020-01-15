---
date: "2019-01-15"
tags: ["python"]
title: "Lecture 3: Python refresher 1"
draft: true
---

[![](https://imgs.xkcd.com/comics/sigil_cycle.png)](https://xkcd.com/1306/)

# What is Python?

Python is a modern, general-purpose, object-oriented, high-level programming language.

<div class="alert alert-info" role="alert">
  This material is heavily inspired by <a href="http://pycam.github.io/">Materials for the course run by the Graduate School of Life Sciences, University of Cambridge</a> with some modifications.
</div>

## General characteristics of Python:

 - **Clean and Simple**: Easy-to-read and intuitive code, easy-to-learn minimalistic syntax, maintainability scales well with size of projects.
 - **Expressive**: Fewer lines of code, fewer bugs, easier to maintain.

### Technical details:

 - **dynamically typed**: No need to define the type of variables, function arguments or return types.
 - **automatic memory management**: No need to explicitly allocate and deallocate memory for variables and data arrays. No memory leak bugs.
 - **interpreted**: No need to compile the code. The Python interpreter reads and executes the python code directly.

### Advantages:

The main advantage is ease of programming, minimizing the time required to develop, debug and maintain the code.
Well designed language that encourage many good programming practices:
Modular and object-oriented programming, good system for packaging and re-use of code. This often results in more transparent, maintainable and bug-free code.
Documentation tightly integrated with the code.
A large standard library, and a large collection of add-on packages.

### Disadvantages:

Since Python is an interpreted and dynamically typed programming language, the execution of python code can be slow compared to compiled statically typed programming languages, such as C and Fortran.
Somewhat decentralized, with different environment, packages and documentation spread out at different places. Can make it harder to get started.

# So...

## Open lecture notebook for today:

We will start by using [Colaboratory](https://colab.research.google.com) to start a [Jupyter](http://jupyter.org) notebook that is stored on [GitHub](https://github.com/nekrut/BMMB554). 

Go to http://collab.research.google.com:

<div class="card mb-3">
  <img class="card-img-top" src="/BMMB554/img/collab1.png" alt="Card image cap">
  <div class="card-footer">
    	<footer class="blockquote-footer">
    		Default Colaboratory interface.
    	</footer>
  	</div>
</div>

Select "Upload notebook" (you will be prompted for Google sign-in):

<div class="card mb-3">
  <img class="card-img-top" src="/BMMB554/img/colab2.png" alt="Card image cap">
  <div class="card-footer">
    	<footer class="blockquote-footer">
    		Select "Upload notebook".
    	</footer>
  	</div>
</div>

Use `https://github.com/nekrut/BMMB554` as the source URL and select `2019/ipynb/intro1.ipynb`:

<div class="card mb-3">
  <img class="card-img-top" src="/BMMB554/img/colab_lec3.png" alt="Card image cap">
  <div class="card-footer">
    	<footer class="blockquote-footer">
    		Select <tt>2019/ipynb/intro1.ipynb</tt>
    	</footer>
  	</div>
</div>
