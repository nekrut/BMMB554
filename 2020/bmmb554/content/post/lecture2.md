---
date: "2020-01-27"
tags: ["sequencing", "sanger","illumina","pacbio","oxford nanopore"]
title: "Lecture 2: What is the nature of sequencing data?"
---
![png](/BMMB554/img/illumina_pseudocolor.png)

# The 50s, 60s and the 70s

The difficulty with sequencing nucleic acids is nicely summarized by [Hutchinson:2007](http://dx.doi.org/10.1093/nar/gkm688):

> 1. The chemical properties of different DNA molecules were so similar that it appeared difficult to separate them.
> 2. The chain length of naturally occurring DNA molecules was much greater than for proteins and made complete sequencing seems unapproachable.
> 3. The 20 amino acid residues found in proteins have widely varying properties that had proven useful in the separation of peptides. The existence of only four bases in DNA therefore seemed to make sequencing a more difficult problem for DNA than for protein.
> 4. No base-specific DNAases were known. Protein sequencing had depended upon proteases that cleave adjacent to certain amino acids.

It is therefore not surprising that protein-sequencing was developed before DNA sequencing by [Sanger and Tuppy:1951](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1197535/). 

tRNA was the first complete nucleic acid sequenced (see pioneering work of [Robert Holley and colleagues](http://www.jstor.org/stable/1715055) and also [Holley's Nobel Lacture](https://www.nobelprize.org/nobel_prizes/medicine/laureates/1968/holley-lecture.pdf)). Conceptually, Holley's approach was similar to Sanger's protein sequencing: break molecule into small pieces with RNases, determine sequences of small fragments, use overlaps between fragments to reconstruct (assemble) the final nucleotide sequence. 

The work on finding approaches to sequencing DNA molecules began in late 60s and early 70s. One of the earliest contributions has been made by Ray Wu (Cornell) and Dave Kaiser (Stanford), who used _E. coli_ DNA polymerase to [incorporate radioactively labelled nucleotides into protruding ends of bacteriphage lambda](http://www.sciencedirect.com/science/article/pii/S0022283668800129?via%3Dihub). It took several more years for the development of more "high throughput" technologies by Sanger and Maxam/Gilbert. The Sanger technique has ultimately won over Maxam/Gilbert's protocol due to its relative simplicity (once dideoxynucleotides has become commercially available) and the fact that it required smaller amount of starting material as the polymerase was used to generate fragments necessary for sequence determination. 

## [Sanger/Coulson](http://www.sciencedirect.com/science/article/pii/0022283675902132?via%3Dihub) plus/minus method

This methods builds on idea of Wu and Kaiser (for *minus* part) and on special property of DNA polymerase isolated from phage T4 (for *plus* part). The schematics of the method is given in the following figure:

|          |
|----------|
|![png](/BMMB554/img/plus_minus_1975.png)|
|<small>**Plus/minus method**. From [Sanger & Coulson: 1975](http://www.sciencedirect.com/science/article/pii/0022283675902132?via%3Dihub)</small>|
<hr>

In this method a primer and DNA polymerase is used to synthesize DNA in the presence of P<sup>32</sup>-labeled nucleotides (only one of four is labeled). This generates P<sup>32</sup>-labeled copies of DNA being sequenced. These are then purified and (without denaturing) separated into two groups: *minus* and *plus*. Each group is further divided into four equal parts. 

In the case of *minus* polymerase and a mix of nucleotides minus one are added to each of the four aliquotes: ACG (-T), ACT (-G), CGT (-A), AGT (-C). As a result in each case DNA strand is extended up to a missing nucleotide. 


In the case of plus only one nucleotide is added to each of the four aliquotes (+A, +C, +G, and +T) and T4 DNA polymerase is used. T4 DNA polymerase acts as an exonuclease that would degrade DNA from 3'-end up to a nucleotide that is supplied in the reaction. 

The products of these are loaded into a denaturing polyacrylamide gel as a eight tracks (four for minus and four for plus):

|          |
|----------|
| ![png](/BMMB554/img/plus_minus_gel.png) |
|<small>**Plus/minus method gel radiograph**. From [Sanger & Coulson: 1975](http://www.sciencedirect.com/science/article/pii/0022283675902132?via%3Dihub)</small>|
<hr>


## Maxam/Gilbert chemical cleavage method

In this method DNA is terminally labeled with P<sup>32</sup>, separated into four equal aliquotes.  Two of these are treated with [Dimethyl sulfate (DMSO)](https://en.wikipedia.org/wiki/Dimethyl_sulfate) and remaining two are treated with [hydrazine](https://en.wikipedia.org/wiki/Hydrazine). 

DMSO methylates G and A residues. Treatment of DMSO-incubated DNA with alkali at high temperature will break DNA chains at G and A with Gs being preferentially broken, while treatment of DMSO-incubated DNA with acid will preferentially break DNA at As. Likewise treating hydrazine-incubated DNA with [piperidine](https://en.wikipedia.org/wiki/Piperidine) breaks DNA at C and T, while DNA treated with hydrazine in the presence of NaCl preferentially brakes at Cs. The four reactions are then loaded on a gel generating the following picture:

|          |
|----------|
| ![png](/BMMB554/img/maxam_gilbert_gel.png) |
|<small>**Radiograph of Maxam/Gilbert gel**. From [Maxam & Gilbert: 1977](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC392330/pdf/pnas00024-0174.pdf)</small>|
<hr>


## Sanger dideoxy method

The original Sanger +/- method was not popular and had a number of technical limitations. In a new approach Sanger took advantage of inhibitors that stop the extension of a DNA strand at particular nucleotides. These inhibitors are dideoxy analogs of normal nucleotide triphosphates:

|          |
|----------|
| ![png](/BMMB554/img/sanger_ddntp_gel.png) |
|<small>**Sanger ddNTP gel**. From [Sanger:1977](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC431765/pdf/pnas00043-0271.pdf)</small>|
<hr>


# Original approaches were laborious

In the original [Sanger paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC431765/pdf/pnas00043-0271.pdf) the authors sequenced bacteriophage phiX174 by using its own restriction fragments as primers. This was an ideal set up to show the proof of principle for the new method. This is because phiX174 DNA is homogeneous and can be isolated in large quantities. Now suppose that you would like to sequence a larger genome (say _E. coli_). Remember that the original version of Sanger method can only sequence fragments up to 200 nucleotides at a time. So to sequence the entire _E. coli_ genome (which by-the-way was not sequenced until [1997](http://science.sciencemag.org/content/277/5331/1453)) you would need to split the genome into multiple pieces and sequence each of them individually. This is hard, because to produce a readable Sanger sequencing gel each sequence must be amplified to a suitable amount (around 1 nanogram) and be homogeneous (you cannot mix multiple DNA fragments in a single reaction as it will be impossible to interpret the gel). Molecular cloning enabled by the availability of commercially available restriction enzymes and cloning vectors simplified this process. Until the onset of next generation sequencing in 2005 the process for sequencing looked something like this:

* (**1**) - Generate a collection of fragments you want to sequence. It can be a collection of fragments from a genome that was mechanically sheared or just a single fragment generated by PCR.
* (**2**) - These fragment(s) are then cloned into a plasmid vector (we will talk about other types of vectors such as BACs later in the course).
* (**3**) - Vectors are transformed into bacterial cells and positive colonies (containing vectors with insert) are picked from an agar plate.
* (**4**) - Each colony now represents a unique piece of DNA. 
* (**5**) - An individual colony is used to seed a bacterial culture that is grown overnight.
* (**6**) - Plasmid DNA is isolated from this culture and now can be used for sequencing because it is (1) homogeneous and (2) we now a sufficient amount.
* (**7**) - It is sequenced using universal primers. For example the image below shows a map for pGEM-3Z plasmid (a pUC18 derivative). Its multiple cloning site is enlarged and sites for **T7** and **SP6** sequencing primers are shown. These are the **pads** I'm referring to in the lecture. These provide universal sites that can be used to sequence any insert in between. 

|                     |
|---------------------|
| ![png](/BMMB554/img/pgem3z.png) |
|<small>**pGEM-3Z**. Figure from Promega, Inc.</small>| 
<hr>

Until the invention of NGS the above protocol was followed with some degree of automation. But you can see that it was quite laborious if the large number of fragments needed to be sequenced. This is because each of them needed to be subcloned and handled separately. This is in part why Human Genome Project, a subject of our next lecture, took so much time to complete. 

## Evolution of sequencing machines

The simplest possible sequencing machine is a [gel rig with polyacrylamide gel](https://en.wikipedia.org/wiki/Polyacrylamide_gel_electrophoresis). Sanger used it is his protocol obtaining the following results:

|                     |
|---------------------|
| ![png](/BMMB554/img/sangerGel.png) |
|<small>Figure from [Sanger et al. 1977](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC431765/pdf/pnas00043-0271.pdf).</small>|
<hr>

Here for sequencing each fragment four separate reactions are performed (with ddA, ddT, ggC, and ddG) and four lanes on the gel are used. [One simplification of this process](http://www.jstor.org/stable/pdf/2879539.pdf) that came in the 90s was to use fluorescently labeled dideoxy nucleotides. This is easier because everything can be performed in a single tube and uses a single lane on a gel:

|                     |
|---------------------|
| ![png](/BMMB554/img/dd_labels.png) |
|<small>Figure from Applied Biosystems [support site](https://www3.appliedbiosystems.com/cms/groups/mcb_support/documents/generaldocuments/cms_041003.pdf).</small>|
<hr>

However, there is still substantial labor involved in pouring the gels, loading them, running machines, and cleaning everything post-run. A significant improvement was offered by the development of capillary electrophoresis allowing automation of liquid handling and sample loading. Although several manufacturers have been developing and selling such machines a _de facto_ standard in this area was (and still is) the Applied Biosystems (ABI) Genetics and DNA Anlayzer systems. The highest throughput ABI system, 3730_xl_, had 96 capillaries and could automatically process 384 samples. 

# NGS!

384 samples may sound like a lot, but it is nothing if we are sequencing an entire genome. The beauty of NGS is that these technologies are not bound by sample handling logistics. They still require preparation of libraries, but once a library is made (which can be automated) it is processed more or less automatically to generate multiple copies of each fragment (in the case of 454, Illumina, and Ion Torrent) and loaded onto the machine, where millions of individual fragments are sequenced simultaneously. The following videos and slides explains how these technologies work.

## Watch introductory video

{{< vimeo 181072208 >}}

# NGS in depth


## 1: 454 sequencing 

454 Technology is a massively parallel modification of [pyrosequencing](http://genome.cshlp.org/content/11/1/3) technology. Incorporation of nucleotides are registered by a [CCD](https://en.wikipedia.org/wiki/Charge-coupled_device) camera as a flash of light generated from the interaction between ATP and Luciferin. The massive scale of 454 process is enabled by generation of a population of beads carrying multiple copies of the same DNA fragment. The beads are distributed across a microtiter plate where each well of the plate holding just one bead. Thus every unique coordinate (a well) on the plate generates flashes when a nucleotide incorporation event takes plate. This is "monochrome" technique: flash = nucleotide is incorporated; lack of flash = no incorporation. Thus to distinguish between A, C, G, and T individual nucleotides are "washed" across the microtiter plate at discrete times: if **A** is being washed across the plate and a flash of light is emitted, this implies that A is present in the fragment being sequenced. 

454 can generated fragments up 1,000 bases in length. Its biggest weakness is inability to precisely determine the length of [homopolymer runs](https://www.broadinstitute.org/crd/wiki/index.php/Homopolymer). Thus the main type if sequencing error generated by 454 are insertions and deletions (indels).

### Slides

<script async class="speakerdeck-embed" data-id="28bd628499b54d09b4f9c6e7534c7e8f" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>


### Video

{{< vimeo 121286060 >}}

Underlying slides are [here](https://speakerdeck.com/nekrut/ngs-technologies-454#)

## Reading

* 2001 | [Overview of pyrosequencing methodology - Ronaghi](http://genome.cshlp.org/content/11/1/3)
* 2005 | [Description of 454 process - Margulies et al.](http://www.nature.com/nature/journal/v437/n7057/pdf/nature03959.pdf)
* 2007 | [History of pyrosequencing - Pål Nyrén](http://link.springer.com/protocol/10.1385/1-59745-377-3:1)
* 2007 | [Errors in 454 data - Huse et al. ](http://genomebiology.com/content/pdf/gb-2007-8-7-r143.pdf)
* 2010 | [Properties of 454 data - Balzer et al.](http://bioinformatics.oxfordjournals.org/content/26/18/i420.full.pdf+html)

# A few classical papers to start

In a series of now classical papersp Philip Green and co-workers has developed a quantitative framework for the analysis of data generated by automated DNA sequencers. 

|          |
|----------|
|[![](/BMMB554/img/ewing_green1.png)](http://genome.cshlp.org/content/8/3/175.full)|
|[![](/BMMB554/img/ewing_green2.png)](http://genome.cshlp.org/content/8/3/186.full)|
|<small>**Two papers** were published back to back in *Genome Research*.|
	<hr>

In particular they developed a standard metric for describing the reliability of base calls:

>An important technical aspect of our work is the use of log-transformed error probabilities rather than untransformed ones, which facilitates working with error rates in the range of most importance (very close to 0). Specifically, we define the quality value q assigned to a base-call to be<br><br>
>$q = -10\times log_{10}(p)$<br><br>
> where p is the estimated error probability for that base-call. Thus a base-call having a probability of 1/1000 of being incorrect is assigned a quality value of 30. Note that high quality values correspond to low error probabilities, and conversely.

We will be using the concept of "*quality score*" or "*phred-scaled quality score*" repeatedly in this course. 

# Illumina

Illumina (originally called "Solexa") uses glass flowcells with oligonucleotides permanently attached to internal surface. These oligonucleotides are complementary to sequencing adapters added to DNA fragments being sequenced during library preparation. The DNA fragments that are "stuck" on the flowcell due to complementary interaction between adapters are amplified via "bridge amplification" to form clusters. Sequencing is performed using reversible terminator chemistry with nucleotides modified to carry dyes specific to each base. As a result all nucleotides can be added at once and are distinguished by color. Currently, it is possible to sequence up to 300 bases from each end of the fragment being sequenced. Illumina has the highest throughput (and lowest cost per base) of all existing technologies at this moment. The NovaSeq 6000 machine can produce [6000 billion nucleotides in 44 hours](https://www.illumina.com/systems/sequencing-platforms.html). In this course we will most often work with Illumina data.

## NextSeq two dye system:

|          |
|----------|
|![](https://www.illumina.com/content/dam/illumina-marketing/images/science/v2/web-graphic/sbs-redgreen-web-graphic.jpg)|
|<small>**NextSeq** uses [two dye](https://www.illumina.com/science/technology/next-generation-sequencing/sequencing-technology/2-channel-sbs.html) system.</small>|

<hr>

### Slides

<script async class="speakerdeck-embed" data-id="942908c8c24546d58cf8b61b3598feb3" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

### Video

{{< vimeo 121178846 >}}

### Reading

* 2008 | [Human genome sequencing on Illumina - Bentley et al.](http://www.nature.com/nature/journal/v456/n7218/pdf/nature07517.pdf)
* 2010 | [Data quality 1 - Nakamura et al.](http://nar.oxfordjournals.org/content/39/13/e90.full-text-lowres.pdf)
* 2011 | [Data quality 2 - Minoche et al.](http://genomebiology.com/content/pdf/gb-2011-12-11-r112.pdf)
* 2011 | [Illumina pitfalls - Kircher et al.](http://www.biomedcentral.com/content/pdf/1471-2164-12-382.pdf)

### 10X: A way to extend the utility of short Illumina reads

A company called [10X Genomics](http://www.10xgenomics.com/technology/) has developed a technology which labels reads derived from continuous fragments of genomic DNA. In this technology a gel bead covered with a large number of adapter molecules is placed within a droplet containing PCR reagents and one or several long molecules of genomic DNA to be sequenced.

|          |
|----------|
| ![](/BMMB554/img/10x.png) |
|<small>**10X bead** containing the standard Illumina P5 adapter combined with barcode, sequencing primer annealing site (R1) and random primer (N-mer) Slide from [Slideshare](http://www.slideshare.net/GenomeInABottle/aug2015-analysis-team-04-10x-genomics).</small>|
<hr>

The droplets are generated by combining beads, PCR reagents, and genomic DNA in a microfluidic device:

|          |
|----------|
| [![](/BMMB554/img/10x-overview.jpg)](http://www.nature.com/nbt/journal/v34/n3/fig_tab/nbt.3432_F1.html) |
|<small>**10X workflow** (**a**) Gel beads loaded with primers and barcoded oligonucleotides are mixed with DNA and enzyme mixture then oil-surfactant solution at a microfluidic 'double-cross' junction. Gel bead–containing droplets flow to a reservoir where gel beads are dissolved, initiating whole-genome primer extension. The products are pooled from each droplet. The final library preparation requires shearing the libraries and incorporation of Illumina adapters. (**b**) Top, linked reads of the ALK gene from the NA12878 WGS sample. Lines represent linked reads; dots represent reads; color indicates barcode. Middle, exon boundaries of the ALK gene. Bottom, linked reads of the ALK gene from the NA12878 exome data. Reads from neighboring exons are linked by common barcodes. Only a small fraction of linked reads is presented here. Reproduced from [Zheng:2015](http://www.nature.com/nbt/journal/v34/n3/full/nbt.3432.html) (click the image to go to the original paper).</small>|
<hr>

In essence, 10X allows to uniquely map reads derived from long genomic fragments. This information is essential for bridging together genome and transcriptome assemblies as we will see in later in this course. 

{{< vimeo 120429438 >}}

[![](https://raw.githubusercontent.com/rrwick/Basecalling-comparison/master/images/logo.png)](https://github.com/rrwick/Basecalling-comparison)

# PacBio Single Molecule Sequencing

PacBio is a fundamentally different approach to DNA sequencing as it allows reading single molecules. Thus it is an example is so called _Single Molecule Sequencing_ or _SMS_. PacBio uses highly processive DNA polymerase placed at the bottom of each well on a microtiter plate. The plate is fused to the glass slide illuminated by a laser. When polymerase is loaded with template it attracts fluorescently labeled nucleotides to the bottom of the well where they emit light with a wavelength characteristic of each nucleotide. As a result a "movie" is generated for each well recording the sequence and duration of incorporation events. One of the key advantage of PacBio technology is its ability to produce long reads with ones at 10,000 bases being common. 

### Slides

<script async class="speakerdeck-embed" data-id="ccb3d34f1a214f66ac7a2d233caedaf5" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

And another set of slides from [@biomonika](https://twitter.com/biomonika?lang=en):

<script async class="speakerdeck-embed" data-id="5850fe7ede3b45df816c3eaa502ea3d1" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

### Video

{{< vimeo 121267426 >}}

Underlying slides are [here](https://speakerdeck.com/nekrut/ngs-technologies-pacific-biosceinces)

### Reading

* 2015 | [Resolving complex regions in Human genomes with PacBio - Chaisson et al.](http://dx.doi.org/10.1038/nature13907)
* 2014 | [Transcriptome with PacBio - Taligner et al.](http://www.pnas.org/cgi/doi/10.1073/pnas.1400447111)
* 2012 | [Error correction of PacBio reads - Koren et al.](http://www.nature.com/nbt/journal/v30/n7/pdf/nbt.2280.pdf)
* 2010 | [Modification detection with PacBio - Flusberg et al.](http://www.nature.com/nmeth/journal/v7/n6/pdf/nmeth.1459.pdf)
* 2009 | [Real Time Sequencing with PacBio - Eid et al.](http://www.sciencemag.org/content/323/5910/133.full)
* 2008 | [ZMW nanostructures - Korlach et al.](http://www.pnas.org/content/105/4/1176.full)
* 2003 | [Single Molecule Analaysis at High Concentration - Levene et al.](http://www.sciencemag.org/content/299/5607/682.full.pdf)

# Oxford Nanopore

Oxford nanopore is another dramatically different technology that threads single DNA molecules through biologically-derived (transmembrane proteins) pore in a membrane impermeable to ions. It uses a motor protein to control the speed of translocation of the DNA molecule through membrane. In that sense it is not _Sequencing by synthesis_ we have seen in the other technologies discussed here. This technology generates longest reads possible today: in many instances a single read can be hundreds of thousands if nucleotides in length. It still however suffers from high error rate and relatively low throughput (compared to Illumina). On the upside Oxford Nanopore sequencing machines are only slightly bigger than a thumb-drive and cost very little. 

### Slides

<script async class="speakerdeck-embed" data-id="3895a3069bc64ad5bc74c972a0353911" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

A recent overview of latest developments at Oxford Nanopore can be found [here](https://github.com/lmmx/talk-transcripts/blob/master/Nanopore/NoThanksIveAlreadyGotOne.md) as well as in the following video

{{< youtube nizGyutn6v4 >}}

### Reading

* 2018 | [Comparison of Oxford Nanopore basecalling tools](https://github.com/rrwick/Basecalling-comparison)
* 2017 | [The long reads ahead: de novo genome assembly using the MinION](https://f1000research.com/articles/6-1083/v2)
* 2016 | [The promises and challenges of solid-state sequencing](http://nature.com/nnano/journal/v11/n2/full/nnano.2016.9.html)
* 2015 | [Improved data analysis for the minion nanopore sequencer](http://nature.com/nmeth/journal/v12/n4/full/nmeth.3290.html)
* 2015 | [MinION Analysis and Reference Consortium](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4722697/)
* 2015 | [A complete bacterial genome assembled *de novo* using only nanopore sequencing data](http://www.nature.com/nmeth/journal/v12/n8/full/nmeth.3444.html)
* 2012 | [Reading DNA at single-nucleotide resolution with a mutant MspA nanopore and phi29 DNA polymerase](http://nature.com/nbt/journal/v30/n4/full/nbt.2171.html)
* Simpson Lab [blog](http://simpsonlab.github.io/2015/04/08/eventalign/)
* Poretools analysis [suite](http://poretools.readthedocs.org/)
* Official Nanopore [videos](https://vimeo.com/208466748)

# Other weird stuff

There were of course other sequencing technologies. Most notably SOLiD, Complete Genomics, and Ion Torrent. The slides below briefly summarize these:

<script async class="speakerdeck-embed" data-id="52845e932e004b88b63a76b327b2402e" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>


### Reading 

* SOLiD | [A high-resolution, nucleosome position map of C. elegans reveals a lack of universal sequence-dictated positioning](http://dx.doi.org/10.1101/gr.076463.108)
* Complete Genomics | [Human genome sequencing using unchained base reads on self-assembling DNA nanoarray](http://dx.doi.org/10.1126/science.1181498)
* Ion Torrent | [An integrated semiconductor device enabling non-optical genome sequencing](http://dx.doi.org/10.1038/nature10242)


