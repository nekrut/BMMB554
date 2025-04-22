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



## Particularities of variant calling

### Indels = trouble

Left aligning of indels (a variant of re-aligning) is extremely important for obtaining accurate variant calls. For illustrating how left-aligning works, we expanded on an example provided by Tan et al. [2015](https://doi.org/10.1093/bioinformatics/btv112). Suppose you have a reference sequence and a sequencing read:


```
Reference GGGCACACACAGGG
Read      GGGCACACAGGG
```

If you look carefully you will see that the read is simply missing a `CA` repeat. But it is not apparent to a mapper, so some of possible alignments and corresponding variant calls include:

```
Alignment                 Variant Call

GGGCACACACAGGG            Ref: CAC
GGGCAC--ACAGGG            Alt: C

GGGCACACACAGGG            Ref: ACA
GGGCA--CACAGGG            Alt: A

GGGCACACACAGGG            Ref: GCA
GGG--CACACAGGG            Alt: G
```

### Things to be aware of

[Erik Garrison](https://github.com/ekg) has a beautiful illustration of various biases potentially affecting called variants and making a locus sequence-able.

-----

![](https://i.imgur.com/eDP2Eu6.png)

 Here you can see that in an ideal case (indicated with a green star) a variant is evenly represent by different areas of sequencing reads (cycle and placement biases) and is balanced across the two strands (strand bias). Allele imbalance is not applicable in our case as it reflects significant deviation from the diploid (50/50) expectation.
 
-----

### Strand bias computation

----

[![](https://i.imgur.com/Z5Snfsa.png)](https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-13-666)

Various strand bias (SB) measures from Guo et al. [2012](https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-13-666.)

----

### `lofreq` - the most appropriate variant caller

----

![](https://i.imgur.com/Dr60qnr.png)

Model for evaluating variant calls (Wilm et al. [2012](https://academic.oup.com/nar/article/40/22/11189/1152727)).


The development of modern genomic tools and formats have been driven by large collaborative initiatives such as 1,000 Genomes, GTEx and others. As a result the majority of current variant callers have been originally designed  for diploid genomes of human or model organisms where discrete allele frequencies are expected. Bacterial and viral samples are fundamentally different. They are represented by mixtures of multiple haploid genomes where the frequencies of individual variants are continuous. This renders many existing variant calling tools unsuitable for microbial and viral studies unless one is looking for fixed variants. However, recent advances in cancer genomics have prompted developments of somatic variant calling approaches that do not require normal ploidy assumptions and can be used for analysis of samples with chromosomal malformations or circulating tumor cells. The latter situation is essentially identical to viral or bacterial resequencing scenarios. As a result of these developments the current set of variant callers appropriate for microbial studies includes updated versions of “legacy” tools ([`FreeBayes`](https://github.com/ekg/freebayes) and `mutect2` (a part of [GATK](https://github.com/broadinstitute/gatk)) as well as dedicated packages ([`Breseq`](https://github.com/barricklab/breseq), [`SNVer`](http://dx.doi.org/10.1093/nar/gkr599), and [`lofreq`](https://github.com/CSB5/lofreq)). To assess the applicability of these tools we first considered factors related to their long-term sustainability, such as the health of the codebase as indicated by the number of code commits, contributors and releases as well as the number of citations. After initial testing we settled on three callers: `FreeBayes`, `mutect2`, and `lofreq` (Breseq’s new “polymorphism mode” has been in experimental state at the time of testing. `SNVer` is no longer actively maintained). `FreeBayes` contains a mode specifically designed for finding sites with continuous allele frequencies; `Mutect2` features a so called mitochondrial mode, and `lofreq` was specifically designed for microbial sequence analysis. 

### Benchmarking callers: `lofreq` is the best choice

Our goal was to identify variants in mixtures of multiple haplotypes sequenced at very high coverage. Such dataset are typical in modern bacterial and viral genomic studies. In addition, we are seeking to be able to detect variants with frequencies around the NGS detection threshold of ~ 1% ([Salk et al. 2018](http://dx.doi.org/10.1038/nrg.2017.117)). In order to achieve this goal we selected a test dataset, which is distinct from data used in recent method comparisons ([Bush et al. 2019](http://dx.doi.org/10.1101/653774); [Yoshimura et al. 2019](http://dx.doi.org/10.1099/mgen.0.000261)). These data originate from a duplex sequencing experiment recently performed by our group ([Mei et al. 2019](https://academic.oup.com/gbe/article/11/10/3022/5572121)).  In this dataset a population of *E. coli* cells transformed with pBR322 plasmid is maintained in a turbidostat culture for an extensive period of time. Adaptive changes accumulated within the plasmid are then revealed with duplex sequencing ([Schmitt et al. 2012](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Citation&list_uids=22853953)). Duplex sequencing allows identification of variants at very low frequencies. This is achieved by first tagging both ends of DNA fragments to be sequenced with unique barcodes and subjecting them to paired-end sequencing. After sequencing read pairs containing identical barcodes are assembled into families. This procedure allows to reliably separate errors introduced during library preparation and/or sequencing (present in some but not all members of a read family) from true variants (present in all members of a read family derived from both strands).

For the following analysis we selected two data points from [Mei et al. 2019](https://academic.oup.com/gbe/article/11/10/3022/5572121): one corresponding to the beginning of the experiment (s0) and the other to the end (s5). The first sample is expected to be nearly clonal with no variation, while the latter contains a number of adaptive changes with frequencies around 1%. We aligned duplex consensus sequences (DCS) against the pBR322. We then walked through read alignments to produce counts of non-reference bases at each position (Fig. 1). 

-------

![](https://i.imgur.com/5q6znPd.png)

<small>**Figure 1.** Counts of alternative bases at eight variable locations within pBR322.</small>

-------

Because all differences identified this way are derived from DCS reads they are a reasonable approximation for a “true” set of variants. s0 and s5 contained 38 and 78 variable sites with at least two alternative counts, respectively (among 4,361 bases on pBR322) of which 27 were shared. We then turned our attention to the set of sites that were determined by Mei et al. to be under positive selection (sites 3,029, 3,030, 3,031, 3,032, 3,033, 3,034, 3,035, 3,118). Changes at these sites increase the number of plasmid genomes per cell. Sample s0 does not contain alternative bases at any of these sites. Results of the application of the three variant callers with different parameter settings (shown in Table 2) are summarized in Fig. 2. 

------

![](https://i.imgur.com/Wmz3TsM.png)

<small>**Figure 2.** Calls made by `mutect2`, `freebayes`, and `lofreq`. For explanation of x-axis labels see Table 1.</small>

------

The `lofreq` performed the best followed by `mutect2` and `FreeBayes` (contrast "Truth" with "nf" and "def" in Fig. 2). The main disadvantage of `mutect2` is in its handling of multiallelic sites (e.g., 3,033 and 3,118) where multiple alternative bases exist. At these sites `mutect2` outputs alternative counts for only one of the variants (the one with highest counts; this is why at site 3,118 A and T counts are identical). Given these results we decided to use `lofreq` for the main analysis of the data.

<small>**Table 2.** Command line options for each caller.</small>

| Caller | Command line | Figure 2 label |
|:-------|:-------------|:--------------|
| `mutect2` | `--mitochondria-mode true` | m |
| `mutect2` | default | m_noM |
| `mutect2` | `--mitochondria-mode true --f1r2-max-depth 1000000` | m_md_inf |
| `mutect2` | `--mitochondria-mode true --f1r2-max-depth 1000000 -max-af 1`  | m_md_inf_max_af1 |
| `freebayes` | `--haplotype-length 0 --min-alternate-fraction 0.001 --min-alternate-count 1 --pooled-continuous --ploidy 1` | hl-0_maf-001_pc |
| `freebayes` | `-min-alternate-fraction 0.001 --pooled-continuous --ploidy 1` | maf-001_pc |
| `lofreq` | `--no-default-filter` | nf |
| `lofreq` | default | def |



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

Sure! Let’s walk through a **Bayesian approach to genotyping a diploid SNP**, with a detailed explanation of each step.

---

## The Problem

Imagine we want to determine the genotype at a particular **biallelic SNP** site in a **diploid** organism (e.g., human). The possible genotypes are:

- **AA** (homozygous reference)
- **AB** (heterozygous)
- **BB** (homozygous alternate)

We observe **sequencing reads** that cover this SNP, each reporting a base (either A or B), possibly with errors.

---

## Example Data

Let's say we have:

- **Total reads:** 10
- **Observed bases:**
  - A: 7 reads
  - B: 3 reads
- **Sequencing error rate (ε):** 1% = 0.01

We want to compute the **posterior probability** of each genotype given the data:

$$
P(\text{Genotype} \mid \text{Data})
$$

using **Bayes’ theorem**:

$$
P(G \mid D) = \frac{P(D \mid G) \cdot P(G)}{P(D)}
$$

Where:
- $ G \in \{AA, AB, BB\} $
- $$ D $$: observed reads
- $$ P(G) $$: prior probability of genotype
- $$ P(D \mid G) $$: likelihood
- $$ P(D) $$: normalization constant

---

## Step-by-Step Calculation

### Step 1: Define Priors

Assume a uniform prior:
- $$ P(AA) = P(AB) = P(BB) = 1/3 $$

### Step 2: Compute Likelihoods

We assume that each read is an **independent** observation.

Let’s compute \( P(D \mid G) \) for each genotype:

#### For AA (only A is correct):
- Each A read has probability ≈ 0.99 (correct base)
- Each B read has probability ≈ 0.01 (error)

\[
P(D \mid AA) = (0.99)^7 \cdot (0.01)^3
\]

#### For AB (A and B equally likely):
- Each read has a 0.5 chance of being from either allele.
- So:
  - A read: probability = \(0.5 \cdot 0.99 + 0.5 \cdot 0.01 = 0.5\)
  - B read: same thing = 0.5

\[
P(D \mid AB) = (0.5)^{10}
\]

#### For BB (only B is correct):
- A read: 0.01 (error)
- B read: 0.99

\[
P(D \mid BB) = (0.01)^7 \cdot (0.99)^3
\]

---

### Step 3: Compute Unnormalized Posteriors

Multiply each likelihood by prior:

- \( P(AA \mid D) \propto (0.99)^7 \cdot (0.01)^3 \cdot \frac{1}{3} \)
- \( P(AB \mid D) \propto (0.5)^{10} \cdot \frac{1}{3} \)
- \( P(BB \mid D) \propto (0.01)^7 \cdot (0.99)^3 \cdot \frac{1}{3} \)

Let’s compute these numerically:

```python
aa = (0.99**7)*(0.01**3)*(1/3)
ab = (0.5**10)*(1/3)
bb = (0.01**7)*(0.99**3)*(1/3)

total = aa + ab + bb
paa = aa / total
pab = ab / total
pbb = bb / total

paa, pab, pbb
```

This gives approximately:

- \( P(AA \mid D) ≈ 0.92 \)
- \( P(AB \mid D) ≈ 0.08 \)
- \( P(BB \mid D) ≈ \text{very small (≈0)} \)

---

## Final Interpretation

- **Most likely genotype: AA** (92% posterior probability)
- **AB** is possible but much less likely
- **BB** is extremely unlikely given the observed data

---

## Why Bayesian?

Bayesian reasoning allows you to:
- Incorporate prior knowledge (e.g., population frequencies)
- Explicitly model sequencing error
- Get **posterior probabilities**, not just point estimates

---

Let me know if you want a version that incorporates **allele frequency priors** from population data (e.g., Hardy-Weinberg), or if you want to visualize this in Python!

Ultimately:

----

![](https://i.imgur.com/4ZSvZlM.png)

Polybayes formula. Image by [Aaron Quinlan](http://quinlanlab.org/). 

-----

## Haplotype-based variant calling

is implemented is the current *de facto* stabdard tools such as [FreeBayes](https://github.com/freebayes/freebayes) or [GATK](https://gatk.broadinstitute.org/hc/en-us):

![](https://i.imgur.com/CZVQgXW.png)

