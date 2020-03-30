---
date: "2020-01-28"
tags: ["python","conda","bioconda","sra","duplex sequencing","HIV"]
title: "Defining project and getting data"
---

![https://xkcd.com/1987/]( https://imgs.xkcd.com/comics/python_environment.png)

## WarmUp with Python Strings

 - Open [this notebook](https://drive.google.com/file/d/18IEkP6FF6KH-ftONzrpF9yuzxY0j0mC7/view?usp=sharing)
 - Make a copy of it in your drive
 - Go through it and execute all cells


## The project

The goal of our project will be finding a perfect variant caller for non-diploid data (e.g., viral, bacterial, organellar).

For this we will use two datasets:

 - An HIV resequencing data from the DC cohort [study](https://doi.org/10.1371/journal.pone.0214820)
 - A [duplex sequencing](https://www.pnas.org/content/109/36/14508.long) dataset from an experimental evolution [study](https://doi.org/10.1093/gbe/evz197)

 The idea is to use duplex data as the "golden standard" and then apply the best caller we find to HIV data and see if we can find anything interesting.

## Prep the system

 1. Log in into Google Drive using your Penn State credentials (obviously if you are outside Penn State just use your Google log in or whatever works)
 2. Start a new **Python 3** notebook in colaboratory
 3. Name it an intelligent way (e.g., `seq_data_QC`)

## Install [Conda](https://docs.conda.io/en/latest/)

Run a cell with the following code

 ```python
!wget -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
!chmod +x Anaconda3-5.1.0-Linux-x86_64.sh
!bash ./Anaconda3-5.1.0-Linux-x86_64.sh -b -f -p /usr/local

import sys
sys.path.append('/usr/local/lib/python3.6/site-packages/')

!conda config --add channels defaults
!conda config --add channels bioconda
!conda config --add channels conda-forge
```

This code will install and configure [Conda](https://docs.conda.io/en/latest/) without colaboratory virtual machine.

## Get the data from [Zenodo](https://zenodo.org/)

First we will download duplex data from Zenodo repository <a href="https://doi.org/10.5281/zenodo.3565911"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3565911.svg" alt="DOI"></a>

First use `wget` to get just one file:

```
!wget https://zenodo.org/record/3565911/files/pbr322.fa
```

This is not convenient because you would have to do this five times. So let's install `zenodo-get` -- a tool for sucking things out of Zenodo (remember that this instance of Jupyter runs in your little personal virtual machine where you can install whatever you want):


```
!pip install zenodo-get
```

Now we can download everything from this Zenodo project:

```
!zenodo_get.py -d 10.5281/zenodo.3565911
```

Once it is done, use `ls` to look if the files are there.


## Get the data from [SRA](https://www.ncbi.nlm.nih.gov/sra)

The DC cohort re-sequencing data has been deposited to SRA at NCBI. We will download just one dataset for today's lecture: `SRR8525907`. We will do this programmatically using `sra-toolkit`, which we first need to install. This is really why we installed Conda in the first place:

```
!conda install -y sra-tools
```

once finished look at command options of the tool we will be using `fasterq-dump`:

```
!fasterq-dump -h
```

the option we need is `-S` (write reads into different files). We also remember that we need to download data with accession `SRR8525907`:

```
!fasterq-dump -S -p SRR8525907
```

Use `ls` to look at the files. This will produce two files with extension `.fastq`. 

## Harmonize filenames

First the files we downloaded from SRA are not compressed and there is no good reason to keep then uncompressed. But before we compress them check their sizes with `ls -lh`. Now let's compress them (`*` is the wild card):


```
!gzip *.fastq
```

check the sizes of files with `ls -lh` again to appreciate how much space is saved by compression.

Now let's get all fastq files in our directory to have the same extension:

```python
import os

for file in os.listdir():
  if file.endswith('.fastq.gz'):
    new_name = file.replace('fastq.gz','fq.gz')
    !mv {file} {new_name}
```


now all files have extension `fq.gz`!

## QCing

To get some idea about the quality of the reads we will install and run [`fastqc`](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/). First install:

```
!conda install -y fastqc
```

and now run on all `*.fq.gz` files:

```
!fastqc *.fq.gz
```

`fastqc` generates a separate html report for each file. It is tedious to look through everyone of them. We can aggregate results with [`multiqc`](https://multiqc.info/). Install `multiqc` with this commands:


```
!conda install -y multiqc
```

and run in:

```
!multiqc ./
```

it will generate a web page containing a report. You can visualize this web-page directly in your notebook:


```python
from IPython.display import HTML
HTML(filename="multiqc_report.html")
```

## Adapter trimming

It really looks like we need to trim adapters off of some of the sequences. For this purpose we will use [`trim-galore`](http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/). Let's install it first:

```
!conda install -y trim-galore
``` 

Once it is installed look at command line options using `--help` flag. Now we can trim the adapters using the following command:

```
!trim_galore --paired *.fq.gz
```

This will generate a new set of fastq files with extension `_val_1{1|2}.fq.gz`. Before we do anything with these files let's summarize what `trim-galore` actually did. This is again done with `multiqc`:

```
!multiqc -n tg *trimming_report.txt
```

and to look at the report execute the following:

```python
from IPython.display import HTML
HTML(filename="tg.html")
```

you can see that HIV samples were trimmed to a much higher extent than the other datasets. 

## Saving your work

Now we need to same the trimmed files to Google Drive, so we can use them in the next class. To do this click on the folder icon in the upper left and click "<kbd>Mount drive</kbd>". This will ask you execute a code cell and enter an authorization code. No go to your drive and create an appropriately names folder. For example, `bmmb554_data`. Now copy all trimmed files into this folder:

```
cp *val* /content/drive/My\ Drive/bmmb554_data
```

your files will magically appear there!


