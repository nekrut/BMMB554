+++
categories = []
date = "2018-01-24"
#draft = true
menu = ""
tags = ['DNA sequencing', 'PacBio', 'Oxford Nanopore']
title = "DNA Sequencing: PabBio, ONT and others"
+++

[![](https://raw.githubusercontent.com/rrwick/Basecalling-comparison/master/images/logo.png)](https://github.com/rrwick/Basecalling-comparison)

# PacBio Single Molecule Sequencing

PacBio is a fundamentally different approach to DNA sequencing as it allows reading single molecules. Thus it is an example is so called _Single Molecule Sequencing_ or _SMS_. PacBio uses highly processive DNA polymerase placed at the bottom of each well on a microtiter plate. The plate is fused to the glass slide illuminated by a laser. When polymerase is loaded with template it attracts fluorescently labeled nucleotides to the bottom of the well where they emit light with a wavelength characteristic of each nucleotide. As a result a "movie" is generated for each well recording the sequence and duration of incorporation events. One of the key advantage of PacBio technology is its ability to produce long reads with ones at 10,000 bases being common. 

### Slides

{{< speakerdeck ccb3d34f1a214f66ac7a2d233caedaf5 >}}

And another set of slides from [@biomonika](https://twitter.com/biomonika?lang=en):

{{< speakerdeck 5850fe7ede3b45df816c3eaa502ea3d1 >}}

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

{{< speakerdeck 3895a3069bc64ad5bc74c972a0353911 >}}

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

{{< speakerdeck 52845e932e004b88b63a76b327b2402e >}}


### Reading 

* SOLiD | [A high-resolution, nucleosome position map of C. elegans reveals a lack of universal sequence-dictated positioning](http://dx.doi.org/10.1101/gr.076463.108)
* Complete Genomics | [Human genome sequencing using unchained base reads on self-assembling DNA nanoarray](http://dx.doi.org/10.1126/science.1181498)
* Ion Torrent | [An integrated semiconductor device enabling non-optical genome sequencing](http://dx.doi.org/10.1038/nature10242)
