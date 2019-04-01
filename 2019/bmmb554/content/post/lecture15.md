---
date: "2019-04-01"
tags: ["SNPs", "variants"]
title: "Lecture 15: Calling variants"
---	

Calling varinats is complicated!

 - [Haploid systems](https://galaxyproject.github.io/training-material/topics/variant-analysis/tutorials/non-dip/tutorial.html)
 - [Diploid system](https://galaxyproject.github.io/training-material/topics/variant-analysis/tutorials/dip/tutorial.html)
 - [Finding really rare variants](https://galaxyproject.github.io/training-material/topics/variant-analysis/tutorials/dunovo/tutorial.html)

# Why call varinats? An example from Tibet

Many residents of the Tibetian Plateau live above 4,000 meters where oxygen concentration is approximately 40% lower than at sea level:

>
>![](/BMMB554/img/tibet.png)
>
>Tibetan Plateau and surrounding areas (from [Wikipedia](https://en.wikipedia.org/wiki/Tibet)).

Tibetian experience a number of adaptations to high altitudes manifesting in the following phenotypic differences:

- lower hemoglobin concentration [Wu:2005](http://science.sciencemag.org/lookup/ijlink?linkType=ABST&journalCode=jap&resid=98/2/598&atom=%2Fsci%2F329%2F5987%2F75.atom)
- higher arterial oxygen saturation [Niermeyer:1995](http://science.sciencemag.org/lookup/ijlink?linkType=ABST&journalCode=jap&resid=98/2/598&atom=%2Fsci%2F329%2F5987%2F75.atom)
- more efficient pulmonary gas exchange [Zhuang:1996](https://www.ncbi.nlm.nih.gov/pubmed/8822225)

What are the genetic causes of these adaptations?

# Sequencing of 50 Human Exomes Reveals Adaptation to High Altitude

[Emilia Huerta-Sanchez and Rasmus Nielsen](http://science.sciencemag.org/content/329/5987/75) decided to investigate this phenomenon using the following experimental design:

## Design

They sequenced exomes from 50 unrelated individuals from two villages (both situated at or above 4,300 m above sea level) in the Tibet Autonomous Region of China. Exomes were enriched using [Numblegen exome capture system](http://sequencing.roche.com/products/nimblegen-seqcap-target-enrichment.html) (approximately 20,000 genes) and sequenced to mean depth of ~18x. 

## SNPs

18x coverage does not guarantee accurate assignment of individual genotypes. To address this challenge Nielsen et al. devised a Bayesian approach that would (1) estimate reliability for SNP calls and (2) compute population allele frequencies for each site. 

They found:

 - 151,825 SNPs > 50% of probability being variable
 - 101,668 SNPs > 99% probability of being variable

Sanger sequencing validated 53 out of 56 that had >95% probability of being variable and minor allele frequencies between 3% and 50%.

## Population history of Tibetians and Han Chinese

The Tibetian exome was compared with 40 Han Chinese from Beijing genomes (HCB) from the 1000 Genomes Project. Beijing is approximately 50 m above sea level and the adsolute Majority of Han Chinese live below 2,000 m. The amount of genetic differentiation between Tibetian and Han samples is low ([F<sub>*ST*</sub>](https://en.wikipedia.org/wiki/Fixation_index) = 0.026). In addition, there is also no differentiation between the two Tibetian villages (F<sub>*ST*</sub>=0.014) and so they are treated as a single population. The paper estimated that the Tibetian and Han populations diverged ~2,750 years ago with Tibetian population shrinking and Han population expanding. 

>
>![](https://d2ufo47lrtsv5s.cloudfront.net/content/sci/329/5987/75/F1.large.jpg?width=800&height=600&carousel=1)
>
>Two-dimensional unfolded site frequency spectrum for SNPs in Tibetan (x axis) and Han (y axis) population samples. The number of SNPs detected is color-coded according to the logarithmic scale plotted on the right. Arrows indicate a pair of intronic SNPs from the EPAS1 gene that show strongly elevated derived allele frequencies in the Tibetan sample compared with the Han sample.
>

## Finding casual SNPs

With two populations we one can potentially find genes with significant allele frequency differences but we will not be able to tell which of the two populations is affected by selection. To do this we need an outgroup represented by a distantly related population. In this study they've chosen a Danish population as an outgroup. 

>
>![](https://d2ufo47lrtsv5s.cloudfront.net/content/sci/329/5987/75/F2.large.jpg?width=800&height=600&carousel=1)
>
>Population-specific allele frequency change. (A) The distribution of F<sub>*ST*</sub>-based PBS statistics for the Tibetan branches, according to the number of variable sites in each gene. Outlier genes are indicated in red. (B) The signal of selection on EPAS1: Genomic average F<sub>*ST*</sub>-based branch lengths for Tibetan (T), Han (H), and Danish (D) branches (left) and branch lengths for EPAS1, indicating substantial differentiation along the Tibetan lineage (right).

## *EPAS1*

The strongest signal was observed for the *EPAS1* gene, which has 9% derived allele frequency in Han Chinese and 87% in Tibetian population. To establish functional link between this site and inhabiting high altitudes authors performed association analysis:  "*Significant associations were discovered for erythrocyte count (F test P = 0.00141) and for hemoglobin concentration (F test P = 0.00131), with significant or marginally significant P values for both traits when each village was tested separately
The allele at high frequency in the Tibetan sample was associated with lower erythrocyte quantities and correspondingly lower hemoglobin levels (table S4). Because elevated erythrocyte production is a common response to hypoxic stress, it may be that carriers of the “Tibetan” allele of EPAS1 are able to maintain sufficient oxygenation of tissues at high altitude without the need for increased erythrocyte levels. Thus, the hematological differences observed here may not represent the phenotypic target of selection and could instead reflect a side effect of EPAS1-mediated adaptation to hypoxic conditions.*"

# Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA

[Emilia Huerta-Sanchez and Rasmus Nielsen](http://www.nature.com/nature/journal/v512/n7513/full/nature13408.html)

>
>![](http://www.nature.com/nature/journal/v512/n7513/images/nature13408-f2.jpg)
>
>Each column is a polymorphic genomic location (95 in total), each row is a phased haplotype (80 Han and 80 Tibetan haplotypes), and the coloured column on the left denotes the population identity of the individuals. Haplotypes of the Denisovan individual are shown in the top two rows (green). The black cells represent the presence of the derived allele and the grey space represents the presence of the ancestral allele (see Methods). The first and last columns correspond to the first and last positions in Supplementary Table 3, respectively. The red and blue arrows indicate the 32 sites in Supplementary Table 3. The blue arrows represent a five-SNP haplotype block defined by the first five SNPs in the 32.7-kb region. Asterisks indicate sites at which Tibetans share a derived allele with the Denisovan individual.

>
>![](http://www.nature.com/nature/journal/v512/n7513/images/nature13408-f3.jpg)
>
>The haplotypes were defined from all the SNPs present in the combined 1000 Genomes and Tibetan samples: 515 SNPs in total within the 32.7-kb EPAS1 region. The Denisovan haplotypes were added to the set of the common haplotypes. The R software package pegas23 was used to generate the figure, using pairwise differences as distances. Each pie chart represents one unique haplotype, labelled with Roman numerals, and the radius of the pie chart is proportional to the log2(number of chromosomes with that haplotype) plus a minimum size so that it is easier to see the Denisovan haplotype. The sections in the pie provide the breakdown of the haplotype representation amongst populations. The width of the edges is proportional to the number of pairwise differences between the joined haplotypes; the thinnest edge represents a difference of one mutation. The legend shows all the possible haplotypes among these populations. The numbers (1, 9, 35 and 40) next to an edge (the line connecting two haplotypes) in the bottom right are the number of pairwise differences between the corresponding haplotypes. We added an edge afterwards between the Tibetan haplotype XXXIII and its closest non-Denisovan haplotype (XXI) to indicate its divergence from the other modern human groups. Extended Data Fig. 5a contains all the pairwise differences between the haplotypes presented in this figure. ASW, African Americans from the south western United States; CEU, Utah residents with northern and western European ancestry; GBR, British; FIN, Finnish; JPT, Japanese; LWK, Luhya; CHS, southern Han Chinese; CHB, Han Chinese from Beijing; MXL, Mexican; PUR, Puerto Rican; CLM, Colombian; TSI, Toscani; YRI, Yoruban. Where there is only one line within a pie chart, this indicates that only one population contains the haplotype.
