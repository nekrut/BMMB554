# Variant calling in microbes

## Notes on microbial population genetics

-----

[![](https://i.imgur.com/uwW3jYK.png)](https://docs.google.com/presentation/d/1m8-EYIm8tp--tY47gB9nboPCvvv068PrEdQeR0XvLjQ/edit?usp=sharing)

From Dykhuizen & Hartl, [1983](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC281569/)

-----

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


