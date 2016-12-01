+++
date = "2016-11-28T16:20:10-05:00"
title = "Assembly basics"
description = "**Topic12** | Challenges of genome (and transcriptome) assembly"
menu = ""
#draft = true
tags = [
]
categories = [
]
featureimage = "img/topic12_cover.png"

+++

Genome assembly is a difficult task. It is especially challenging to describe it without using formal mathematical reasoning. Fortunately, others have been extremely successful in achieving this goal. Perhaps the best explanation of genome  assembly logic for biological audiences was provided by two highly regarded sources:

- [Ben Langmead](http://www.langmead-lab.org/teaching-materials/)
- [Pevzner and Compeau](http://www.amazon.com/Bioinformatics-Algorithms-Active-Learning-Approach/dp/0990374602). 

The material in this lecture relies heavily on these two sources. Really, all I've done here was to make it slightly less technical and more biologically centered. 


# Genomes and reads: Strings and $k$-mers

## $k$-mer composition

Genomes are strings of text. When we sequence genomes we use sequqneing machines that generate reads. For now let's assume that all reads have the same length $k$. Thus sequencies a genome generates a large list of $k$-mers.  

Suppose we are dealing with a *very* short genome $\texttt{TATGGGGTGC}$. Its $k$-mer composition (note the subscript) $Composition_k(Text)$ is the collection of all $k$-mer substrings (including repeated ones). When $k = 3$ we get (basically we split sequence into windows of length 3 sliding window by 1 base every time):

<div>
	$$
Composition_3(\texttt{TATGGGGTGC}) = \texttt{ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
$$
</div>

Note that we have listed $k$-mers in lexicographic order (i.e., how they would appear in a dictionary) rather than in the order of their appearance in $\texttt{TATGGGGTGC}$. We have done this because the correct ordering of the reads is unknown when they are generated (i.e., a sequencing machine does not generate reads in any particular order). 

## Assembly by overlap

In the example above we knew what the "genome" sequence was. In real life we don't know that sequence and our goal is to detemine it given a scrambled collection of $k$-mers. Let's consider the following collection of 3-mers representing a hypothetical genome:

<div>
  $$
\texttt{AAT ATG GTT TAA TGT}
$$
</div>

Let's "tile" $k$-mers if they overlap in $k$-1 nucleotides:


```
TAA
 AAT
  ATG
   TGT
    GTT
TAATGTT
```

Now let's apply it to slightly longer "genome" with the following 3-mer composition sorted in a lexicographic order:

<div>
  $$
  \texttt{AAT ATG ATG ATG CAT CCA GAT GCC GGA GGG GTT TAA TGC TGG TGT}
$$
</div> 

`TAA` looks like a great beginning and we are continuing:
```
1 TAA
2  AAT
3   ATG
4    TGT
5     GTT
```

There is nothing in the original 3-mer composition, which starts with `TT`. Let's track back and instead of `TGT` in step 4 insert `TGC`:

```
 1 TAA
 2  AAT
 3   ATG
 4    TGC
 5     GCC
 6      CCA
 7       CAT
 8        ATG
 9         TGG
10          GGA
11           GAT
12            ATG
13             TGT
14              GTT
```

We only used 14 3-mers from the total of 15, so our genome is shorter (we have extra parts!). This difficulty is related to the fact that there are three repeated `ATG` motifs in this genome and as a result each `ATG` can be extended by either `TGG`, `TGC`, or `TGT`. 

## The concept of coverage

*Coverage* is the number of reads covering a particular position in the genome. For example, in the following case:

```
TAA
 AAT
  ATG     <- "reads" (15 bases total)
   TGT
    GTT
-------
TAATGTT   <- "genome" (7 bases)
-------
0123456    
```
The *Coverage* at positions 1 and 6 is *1*, at positions 1 and 5 is *2*, and at position 2, 3, and 4 is *3*. <br>The *Average Coverage* will be $\frac{15}{7}\approx2\times$ 

Below is another, slightly more realistic example where average coverage is $\frac{177}{35}\approx7\times$ 

```
                  CTAGGCCCTCAATTTTT
                CTCTAGGCCCTCAATTTTT
              GGCTCTAGGCCCTCATTTTTT
           CTCGGCTCTAGCCCCTCATTTT
        TATCTCGACTCTAGGCCCTCA         <- 177 bases
        TATCTCGACTCTAGGCC
    TCTATATCTCGGCTCTAGG
GGCGTCTATATCTCG
GGCGTCGATATCT
GGCGTCTATATCT
-----------------------------------
GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT   <- 35 bases
-----------------------------------
|         |         |         |   |
0         10        20        30  34
```

## The First and the Second laws on assembly

The goal of assembly process is to reconstruct unknown genome sequences given a collection of scrambled sequencing reads:

>
```
CTAGGCCCTCAATTTTT
CTCTAGGCCCTCAATTTTT
GGCTCTAGGCCCTCATTTTTT
CTCGGCTCTAGCCCCTCATTTT
TATCTCGACTCTAGGCCCTCA                 <- Reads (Given)
TATCTCGACTCTAGGCC
TCTATATCTCGGCTCTAGG
GGCGTCTATATCTCG
GGCGTCGATATCT
GGCGTCTATATCT
-----------------------------------
???????????????????????????????????   <- Genome (Unknown)
```
>
>**The goal of assembly process**. Given sequencing reads reconstruct underlying genome sequence. 


 We've seen that this can (in principle) be accomplished by finding overlaps. We also discussed the concept of the coverage.  We can now formulate the two first assembly laws.

### The First Assembly Law: Overlaps imply co-location

Let's define terms **Prefix** and **Suffix** using string $\texttt{TAA}$ as an example:

 * $Prefix(\texttt{TAA}) = \texttt{TA}$
 * $Suffix(\texttt{TAA}) = \texttt{AA}$

The First law states that if a *suffix* of one read is similar to a *prefix* of another read...

```
TCTATATCTCGGCTCTAGG    <- read 1
    ||||||| ||||||| 
    TATCTCGACTCTAGGCC  <- read 2
```

...then they may overlap (may be derived from the same location) within the genome

```
      TCTATATCTCGGCTCTAGG                  <- read 1
 -------------------------------------
 AGCGTTCTATATCTCGGCTCTAGGCCGTGCAGGACGT     <- genome
 -------------------------------------
          TATCTCGACTCTAGGCC                <- read 2
```
Note that in the above example suffix of the first read is *not* exactly identical to the prefix of the second read: they differ by a G-to-A substitution. Such differences are quite common is may be caused by:

* **sequencing errors** - experimental or computational artifacts of DNA sequencing procedures.
* **allelic differences** - organisms such as human are diploid (and others, such as wheat are hexaploid) which maternal and paternal genomes being different at a number of genomic sites. 
* **polymorphic sites** - DNA that is being sequenced is usually isolated from a large number of cells (e.g., white blood cells) or individuals (bacterial and viral cultures). Natural variation present in these cell (or viral particle) populations will manifest itself as these differences. 

### The Second Assembly Law: The higher the coverage, the better

The Second law states that higher coverage leads to more frequent and longer overlaps:

```
                   CTAGGCCCTCAATTTTT
         TATCTCGACTCTAGGCCCTCA         <- Low coverage
 GGCGTCTATATCT
 -----------------------------------
 GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT   <- Genome
 -----------------------------------
                   CTAGGCCCTCAATTTTT
                 CTCTAGGCCCTCAATTTTT
               GGCTCTAGGCCCTCATTTTTT
            CTCGGCTCTAGCCCCTCATTTT
         TATCTCGACTCTAGGCCCTCA         <- Higher coverage
         TATCTCGACTCTAGGCC
     TCTATATCTCGGCTCTAGG
 GGCGTCTATATCTCG
 GGCGTCGATATCT
 GGCGTCTATATCT
```

# Solving assembly problem with graphs

We can solve assembly challenge using overlaps between sequencing reads. However, to solve this problem effectively we need to first represent all overlaps in a way that would facilitate further analysis. *Directed graphs* help achieving this. 

## Directed graphs 

Finding overlaps is identical to building a *directed graph* where directed *edges* connect *nodes* representing overlapping reads:

>![](/BMMB554/img/dag.png)
>
>**Directed graph** representing overlapping reads. (Image from [Ben Langmead](http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_scs.pdf)).


For example, the following string reconstruction:

```
 1 TAA
 2  AAT
 3   ATG
 4    TGC
 5     GCC
 6      CCA
 7       CAT
 8        ATG
 9         TGG
10          GGA
11           GAT
12            ATG
13             TGT
14              GTT
   TAATGCCATGGATGTT
```

can be represented as a following directed graph (or genome path):

>![](http://www.bx.psu.edu/~anton/bioinf-images/4.6.png)
>
>**Genome path**. Trimers composing the $\texttt{TAATGCCATGGGATGTT}$ sequence represented as the "genome" path. (Fig. 4.6 from CP). In this path a suffix of a 3-mer is equal to prefix of the next 3-mer. 

**However**, we do not know the actual genome! All we have in real life is a collection of reads. Let's first build an overlap graph by connecting two 3-mers if suffix of one is equal to the prefix of the other:


>![](http://www.bx.psu.edu/~anton/bioinf-images/4.7.png)
>
>**Overlap graph**. All possible overlap connections for our 3-mer collection. (Fig. 4.7 from CP)

In essence, we are looking a path in a graph that visits every node (3-mer) once. Such path is called [Hamiltonial path](https://en.wikipedia.org/wiki/Hamiltonian_path) and it may not be unique. For example for our 3-mer collection there two possible Hamiltonian paths:


>![](http://www.bx.psu.edu/~anton/bioinf-images/4.9a.png)
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.9b.png)
>
>**Two Hamiltonian paths for the 15 3-mers**. Edges spelling "genomes" $\texttt{TAATGCCATGGGATGTT}$ and $\texttt{TAATGGGATGCCATGTT}$ are highlighted in black. (Fig. 4.9. from CP). 

The reason for this "duality" is the fact that we have a *repeat*: 3-mer $\texttt{ATG}$ is present twice on our data (red and blue). As we will see later repeats cause a lot of trouble in genome assembly.

## Finding overlaps

In the example above we had a collection of 3-mers and were always looking for overlaps of length two. In real life things may not be so "regular". Suppose we have two reads:

```
Read X CTCTAGGCC
Read Y TAGGCCCTC
```
what is the overlap between these two reads? For now we will define overlap of $length - l$ suffix of Read X matches $length - l$ prefix of Read Y, where $l$ is given. To find these overlap we look in Read Y for instances $length - l$ suffix of Read X. We will start with some minimal match of length $k$. Once a match is found it will be extended to the left to verify that the entire prefix of Read Y matches:

>![](/BMMB554/img/find_overlap.png)
>
>**Finding overlaps** between Read X and Read Y (Image from [Ben Langmead](http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_scs.pdf)). As a result we represent two two reads are connected nodes:
>
>![](/BMMB554/img/og1.png)
>
>Number above the edge shows the length of the overlap. 

While with just two reads the problem may seen quite straightforward. Let now consider a set of reads representing a very short genome $\texttt{GTACGTACGAT}$:

```
GTACGT
TACGTA
CGTACG
ACGTAC
GTACGA
TACGAT
```

Building an overlap graph with overlap of $length \geq 4$ will give us the following:

>![](/BMMB554/img/og2.png)
>
>You can see that there is a path through this graph that would spell out the original genome sequence $\texttt{GTACGTACGAT}$:
>
>![](/BMMB554/img/og3.png)
>
>Here we are lucky enough to have all nodes having a single outgoing edge with the highest number (the length of overlap). 

## The Shortest Common Superstring Problem

The problem of reconstructing genome using the overlap graph that we have just illustrated can be initially formulated as the *Shortest Common Superstring (SCS)* problem. It states: *given a collection of strings *S*, find *SCS(S), which is the shortest string that contains all strings from the set *S* as substrings*.

For simplicity let's suppose that we have the following set of strings $S$:

<div>
  $$
  S: \texttt{BAA AAB BBA ABA ABB BBB AAA BAB}
  $$
</div>

one way of getting a string that would contain all of these as substrings will simply be concatenating them:

<div>
  $$
  Concat(S):  \texttt{BAAAABBBAABAABBBBBAAABAB}\ (length = 24)
$$
</div>

this, however, is not the *shortest* superstring that contains all strings from $S$. Instead the SCS is:

<div>
  $$
  SCS(S): \texttt{AAABBBABAA}\ (length = 10)
  $$
  </div>

It looks like finding SCS for a set of sequencing reads may just be what we need to produce a genome assembly. But how can this work in practice. One potential idea is to order the strings in some way and "reduce" them into a superstring:
 
>![](/BMMB554/img/scs1.png)
>
>Let's look at the first two strings. They can be "reduced" to `AAAB`:
>
>![](/BMMB554/img/scs2.png)
>
>The next two add an `A`:
>
>![](/BMMB554/img/scs3.png)
>
>Third and fourth add `BB`:
>
>![](/BMMB554/img/scs4.png)
>
>Continuing this we will eventually get `AAABABBAABABBABB`:
>
>![](/BMMB554/img/scs5.png)
>
>But `AAABABBAABABBABB` is the shortest only for this particular ordering. So let's reorder and try again:
>
>![](/BMMB554/img/scs6.png)
>
>Now we did better, but maybe we can do even better.

Ultimately we need to try all possible ordering and pick the shortest among all. Using this approach is we have $S$ strings we will need to do $S!$ tries. This can quickly get impossible. For our set of 
eight strings $8! = 40320$. If we get, say, a 1,000,000 reads from an Illumina machine that the factorial of a million is not going to be an attractive analysis option. 

## Shortest common superstring: Greedy approach

As we've seen it will be impossible to assemble the genome using SCS logic. There is a simplification called *Greedy* approach to SCS problem. Let's take the following set of "reads":

<div>
  $$
  S: \texttt{AAA AAB ABB BBA BBB}
  $$
</div>

and first build an overlap graph:

>![](/BMMB554/img/greedy1.png)
>
>**An overlap graph** for set $S: \texttt{AAA AAB ABB BBA BBB}$.

Next, we start collapsing the nodes to maximize the overlap (and hence to decrease the length of the SCS we are trying to construct):

>In the graph below there are multiple ties: nodes with outgoing edges of identical weights (e.g., edges pointing from `ABB` to both `BBA` and `BBB` have weight of two. Remember, that the weight is the length of overlap between two nodes' labels). In this situation we will break ties by randomly picking an edge to traverse. Let's pick <font color="red">`AAA` &#8594; `AAB`</font>:
>
>![](/BMMB554/img/greedy2.png)
>
>We then merge `AAA` and `AAB` into an SCS containing both, which will be `AAAB`:
>
>![](/BMMB554/img/greedy3.png)
>
>Now let's pick edge <font color="red">`ABB` &#8594; `BBB`</font>:
>
>![](/BMMB554/img/greedy4.png)
>
>Collapse the nodes:
>
>![](/BMMB554/img/greedy5.png)
>
>Pick <font color="red">`ABBB` &#8594; `BBA`</font>:
>
>![](/BMMB554/img/greedy6.png)
>
>Collapse the nodes:
>
>![](/BMMB554/img/greedy7.png)
>
>Pick <font color="red">`AAAB` &#8594; `ABBBA`</font>:
>
>![](/BMMB554/img/greedy8.png)
>
>Collapse again and now we are left with a superstring of length 7:
>
>![](/BMMB554/img/greedy9.png)

The above procedure can be computed *very* quickly. But there is a catch: it does not guarantee that it will give us truly the shortest superstring. It really depends on how we choose edges. Below is another example of using the same dataset in which we traverse graph an a slightly different way:

>We start the same way as before by choosing <font color="red">`AAA` &#8594; `AAB`</font>:
>
>![](/BMMB554/img/greedy2.png)
>
>Merge `AAA` and `AAB`:
>
>![](/BMMB554/img/greedy3.png)
>
>But now we pick a different edge <font color="red">`ABB` &#8594; `BBA`</font>:
>
>![](/BMMB554/img/greedy4_alt.png)
>
>Collapsing these nodes dramatically changes the graph:
>
>![](/BMMB554/img/greedy5_alt.png)
>
>Now we pick <font color="red">`AAAB` &#8594; `ABBA`</font> as this is the edge with the highest weight:
>
>![](/BMMB554/img/greedy6_alt.png)
>
>Collapsing it produces two nodes that are not connected to each other:
>
>![](/BMMB554/img/greedy7_alt.png)

And the SCS of these two will be a concatenation `AAABBABBB` of length 9. Thus a greedy approach may produce different answers. However, it is a sufficient approximation as the superstring yielded this way will not be more than ~2.5 times longer than the true SCS ([Gusfield](https://www.amazon.com/Algorithms-Strings-Trees-Sequences-Computational/dp/0521585198) 16.17.1)

## The Third Law of Assembly: Repeats are Evil!

Let's again apply Greedy SCS to a different "genome". Suppose we want to reconstruct the phrase:

```
a_long_long_long_time 
```

from all 6-mers that overlap by at least 3 characters. The list of 6-mers is:

```
ng_lon 
_long_
a_long
long_l 
ong_ti
ong_lo
long_t
g_long
g_time
ng_tim
```

An overlap graph will look like this:

>![](/BMMB554/img/long.png)
>
>**An overlap graph** for with overlap length $\geq 3$.

If we proceed with Greedy SCS we will follow the following trajectory through the graph:

>![](/BMMB554/img/long_opt.png)
>
>To make things even clearer let's isolate the path:
>
>![](/BMMB554/img/long_opt_focus.png)
>
>The total overlap here (the sum of edge weights) is 4+5+5+5+5+5+5+5+5=44 but it gives us `a_long_long_time` as the shortest superstring:
>

>```
a_long
  long_l
   ong_lo
    ng_lon
     g_long
      _long_
       long_t
        ong_ti
         ng_tim
          g_time
----------------
a_long_long_time
```


We are missing one instance of 'long' in this string. The following graph shows the path that would return the *correct* string:

 >![](/BMMB554/img/long_corr.png)
 >
 >A path yielding the correct string with three repeats. The total overlap here is 5+3+3+5+4+4+5+5+5=39, which is *worse* than the previous path if our goal is to find the shortest superstring:
>
>```
a_long
 _long_
    ng_lon
       long_l
        ong_lo
          g_long
            long_t
             ong_ti
              ng_tim
               g_time
---------------------
a_long_long_long_time
``` 


## Are we really looking for the shortest superstring?

As we've seen above the shortest common superstring (SCS) is:

1. **Difficult to obtain** as Greedy SCS algorithm does not guarantee funding it. So the answer we get may be longer that the real genome we are trying to assemble.

2. **May be shorter than we want** because if the genome contains repeats that are longer than the reads we are using, Greedy SCS will collapse them and make assembly shorter that the genome we are trying to get. 

Let's talk about an alternative *k*-mer representation.

# de Bruijn graphs

[Nicolaas de Bruijn](https://en.wikipedia.org/wiki/Nicolaas_Govert_de_Bruijn) had a purely theoretical interest of constructing _k_-universal strings for an arbitrary value of _k_. A _k_-universal string contains every possible _k_-mer only once:

>[![](http://www.bx.psu.edu/~anton/bioinf-images/deBruijn.png)](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html)
>
>**de Bruijn graph**. From [Compeau:2011](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html)

This problem is equivalent to a string reconstruction problem we have been talking about above: finding a _k_-universal string is equivalent to finding a Hamiltonian path in an overlap graph constructed from all _k_-mers. Yet finding a Hamiltonian path in a really large graph (representing a real genome) is not a tractable problem as we have seen. Instead de Bruijn decided to represent _k_-mer composition in a graph using a slightly different logic. Again, suppose we have a "genome" $\texttt{TAATGCCATGGGATGTT}$ split in a collection of 3-mers:

```
TAA AAT ATG TGC GCC CCA CAT ATG TGG GGG GGA GAT ATG TGT GTT
```

We will assign 3-mers to _edges_ instead or _nodes_:


>![](http://www.bx.psu.edu/~anton/bioinf-images/4.12.png)
>
>**_k_-mers as edges**. Edges represented by 3-mers connect nodes representing the overlaps. (Fig. 4.12 from CP)

This graph can be simplified by gluing identical nodes together:

>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13a.png)
>
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13b.png)
>
>Here the complexity of the graph is reduced by first gluing redundant <font color="red">`AT`</font> nodes
>
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13c.png)
>
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13d.png)
>
>Next, <font color="blue">`TG`</font> nodes are merged
>
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13e.png)
>
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13f.png)
>
>And, finally the two <font color="green">`GG`</font> nodes are resolved. (Fig. 4.13 from CP)

Because we now represent _k_-mers as edges (rather than nodes), our problem has morphed into finding a path that visits every _edge_ once, or an [Eulerian Path](https://en.wikipedia.org/wiki/Eulerian_path):

>![](http://www.bx.psu.edu/~anton/bioinf-images/4.15.png)
>
>**Eulerian paths for the 15 3-mers**. Numbering of edges provides a way to reconstruct the original "genome". (Fig. 4.15 from CP)

## Euler's Theorem

Some definitions:

 * **Balanced node** - a node where the number of incoming edges is equal to the number of outgoing edges
 * **Balanced graph** - a graph where all nodes are balanced
 * **Strongly connected graph** - any node can be reached from any other node

**Euler's Theorem**:

>Every balanced, strongly connected directed graph is Eulerian.

Let's apply Euler's Theorem to a classical problem: The bridges of Köninsberg problem. Here the question is: *Can you walk through all of Köninsberg traversing every bridge exactly one time?* In other words: *Is there a Eulerian path through the city of Köninsberg?*


>![](http://www.bx.psu.edu/~anton/bioinf-images/koninsberg.png)
>
>**Köninsberg and Euler's Theorem**. (a) A map of old Königsberg, in which each area of the city is labeled with a different color point. (b) The Königsberg Bridge graph, formed by representing each of four land areas as a node and each of the city's seven bridges as an edge. (From [Campeau, Pevzner, and Tesler](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html#close))

By looking at this graph we can see that it is *unblanaced*. If one arrives to, say, the <font color="orange">orange</font> node from the <font color="blue">blue</font> node there are two ways to get out. Thus there is no way to see all of the City and traverse every bridge once!

## Repeats are still a challenge

Let's look at the de Bruijn graph from above again. But this time let's drop edge numbering and pretend that the genome is now really known to us (as is usually the case):

>![](/BMMB554/img/dg1.png)
>
>**Eulerian paths for the 15 3-mers**. 

In the original sequence `TAATGCCATGGGATGTT` *k*-mer <font color="red">`AT`</font> is present 3 times and *k*-mer <font color="blue">`TG`</font> is found twice. Thus *multiple* Eulerian walks are now possible like this:

>![](/BMMB554/img/dg2.png)
>
>**Possible path #1**.

The above path spells out:

```
TAA
 AAT
  ATG
   TGC
    GCC
     CCA
      CAT
       ATG
        TGG
         GGG
          GGA
           GAT
            ATG
             TGT
              GTT
-----------------
TAATGCCATGGGATGTT
```
Yet there is an alternative:

>![](/BMMB554/img/dg3.png)
>
>**Possible path #2**

Which spells:

```
TAA
 AAT
  ATG
   TGG
    GGA
     GAT
      ATG
       TGC
        GCC
         CCA
          CAT
           ATG
            TGT
             GTT
----------------
TAATGGATGCCATGTT
```

Note how different these are:

```
TAATGCCATGGGATGTT
|||||
TAATGGATGCCATGTTT
```

## *k*-mer size affects repeat resolution

In the above example we have used *k*-mer size of 3. But what if we try 4 or 5? Below are DeBruijn graphs for different values of *k*:

#### *k* = 3

>![](/BMMB554/img/k2.png)
>
>This is our original graph

#### *k* = 4

>![](/BMMB554/img/k3.png)
>
>Here complexity is decreasing, but we still have the problem with having `ATG` twice.


#### *k* = 5

>![](/BMMB554/img/k4.png)
>
>In this case there is only one path. This because our *k* is larger that the repeat size, so we can resolve it accurately.

# Assembly in real life

In this topic we've learned about two ways of representing the relationship between reads derived from a genome we are trying to assemble:

1. **Overlap graphs** - nodes are reads, edges are overlaps between reads.
2. **DeBruijn graphs** - nodes are overlaps, edges are reads.

>![](http://www.bx.psu.edu/~anton/bioinf-images/4.7.png)
>
>**A**.
>
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.13f.png)
>
>**B.**
>An overlap (A) and DeBruijn (B) graphs for the same string. 

Whatever the representation will be it will be messy:

>![](/BMMB554/img/t12_mess.png)
>
>A fragment of a very large DeBruijn graph (Image from [BL](https://github.com/BenLangmead/ads1-slides/blob/master/0580_asm__practice.pdf)).

There are multiple reasons for such messiness:

### Sequence errors

Sequencing machines do not give perfect data. This results in spurious deviations on the graph. Some sequencing technologies such as Oxford Nanopore have very high error rate of ~15%. 

>![](/BMMB554/img/t12_errors.png)
>
>Graph components resulting from sequencing errors (Image from [BL](https://github.com/BenLangmead/ads1-slides/blob/master/0580_asm__practice.pdf)).

### Ploidy

As we discussed earlier humans are, for example, diploid and there are multiple differences between maternal and paternal genomes. This creates "bubbles" on assembly graphs:

>![](/BMMB554/img/t12_bubble.png)
>
>Bubbles due to a heterozygous site  (Image from [BL](https://github.com/BenLangmead/ads1-slides/blob/master/0580_asm__practice.pdf)).

### Repeats

As we've seen the third law of assembly is unbeatable. As a result some regions of the genome simply cannot be resolved and are reported in segments called *contigs*:

>![](/BMMB554/img/t12_contigs.png)
>
>The following "genomic" segment will be reported in three pieces corresponding to reagions flanking the repeat and repeat itself (Image from [BL](https://github.com/BenLangmead/ads1-slides/blob/master/0580_asm__practice.pdf)).

# Next

Next topic will cover assembly in practice as we will attempt to put together an *E. coli* genome sequenced with Illumina and Oxford Nanopore. 