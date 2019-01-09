---
date: "2019-01-09"
tags: ["jupyter", "github", "python"]
title: "Lecture 2: Basic machinery = Jupyter + GitHub"
---

[![](https://imgs.xkcd.com/comics/python.png)](https://xkcd.com/353/)

# Welcome to Notebooks 

When you start an analysis, you don't really know how it will go. Maybe data is bad and there is no real reason to analyze anything at all. Maybe data data outliers that need to be dealt with. Maybe data is too sparse and cannot be analyzed using standard approaches. Whatever is the case there are multiple steps that depend on each other. Because real analyses contain many such steps it is easy to end up with tangled mess of little scripts that cannot be comprehended even by their own author. As Steven Skiena points out in his book ["The data science design manual"](http://www.data-manual.com/):

<div class="card">
  
  <div class="card-body">
      <em>The primary deliverable for a data science project should not be a program. It should not be a data set. It should not be the results of running the program on your data. It should not just be a written report. The deliverable result of every data science project should be a computable notebook tying together the code, data, computational results, and written analysis of what you have learned in the process.</em>
 
  </div>
  <div class="card-footer">
    <footer class="blockquote-footer">From "<em>The data science design manual</em>" by Steven Skiena.</footer>
  </div>
</div>

