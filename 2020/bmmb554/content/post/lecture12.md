---
date: "2020-03-30"
tags: ["SARS-COV-2","COVID-19","RNAseq"]
title: "Analysis of RNA II: RiboSeq, and other things"
---

# Potentially interesting sites

<div class="alert alert-warning" role="alert">
This only works for PSU-based people
</div>

Open [this spreadsheet](https://docs.google.com/spreadsheets/d/1bp8G68MGqEbuJxROqpjViyZ5YoKWsmyAl0MO3BxOeR8/edit?usp=sharing).

It has the following columns:

 - Group: People, to whom variants are assigned
 - Sample: SRA accession
 - CHROM: Reference genome (same for all rows)
 - POS: Position of the variant in the genome (1-based)
 - REF: Reference allele
 - ALT: Alternative allele
 - DP: Read depth
 - AF: Alternative allele frequency
 - SB: Strand bias as calculated by [lofreq](https://csb5.github.io/lofreq/) (0 = no strand bias)
 - DP4: Strand-specific depth for reference and alternate allele observations (Forward reference, reverse reference, forward alternate, reverse alternate)
 - IMPACT: functional impact of the substitution
 - FUNCLASS: type of change
 - EFFECT: effect of the change
 - GENE: gene name
 - CODON: codon
 - type: type of variant (`S` = SNP, `I` = Indel, `M` = MNP )
 - GENE: gene name
 - SITE: codon within the gene
 - FEL: Is site identified by [FEL](https://stevenweaver.github.io/hyphy-site/methods/selection-methods/#fel) as being under selection
 - MEME: Is site identified by [MEME](https://stevenweaver.github.io/hyphy-site/methods/selection-methods/#meme) as being under selection
 - MEME.FRACTION: fraction of branches under selection
 - CLASSIFICATION: Type of selection (also see [here](https://observablehq.com/@spond/natural-selection-analysis-of-sars-cov-2-covid-19))
 - SYN.SUBS: # synonymous substitutions
 - NONSYN.SUBS: # non-synonymous substitutions
 - COMPOSITION: composition of the alignment column 
 - PROPRETIES: amino acid change effect
 - gSITE: Genomic coordinate 

## Instructions

 1. Find you group
 2. Perform additional filtering to create a conservative set of sites
 3. Find latest papers on the gene of interest
 4. See if any of the sites may be significant based on published biochemical or structural data. 

# Continuing RNAseq

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQEFrIAGIGnNO5lDKRfFi6tlUK4ZiEMXqn2TTQ8pKAp_h9h5cqoUBhoCVXCCaeQOVtq_j5r51GFKYfx/embed?start=false&loop=false&delayms=3000" frameborder="0" width="683" height="541" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>