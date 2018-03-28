+++
menu = ""
#draft = true
tags = ['writing','papers','grants'
]
categories = [
]
featureimage = "img/topic11_cover.png"
date = "2018-03-28"
title = "Continuing MEGA analysis"

+++

# Refresher

We were analyzing the following data:

|          |
|----------|
|![](/img/team_data.png)|
|<small>Trajectories for the four teams in this class:</small>|

|    Team 1     |      Team 2      |       Team 3      |      Team 4         |
|----------|---------|--------------|--------------|
|10.SRR3722230|103.SRR3721968|100.SRR3722240|2.SRR3721964|
|2.SRR3721964|104.SRR3721969|101.SRR3721966|34.SRR3722148|
|36.SRR3722150|105.SRR3721970|122.SRR3721989|38.SRR3722152|
|37.SRR3722151|106.SRR3721971|2.SRR3721964|43.SRR3722158|
|64.SRR3722201|168.SRR3722039|74.SRR3722212|63.SRR3722200|
|7.SRR3722197|169.SRR3722040|95.SRR3722235|67.SRR3722204|
|8.SRR3722208||96.SRR3722236|68.SRR3722205|
|9.SRR3722219||97.SRR3722237|69.SRR3722206|
|||98.SRR3722238|7.SRR3722197|
|||99.SRR3722239|70.SRR3722207|
||||71.SRR3722209|
||||72.SRR3722210|
||||73.SRR3722211|

The data is at [this location](https://usegalaxy.org/library/list#folders/F9b810fe4cca869a8):

|                       |
|-----------------------|
|![](/img/mega_data.png)|
|<small>Folders T1 through T4 contain data for each team. `U00096` is a Genbank file containing annotations and genome sequence for *E. coli* genome used by [Baym:2016](http://science.sciencemag.org/content/353/6304/1147) (see Methods section).</small>|

# Analysis

## Initial processing and finding variants

For initial analysis (mapping and variant calling) we used the following [workflow](https://usegalaxy.org/u/aun1/w/megatovcf):

|                       |
|-----------------------|
|![](/img/mega_workflow.png)|
|<small>Workflow for the initial MEGA analysis</small>|

This workflow contains the following steps:

 1. Inputs:
  - A collection of fastq datasets
  - A reference genome in Genbank format
 1. Genbank dataset in processed by **SnpEff Build** tool to generate two outputs:
  - FASTA dataset
  - snpEff annotation database
 1. Mapping against *E. coli* with BWA-MEM
 1. Deduplcating reads
 1. Filtering reads
 1. Running **Freebayes**

Results of these analyses for individual teams are:

 - [T1](https://usegalaxy.org/u/aun1/h/t1-analysis)
 - [T2](https://usegalaxy.org/u/aun1/h/t2-analysis)
 - [T3](https://usegalaxy.org/u/aun1/h/t3-analysis)
 - [T4](https://usegalaxy.org/u/aun1/h/t4-analysis)


## Postprocessing

For deciding which variants are "good" and understanding their effects we will use two toolkits we will try to do this:

 - Run [SnpEff](http://snpeff.sourceforge.net/SnpEff_manual.html)
 - Run [SnpSift](http://snpeff.sourceforge.net/SnpSift.html)
 - Calculate [Stand Bias](https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-13-666)
 - Analyze data in Jupyter






