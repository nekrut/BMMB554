---
tags: BMMB554-23
---

![](https://i.imgur.com/VJvUNIu.png)


# Lecture 17: Oxford Nanopore

> [!IMPORTANT]
> This text and figures are based on the Oxford nanopоре documentation from the official [nanoporetech](https://community.nanoporetech.com/) site and official [videos](https://www.youtube.com/@OxfordNanoporeTechnologies).

The basic principle of the Oxford Nanopore Technology (ONT) is straightforward. Molecules are driven through a pore in a membrane. As a molecule moves through membrane it blocks current. In fact the extent of "blockage" is sequence specific generating using current change profiles that can be "translated" into sequence.    

![](https://i.imgur.com/e6zA8O2.png)

## Length-specific translocation speed

It began as technique for measuring polynecleotide length

[![](https://i.imgur.com/xl8KQjC.png)](https://www.pnas.org/doi/full/10.1073/pnas.93.24.13770)

## Blockage can be used to identify nucleotides

[![](https://i.imgur.com/1dzTNa8.png)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2683137/)

![](https://i.imgur.com/Do6TLIh.png)


## Speed can be controlled enzymatically

followed by experimentation on controlling the translocation speed using a variety of enzymes including a DNA polymerase:

[![](https://i.imgur.com/qipZfI0.png)](https://pubs.acs.org/doi/full/10.1021/ja1087612)


![](https://i.imgur.com/Hrnls6l.png)

## ONT also requires libraries

![](https://i.imgur.com/CeecGrO.png)

## Duplex versus simplex

![](https://i.imgur.com/lW90eiu.png)

![](https://i.imgur.com/R5BU1v1.png)

## Inny versus Outy

![](https://i.imgur.com/Vwh99tc.png)

![](https://i.imgur.com/6ewx95i.png)

![](https://i.imgur.com/U3ELctd.png)

![](https://i.imgur.com/HvaD9qH.png)

## ReadUntil

[ReadUntil](https://github.com/nanoporetech/read_until_api) allows "adaptive sampling" of reads in real time. In particular it makes things like [UNCALLED](https://github.com/skovaka/UNCALLED) possible:

[![](https://i.imgur.com/GXs57S3.png)](https://www.nature.com/articles/s41587-020-0731-9)

The general idea behind UNCALLED is summarized in this figure from the above manuscript:

-----

![](https://i.imgur.com/5itIs1D.png)

**a**, Overview of the algorithm: inputs are an FM index built from the DNA reference and the raw nanopore signal. The signal is converted to events, and the log probability of events matching each k-mer is computed. All paths through the FM index that are consistent with k-mers matching each event above a threshold are searched, conceptually forming a forest of trees (Extended Data Fig. 1 provides more details). **b**, Boxplots showing the speed of UNCALLED mapping of 100,000 E. coli reads to the *E. coli* K12 reference genome (kb s–1, left) and total number of milliseconds required to map reads (right). Center lines represent the median, box limits represent the upper and lower quartiles and whiskers represent the 5 and 95% confidence intervals. **c**, Percentage of mapped reads that can be confidently placed within a certain number of base pairs of sequencing. Note the ONT MinION sequences at approximately 450 bp s–1. **b,c**, Only reads that were mapped by UNCALLED are considered.


## [Software flow](https://github.com/nanoporetech)

[POD5](https://github.com/nanoporetech/pod5-file-format) -> [Dorado](https://github.com/nanoporetech/dorado)/[Remora](https://github.com/nanoporetech/remora)

Open [this](https://colab.research.google.com/drive/1GdUhZMmopyUMNTMEJh0TE9GtoIiO-U0-?usp=sharing) notebook to have a look at raw data.

