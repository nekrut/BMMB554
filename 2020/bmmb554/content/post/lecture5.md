---
date: "2020-02-05"
tags: ["mapping", "SAM/BAM"]
title: "Lecture 5: Mapping Reads II"
---

## Prep the environment

Install [conda](https://docs.conda.io/en/latest/), configure path and channles:


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

Mount the drive and copy duplex files into notebook filesystem (in my specific case I created `bmmb554_data` directiory at the root of my drive):


```python
cp /content/drive/My\ Drive/bmmb554_data/r1* ./
```

## Mapping data with `bwa` and processing with `samtools`


```python
ls
```

Install [bwa](https://github.com/lh3/bwa) [also see [Li:2012](https://arxiv.org/pdf/1303.3997.pdf)]  :


```python
!conda install -y bwa
```

Upload sequence of pBR322 from Zenodo [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3637681.svg)](https://doi.org/10.5281/zenodo.3637681)



```python
!wget https://zenodo.org/record/3637681/files/pbr322.fa
```

Create bwa index files:


```python
!bwa index -p plasmid pbr322.fa
```

Let look at bwa command line options:


```python
!bwa
```


```python
!bwa mem
```

We can speed up process to give `bwa` more threads to work with. How many threads does our system have:


```python
cat /proc/cpuinfo
```

Our paired end data is represented as two files: forward and reverse. We can feed these to bwa manually by typing their names but since we are inside a python envirtonment we can do this programmatically.


```python
# Get the list of `fq.gz` files

import os

files = []

for file in os.listdir():
  if file.endswith('fq.gz'):
    files.append(file)
files = sorted(files)
```


```python
# It is a list:

files
```


```python
# We need toi organize these file names in pairs. In this particular case we want to have a list of two pairs.
# A flat list can be organzed into a 2 x 2 list using numpy

import numpy as np

pairs = np.reshape(files,(2,2))
pairs
```


```python
# To make it more generic we can do this:

pairs = np.reshape(files,(len(files)//2,2))
pairs
```

Now we can run bwa to produce sam files:


```python
# Now let's create a command line and execute it

for pair in pairs:
  cmd = 'bwa mem -t 2 plasmid {} {} > {}.sam'.format(pair[0],pair[1],pair[0][:5])
  print(cmd)
  !{cmd}
```

This generates two sam files:


```python
ls
```

Sam format looks like this:


```python
!head r1-s0.sam
```

Let's look at SAM/BAM format [specification](https://samtools.github.io/hts-specs/SAMv1.pdf). Before we can use BAM file they need to be softed and indexed:


```python
!conda install -y samtools
```


```python
!samtools view -bh r1-s0.sam > r1-s0.bam
```


```python
!samtools sort r1-s0.bam > r1-s0.sorted.bam
```


```python
!samtools index r1-s0.sorted.bam
```


```python
ls
```

Alternatively, this can be done in one go using piping. First, let's delete sam and bam files we've produced so far:


```python
rm *.sam *.bam*
```


```python
ls
```


```python
# Rerunning bwa piping output directly into samtools:

for pair in pairs:
  cmd = 'bwa mem -t 2 plasmid {0} {1} | samtools view -bh - | samtools sort - > {2}.bam; samtools index {2}.bam'.format(pair[0],pair[1],pair[0][:5])
  print(cmd)
  !{cmd}
```

## Assessing mapping results

`deepTools` is an excellent set of tools for manipulation of mapping data


```python
pip install deeptools
```


```python
import os
for file in os.listdir():
  if file.endswith('bam'):
    cmd = 'bamCoverage -b {0}.bam -o {0}.bw'.format(file[:-4])
    !{cmd}
```


```python
pip install pygenometracks
```

Upload annotaion of pBR322 from Zenodo [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3637681.svg)](https://doi.org/10.5281/zenodo.3637681)

Pull in annotaion of pBR322 from Zenodo


```python
!wget https://zenodo.org/record/3637681/files/pBR322.bed
```

The bed file we just uploaded is not sorted. To sort it let's install and use bedtools:


```python
!sudo apt-get install bedtools
```


```python
!bedtools sort -h -i pBR322.bed > a; mv a pBR322.bed
```

Now, create configuration file for pyGenomeTracks:


```python
!make_tracks_file --trackFiles pBR322.bed *.bw -o tracks.ini
```

And visualize!


```python
!pyGenomeTracks --tracks tracks.ini --region pBR322:1-3000 --outFileName nice_image.svg
```


```python
from IPython.core.display import SVG
SVG(filename='nice_image.svg')
```
