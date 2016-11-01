+++
#draft = true
tags = [
]
categories = [
]
featureimage = "img/topic9_cover.png"
menu = ""
date = "2016-10-31T10:11:10-04:00"
title = "Non-diploid variant calling"
description = "**Topic 9** | Finding variants in mixed samples"

+++

The majority of life on Earth is non-diploid and represented by prokaryotes, viruses and their derivatives such as our own mitochondria or plant's chloroplasts. In non-diploid systems allele frequencies can range anywhere between 0 and 100% and there could be multiple (not just two) alleles per locus. The main challenge associated with non-diploid variant calling is the difficulty in distinguishing between sequencing noise (abundant in all NGS platforms) and true low frequency variants. Some of the early attempts to do this well have been accomplished on human mitochondrial DNA although the same approaches will work equally good on viral and bacterial genomes:

* 2014 | [Maternal age effect and severe germ-line bottleneck in the inheritance of human mitochondrial DNA](http://www.pnas.org/content/111/43/15474.abstract)
* 2015 | [Extensive tissue-related and allele-related mtDNA heteroplasmy suggests positive selection for somatic mutations](http://www.pnas.org/content/112/8/2491.abstract).

# Calling variants in non-diploid systems

As an example of non-diploid system we will be using human mitochondrial genome as an example. However, this approach will also work for most bacterial and viral genomes as well.

## Mapping or assembling

There are two ways one can call variants: 

1. By comparing reads against an existing genome assembly
2. By assembling genome first and then mapping against that assembly

>![](/BMMB554/img/ref_vs_assembly.jpg)
>
> This figure from a manuscript by [Olson:2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4493402/) contrasts the two approaches.

In this tutorials we will take the *first* path is which we map reads against an existing assembly. Later in the course (after we learn about assembly approaches) we will try the second approach as well. 

## Finding variants in human mitochondria

The goal of this example is to detect heteroplasmies (variants within mitochondrial DNA). Mitochondria is transmitted maternally and heteroplasmy frequencies may change dramatically and unpredictably during the transmission, due to a germ-line bottleneck [Cree:2008](http://www.nature.com/ng/journal/v40/n2/abs/ng.2007.63.html). As we mentioned above the procedure for finding variants in bacterial or viral genomes will be essentially the same.

### The data

[A Galaxy Library](https://usegalaxy.org/library/list#folders/Fe4842bd0c37b03a7) contains datasets representing a child and a mother. These datasets are obtained by paired-end Illumina sequencing of human genomic DNA enriched for mitochondria. The enrichment was performed using long-range PCR with two primer pairs that amplify the entire mitochondrial genome. This means that these samples still contain a lot of DNA from the nuclear genome, which, in this case, is a contaminant. 

But first lets import data into Galaxy:

>![](/BMMB554/img/mt_lib.png)
>
>Select four datasets from [a library](https://usegalaxy.org/library/list#folders/Fe4842bd0c37b03a7) and click **to History**. 

Let's QC the datasets first by running  **NGS: QC and manipulation &#8594; FastQC**:

>![](/BMMB554/img/mt_qc.png)
>
>QC'ing reads using [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/). Note that we selected all four datasets at once by pressing the middle button ![](/BMMB554/img/mt_middle_button.png) adjacent to the **Short read data from your current history** widget. 

The data have generally high quality in this example:

>![](/BMMB554/img/mt_qc_plot.png)
>
>FastQC plot for one of the mitochondrial datasets shows that qualities are acceptable for 250 bp reads (mostly in the green, which is at or above [phred score](https://en.wikipedia.org/wiki/Phred_quality_scorescore) of 30). 

### Mapping the reads

Our reads are long (250 bp) and as a result we will be using [bwa mem](https://arxiv.org/pdf/1303.3997v2.pdf) to align them against the reference genome as it has good mapping performance for longer reads (100bp and up).

>![](/BMMB554/img/mt_bwa_mem.png)
>
>Running `bwa mem` on our datasets. Look **carefully** at parameter settings:
>
> * We select `hg38` version of the human genome as the reference
> * By using the middle button again ![](/BMMB554/img/mt_middle_button.png) we select datasets 1 and 3 as **Select the first set of reads** and datasets 2 and 4 as **Select the second set of reads**. Galaxy will automatically launch two bwa-mem jobs using datasets 1,2 and 3,4 generating two resulting BAM files.
> * By setting **Set read groups information** to `Set read groups (SAM/BAM specifications) and clicking **Auto-assign** we will ensure that the reads in the resulting BAM dataset are properly set.

<hr color="red">

### <font color="red">&#9888; Reminder</font>

We already learned about read groups. Read again [here](/BMMB554/post/topic7/).

<hr color="red">

### Merging BAM datasets

Because we have set read groups we can now merge the two BAM dataset into one. This is because read groups label each read as belonging to either mother or child. 

We can BAM dataset using **NGS: Picard** &#8594; **MergeSAMFiles** tool:

>![](/BMMB554/img/mt_bam_merging.png)
>
>Merging two BAM datasets into one. Note that two inputs are highlighted. 

### Removing duplicates

Recall from our [earlier material](/BMMB554/post/topic7/):

>Preparation of sequencing libraries (at least at the time of writing) for technologies such as Illumina (used in this examples) involves PCR amplification. It is required to generate sufficient number of sequencing templates so that a reliable detection can be performed by base callers. Yet PCR has it's biases, which are especially profound in cases of multitemplate PCR used for construction of sequencing libraries (Kanagawa et al. [2003](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=16233530)). 
>
>Duplicates can be identified based on their outer alignment coordinates or using sequence-based clustering. One of the common ways for identification of duplicate reads is the `MarkDuplicates` utility from [Picard](https://broadinstitute.github.io/picard/command-line-overview.html) package. It is designed to identify both PCR and optical duplicates:
>
>Duplicates are identified as read pairs having identical 5' positions (coordinate and strand) for both reads in a mate pair (and optionally, matching unique molecular identifier reads; see BARCODE_TAG option). Optical, or more broadly Sequencing, duplicates are duplicates that appear clustered together spatially during sequencing and can arise from optical/imagine-processing artifacts or from bio-chemical processes during clonal amplification and sequencing; they are identified using the READ_NAME_REGEX and the OPTICAL_DUPLICATE_PIXEL_DISTANCE options. The tool's main output is a new SAM or BAM file in which duplicates have been identified in the SAM flags field, or optionally removed (see REMOVE_DUPLICATE and REMOVE_SEQUENCING_DUPLICATES), and optionally marked with a duplicate type in the 'DT' optional attribute. In addition, it also outputs a metrics file containing the numbers of READ_PAIRS_EXAMINED, UNMAPPED_READS, UNPAIRED_READS, UNPAIRED_READ DUPLICATES, READ_PAIR_DUPLICATES, and READ_PAIR_OPTICAL_DUPLICATES. Usage example: java -jar picard.jar MarkDuplicates I=input.bam \ O=marked_duplicates.bam M=marked_dup_metrics.txt.`

Let's use **NGS: Picard** &#8594; **MarkDuplicates** tool:

>![](/BMMB554/img/mt_dedup.png)
>
>De-duplicating the merged BAM dataset

**MarkDuplicates** produces a BAM dataset with duplicates removed and also a metrics file. Let's take a look at the metrics data:

```
raw_child-ds-	55	27551	55	50	1658	0	0.061026	219628
raw_mother-ds-	96	54972	96	90	4712	0	0.086459	302063
```

where columns are:

- LIBRARY (read group in our case)
- UNPAIRED_READS_EXAMINED
- READ_PAIRS_EXAMINED-
- UNMAPPED_READS
- UNPAIRED_READ_DUPLICATES
- READ_PAIR_DUPLICATES
- READ_PAIR_OPTICAL_DUPLICATES
- PERCENT_DUPLICATION
- ESTIMATED_LIBRARY_SIZE

In other words the two datasets had ~6% and ~9% duplicates, respectively. 

### Left-aligning indels

Left aligning of indels (a variant of re-aligning) is extremely important for obtaining accurate variant calls. This concept, while not difficult, requires some explanation. For illustrating how left-aligning works we expanded on an example provided by [Tan:2015](http://bioinformatics.oxfordjournals.org/content/31/13/2202.abstract). Suppose you have a reference sequence and a sequencing read mapping to it:


```
GGGCACACACAGGG
GGGCACACAGGG
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

The last of these is *left-aligned*. In this case gaps (dashes) as moved as far left as possible (for a formal definition of left-alignment and variant normalization see [Tan:2015](http://bioinformatics.oxfordjournals.org/content/31/13/2202.abstract)). 

Let's perform left alignment using **NGS: Variant Analysis** &#8594; **BamLeftAlign**:

>![](/BMMB554/img/mt_left_align.png)
>
>Left-aligning a de-duplicated BAM dataset

### Filter reads

Remember that we are trying to call variants in mitochondrial genome. Let focus only on the reads derived from the mitochondrial genome by filtering everything else out. For this we will use **NGS: BamTools** &#8594; **Filter**:

>![](/BMMB554/img/mt_filtering.png)
>
>Filtering reads. There are several important point to note here:
>
>- **mapQuality** is set to &#8925; 20 Mapping quality reflects the probability that the read is placed *incorrectly*. It uses [phred scale](https://en.wikipedia.org/wiki/Phred_quality_scorescore). Thus 20 is 1/100 or 1% chance that the read is incorrectly mapped. By setting this parameter to &#8925; 20 we will keep all reads that have 1% or less probability of being mapped incorrectly. 
>- *isPaired* will eliminate singleton (unpaired) reads (make sure **Yes** is clicked on)
>- *isProperPair* will only keep reads that map to the same chromosome and are properly placed (again, make sure **Yes** is clicked)
>- *reference* is set to *chrM* 

### Call variants

Here we will call variants using two tools: [FreeBayes](https://github.com/ekg/freebayes) and [Naive Variant Caller](https://github.com/blankenberg/tools-blankenberg/tree/master/tools/naive_variant_caller).

#### FreeBayes







