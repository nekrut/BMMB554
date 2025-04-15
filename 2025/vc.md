# Variant calling (aka "Resequencing")

## SAM/BAM datasets

The [SAM/BAM](https://samtools.github.io/hts-specs/SAMv1.pdf) format is an accepted standard for storing aligned reads (it can also store unaligned reads and some mappers such as BWA are accepting unaligned BAM as input). The binary form of the format (BAM) is compact and can be rapidly searched (if indexed). In Galaxy BAM datasets are always indexed (accompanies by a .bai file) and sorted in coordinate order. In the following duscussion I once again rely on [tutorial](http://chagall.med.cornell.edu/RNASEQcourse/Intro2RNAseq.pdf) by Friederike D&uuml;ndar, Luce Skrabanek, and Paul Zumbo.

The Sequence Alignment/Map (SAM) format is, in fact, a generic nucleotide alignment format that describes the alignment of sequencing reads (or query sequences) to a reference. The human readable, TABdelimited SAM files can be compressed into the Binary Alignment/Map format. These BAM files are bigger than simply gzipped SAM files, because they have been optimized for fast random access rather than size reduction. Position-sorted BAM files can be indexed so that all reads aligning to a locus can be efficiently retrieved without loading the entire file into memory.

As shown below, SAM files typically contain a short header section and a very long alignment section where each row represents a single read alignment. The following sections will explain the SAM format in a bit more detail. For the most comprehensive and updated information go to https://github.com/samtools/hts-specs.

------
![](https://i.imgur.com/ibK6sLg.png)

Schematic representation of a SAM file. Each line of the optional header section starts with “@”, followed by the appropriate abbreviation (e.g., SQ for sequence dictionary which lists all chromosomes names (SN) and their lengths (LN)). The vast majority of lines within a SAM file typically correspond to read alignments where each read is described by the 11 mandatory entries (black font) and a variable number of optional fields (grey font). From [tutorial](http://chagall.med.cornell.edu/RNASEQcourse/Intro2RNAseq.pdf) by Friederike D&uuml;ndar, Luce Skrabanek, and Paul Zumbo.

------

### SAM Header

The header section includes information about how the alignment was generated and stored. All lines in the header section are tab-delimited and begin with the “@” character, followed by tag:value pairs, where tag is a two-letter string that defines the content and the format of value. For example, the “@SQ” line in the header section contains the information about the names and lengths of the *reference sequences to which the reads were aligned. For a hypothetical organism with three chromosomes of length 1,000 bp, the SAM header should contain the following three lines:

```
@SQ SN:chr1 LN:1000
@SQ SN:chr2 LN:1000
@SQ SN:chr3 LN:1000
```

### SAM alignment section

The optional header section is followed by the alignment section where each line corresponds to one sequenced read. For each read, there are 11 mandatory fields that always appear in the same order:

```
<QNAME> <FLAG> <RNAME> <POS> <MAPQ> <CIGAR> <MRNM> <MPOS> <ISIZE> <SEQ> <QUAL>
```

If the corresponding information is unavailable or irrelevant, field values can be ‘0’ or ‘*’ (depending on the field, see below), but they cannot be missing! After the 11 mandatory fields, a variable number of optional fields can be present. Here’s an example of one single line of a real-life SAM file (you may need to scroll sideways):

```
ERR458493 .552967 16 chrI 140 255 12 M61232N37M2S * 0 0 CCACTCGTTCACCAGGGCCGGCGGGCTGATCACTTTATCGTGCATCTTGGC BB?HHJJIGHHJIGIIJJIJGIJIJJIIIGHBJJJJJJHHHHFFDDDA1+B NH:i:1 HI:i:1 AS:i:41 nM:i:2
```

The following table explains the format and content of each field. The `FLAG`, `CIGAR`, and the optional fields (marked in blue) are explained in more detail below. The number of optional fields can vary widely between different SAM files and even between reads within in the same file. The field types marked in blue are explained in more detail in the main text below.

-----

![](https://i.imgur.com/7ix4oFy.png)

###### SAM fields. From SAM/BAM spec [document](https://samtools.github.io/hts-specs/SAMv1.pdf)

-----

### `FLAG` field

The FLAG field encodes various pieces of information about the individual read, which is particularly important for PE reads. It contains an integer that is generated from a sequence of Boolean bits (0, 1). This way, answers to multiple binary (Yes/No) questions can be compactly stored as a series of bits, where each of the single bits can be addressed and assigned separately.

The following table gives an overview of the different properties that can be encoded in the FLAG field. The developers of the SAM format and samtools tend to use the hexadecimal encoding as a means to refer to the different bits in their documentation. The value of the FLAG field in a given SAM file, however, will always be the decimal representation of the sum of the underlying binary values (as shown in Table below, row 2).

------

![](https://i.imgur.com/kBiYRb0.png)

The `FLAG` field of SAM files stores information about the respective read alignment in one single decimal number. The decimal number is the sum of all the answers to the Yes/No questions associated with each binary bit. The hexadecimal representation is used to refer to the individual bits (questions). A bit is set if the corresponding state is true. For example, if a read is paired, `0x1` will be set, returning the decimal value of 1. Therefore, all `FLAG` values associated with paired reads must be uneven decimal numbers. Conversely, if the `0x1` bit is unset (= read is not paired), no assumptions can be made about `0x2`, `0x8`, `0x20`, `0x40` and `0x80` because they refer to paired reads. From [tutorial](http://chagall.med.cornell.edu/RNASEQcourse/Intro2RNAseq.pdf) by Friederike D&uuml;ndar, Luce Skrabanek, and Paul Zumbo

-----

In a run with single reads, the flags you most commonly see are:

- 0: This read has been mapped to the forward strand. (None of the bit-wise flags have been set.)
- 4: The read is unmapped (`0x4` is set).
- 16: The read is mapped to the reverse strand (`0x10` is set)

(`0x100`, `0x200` and `0x400` are not used by most aligners/mappers, but could, in principle be set for single reads.) Some common `FLAG` values that you may see in a PE experiment include:


|     Value                |               Meaning                       |
----------------------|---------------------------------------
|**69** (= 1 + 4 + 64) | The read is paired, is the first read in the pair, and is unmapped.|
|**77** (= 1 + 4 + 8 + 64) | The read is paired, is the first read in the pair, both are unmapped.|
|**83** (= 1 + 2 + 16 + 64) | The read is paired, mapped in a proper pair, is the first read in the pair, and it is mapped to the reverse strand.|
|**99** (= 1 + 2 + 32 + 64) | The read is paired, mapped in a proper pair, is the first read in the pair, and its mate is mapped to the reverse strand.|
|**133** (= 1 + 4 + 128) | The read is paired, is the second read in the pair, and it is unmapped.|
|**137** (= 1 + 8 + 128) | The read is paired, is the second read in the pair, and it is mapped while its mate is not.|
|**141** (= 1 + 4 + 8 + 128) | The read is paired, is the second read in the pair, but both are unmapped.|
|**147** (= 1 + 2 + 16 + 128) | The read is paired, mapped in a proper pair, is the second read in the pair, and mapped to the reverse strand.|
|**163** (= 1 + 2 + 32 + 128) | The read is paired, mapped in a proper pair, is the second read in the pair, and its mate is mapped to the reverse strand.|

A useful website for quickly translating the FLAG integers into plain English explanations like the ones shown above is: https://broadinstitute.github.io/picard/explain-flags.html

### `CIGAR` string

`CIGAR` stands for *Concise Idiosyncratic Gapped Alignment Report*. This sixth field of a SAM file
contains a so-called CIGAR string indicating which operations were necessary to map the read to the reference sequence at that particular locus.

The following operations are defined in CIGAR format (also see figure below):

- **M** - Alignment (can be a sequence match or mismatch!)
- **I** - Insertion in the read compared to the reference
- **D** - Deletion in the read compared to the reference
- **N** - Skipped region from the reference. For mRNA-to-genome alignments, an N operation represents an intron. For other types of alignments, the interpretation of N is not defined.
- **S** - Soft clipping (clipped sequences are present in read); S may only have H operations between them and the ends of the string
- **H** - Hard clipping (clipped sequences are NOT present in the alignment record); can only be present as the first and/or last operation
- **P** - Padding (silent deletion from padded reference)
- **=** - Sequence match (not widely used)
- **X** - Sequence mismatch (not widely used)

The sum of lengths of the **M**, **I**, **S**, **=**, **X** operations must equal the length of the read. Here are some examples:

------

![](https://i.imgur.com/xtj0guO.png)

CIGAR string examples. From [tutorial](http://chagall.med.cornell.edu/RNASEQcourse/Intro2RNAseq.pdf) by Friederike D&uuml;ndar, Luce Skrabanek, and Paul Zumbo

-----

### Optional fields

Following the eleven mandatory SAM file fields, the optional fields are presented as key-value
pairs in the format of `<TAG>:<TYPE>:<VALUE>`, where `TYPE` is one of:

- `A` - Character
- `i` - Integer
- `f` - Float number
- `Z` - String
- `H` - Hex string

The information stored in these optional fields will vary widely depending on the mapper and new tags can be added freely. In addition, reads within the same SAM file may have different numbers of optional fields, depending on the program that generated the SAM file. Commonly used optional tags include:

- `AS:i` - Alignment score
- `BC:Z` - Barcode sequence
- `HI:i` - Match is i-th hit to the read
- `NH:i` - Number of reported alignments for the query sequence
- `NM:i` - Edit distance of the query to the reference
- `MD:Z` - String that contains the exact positions of mismatches (should complement the CIGAR string)
- `RG:Z` - Read group (should match the entry after ID if @RG is present in the header.

Thus, for example, we can use the NM:i:0 tag to select only those reads which map perfectly to the reference(i.e., have no mismatches). While the optional fields listed above are fairly standardized, tags that begin with `X`, `Y`, and `Z` are reserved for particularly free usage and will never be part of the official SAM file format specifications. `XS`, for example, is used by TopHat (an RNA-seq analysis tool we will discuss later) to encode the strand information (e.g., `XS:A:+`) while Bowtie2 and BWA use `XS:i:` for reads with multiple alignments to store the alignment score for the next-best-scoring alignment (e.g., `XS:i:30`).

### Read Groups

One of the key features of SAM/BAM format is the ability to label individual reads with readgroup tags. This allows pooling results of multiple experiments into a single BAM dataset. This significantly simplifies downstream logistics: instead of dealing with multiple datasets one can handle just one. Many downstream analysis tools such as variant callers are designed to recognize readgroup data and output results on per-readgroup basis.

One of the best descriptions of BAM readgroups is on [GATK support site](https://gatkforums.broadinstitute.org/discussion/1317/collected-faqs-about-bam-files). We have gratefully stolen two tables describing the most important readgroup tags - `ID`, `SM`, `LB`, and `PL` - from GATK forum and provide them here:

------

![](https://i.imgur.com/zUSpOtc.png)

Key ReadGroup tags.

-----


GATK forum also provides the following example:

-------

![](https://i.imgur.com/8VB86Pv.png)

Examples of ReadGroup use provided by GATK

------

### Manipulating SAM/BAM datasets

We support four major toolsets for processing of SAM/BAM datasets:

 * [DeepTools](https://deeptools.readthedocs.io) - a suite of user-friendly tools for the visualization, quality control and normalization of data from deep-sequencing DNA sequencing experiments.
 * [SAMtools](http://www.htslib.org/) - various utilities for manipulating alignments in the SAM/BAM format, including sorting, merging, indexing and generating alignments in a per-position format.
 * [BEDtools](https://bedtools.readthedocs.io/en/latest/) - a toolkit originally written for BED format was expanded for analysis of BAM and VCF datasets.
 * [Picard](https://broadinstitute.github.io/picard/) - a set of Java tools for manipulating high-throughput sequencing data (HTS) data and formats.

## Diploid variant calling

## Key references

- [Genotype and SNP calling from next-generation sequencing data](https://www.nature.com/articles/nrg2986)
- [A general approach to single-nucleotide polymorphism discovery](https://www.nature.com/articles/ng1299_452)
- [Haplotype-based variant detection from short-read sequencing](https://arxiv.org/pdf/1207.3907.pdf)



Variant calling is a complex field that was significantly propelled by advances in DNA sequencing and efforts of large scientific consortia such as the [1000 Genomes](http://www.1000genomes.org). Here we summarize basic ideas central to Genotype and Variant calling. First, let's contrast the two things although they often go together:

 * **Variant calling** - identification of positions where the sequenced sample is different from the reference sequence (or [reference genome graph](https://github.com/vgteam/vg));
 * **Genotype calling** - identifying individual's genotype at variable sites.

A typical workflow for variation discovery involves the following steps (e.g., see Nielsen et al. [2011](http://www.nature.com/nrg/journal/v12/n6/full/nrg2986.html)):

 1. Mapping reads against the reference genome
 2. Thresholding BAM datasets by, for example, retaining paired, properly mapped reads
 3. Performing quality score recalibration
 4. Performing realignment
 5. Performing variant calling/genotype assignment
 6. Performing filtering and genotype quality score recalibration
 7. Annotating variants and performing downstream analyses

However, continuing evolution of variant detection methods has made some of these steps obsolete. For instance, omitting quality score recalibration and re-alignment (steps 3 and 4 above) when using haplotype-aware variant callers such as [FreeBayes](https://github.com/ekg/freebayes) does not have an effect on the resulting calls (see Brad Chapman's methodological comparisons at [bcbio](http://bit.ly/1S9kFJN)). Before going forward with an actual genotype calling in Galaxy let's take a look as some basic ideas behind modern variant callers.

Consider a set of sequencing reads derived from a diploid individual:

```
REFERENCE: atcatgacggcaGtagcatat
--------------------------------
READ1:     atcatgacggcaGtagcatat
READ2:         tgacggcaGtagcatat
READ3:     atcatgacggcaAtagca
READ4:            cggcaGtagcatat
READ5:     atcatgacggcaGtagc
```

The capitalized position contains a G &#8594; A [transition](https://en.wikipedia.org/wiki/Transition_(genetics)). So, in principle this can be a heterozygous site with two alleles **G** and **A**. A commonly used naïve procedure would define a site as *heterozygous* if there is a non-reference allele with frequency between 20% and 80%. In this case **A** is present in 1/5 or 20% of the cases, so we can say that this is a heterozygous site. Yet it is only represented by a single read and thus is hardly reliable. Here are some of the possibilities that would explain this *variant*. It can be:

 * A true variant
 * Experimental artifact: A library preparation error (e.g., PCR-derived)
 * Base calling error
 * Analysis error: A misalignment (though unlikely in the above example)

## Types of genetic variation

You can have a SNP:

```
ctcCgag
ctcTgag
```

An indel:

```
atgcttgc
atg--tgc
```

Or a structural variant that can an extra block like this

```
tgcc-------------------------------------agtgc
tgcc------A very large insertion here----agtgc
```

or inversion, duplication, and so on...

## Somatic versus germline

All cells have genomes and all can accumulate mutations. However, mutations within *somatic* cells cannot be passed to the next generation:

-----

![](https://i.imgur.com/zECo5Gh.png)

Somatic versus Germilne. Image by [Aaron Quinlan](http://quinlanlab.org/). 
    
-----

## Fate of mutations in population

Selection and drift affect the dynamics of mutations in the population:

----

![](https://i.imgur.com/2Aw6sOi.png)

Selection and drift. Image by [Aaron Quinlan](http://quinlanlab.org/). 

-----

In addition, sampling issues such as *Bottleneck* can have dramatic effect on allele frequencies:

-----

![](https://i.imgur.com/rGJ3l1V.png)

Bottleneck effect. Image by [Aaron Quinlan](http://quinlanlab.org/). 

-----

## Humans are diploid

You inherit two haplotypes: one from mom and one from dad:

> (all images from [Aaron Quinlan](http://quinlanlab.org/))

![](https://i.imgur.com/OW79ZPB.png)

Recombination during meiosis breaks the linkage pattern:

![](https://i.imgur.com/ZYMV40T.png)

For mechanical reasons the frequency of recombination is proportional to the physical distance across the chromosome. Before the physical units were known the distance between chromosomal landmarks (e.g., genes) were measured in centimorgans (cM), which is really a measure of recombination frequency:

![](https://i.imgur.com/HpDsHp3.png)

This brings us to the concept of Lunkage (dis)equilibrium. If recombination is equally likely for any genome position, there is linkage equlibrium:

![](https://i.imgur.com/KW4Nd9r.png)

However, we often see a non-random association (linkage) like this:

![](https://i.imgur.com/guxoWjP.png)

Thus genotypes can be predicted (imputed), when some variants are known. 

## Calling heterozygotes is not easy

When finding variants in diploid genomes there are three possible outcomes:

1. Homozygous for the "reference" allele:

![](https://i.imgur.com/TeIwgd1.png)

2. Homozygous for alternative allele

![](https://i.imgur.com/SANFBN4.png)

3. Heterozygous for alternative allele

![](https://i.imgur.com/XfS6Y5r.png)

So, are the following reads derived from homo- or heterozygote?

```
REFERENCE: atcatgacggcaGtagcatat
--------------------------------
READ1:     atcatgacggcaGtagcatat
READ2:         tgacggcaGtagcatat
READ3:     atcatgacggcaAtagca
READ4:            cggcaGtagcatat
READ5:     atcatgacggcaGtagc
```

## Coverage is important

In this case we are dealing with discrete events: a site at a given position can be either (1) Reference (<font color="green">Success</font>) or (2) Alternate allele (<font color="red">Failure</font>). These can be modeled as draws from [Binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution) where the probability of $k$ successes in $n$ trials is:

$$
P(X=k)=\binom{n}{k} p^k p^{n-k}
$$

Putting this is biological context given the number of reads ($n$) and probability of seeing reference or alternate (0.5) we can compute the number of successes (reference alleles) using the following python code:

```python=
binom.rvs(n,p,size=size)
```
You can run it in this [notebook](https://colab.research.google.com/github/nekrut/BMMB554/blob/master/2021/ipynb/binomial.ipynb). Let's play with it to see how coverage would affect assessing heterozygous sites.

## Bayes Theorem: Math behind main variant callers

> About Bayes -> https://youtu.be/K2proaXGERU?feature=shared

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

Suppose at a given site you have the following arrangement:

```
aaaaaaaccc
```

Here $C$ is a SNP and $A$ is Reference (no SNP). In this configuration the probability of having an $A$ is $P(A)=\frac{7}{10}$ and probability of having a $C$ is $P(C)=\frac{3}{10}$

Now, let's suppose that you only observe nucleotides that are shown in UPPER CASE:

```
aaaaaAACcc
```

what is the probability of $AAC$? It is $P(AAC)=\frac{3}{10}$. Now let's make it more interesting. First, let's call $ACC$ observed data ($O$). 

What is the probability of $O$ given $A$: 

$$
P(O|A)=\frac{2}{7}
$$

What is the probability of $O$ given $C$:

$$
P(O|C)=\frac{1}{3}
$$

Now, let's change the direction. What is the probability of having a SNP($C$) or no SNP ($A$) given the observed data:

$$
P(A|O)=\frac{2}{3}\\
P(C|O)=\frac{1}{3}
$$

Now, let's go back to Bayes formula again. What is the probability of having $A$ given the observed data $O$:

$$
P(A|O)=\frac{P(O|A)P(A)}{P(O)}=\frac{\frac{2}{7}\times\frac{7}{10}}{\frac{3}{10}}=\frac{2}{3}
$$

What is the probability of having $C$ given the observed data $O$:

$$
P(C|O)=\frac{P(O|C)P(C)}{P(O)}=\frac{\frac{1}{3}\times\frac{3}{10}}{\frac{3}{10}}=\frac{1}{3}
$$

In this formula:
- $P(A|O)$ is *poterior probability*
- $P(A)$ is prior probability of $A$

In generic form this would look like this:

$$
P(SNP|Data)=\frac{P(Data|SNP)P(SNP)}{P(Data)}
$$

Let's look at this example:

```
ACACGCTAgCTAGCT
      TAgCT       Q = 20
     CTAaCT       Q = 10
        gCTAGC    Q = 50
```

we need to compute the probability of observed genotype (homozygote for $C$) given the data:

$$
P(G|D)=\frac{P(D|G)P(G)}{P(D)}
$$

Here:

- $P(D|G)$ - conditional probability of data given genotype that we would calculate below
- $P(G)$ - a prior informed by previous studies as well as by properties of the data
- $P(D)$ - is a constant as it is the same for all genotypes

So ...

$$
P(D|G)=\prod_{j=1}^{3}(\frac{P(D_j|H_1)}{2}+\frac{P(D_j|H_2)}{2})\\
P(b1 = G|AG)=\frac{1}{2}((1-10^{-2})+\frac{10^{-2}}{3})\\
P(b2 = A|AG)=\frac{1}{2}((1-10^{-2})+\frac{10^{-2}}{3})\\
P(b3 = G|AG)=\frac{1}{2}((1-10^{-2})+\frac{10^{-2}}{3})
$$

Ultimately:

----

![](https://i.imgur.com/4ZSvZlM.png)

Polybayes formula. Image by [Aaron Quinlan](http://quinlanlab.org/). 

-----

## Haplotype-based variant calling

is implemented is the current *de facto* stabdard tools such as [FreeBayes](https://github.com/freebayes/freebayes) or [GATK](https://gatk.broadinstitute.org/hc/en-us):

![](https://i.imgur.com/CZVQgXW.png)

