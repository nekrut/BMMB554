---
tags: BMMB554-23
---

# Lecture 3: Shell II

[![](https://imgs.xkcd.com/comics/startling.png)](https://xkcd.com/354)

Shell allows interaction with operating system. Today we will play with [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), which is one of [many](https://en.wikipedia.org/wiki/Comparison_of_command_shells#General_characteristics) existing shells. 

## Lecture setup

1. Start [JupyterLab](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/try.jupyter.org?urlpath=lab)
2. Start terminal within JupyterLab instance

![](https://i.imgur.com/qSrZwOI.png)


3. Download notebook for today's lecture into the JupyterLab environment by executing the following command (cut the command and paste it into terminal you opened at step 2)

```bash=
wget https://raw.githubusercontent.com/nekrut/BMMB554/master/2023/ipynb/L3-shell2_ws.ipynb
```
4. Refresh your file browser
5. Double click on the notebook to launch it (select Python 3 kernel)
6. Drag notebook tag to a side to have side-by-side view of the notebook and terminal.
7. Go to terminal tab end execute the following commands:

```bash=
cd ~/
mkdir -p Desktop/
cd Desktop/
wget -c https://github.com/swcarpentry/shell-novice/raw/2929ba2cbb1bcb5ff0d1b4100c6e58b96e155fd1/data/shell-lesson-data.zip
unzip -u shell-lesson-data.zip
```
8. Let the lecture begin!

## A note on UNIX shortcuts

{%gist tuxfight3r/60051ac67c5f0445efee %}

## A note on package managers (and virtual environments)

![](https://i.imgur.com/TYXUnJj.png)


Today we will use a package manager called [`Conda`](https://docs.conda.io/en/latest/). It is used to install software and to manage *virtual environments* (more about virtual environments when we talk about Python programming). Today we will use `Conda`   to install a directory structure visualizer[`tree`](https://en.wikipedia.org/wiki/Tree_(command)):

```bash=
conda install tree
```

to make things faster you can also use an alternative implementation of`Conda`called[`mamba`](https://mamba.readthedocs.io/en/latest/):

```bash=
mamba install tree
```

## Quiz 1

> (You will receive instructions at the end of the lecture)


