# Analysis project

## Project groups

I have subdivided this class into the following groups:

| Group | MEGA plate starting point | Figure in the paper's [supplement](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5534434/bin/NIHMS874162-supplement-Supplemental_Methods_And_Figures.pdf) |
|---------|---------------------------|-----|
| 1 | Sym | S3 A |
| 2 | Manifold 4 | S3 B |
| 3 | Manifold 168 | S3 B |
| 4 | Manifold 2 | S3 B |
| 5 | Manifold 5 | S3 B |

These numbers correspond to colony labels in Fig S3 of the [supplement](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5534434/bin/NIHMS874162-supplement-Supplemental_Methods_And_Figures.pdf).

## Task 1: Prep
(due March 26, 2024 in class)

1. Go to NCBI SRA
2. Find datasets corresponding to `SRP077287`
3. Download RunInfo table as I showed in class
4. Look at figure S3A (if you are `Sym`) or figure S3B (if you are any of the `Manifold`s)
5. Find a colony corresponding to your number (for `Sym` you can pick any trajectory you like)
6. Write down numbers of colonies corresponding to a progression so that you have a good representatioin of colonies starting from wild type to super-resistant (see image below for an example)
7. Pull rows corresponding to these numbers from RunInfo table (Step 3)
8. Upload this into Galaxy
9. La Fin

![mega_example](https://github.com/nekrut/BMMB554/assets/4291636/af3e7bcd-c588-4965-bce6-5f685342f24e)

Here:

**Start point** - point with the number that was assigned to your group (e.g., Point 4 for Manifold4)

Now all numbers were sequenced. So you objective is to find adaptation trajectory which has the data in SRA.

## Task 2: Analysis
(due May 1st, 2024 by email)

### Assumptions

1. You have a final varinat dataset for your samples (see below for an example)
2. You have created a mapping between your samples and accession numbers as was [described here](https://github.com/nekrut/BMMB554/blob/master/2024/assessimg_variants.md#establish-the-relationship-between-samples-and-accessions) and downloaded it as a .csv file named `names.csv`.

Example of variant dataset:

```
Sample	CHROM	POS	REF	ALT	AF	DP	DP4	EFF[*].GENE	EFF[*].CODON	EFF[*].FUNCLASS
SRR3722117	CP009273	360103	C	T	0.075949	79	30,43,0,6	.	.	NONE
SRR3722117	CP009273	870516	G	T	0.157895	19	10,6,2,1	yliE	ctG/ctT	SILENT
SRR3722117	CP009273	1330682	G	T	0.363636	11	4,3,2,2	acnA	Ggt/Tgt	MISSENSE
SRR3722117	CP009273	1631797	C	A	0.25	16	4,8,2,2	ydfJ	.	NONE
```
### What do do

1. Create a copy of this nodebook -> https://colab.research.google.com/drive/1hnoNGQx7MEORWv7KcQAMzpFIsRxvdYVM?usp=sharing
2. Upload you `names.csv` file into notebook disk
3. Run your samples through the notebook

#### Group 1 (Sym) 

1. Identify which FIXED mutations are shared within clusters. 
2. Plot a comparison of these mutations across clusters
   
#### Gloups 2 - 4 (Manifold)

1. Identify all fixed mutations that are present in the terminal points but are absent at the start
2. Trace their trajectroies through the time points from beginning to end
3. Plot the change in frequencies

## Task 3: Write up

Put your findings into a Google Doc that will be shared with you. IF YOU DO NOT GET A LINK: EMAIL YOUR INSTRUCTOR!!!


