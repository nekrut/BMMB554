+++
categories = []
date = "2016-10-10T11:26:49-04:00"
#draft = true
featureimage = "img/topic7_cover.png"
menu = ""
tags = []
title = "NGS data: Practicalities"
description = "**Topic 7** | Handling NGS data: from FASTQ to BAM"

+++

# Getting NGS data in

You can data in Galaxy using one of five ways:

## From your computer

This works well for small files because web browser do not like lengthy file transfers:

{{<vimeo 120901536>}}

## Using FTP

FTP ([file transfer protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)) allows transferring large collection of files: 

{{<vimeo 120972739>}}

## From the Web

Upload from the web works when URL (addresses) of data files are known:

{{<vimeo 120973708>}}

## From EBI short read archive

This is the best way to upload published datasets deposited to EBI SRA. The problem is that not all datasets are available from EBI. Next option (below) explain how to deal with NCBI SRA datasets:

{{<vimeo 121187220>}}

## From NCBI short read archive

Finally, datasets can be uploaded directly from NCBI's short read archive:

{{<vimeo 121190377>}}

# Fastq manipulation and quality control

## What is Fastq?

[FastQ](http://en.wikipedia.org/wiki/FASTQ_format) is not a very well defined format. In the beginning various manufacturers of sequencing instruments were free to interpret fastq as they saw fit, resulting in a multitude of fastq flavors. This variation stemmed primarily from different ways of encoding quality values as described [here](http://en.wikipedia.org/wiki/FASTQ_format) (below you will explanation of quality scores and their meaning). Today, [fastq Sanger](http://www.ncbi.nlm.nih.gov/pubmed/20015970) version of the format is considered to be the standard form of fastq. Galaxy is using fastq sanger as the only legitimate input for downstream processing tools and provides [a number of utilities for converting fastq files](http://www.ncbi.nlm.nih.gov/pubmed/20562416) into this form (see **NGS: QC and manipulation** section of Galaxy tools). 

Fastq format looks like this:


```

@M02286:19:000000000-AA549:1:1101:12677:1273 1:N:0:23
CCTACGGGTGGCAGCAGTGAGGAATATTGGTCAATGGACGGAAGTCTGAACCAGCCAAGTAGCGTGCAG
+
ABC8C,:@F:CE8,B-,C,-6-9-C,CE9-CC--C-<-C++,,+;CE<,,CD,CEFC,@E9<FCFCF?9
@M02286:19:000000000-AA549:1:1101:15048:1299 1:N:0:23
CCTACGGGTGGCTGCAGTGAGGAATATTGGACAATGGTCGGAAGACTGATCCAGCCATGCCGCGTGCAG
+
ABC@CC77CFCEG;F9<F89<9--C,CE,--C-6C-,CE:++7:,CF<,CEF,CFGGD8FFCFCFEGCF
@M02286:19:000000000-AA549:1:1101:11116:1322 1:N:0:23
CCTACGGGAGGCAGCAGTAGGGAATCTTCGGCAATGGACGGAAGTCTGACCGAGCAACGCCGCGTGAGT
+
AAC<CCF+@@>CC,C9,F9C9@9-CFFFE@7@:+CC8-C@:7,@EFE,6CF:+8F7EFEEF@EGGGEEE

```

Each sequencing read is represented by four lines:

1. @ followed by read ID and optional information about sequencing run
2. sequenced bases
3. + (optionally followed by the read ID and some additional info)
4. quality scores for each base of the sequence encoded as [ASCII symbols](https://en.wikipedia.org/wiki/ASCII)

## Paired end data

It is common to prepare pair-end and mate-pair sequencing libraries. This is highly beneficial for a number of applications discussed in subsequent topics. For now let's just briefly discuss what these are and how they manifest themselves in fastq form. 

>
> {{< figure src="/BMMB554/img/pe_mp.png" >}}
>
> **Paired-end and mate-pair reads**. In paired end sequencing (left) the actual ends of rather short DNA molecules (<1kb) are determined, while for mate pair sequencing (right) the ends of long molecules are joined and prepared in special sequencing libraries. In these mate pair protocols, the ends of long, size-selected molecules are connected with an internal adapter sequence (i.e. linker, yellow) in a circularization reaction. The circular molecule is then processed using restriction enzymes or fragmentation. Fragments are enriched for the linker and outer library adapters are added around the two combined molecule ends. The internal adapter can then be used as a second priming site for an additional sequencing reaction in the same orientation or sequencing can be performed from the second adapter, from the reverse strand. (From Ph.D. dissertation by [Martin Kircher](https://core.ac.uk/download/pdf/35186947.pdf))

Thus in both cases (paired-end and mate-pair) a single physical piece of DNA (or RNA in the case of RNA-seq) is sequenced from two ends and so generates two reads. These can be represented as separate files (two fastq files with first and second reads) or a single file were reads for each end are interleaved. Here are examples:

#### Two single files

> **File 1**
>
>```
> @M02286:19:000000000-AA549:1:1101:12677:1273 1:N:0:23
> CCTACGGGTGGCAGCAGTGAGGAATATTGGTCAATGGACGGAAGTCT
> +
> ABC8C,:@F:CE8,B-,C,-6-9-C,CE9-CC--C-<-C++,,+;CE
> @M02286:19:000000000-AA549:1:1101:15048:1299 1:N:0:23
> CCTACGGGTGGCTGCAGTGAGGAATATTGGACAATGGTCGGAAGACT
> +
> ABC@CC77CFCEG;F9<F89<9--C,CE,--C-6C-,CE:++7:,CF
>```
>
>------
>
> **File 2**
>
>```
>@M02286:19:000000000-AA549:1:1101:12677:1273 2:N:0:23
>CACTACCCGTGTATCTAATCCTGTTTGATACCCGCACCTTCGAGCTTA
>+
>--8A,CCE+,,;,<CC,,<CE@,CFD,,C,CFF+@+@CCEF,,,B+C,
>@M02286:19:000000000-AA549:1:1101:15048:1299 2:N:0:23
>CACTACCGGGGTATCTAATCCTGTTCGCTCCCCACGCTTTCGTCCATC
>+
>-6AC,EE@::CF7CFF<<FFGGDFFF,@FGGGG?F7FEGGGDEFF>FF
>```
>----
>Note that read ID are **identical** in two files and they are listed in **the same** order. In some cases read IDs in the first and second file may be appended with `/1` and `/2` tags, respectively. 

#### Interleaved file

>```
>@1/1
>AGGGATGTGTTAGGGTTAGGGTTAGGGTTAGGGTTAGGGTTAGGGTTA
>+
>EGGEGGGDFGEEEAEECGDEGGFEEGEFGBEEDDECFEFDD@CDD<ED
>@1/2
>CCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAAC
>+
>GHHHDFDFGFGEGFBGEGGEGEGGGHGFGHFHFHHHHHHHEF?EFEFF
>@2/1
>AGGGATGTGTTAGGGTTAGGGTTAGGGTTAGGGTTAGGGTTAGGGTTA
>+
>HHHHHHEGFHEEFEEHEEHHGGEGGGGEFGFGGGGHHHHFBEEEEEFG
>@2/2
>CCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAAC
>+
>HHHHHHHHHHHHHGHHHHHHGHHHHHHHHHHHFHHHFHHHHHHHHHHH
>```
>----
>Here the first and the second reads are identified with `/1` and `/2` tags.

<font color="red">&#10148;</font> **Note**: Fastq format is not strictly defined and its variations will always cause headache for you. See [this page](https://www.ncbi.nlm.nih.gov/books/NBK242622/) for more information.

## What are base qualities?

As we've seen above, fastq datasets contain two types of information: 

- *sequence of the read*
- *base qualities* for each nucleotide in the read. 

The base qualities allow us to judge how trustworthy each base in a sequencing read is. The following excerpt from an excellent [tutorial](http://chagall.med.cornell.edu/RNASEQcourse/Intro2RNAseq.pdf) by Friederike D&uuml;ndar, Luce Skrabanek, Paul Zumbo explains what base qualities are:

>Illumina sequencing is based on identifying the individual nucleotides by the fluorescence signal emitted upon their incorporation into the growing sequencing read. Once the fluorescence intensities are extracted and translated into the four letter code. The deduction of nucleotide sequences from the images acquired during sequencing is commonly referred to as base calling. Due to the imperfect nature of the sequencing process and limitations of the optical instruments, base calling will always have inherent uncertainty. This is the reason why FASTQ files store the DNA sequence of each read together with a position-specific quality score that represents the error probability, i.e., how likely it is that an individual base call may be incorrect. The score is called [Phred score](http://www.phrap.com/phred/), $Q$, which is proportional to the probability $p$ that a base call is incorrect, where $Q = −10lg(p)$. For example, a Phred score of 10 corresponds to one error in every ten base calls ($Q = −10lg(0.1)$), or 90% accuracy; a Phred score of 20 corresponds to one error in every 100 base calls, or 99% accuracy. A higher Phred score thus reflects higher confidence in the reported base. To assign each base a unique score identifier (instead of numbers of varying character length), Phred scores are typically represented as ASCII characters. At http://ascii-code.com/ you can see which characters are assigned to what number. For raw reads, the range of scores will depend on the sequencing technology and the base caller used (Illumina, for example, used a tool called Bustard, or, more recently, RTA). Unfortunately, Illumina has been anything but consistent in how they a) calculated and b) ASCII-encoded the Phred score (see below)! In addition, Illumina now allows Phred scores for base calls with as high as 45, while 41 used to be the maximum score until the HiSeq X. This may cause issues with downstream sapplications that expect an upper limit of 41.
>
>-----
>
> {{< figure src="/BMMB554/img/illumina_qs.png" >}}
>
>Base call quality scores are represented with the Phred range. Different Illumina (formerly Solexa) versions
used different scores and ASCII offsets. Starting with Illumina format 1.8, the score now represents the standard
Sanger/Phred format that is also used by other sequencing platforms and the sequencing archives.
>
>-----
>
> {{< figure src="/BMMB554/img/fastq_qs.png" >}}
>
>The ASCII interpretation and ranges of the different Phred score notations used by Illumina and the original
Sanger interpretation. Although the Sanger format allows a theoretical score of 93, raw sequencing
reads typically do not exceed a Phred score of 60. In fact, most Illumina-based sequencing will result in maximum
scores of 41 to 45 (image from [Wikipedia](https://en.wikipedia.org/wiki/FASTQ_format)).

## Assessing data quality

One of the first steps in the analysis of NGS data is seeing how good the data actually is. [FastqQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/) is a fantastic tool allowing you to gauge the quality of fastq datasets (and deciding whether to blame or not to blame whoever has done sequencing for you). 

  | 
:--|:---
![](https://galaxyproject.org/ngs101/good_fq.png) | ![](https://galaxyproject.org/ngs101/bad_fq.png)
**A.** Excellent quality | **B.** Hmmm...OK

Here you can see FastQC base quality reports (the tools gives you many other types of data) for two datasets: **A** and **B**. The **A** dataset has long reads (250 bp) and very good quality profile with no qualities dropping below [phred score](http://www.phrap.com/phred/) of 30. The **B** dataset is significantly worse with ends of the reads dipping below phred score of 20. The **B** reads may need to be trimmed for further processing. 
## Mapping your data

Mapping of NGS reads against reference sequences is one of the key steps of the analysis. In [Topic 5](/post/topic5/) we covered basic principles behind mapping of sequencing reads against large genomes. Now it is time to see how this is done in practice. Below is a list of key publications highlighting popular mapping tools:

- 2009 Bowtie 1 - [Langmead et al.](http://genomebiology.com/content/10/3/R25)
- 2012 Bowtie 2 - [Langmead and Salzberg](http://www.nature.com/nmeth/journal/v9/n4/full/nmeth.1923.htm)
- 2009 BWA - [Li and Durbin](http://bioinformatics.oxfordjournals.org/content/25/14/1754.long)
- 2010 BWA - [Li and Durbin](http://bioinformatics.oxfordjournals.org/content/26/5/589)
- 2013 BWA-MEM - [Li](http://arxiv.org/abs/1303.3997)

### Mapping against a pre-computed genome index

Mappers usually compare reads against a reference sequence that has been transformed into a highly accessible data structure called genome index. Such indexes should be generated before mapping begins. Galaxy instances typically store indexes for a number of publicly available genome builds. 

>
> {{< figure src="/BMMB554/img/cached_genome.png" >}}
>
> Mapping against a pre-computed index in Galaxy

For example, the image above shows indexes for `hg38` version of the human genome. You can see that there are actually three choices: (1) `hg38`, (2) `hg38 canonical` and (3) `hg38 canonical female`. The `hg38` contains all chromosomes as well as all unplaced contigs. The `hg38 canonical` does not contain unplaced sequences and only consists of chromosomes 1 through 22, X, Y, and mitochondria. The 
`hg38 canonical female` contains everything from the canonical set with the exception of chromosome Y. 

The following video show mapping using BWA:

{{<vimeo 123102338>}}

