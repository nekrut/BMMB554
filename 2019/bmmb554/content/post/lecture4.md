---
date: "2019-01-16"
tags: ["python", "conditionals","working with files","TnSeq"]
title: "Lecture 4: Python refresher 2"
---

[![](https://imgs.xkcd.com/comics/standards.png)](https://xkcd.com/927/)

# Conditionals, Loops, and Files

<div class="alert alert-info" role="alert">
  This material is heavily inspired by <a href="http://pycam.github.io/">Materials for the course run by the Graduate School of Life Sciences, University of Cambridge</a> with some modifications.
</div>

# Let's get started

 - Point your browser to http://colab.research.google.com
 - Open notebook `2019/ipynb/intro2.ipynb` from `https://github.com/nekrut/BMMB554`

# Case study: Transposon insertion sequencing (TnSeq)

Transposon insertion allows genome-wide identification of essential genes. The idea is simple = important genes cannot be disrupted and there will not accept any transposon insertions.  

<div class="card mb-3">
  <img class="card-img-top" src="/BMMB554/img/nrmicro.2015.7-f1.jpg" alt="Card image cap">
  <div class="card-footer">
    	<footer class="blockquote-footer">
    		An overview of transposon insertion sequencing from <a href="https://www.nature.com/articles/nrmicro.2015.7">a review</a> by Chao et al. 2016. <hr>
    		<b>a</b> | A high-density transposon insertion library containing multiple insertions in every non-essential genomic locus is created and then grown under different conditions (for example, selective (condition B) and non-selective (condition A)), and mutants that are viable under each condition are recovered. The transposon junctions in the selected and non-selected pools are attached to sequencing adaptors and amplified, then subjected to high-throughput sequencing. <b>b</b> | The sequences are mapped to the genome and the read counts at each insertion site are subjected to statistical analysis to define the genomic loci that seem significantly underrepresented under the selective growth condition (conditionally essential loci, blue box). The insertions in the non-selected library (condition A) can also be statistically evaluated to define essential loci (orange box) that are required for growth under optimal conditions. In highly saturated libraries (see high-saturation graph), non-essential and essential genes are easily distinguishable; conversely, many non-essential genes are likely to not have been disrupted by chance in less saturated libraries (see low-saturation graph).
    	</footer>
  	</div>
</div>

[Tim Meredith](https://bmb.psu.edu/directory/txm50) from PennState and colleagues developed [a more advanced version of TnSeq](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-015-1361-3) that alters gene expression level. 

<div class="card mb-3">
  <img class="card-img-top" src="/BMMB554/img/tnseq_santiago2015.png" alt="Card image cap">
  <div class="card-footer">
    	<footer class="blockquote-footer">
    		From Santiago et al. <a href="https://doi.org/10.1186/s12864-015-1361-3">2015</a>.<hr>
    		Protocol for the preparation of a high quality transposon DNA library for NGS. (A) (1) Genomic DNA is isolated and digested with NotI. High molecular weight DNA is selectively precipitated using an 8%PEG + NaCl solution, and transposon-plasmid junctions (106 bp) are removed in the supernatant. A biotinylated dsDNA adapter with NotI overhang is ligated (2) before digestion with MmeI, which cuts non-specifically 20 bp from its recognition site within ITR2 into the genome to liberate biotinylated-transposon-genome junctions as short DNA fragments (114 bp). (3). Biotinylated fragments are bound to streptavidin beads (4), and an Illumina sequencing primer adapter containing an indexing barcode and MmeI compatible ends is ligated (5). Primers annealing to the P7 site and the Illumina sequencing primer adapter sequence (with a P5 site overhang) are used to PCR amplify the transposon-genome junctions (6), agarose gel purified, and submitted for Illumina sequencing (7). NGS reads capture both the 16-bp of flanking genomic DNA as well as the transposon donor specific barcode located between the P7 and ITR2. (B) Fragments arising from transposon-plasmid junctions are removed by size selective PEG-NaCl precipitation, while the remaining fragments lack both P7 annealing sites and MmeI sites for ligation of the Illumina sequencing primer adapter. These fragments are therefore not amplified in step (6) of 4A. (C) By performing the size-selective precipitation on a 1 kb DNA ladder, we show that small 300 bp fragments of DNA are retained in the solution (SN), while larger DNA is precipitated (P). (D) Six transposon donor constructs were multiplexed and designed to attenuate expression of genes proximal to the insertion site according to the regulatory elements located at the ends of the transposon backbone. Each donor can be identified from NGS reads by the unique 3 bp barcode.
    	</footer>
  	</div>
</div>

We will review the analysis of TnSeq data in greater detail once we are done with programming and quantitative basics. For now let's assume that the data is already processed and exists in the following format:

```
NC_007795.1     2500004 2500006 4.0     3.0     1.0     1.0     2.0     10.0
NC_007795.1     2500008 2500010 3.0     11.0    0.0     1.0     2.0     11.0
NC_007795.1     2500020 2500022 4.0     13.0    8.0     2.0     5.0     13.0
NC_007795.1     2500022 2500024 27.0    15.0    8.0     3.0     7.0     18.0
NC_007795.1     2500031 2500033 27.0    13.0    8.0     3.0     6.0     23.0
NC_007795.1     2500033 2500035 26.0    12.0    8.0     3.0     5.0     23.0
NC_007795.1     2500037 2500039 28.0    12.0    6.0     5.0     7.0     16.0
NC_007795.1     2500043 2500045 6.0     11.0    6.0     4.0     5.0     10.0
```

where columns are as follows:

 1. Chromosome ID (in this case simply genome name)
 2. Start cooredinate
 3. End coordinate
 4. Read count for `blunt`
 4. Read count for `cap`
 4. Read count for `dual_pen`
 4. Read count for `erm`
 4. Read count for `pen`
 4. Read count for `tuf`

Let's use these data to practice file access operation in python. Files can be found here:

 - [Small file](/BMMB554/tnseq_data_short.txt)
 - [Large file](/BMMB554/tnseq_data.txt)

 We will use `intro2.ipynb` notebook to process these files



