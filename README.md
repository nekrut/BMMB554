# Introduction to Data Driven Life Sciences | Spring 2025

## Syllabus

[![https://xkcd.com/2054/](https://imgs.xkcd.com/comics/data_pipeline.png)](https://xkcd.com/2054/)

## Place and Time

[Huck Life Sciences Bldg 005](https://www.map.psu.edu/?id=1134#!m/609644) | Tuesday, Thursday [10:35am - 11:50am EST](https://www.timeanddate.com/)

> [!TIP]
>The class is **in person** only. However, for those who are located in Hershey or unable to attend a particular lecture<sup>1</sup> a [**Zoom**](https://psu.zoom.us/j/92390068604) link is provided. 

> <sup>1</sup>**Notify** the instructor in advance if you are unable to attend a lecture for whatever reason.

## Instructor

**Anton Nekrutenko**
[aun1@psu.edu](mailto:aun1@psu.edu?Subject=BMMB554)
Wartik 505
Office hours by appointment only

> [!NOTE]
> When contacting instructor use the above e-mail and include "BMMB554" in the subject line (simply click on [e-mail](mailto:aun1@psu.edu?Subject=BMMB554) address. It will invoke an email client with subject line pre-filled).

## Course logistics

This course **does not use** Canvas. Canvas is a convoluted system with too many features and undefined purpose. Instead, this course is served from [GitHub](https://github.com/nekrut/BMMB554). 


> [!CAUTION]
> **Do not contact me through Canvas!** I will not check my Inbox there. Instead, contact me via [email](mailto:aun1@psu.edu?Subject=BMMB554) as described above.
> 
## Grading and quizzes

> [!IMPORTANT]
> Each Tuesday class will start with a 10 min quiz. The quiz will be based on reading assignments from the previous week. Each quiz will be scored on `[0;100]` scale. Aggregate of quiz scores will represent 33.3% of the final grade. 

Attendance (33.3%) + Quizzes (33.3%) + Final Project (33.3%)  &#8776; 100%

---

## A note on notebook environments

We will use JupyterLab as our main platform. JupyterLab is an example of a "notebook environment." There are several frameworks for interactive data exploration using code snippets. These include:

- [Jupyter](https://jupyter.org/) | [JupyterLite](https://github.com/jupyterlite) | [Google Colab](https://colab.research.google.com)
- [RStudio](https://posit.co/)
- [ObservableHQ](https://observablehq.com/@d3/gallery?collection=@observablehq/observable-libraries-for-visualization) (learn JavaScript [here](https://eloquentjavascript.net/))

### JupyterLab set up for Shell, Python, and Git lectures

1. Start [JupyterLab](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/try.jupyter.org?urlpath=lab)
2. Start terminal within JupyterLab instance

![](https://i.imgur.com/qSrZwOI.png)


## Lectures

Links to individual lectures will be posted below. 

----

## Block 1: Shell / Python / Generative-AI 

| Lecture | Date | Topic | Reading **before** lecture | Quiz |
|----------|--|---------|---------------------------|----|
| 1 | Jan 14 | [Introduction and History](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture1/tutorial.html) |   |  |
| 2 | Jan 16 | [History of sequencing and simulation of sequencing process: thinking conceptually.](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture2/tutorial.html) | [Shell I](https://gxy.io/GTN:T00076) | Y |
| 3 | Jan 23 | [Simulation of sequencing process: implementing it.](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture2/tutorial.html) | [Shell II](https://gxy.io/GTN:T00074) | Y |
| 4/5 | Jan 28/30 | [Python 1 - Variables, expressions, statements, functions](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture2/tutorial.html) | Chapters [1](https://greenteapress.com/thinkpython2/html/thinkpython2002.html), [2](https://greenteapress.com/thinkpython2/html/thinkpython2003.html), [3](https://greenteapress.com/thinkpython2/html/thinkpython2004.html), [8](https://greenteapress.com/thinkpython2/html/thinkpython2009.html) and [10](https://greenteapress.com/thinkpython2/html/thinkpython2011.html) from "Think Python" | Y |
| 6 | Feb 4 |  [Python 2 - Strings and lists and FASTQ](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture3/tutorial.html) |  | N | 
| 7 | Feb 6 |  [Python 3 - A more careful look at lists and dictionaries](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture4/tutorial.html) |  | N | 
| 8 | Feb 11 |  [Python 4 - Processing files](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture5/tutorial.html) |  | N | 
| 9 | Feb 13 | [ Pandas 1 - Creating and using dataframes ](https://colab.research.google.com/github/nekrut/BMMB554/blob/master/notebooks/pandas.ipynb) | | Home assignment |
| 10 | Feb 18 | [ Pandas 2 - Narrow data versus wide data. Melts, pivots, and joins](https://colab.research.google.com/github/nekrut/BMMB554/blob/master/notebooks/pandas.ipynb) | | |
| 11 | Feb 20 | Data analysis platforms and workflow languages: An overview + Defining class project | | ❗ [Home assignment due](https://github.com/nekrut/BMMB554/blob/master/2025/hm1.md) ❗ |

<!--
  
- [Lecture 4](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture2/tutorial.html) - Intermission + History of Sequencing
- [Lecture 5](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture2/tutorial.html) - Python 1 - Variables, expressions, statements, functions
- [Lecture 6](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture3/tutorial.html) - Python 2 - Strings and lists and FASTQ
- [Lecture 7](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture4/tutorial.html) - Python 3 - A more careful look at lists and dictionaries
- [Lecture 8](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture5/tutorial.html) - Python 4 - Processing files
- [Lecture 9](https://training.galaxyproject.org/training-material/topics/data-science/tutorials/python-basics/tutorial.html) - Python 5 - Recap (If you feel bored, do [this](https://training.galaxyproject.org/training-material/topics/data-science/tutorials/python-advanced-np-pd/tutorial.html))
- [Lecture 10](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture6/tutorial.html) - Pandas - A set of tools for data wrangling
- [Lecture 11](https://gallantries.github.io/video-library/videos/statistics/CNN/) - What is Machine Learning: A CNN example 
- [Lecture 12](https://training.galaxyproject.org/topics/data-science/tutorials/gnmx-lecture7/tutorial.html) - Git/GitHub 1 - Git logic
- Lecture 13 - How to create your own web-site using GitHub and Markdown + [Project discussion](https://www.science.org/doi/10.1126/science.aag0822) 
- Lecture 14 - How Illumina works + [Introduction to Galaxy](https://gxy.io/GTN:T00186)
- Lecture 15 - [QCing](https://training.galaxyproject.org/training-material/topics/introduction/tutorials/vsi_qc/tutorial.html) and [algorithmic foundation of mapping](https://github.com/nekrut/BMMB554/blob/master/2024/finding_matches.md)
- Lecture 16 - [Element Biosciences Sequencing](http://dx.doi.org/10.1038/s41587-023-01750-7) + [Adding yourself to BMMB554 queue](https://github.com/nekrut/BMMB554/blob/master/2024/galaxy_queue.md) + [Mapping and postprocessing of mapped data](https://gxy.io/GTN:T00188)
- Lecture 17 - [PacBio](https://github.com/nekrut/BMMB554/blob/master/2024/pacbio.md) + Creating a mapping workflow + [Understanding BAM files](https://samtools.github.io/hts-specs/SAMv1.pdf)
- Lecture 18 - [Calling variants in non-diploid systems](https://github.com/nekrut/BMMB554/blob/master/2024/nonD_variant_calling.md)
- Lecture 18 - [ONT](https://github.com/nekrut/BMMB554/blob/master/2024/ont.md) + [First look at MEGA trajectories: Is there anything?](https://github.com/nekrut/BMMB554/blob/master/2024/assessimg_variants.md)
- Lecture 19 - [Rerunning based on custom reference](https://github.com/nekrut/BMMB554/blob/master/2024/how_to_rerun.md), [Alignment: What are the differences between strains?](https://github.com/nekrut/BMMB554/blob/master/2024/alignment.md)
- Lecture 20 - [Why genome alignments are difficult](https://github.com/nekrut/BMMB554/blob/master/2024/alignment.md)
- Lecture 21 - Discussion of the [final project](https://github.com/nekrut/BMMB554/blob/master/2024/project.md). 

-->

-----

## ECoS Teaching Statement

><tt>In an examination setting, unless the instructor gives explicit prior instructions to the contrary, violations of academic integrity shall consist of any attempt to receive assistance from written or printed aids, from any person or papers or electronic devices, or of any attempt to give assistance, whether the student doing so has completed his or her own work or not. Other violations include, but are not limited to, any attempt to gain an unfair advantage in regard to an examination, such as tampering with a graded exam or claiming another's work to be one's own. Other assessments (including ANGEL-administered quizzes and assessments as well as homework assignments) are expected to represent your own independent work unless specifically stated otherwise. Failure to comply will lead to sanctions against the student in accordance with the Policy on Academic Integrity in the Eberly College of Science. [The Eberly College of Science Code of Mutual Respect and Cooperation](www.science.psu.edu/climate/Code-of-Mutual-Respect-final.pdf) embodies the values that we hope our faculty, staff, and students possess and will endorse to make The Eberly College of Science a place where every individual feels respected and valued, as well as challenged and rewarded.   The Eberly College of Science is committed to the academic success of students enrolled in the College's  courses and undergraduate programs. When in need of help, students can utilize various College and University wide [resources for learning assistance](http://www.science.psu.edu/advising/success). Penn State welcomes students with disabilities into the University's educational programs. If you have a disability-related need for reasonable academic adjustments in this course, contact the Office for Disability Services (ODS) at 814-863-1807 (V/TTY). For further information regarding ODS, please visit the Office for [Disability Services Web site](http://equity.psu.edu/ods/). In order to receive consideration for course accommodations, you must contact ODS and provide documentation (see the [documentation guidelines](http://equity.psu.edu/student-disability-resources/guidelines)). If the documentation supports the need for academic adjustments, ODS will provide a letter identifying appropriate academic adjustments. Please share this letter and discuss the adjustments with your instructor as early in the course as possible. You must contact ODS and request academic adjustment letters at the beginning of each semester.</tt>

