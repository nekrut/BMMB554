![](https://i.imgur.com/I1Agm07.png)
> from a Science issue containing [Levene et al. 2003](http://dx.doi.org/10.1126/science.1079700).

# Pacific Biosciences (PacBio)

PacBio was the second (after [Helicos](https://en.wikipedia.org/wiki/Helicos_single_molecule_fluorescent_sequencing)) single molecule sequencing (SMS) technology on the market.  Today it is an important technology enabling assembly of complex genomes and transcriptomes. 

## Fundamentals

The era of Pacific Biosciences begins with a publication by [Eid et al. 2009](https://science.sciencemag.org/content/323/5910/133/). Yet as was the case with other technologies it did not appear out of thin air. One of the key publications (written by some of the same authors) predating the birth of PacBio is the one by [Levene et al. 2003](http://dx.doi.org/10.1126/science.1079700). In particular it had the following figure:

-----

![](https://i.imgur.com/PmJjCUr.png)

**Figure 1** from [Levene et al. 2003](http://dx.doi.org/10.1126/science.1079700). An apparatus for single-molecule enzymology using zero-mode waveguides.

----

The overall idea of this device is that it can detect fluorescent ligands (such as, for example, labeled dNTPs) in a very small volume: 10<sup>-21</sup> litre. Specifically, envision a glass slide fused to a metal (Aluminum) film with tiny holes. In fact, the diameter of the holes is smaller than the wavelength of light that is used to illuminate the slide. As a result only molecules at the bottom of this "hole" will be detectable. This allows to track single molecule dynamics. Now imagine that you put a single DNA polymerase molecule at the bottom of such a "hole". The polymerase will be pulling dNTPs close to the bottom of the "hole" at it performs polymerization reaction. Thus, only nucleotides that are being added to DNA strand will be detected by the device at any given time. It now make a movie of this process you are recording real time polymerization kinetics. And this is exactly what PacBio process does:

----
![](https://i.imgur.com/TzQWgr7.png)

**Figure 1** from [Eid et al. 2009](https://science.sciencemag.org/content/323/5910/133/)

----

Because the "movie" recorded by the machine contains temporal component of the process (how long does it take for each base to be incorporated to the nascent chain) this information can be directly used to identify modified bases in the template as was shown by [Flushberg et al. 2010](http://www.nature.com/doifinder/10.1038/nmeth.1459):

----

![](https://i.imgur.com/LG6Zkmi.png)

**Figure 1** from [Flushberg et al. 2010](http://www.nature.com/doifinder/10.1038/nmeth.1459).

----

## Real life applications and accuracy

One of the major drawbacks of SNS technologies is a relatively high error. In the case of PacBio it is somewhere between 10 to 25%. However, because PacBio uses library produced by ligating bell-shaped adapters to DNA molecules, a single circular molecule can be sequenced multiple times allowing for error correction:

----

![](https://i.imgur.com/NEvb7Rp.png)

**Figure 1a** from [Wenger et al. 2019](http://dx.doi.org/10.1038/s41587-019-0217-9).

----

Performing multiple passes allows for high accuracy:

-----

![](https://i.imgur.com/BVM5c1g.png)

**Figure 2b** from [Wenger et al. 2019](http://dx.doi.org/10.1038/s41587-019-0217-9).

----

with reads of approximately 13kb:

-----

![](https://i.imgur.com/nhQAQ1y.png)

**Figure 1c** from [Wenger et al. 2019](http://dx.doi.org/10.1038/s41587-019-0217-9).

> [!NOTE]
> Note that it is also possible to read a longer insert just  generating what is called Continuous Long Reads (**CLRs**). These are obviously much longer but are less accurate. Thus current PacBio systems produce two types of reads: Circular Consensus Reads (**CCR**) and Continuous Long Reads (CLRs). A subset of high quality CCR reads (with base $Q > 20$) is called **HiFi** reads.

## Practicalities

In addition to sequencing data and base qualities PacBio machines produce kinetics data. In particular:

- Intra Pulse Duration values (IDPs)
- Pulse width values

Older machines were reporting all this info as [Hierarchical Data Format (HDF)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format). Newer machines are using a special subset of [BAM](https://pacbiofileformats.readthedocs.io/en/12.0/BAM.html) format to report this information. Because of all these additional data PacBio datasets tend to be quite large:

![](https://i.imgur.com/nPJccSr.png)

You can look at a small fragment of the `*.hifi_reads.bam` file in its textual (SAM) representation [here](https://github.com/nekrut/BMMB554/blob/master/2021/data/sample.hifi_reads.sam).

----

![](https://i.imgur.com/kZXeDom.png)

**Kinetogram** of PacBio read (from [here](http://files.pacb.com/software/smrtanalysis/2.0.0/doc/smrtview/help/App_View_Base_Mod_data.htm)).


## Acquisition of Omniome

Recently PacBio has added an interesting short read Sequencing-by-binding (SBB) technology to its portfolio by [bying Omniome](https://www.pacb.com/technology/sequencing-by-binding/). This technology (only remotely related to PacBio) is based on the following principles:

![](https://i.imgur.com/aoy47YX.png)

**Figure 2** from [Cetin et al.](https://pubs.acs.org/doi/10.1021/acssensors.7b00957) 2018. 

![](https://i.imgur.com/egvPuo2.png)

**Figure 3** from [Cetin et al.](https://pubs.acs.org/doi/10.1021/acssensors.7b00957) 2018.

The machine, [Onso system](https://www.pacb.com/onso/) will allow up to 200bp reads with the possibility of paired-end sequencing. I have not yet seen the data.

## Other sequencing technologies

[A brief summary](https://speakerdeck.com/nekrut/other-ngs-technologies) of other sequecning technologies worth mentioning.
