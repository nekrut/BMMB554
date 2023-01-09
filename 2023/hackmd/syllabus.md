---
tags: BMMB554-23
---

> Introduction to Data Driven Life Sciences | Spring 2021

# Syllabus

[![https://xkcd.com/2054/](https://imgs.xkcd.com/comics/data_pipeline.png)](https://xkcd.com/2054/)

## Place and Time

[Ag Engineering](https://www.map.psu.edu/?id=1134#!ce/30540?ct/59509,33177,25403,26748,26749,26750,27255?m/357017?s/) 121 | Tuesday, Thursday [10:35am - 11:50am EST](https://www.timeanddate.com/)

:::success
The class is **in person** only. However, for those who are located in Hershey or unable to attend a particular lecture<sup>1</sup> a [**Zoom**](https://psu.zoom.us/j/432588759?pwd=M2NWR2ZtbEs4ZFEwZVByeU9JaFdQQT09) link is provided. 
:::

> <sup>1</sup>**Notify** the instructor in advance if you are unable to attend a lecture for whatever reason.

## Instructor

**Anton Nekrutenko**
[aun1@psu.edu](mailto:aun1@psu.edu?Subject=BMMB554)
Wartik 505
Office hours by appointment only

:::warning
When contacting instructor use the above e-mail and include "BMMB554" in the subject line (simply click on [e-mail](mailto:aun1@psu.edu?Subject=BMMB554) address. It will invoke an email client with subject line pre-filled).
:::

## Course logistics

This course **does not use** Canvas. Canvas is a convoluted system with too many features and undefined purpose. Instead, this course is served from [GitHub](https://github.com/nekrut/BMMB554). 


:::danger
**Do not contact me through Canvas!** I will not check my Inbox there. Instead, contact me via [email](mailto:aun1@psu.edu?Subject=BMMB554) as described above.
:::

## Grading

Attendance (33.3%) + Homework (33.3%) + Final Project (33.3%)  &#8776; 100%

## Lectures

The will be divided into several blocks:

1. Fundamentals of data science (2 - 14)
2. Datatypes and major analyses in modern biology (15 - 17)
3. Specific applications (18 - 27)

|  #  | Date      | What                                               | Why                                                                                                                                                                                              |
| --:| ---------:| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1  | 1/10/2023 | [Introduction to the course and history of genomics](/kwGlqDuxTkWt26k_gbZwkg) | You will be given a small test that will not affect your grade. This is necessary for me to understand the skill level of the class. We will also cover fundamental events in the history of genomics |
| 2  | 1/12/2023 | Shell 1                                            | Recap of basic functionality of command line interface (CLI)                                                                                                                                           |
| 3  | 1/17/2023 | Shell 2                                            | A more detailed view of command line functionality                                                                                                                                                     |
| 4  | 1/19/2023 | Python 1                                           | Variables, Types and Type Conversion, Functions                                                                                                                                                        |
| 5  | 1/24/2023 | Python 2                                           | Lists, Strings, and Dictonaries                                                                                                                                                                        |
| 6  | 1/26/2023 | Python 3                                           | Flow Control and Loops, Handling Files, Globbing                                                                                                                                                       |
| 7  | 1/31/2023 | Python 4                                           | Testing, Subprocesses, and Coding Style                                                                                                                                                                |
| 8  | 2/2/2023  | Python 5                                           | Numpy and Pandas 1                                                                                                                                                                                     |
| 9  | 2/7/2023  | Python 6                                           | Numpy and Pandas 2                                                                                                                                                                                     |
| 10 | 2/9/2023  | Python 7                                           | Creating beautiful graphics                                                                                                                                                                            |
| 11 | 2/14/2023 | Code logistics with Git                            | Understanding and using version control                                                                                                                                                                |
| 12 | 2/16/2023 | Workflow management                                | Snamemake and NextFlow                                                                                                                                                                                 |
| 13 | 2/21/2023 | Heavilifting with Galaxy 1                         | Using Galaxy for analyzing complex data                                                                                                                                                                |
| 14 | 2/23/2023 | Heavilifting with Galaxy 2                         | Developing tools for Galaxy                                                                                                                                                                            |
| 15 | 2/28/2023 | Major types of sequence data 1                     | Physical and chemical principles of major sequencing technologies: Illumina, Oxford Nanopore (ONT), Pacific Biosciences (PacBio)                                                                       |
| 16 | 3/2/2023  | Major types of sequence data 2                     | Understanding and handling data from Illumina, ONT, and PacBio                                                                                                                                        |
| 17 | 3/14/2023 | Data Flow in Genomics                              | Major data formats and standard analytical procedures                                                                                                                                                  |
| 18 | 3/16/2023 | Alignment and read mapping                         | Fundamentals of aligning long sequences and finding matches in large genomes                                                                                                                           |
| 19 | 3/21/2023 | Genome Assembly 1                                  | Algorithmic fundamentals of assembling haploid and diploid genomes                                                                                                                                     |
| 20 | 3/23/2023 | Genome Assembly 2                                  | Practical aspects of genome assembly: Assembling Yeast genome                                                                                                                                          |
| 21 | 3/28/2023 | Variant analysis 1                                 | Finding variants in SARS-CoV-2                                                                                                                                                                         |
| 22 | 3/30/2023 | Variant analysis 2                                 | Variation of diploid genomes and fundamentals of population genetics                                                                                                                                   |
| 23 | 4/4/2023  | Transcriptomics 1                                  | From reads to counts                                                                                                                                                                                   |
| 24 | 4/6/2023  | Transcriptomics 2                                  | From counts to genes                                                                                                                                                                                   |
| 25 | 4/11/2023 | Single cell tranbscriptomics 1                     | Understanding barcoding and data deconvolution                                                                                                                                                         |
| 26 | 4/13/2023 | Single cell tranbscriptomics 2                     | Practical aspects of single cell data analysis                                                                                                                                                         |
| 27 | 4/18/2023 | Metagenomics 1                                     | Analysis of 16S data                                                                                                                                                                                  |
| 28 | 4/20/2023 | Metagenomics 2                                     | Metatranscriptomic analysis of micribiome RNA-seq data                                                                                                                                                 |
| 29 | 4/25/2023 | Projects 1                                         | Project presentations day 1                                                                                                                                                                            |
| 30 | 4/27/2023 | Projects 2                                         | Project presentations day 2                                                                                                                                                                            |

## ECoS Teaching Statement

><tt>In an examination setting, unless the instructor gives explicit prior instructions to the contrary, violations of academic integrity shall consist of any attempt to receive assistance from written or printed aids, from any person or papers or electronic devices, or of any attempt to give assistance, whether the student doing so has completed his or her own work or not. Other violations include, but are not limited to, any attempt to gain an unfair advantage in regard to an examination, such as tampering with a graded exam or claiming another's work to be one's own. Other assessments (including ANGEL-administered quizzes and assessments as well as homework assignments) are expected to represent your own independent work unless specifically stated otherwise. Failure to comply will lead to sanctions against the student in accordance with the Policy on Academic Integrity in the Eberly College of Science. [The Eberly College of Science Code of Mutual Respect and Cooperation](www.science.psu.edu/climate/Code-of-Mutual-Respect-final.pdf) embodies the values that we hope our faculty, staff, and students possess and will endorse to make The Eberly College of Science a place where every individual feels respected and valued, as well as challenged and rewarded.   The Eberly College of Science is committed to the academic success of students enrolled in the College's  courses and undergraduate programs. When in need of help, students can utilize various College and University wide [resources for learning assistance](http://www.science.psu.edu/advising/success). Penn State welcomes students with disabilities into the University's educational programs. If you have a disability-related need for reasonable academic adjustments in this course, contact the Office for Disability Services (ODS) at 814-863-1807 (V/TTY). For further information regarding ODS, please visit the Office for [Disability Services Web site](http://equity.psu.edu/ods/). In order to receive consideration for course accommodations, you must contact ODS and provide documentation (see the [documentation guidelines](http://equity.psu.edu/student-disability-resources/guidelines)). If the documentation supports the need for academic adjustments, ODS will provide a letter identifying appropriate academic adjustments. Please share this letter and discuss the adjustments with your instructor as early in the course as possible. You must contact ODS and request academic adjustment letters at the beginning of each semester.</tt>

