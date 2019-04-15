---
date: "2019-04-14"
tags: ["Assembly"]
title: "Lecture 18: Hybrid assembly of a small genome"
---	

# The data

In this section we will describe practical aspects of genome assembly. As an example data we will use sequencing reads obtained for E. coli strain [C-1](http://cgsc.biology.yale.edu/Strain.php?ID=8232). Isolated genomic DNA was sequenced on Illumina miSeq and Oxford Nanopore MinION:

* **miSeq data** - 9,345,897 250 bp read pairs (library preparation performed on genomic DNA fragmented to main size of 600 bp)
* **minION data** - 12,738 [2d-reads](http://www.nature.com/nmeth/journal/v12/n4/fig_tab/nmeth.3290_SF13.html). Maximum read length was 27,518. The distribution of reads lengths is shown below:

>![](/BMMB554/img/onp_length.png)

# The assembler

In this example we have two types of data: (1) high quality high coverage but relatively short (250 bp) Illumina data and (2) low quality low coverage but long Oxford Nanopore (ONP) data. This would allow us to perform so called Hybrid assembly. In hybrid assembly long low quality reads produced by ONP will allow bridge contigs assembled from Illumina reads into a fully assembled bacterial genome. 

Currently, one of the best performing tools for hybrid assembly is [hybridSPAdes](http://bioinformatics.oxfordjournals.org/content/early/2015/11/20/bioinformatics.btv688.full.pdf+html), a part of [SPAdes family](http://cab.spbu.ru/software/spades/) of genome, metagenome, and transcriptome assemblers.  

## Key SPAdes innovations

Before briefly explaining some key aspects of the SPAdes assembler we should mention one practical issue. In the previous section we assumed that sequencing reads have identical lengths. In reality this is almost never the case. Thus we cannot assume that reads and *k*-mers are the same thing. Instead, we derive *k*-mers from the reads by breaking them into pieces:

```
atgcgt  <- read

atgc
 tgcg   <- its k-mers of length 4
  gcgt
```


### Multisized deBruijn graph

In the previous lecture we have been constructing graphs for *k*-mers of a fixed size. We have noted that when *k* is small it is difficult to resolve the repeats. If *k* is too high a corresponding graph may become fragments (especially if read coverage is low). SPAdes uses several values for *k* (that are either manually set or inferred automatically) to create a *multisized* graph that minimized tangledness and fragmentation by combining various *k*-mers:

>![](/BMMB554/img/multiGraph.jpeg)
>
>**Multisized de Bruijn graph**. A circular Genome CATCAGATAGGA is covered by a set Reads consisting of nine 4-mers, {ACAT, CATC, ATCA, TCAG, CAGA, AGAT, GATA, TAGG, GGAC}. Three out of 12 possible 4-mers from Genome are missing from Reads (namely {ATAG,AGGA,GACA}), but all 3-mers from Genome are present in Reads. (A) The outside circle shows a separate black edge for each 3-mer from Reads. Dotted red lines indicate vertices that will be glued. The inner circle shows the result of applying some of the glues. (B) The graph DB(Reads, 3) resulting from all the glues is tangled. The three h-paths of length 2 in this graph (shown in blue) correspond to h-reads ATAG, AGGA, and GACA. Thus Reads3,4 contains all 4-mers from Genome. (C) The outside circle shows a separate edge for each of the nine 4-mer reads. The next inner circle shows the graph DB(Reads, 4), and the innermost circle represents the Genome. The graph DB(Reads, 4) is fragmented into 3 connected components. (D) The multisized de Bruijn graph DB(Reads, 3, 4). (From [Bankevich:2012](http://online.liebertpub.com/doi/full/10.1089/cmb.2012.0021)).

### Read pair utilization

While the use of paired reads and mate pairs is not new (and key) to genome assembly, SPAdes utilizes so called paired DeBruin graphs to take the advantage of the paired end data. One of the key issues with paired DeBruin graphs is the resulting genome assemblies do not tolerate variability in insert sizes (the initial formulation of paired DeBruijn graphs assumed constant distance between pairs of reads). In practice this distance is always variable. SPAdes performs *k*-bimer (these are *k*-mers derived from *paired* reads) adjustment to identify exact of nearly-exact distances for each *k*-bimer pair:

>![](/BMMB554/img/k-bimer.jpeg)
>
>**k-bimer adjustment**. **A**. Bireads are decomposed into pairs of k-mers with estimated genomic distances (B-transformation). These are tabulated into histograms of estimated genomic distances between pairs of h-edges (H-transformation), and peaks in the histograms and paths in the graph are used to reveal the actual genomic distances between h-edges (A-transformation). This may be converted back to genomic distances between k-mers on pairs of h-paths (E-transformation, used for presentation purposes but not needed in the implementation). **B**. The h-biedge histogram (α|β,&#42;) corresponding to the exact h-biedge (α|β, 72163) in the assembly graph. path(α) is an h-path (condensed edge representing 72049 edges) in the upper right, and path(β) is an h-path (representing 46097 edges) at the lower left. The histogram collects all distance estimates between α and β derived from bireads. The h-biedge histogram was smoothed using the Fast Fourier Transform (red curve). The peak in the smoothed histogram (marked red) well approximates the actual distance (marked blue). **C**. The h-biedge histogram (α|β,&#42;) estimates the distance between h-edges α and β (|path(α)| = 46054, |path(β)| = 72). Because of the directed cycle formed by the two h-paths of lengths 72 and 13, there may be multiple walks through the graph between α and β. The h-biedge histogram has been divided into clusters with centers at 46060 and 46145. Thus SPAdes transforms the entire histogram into two h-biedges: (α|β, 46054) and (α|β, 46139). (From [Bankevich:2012](http://online.liebertpub.com/doi/full/10.1089/cmb.2012.0021)).

### Error correction

Sequencing data contains a substantial number of sequencing errors that manifest themselves as deviations (bulges and non-connected components) within the assembly graph. One of the ways to improve the graph even constructing it is to minimize the amount sequencing errors by performing error correction. SPAdes uses [BayesHammer](https://goo.gl/1iGkMe) to correct the reads. Here is a brief summary of what it does:

1. SPAdes (or rather BayesHammer) counts *k*-mers in reads and computed *k*-mer statistics that takes into account base quality values. 
2. [Hamming graph](https://en.wikipedia.org/wiki/Hamming_graph) is constructed for *k*-mers is which *k*-mers are nodes. In this graph edges connect nodes (*k*-mers) is they differ from each other by a number of nucleotides up to a certain threshold (the [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)). The graph is central to the error correction algorithm.
3. At this step Bayesian subclustering of the graph produced in the previous step. For each *k*-mer we now know the center of its subcluster. 
4. **Solid** *k*-mers are derived from cluster centers and are assumed to be *error free*.
5. Solid *k*-mers are mapped back to the reads.
6. Reads are corrected using solid *k*-mers:

>![](/BMMB554/img/readCorrection.jpeg)
>
>**Read correction**. Black *k*-mers are solid. Grey k-mers are non-solid. Red k-mers are the centers of the corresponding clusters (two grey k-mers striked through on the right are non-solid singletons). As a result, one nucleotide is changed based on majority rule. (From [Nikolenko:2013](https://goo.gl/1iGkMe)).

In the example data we will be using here running SPAdes error correction changed 14,013,757 bases in 3,382,337 reads - a substantial fraction of the ~18 million read dataset.

### Hybrid assembly

SPAdes first construct an assembly graph from high quality high coverage short read data and then utilizes long reads generated with PacBio, Oxford Nanopore, or Illumina's TruSeq Synthetic Long-Read technology to close assembly gaps and to resolve repetitive regions. 

To close the gaps it finds long reads spanning a coverage gap in the assembly graph. The challenge with long reads (particularly from PacBio and Oxford Nanopore) is their high error rate. To alleviate this issues SPAdes looks for a collection of long reads spanning a given gap and computed a consensus. 

>![](/BMMB554/img/repeatResolution.png)
>
>**Repeat resolution**. This picture represents an example of a collapsed repeat. Somewhere in the genome there are three distinct regions (blue, green, an red) containing a repeat (black). Because black region is highly similar (or identical) among these three regions it is collapsed on the graph as shown here. If we align long reads to this graph we will be able to disentangle this. For example, long reads (dashed lines) span red edges allowing us to partially uncollapse this assembly. (From [Antipov:2015](http://bioinformatics.oxfordjournals.org/content/early/2015/11/20/bioinformatics.btv688.full.pdf+html)) 

# Applying SPAdes to real data

Here we are running SPAdes twice: once using Illumina reads only and once adding Oxford Nanopore reads to improve Illumina assembly. 

## Illumina only

```
# contigs (>= 0 bp)             2348     
# contigs (>= 1000 bp)          104      
# contigs (>= 5000 bp)          52       
# contigs (>= 10000 bp)         45       
# contigs (>= 25000 bp)         39       
# contigs (>= 50000 bp)         28       
Total length (>= 0 bp)          5612247  
Total length (>= 1000 bp)       4559610  
Total length (>= 5000 bp)       4477328  
Total length (>= 10000 bp)      4431518  
Total length (>= 25000 bp)      4332438  
Total length (>= 50000 bp)      3966974  
# contigs                       659      
Largest contig                  434834   
Total length                    4899255  
GC (%)                          50.85    
N50                             129141   
N75                             82088    
L50                             13       
L75                             24       
# N's per 100 kbp               12.17    
# predicted genes (unique)      4880     
# predicted genes (>= 0 bp)     4884     
# predicted genes (>= 300 bp)   4286     
# predicted genes (>= 1500 bp)  575      
# predicted genes (>= 3000 bp)  54       

```

## Illumina + Oxford Nanopore

```
# contigs (>= 0 bp)             2258     
# contigs (>= 1000 bp)          41       
# contigs (>= 5000 bp)          4        
# contigs (>= 10000 bp)         1        
# contigs (>= 25000 bp)         1        
# contigs (>= 50000 bp)         1        
Total length (>= 0 bp)          5682366  
Total length (>= 1000 bp)       4640835  
Total length (>= 5000 bp)       4593355  
Total length (>= 10000 bp)      4576746  
Total length (>= 25000 bp)      4576746  
Total length (>= 50000 bp)      4576746  
# contigs                       586      
Largest contig                  4576746  
Total length                    4973843  
GC (%)                          50.91    
N50                             4576746  
N75                             4576746  
L50                             1        
L75                             1        
# N's per 100 kbp               4.83     
# predicted genes (unique)      4861     
# predicted genes (>= 0 bp)     4914     
# predicted genes (>= 300 bp)   4312     
# predicted genes (>= 1500 bp)  583      
# predicted genes (>= 3000 bp)  58       
```

## What does this mean?

We do not know how big the genome of *E. coli* C is, but the guesstimate will put us somewhere close to 4.5 million bases (close to the genome size of *E. coli* K-12). 

### N50

(From [Wikipedia](https://en.wikipedia.org/wiki/N50,_L50,_and_related_statistics#N50))

N50 statistic defines assembly quality. Given a set of contigs, each with its own length, the N50 length is defined as the shortest sequence length at 50% of the genome. It can be thought of as the point of half of the mass of the distribution; the number of bases from all contigs longer than the N50 will be close to the number of bases from all contigs shorter than the N50. For example, 9 contigs with the lengths 2,3,4,5,6,7,8,9,and 10, their sum is 54, half of the sum is 27, the size of the genome also happens to be 54. 50% of this assembly would be 10 + 9 + 8 = 27 (half the length of the sequence). Thus the N50=8, which is the size of the contig which, along with the larger contigs, contain half of sequence of a particular genome. Note: When comparing N50 values from different assemblies, the assembly sizes must be the same size in order for N50 to be meaningful.

>![](/BMMB554/img/n50.png)
>
>**N50 size**. From ([Schatz:2015](http://schatzlab.cshl.edu/teaching/2015/2015.03.30.GenomeAccess.Sequencing%20and%20Assembly.pdf))

**The higher the N50, the better the assembly!**. In out case for N50 is 129,141 and 4,576,746 for Illumina only and Illumina+ONP assemblies, respectively. Thus this means that the Illumina+ONP assembly is *clearly* better.

# Try for yourself

## Importing the data

[Galaxy library](https://test.galaxyproject.org/library/list#/folders/F0dd345537db0c380) contains the following datasets from *E. coli* C sequencing experiment:

>![](/BMMB554/img/assembly_lib.png)
>
>**Datasets** used for assembly of *E. coli* C genomes. `Ecoli-2_S1_L001_R1_001.fastq` are forward Illumina reads, `Ecoli-2_S1_L001_R2_001.fastq` are reverse Illumina reads, `minion_1.2d_pass.fastq` are Oxford Nanopore reads.

## Building the assembly

To run SPAdes is Galaxy select **NGS: Assembly** &#8594; **spades** and set the following parameters:

>![](/BMMB554/img/spades_galaxy.png)
>
>**SPAdes in Galaxy**. SPAdes has been initially designed for single-cell sequencing data, but it is a generally applicable assembler today. Note the selection of *k*-mer sizes. Because we have long miSeq reads (250 bp paired end configuration) we use *k*-mers up to half of the read length (SPAdes maximum) as described [here](http://spades.bioinf.spbau.ru/release3.9.1/manual.html#sec3.4). We then choose forward and reverse reads and, finally, add Oxford Nanopore reads as the last input. 

## Assessing the assembly quality

In Galaxy spades produces two types of assembly output: *contigs* and *scaffolds*. Contigs represent continuous segments of assembly, while scaffolds are built from contigs and represent the next level of assembly. Thus scaffolds are closer to the "ultimate truth" of what genome sequence is. 

Assessing assembly quality in Galaxy can be using  [Quast](http://cab.spbu.ru/software/quast/) tool produced and maintained by the same [group](http://cab.spbu.ru/) that is responsible for development of SPAdes. 

Let's run Quast (**NGS: Assembly** &#8594; **quast**) on the set of scaffolds generates by SPAdes in the previous step:

>![](/BMMB554/img/quast_galaxy.png)
>
>**Quast in Galaxy**. Here scaffolds generated by SPAdes are used as input. We estimate genome size to be around 4.6 Mb (similar to *E. coli* K12). In fact, we use K12 genome as a reference file to compare our assembly against. This genome is also available form the [Galaxy library](https://test.galaxyproject.org/library/list#/folders/F0dd345537db0c380). 

It would generate summary statistics including the following report:

>![](/BMMB554/img/quast_report.png)
>
>**Quast report**. This report contains two columns: `ont_illumina` and `ont_illumina broken`. Since we used scaffolds that are constructed from contigs often glued together with "Ns" (unknown nucleotide), Quast "breaks" them on "Ns" and aligns these "broken" scaffolds to the reference". This is done to assess the degree to which scaffolds may be incorrect. Of course in this case we expects some scaffolds to be incorrect in relation to *E. coli* K12 since we are sequencing and assembling a different strain. Nonetheless this seems to be a good assembly with a long high quality scaffold at 4.5 Mb!

## Annotating assemblies

To annotate the assemblies we use [Prokka](*http://www.vicbioinformatics.com/software.prokka.shtml) tool (**NGS: Assembly** &#8594; **Prokka**) that was designed for rapid identification of genes in prokaryotic genomes.   

>![](/BMMB554/img/prokka_galaxy.png)
>
>**Prokka in Galaxy**. Here we use SPAdes scaffolds as the input and set the minimal contig size to `1,000`. 

Prokka produces a large number of datasets representing gene annotations in a variety of formats. Below is a snapshot of its [gff](http://www.ensembl.org/info/website/upload/gff.html) output:

```
gnl|C|L_contig000001	barrnap:0.7	rRNA	11	121	7e-12	-	.	ID=L_00001;Parent=L_00001_gene;locus_tag=L_00001;product=5S ribosomal RNA
gnl|C|L_contig000001	prokka	gene	11	121	.	-	1	ID=L_00001_gene;locus_tag=L_00001
gnl|C|L_contig000001	barrnap:0.7	rRNA	220	3120	0	-	.	ID=L_00002;Parent=L_00002_gene;locus_tag=L_00002;product=23S ribosomal RNA
gnl|C|L_contig000001	prokka	gene	220	3120	.	-	1	ID=L_00002_gene;locus_tag=L_00002
gnl|C|L_contig000001	Aragorn:1.2	tRNA	3297	3372	.	-	0	ID=L_00003;Parent=L_00003_gene;inference=COORDINATES:profile:Aragorn:1.2;locus_tag=L_00003;product=tRNA-Ala(tgc)
gnl|C|L_contig000001	prokka	gene	3297	3372	.	-	1	ID=L_00003_gene;locus_tag=L_00003
gnl|C|L_contig000001	Aragorn:1.2	tRNA	3415	3491	.	-	0	ID=L_00004;Parent=L_00004_gene;inference=COORDINATES:profile:Aragorn:1.2;locus_tag=L_00004;product=tRNA-Ile(gat)
gnl|C|L_contig000001	prokka	gene	3415	3491	.	-	1	ID=L_00004_gene;locus_tag=L_00004
gnl|C|L_contig000001	barrnap:0.7	rRNA	3561	5099	0	-	.	ID=L_00005;Parent=L_00005_gene;locus_tag=L_00005;product=16S ribosomal RNA
gnl|C|L_contig000001	prokka	gene	3561	5099	.	-	1	ID=L_00005_gene;locus_tag=L_00005
```

# What is next?

Two extensive tutorials cover assembly and analysis of newly assmebled genomes:

 - [Hybrid assembly of a bacterial genome](https://galaxyproject.github.io/training-material/topics/assembly/tutorials/unicycler-assembly/tutorial.html)
 - [Analysis of new assembly](https://galaxyproject.github.io/training-material/topics/assembly/tutorials/ecoli_comparison/tutorial.html)