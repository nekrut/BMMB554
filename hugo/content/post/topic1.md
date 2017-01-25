+++
#categories = []
date = "2017-01-11T11:41:14-05:00"
#draft = true
featureimage = "img/luria_small.png"
menu = ""
tags = ["history","genetics","DNA"]
title = "1. History"
description = "**Topic 1** | History: From Genetics to Genomics"

+++

![](/BMMB554/img/luria_small.png)

# Why history?

Knowing history is essential for understanding how we arrived to the current state of affairs in our field. It is also full of acciental discoveries and dramatic relationships making it quite interesting to read about. I strongly advise you to take a look at the mansucripts below.

## Classical publications

* 1965 | [A history of genetics](http://www.amazon.com/A-History-Genetics-A-H-Sturtevant/dp/0879696079)
* 1943 | [Delbruck & Luria](http://www.bx.psu.edu/~anton/bioinf1-2014/delbruck-luria-1943.pdf)
* 1944 | [Avery, MacLeod, & McCarty](http://www.bx.psu.edu/~anton/bioinf1-2014/avery-1944.pdf)
* 1952 | [Herhey & Chase](http://www.bx.psu.edu/~anton/bioinf1-2014/hershey-chase-1952.pdf)
* 1953 | [Watson & Crick](http://www.bx.psu.edu/~anton/bioinf1-2014/watsoncrick.pdf)
* 1958 | [Meselson & Stahl](http://www.bx.psu.edu/~anton/bioinf1-2014/Proc%20Natl%20Acad%20Sci%20USA%201958%20Meselson.pdf)
* 1960 | [Jacob and Monod](http://www.bx.psu.edu/~anton/bioinf1-2014/jacob-monod-1961.pdf)

## Popular (yet very informative) literature

Get one of these and read it on a plane:

* 1978 | [Molecular Gemetics: An Itroductory Narrative](https://www.amazon.com/Molecular-Genetics-Introductory-Gunther-Stent/dp/0716700484)
* 2001 | [The double helix](http://www.amazon.com/The-Double-Helix-Discovery-Structure/dp/074321630X)
* 2005 | [The Third Man of the Double Helix](http://www.amazon.com/Third-Man-Double-Helix-Autobiography/dp/019280667X)
* 2014 | [Brave Genius](http://www.amazon.com/Brave-Genius-Philosopher-Adventures-Resistance/dp/0307952347)

------

# Publication highlight | The fluctuation test

In a truly collaborative spirit a german physicist [Max Delbrück](http://www.nobelprize.org/nobel_prizes/medicine/laureates/1969/delbruck-facts.html) joined forces with an italian microbiologist [Salvador Luria](http://www.nobelprize.org/nobel_prizes/medicine/laureates/1969/luria-facts.html) to prove the stochastic nature of mutations and to reject "the last stroghold of Lamarckism". This [classical work](http://www.bx.psu.edu/~anton/bioinf1-2014/delbruck-luria-1943.pdf) was published in 1943 in journal _Genetics_. Here we re-examine some of the fundamental aspects of this work. In this we occasionally rely on a classical textbook in [Molecular Genetics](http://www.amazon.com/Molecular-Genetics-Introductory-Gunther-Stent/dp/0716700484) by Günther Stent. 

So, it has been know for some time that:

* Bacteria sensitive (infectable) by phage becomes resistant as a result of exposure to bacteriophage
* The resistance is preserved when descendants of these cells are incubated

This can, in principle, be explained by two mutually exclusive hypotheses:

## Acquired resistance vs. spontaneous mutation

1. direct action of phage on bacteria triggers "acquisition" of the resistance;
2. some cells in a population already have a mutation conferring the resistance and the exposure to the phage merely brings carriers of such mutations to prominence by killing off all sensitive cells. 

How can we distinguish between these two alternative possibilities? Let's try to put hypothesis (1) into quantitative framework:

* There are two bacterial phenotypes: *S* - sensitive (is lysed by the phage) and *R* - resistant (is not lysed and does not absorb phage)
* Bacterial population progresses from a single cell to $N$ cells
* The probability of changing from *S* to *R* is $a$

So, if one grows $S$ bacteria in a culture and then plates them on agar containing excess of phage, where will be $n$ of $R$ colonies, where $n =  aN$. Since we can estimate $n$ directly (by counting colonies on the plate) and $N$ is also known (a function of the number of generations) the fraction of $R$ individuals in a population is going to be same for all stages of the population:

<div>
$$

\frac{n}{N} = a

$$
</div>

This will not be quite the same for hypothesis (2) since the number of cells carrying the resistance mutation will differ depending on when in population history they occurred and how many generation have passed since their occurrence. After $g$ generations there will be

<div>
$$

N = 2^g

$$
</div>

cells. Consequently, if the probability of mutation is $a$, then by $i$-th generation there will be $a2^i$ cells carrying mutations and we can arrive to the ratio of

<div>
$$

\frac{n}{N} = ga

$$
</div>


Delbück and Luria's experience with estimating such ratio has proven to be difficult as they were observing great fluctuation in the number of $R$ cells. They have subsequently realized that such fluctuation was in fact an indirect indication that the mutation hypothesis is likely true. Delbrück has developed a theoretical framework predicting the distribution of mutant phenotypes for both hypotheses. [Stent](http://www.amazon.com/Molecular-Genetics-Introductory-Gunther-Stent/dp/0716700484) provides the following elegant description of Delbück's reasonong. It is based on measuring the variance in the number of resistant colonies across a number of replicates. Suppose there are $c$ _E. coli_ replicates (cultures) started from a single *S* bacterium. Each is grown for $g$ generations, and each accumulates $N = 2^g$ cells as a result. The entire content of each culture is then spread over agar plate saturated with the phage. The number $n$ of *R* colonies is then counted. If $n_j$ is the number of *R* colonies from culture $j$, then the average of the numbner of resistant colonies is:

<div>
$$

\bar{n} = \frac{\sum_{j=1}^{c}n_j}{c}

$$
</div>


and the variance is:


<div>
$$ 

var_n = \frac{\sum_{j=1}^{c}(\bar{n}-n_j)}{c}

$$
</div>

The behaviour of ratio of `variance/average` is critical to distinguishing between hypothesis (1) and (2). If (1) is true we expect low fluctuation and the ratio will be close to 1. If (2) is true the variation will be considerable and the ratio will be much higher than one. Look at Fig. 1 below. 

* In pane A (Hypothesis 1) phage induces changes in the bacteria upon plating and because the probability of changing from `S` to `R` is the same for  all cells we would see approximately the same number of `R` cells. The mean here is `2.5` and the variance/mean ratio is `1.1`.  
* In pane B (Hypothesis 2) every cell has the same mutation rate, but the mutations may occur at any point during the culture propagation. If they occur early - many resistant colonies will be produced from such culture. If they occur late - just a few. As a result one would expect to see significant fluctuation. Here the mean is the same as in A = `2.5`, but the variance/mean ratio is much higher at `4.3`. 

 | 
:----|:------------
![](/BMMB554/img/luria.png) | ![](/BMMB554/img/stent.png)
**Figure 1** (Fig. 6-4 from Stent) | **Table 1** (Table 6-1 from Stent)

Table 1 settles these issues. Here one can see a significant fluctuation across 20 independent experiments with the main of `11.3` and variance/mean ratio of `61`. This table also show the result of plating aliquots from a bulk culture. In this case 10 ml culture was incubated for the same duration as the 20 independent cultures. Small amount from this culture were then plated on 10 independent plates. Because these cells share their genetic ancestry there is very little variation across these platings. 

This paper settled one of the most contentious issues in biology and won the Nobel prize to its authors.

-----

# Slides

Slides covering material for Lecture 1

{{< speakerdeck 7726e8b8b3ee41f0a2a1497128d59ca0 >}}

------

# Video

Video presentation from last year. 

{{< vimeo 180735569 >}}

------

# What to do before next lecture

Read two following papers:

* "DNA sequencing with chain-terminating inhibitors" by Sanger, Nicklen, and Coulson ([1977](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC431765/pdf/pnas00043-0271.pdf))
* "A new method for sequencing DNA" by Maxam and Gilbert ([1977](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC392330/pdf/pnas00024-0174.pdf))
