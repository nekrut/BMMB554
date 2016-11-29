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

# Genome Assembly

Genome assembly is a difficult task. It is especially challenging to describe it without using formal mathematical reasoning. Fortunately, others have been extremely successful in achieving this goal. Perhaps the best explanation of genome  assembly logic for biological audiences was provided by two highly regarded sources:

- [Pevzner and Compeau](http://www.amazon.com/Bioinformatics-Algorithms-Active-Learning-Approach/dp/0990374602). 
- [Ben Langmead](http://www.langmead-lab.org/teaching-materials/)

The material in this lecture relies heavily on these two sources.


# Strings and _k_-mers

Genomes is a string of text (well multiple strings if you consider multiple chromosomes). Let's divide it into _k_-mers (to approximate the sequencing reads). Given a string, its _k_-mer composition (note the subscript) $Composition_k(Text)$ is the collection of all _k_-mer substrings of Text (including repeated _k_-mers). For example,

<div>
	$$
Composition_3(\texttt{TATGGGGTGC}) = \texttt{ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
$$
</div>

Note that we have listed _k_-mers in lexicographic order (i.e., how they would appear in a dictionary) rather than in the order of their appearance in $\texttt{TATGGGGTGC}$. We have done this because the correct ordering of the reads is unknown when they are generated.

Consider the following example of 3-mer composition:

```
AAT ATG GTT TAA TGT
```

Let's "tile" _k_-mers if they overlap in _k_-1 nucleotides:


```
TAA
 AAT
  ATG
   TGT
    GTT
TAATGTT
```

Now let's apply it to slightly longer "genome" with the following 3-mer composition sorted in a lexicographic order:

```
AAT ATG ATG ATG CAT CCA GAT GCC GGA GGG GTT TAA TGC TGG TGT
``` 
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

## Strings and graphs

Let's define terms **Prefix** and **Suffix**:

 * $Prefix(\texttt{TAA}) = \texttt{TA}$
 * $Suffix(\texttt{TAA}) = \texttt{AA}$

 ###

The following string reconstruction:

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

can be represented as a genome path:

>![](http://www.bx.psu.edu/~anton/bioinf-images/4.6.png)
>
>**Genome path**. Trimers composing the $\texttt{TAATGCCATGGGATGTT}$ sequence represented as the "genome" path. (Fig. 4.6 from CP)

In this path a suffix of a 3-mer is equal to prefix of the next 3-mer. In other words, if we do not know the genome path (which we really never do in real life), we can try to define one by connecting two 3-mers if suffix of one is equal to the prefix of the other:


>![](http://www.bx.psu.edu/~anton/bioinf-images/4.7.png)
>
>**Overlap graph**. All possible overlap connections for our 3-mer collection. (Fig. 4.7 from CP)

In essence, we are looking a path in a graph that visits every node (3-mer) once. Such path is called [Hamiltonial path](https://en.wikipedia.org/wiki/Hamiltonian_path) and it may not be unique. For example for our 3-mer collection there two possible Hamiltonian paths:


>![](http://www.bx.psu.edu/~anton/bioinf-images/4.9a.png)
>![](http://www.bx.psu.edu/~anton/bioinf-images/4.9b.png)
>
>**Two Hamiltonian paths for the 15 3-mers**. Edges spelling "genomes" $\texttt{TAATGCCATGGGATGTT}$ and $\texttt{TAATGGGATGCCATGTT}$ are highlighted in black. (Fig. 4.9. from CP).

## de Bruijn graphs

[Nicolaas de Bruijn](https://en.wikipedia.org/wiki/Nicolaas_Govert_de_Bruijn) was interested in constructing _k_-universal strings for an arbitrary value of _k_. A _k_-universal string contains every possible _k_-mer only once:

>[![](http://www.bx.psu.edu/~anton/bioinf-images/deBruijn.png)](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html)
>
>**de Bruijn graph**. From [Compeau:2011](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html)

This problem is equivalent to a string reconstruction problem demonstrated above: finding a _k_-universal string is equivalent to finding a Hamiltonian path in an overlap graph constructed from all _k_-mers. Yet finding a Hamiltonian path in a really large graph (representing a real genome) is not a tractable problem. Instead de Bruijn decided to represent _k_-mer composition in a graph using a slightly different logic. Again, suppose we have a "genome" $\texttt{TAATGCCATGGGATGTT}$ split in a collection of 3-mers:

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

Because we now represent _k_-mers as edges, our problem has morphed into finding a path that visits every _edge_ once, or an [Eulerian Path](https://en.wikipedia.org/wiki/Eulerian_path):

|Eulerian paths for the 15 3-mers|
|--------|
|![](http://www.bx.psu.edu/~anton/bioinf-images/4.15.png)|
|Numbering of edges provides a way to reconstruct the original "genome". (Fig. 4.15 from CP)|

## The seven bridges of Köninsberg

| Köninsberg and Euler | 
|----------------------|
|![](http://www.bx.psu.edu/~anton/bioinf-images/koninsberg.png)|
|From [Campeau, Pevzner, and Tesler](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html#close) (a) A map of old Königsberg, in which each area of the city is labeled with a different color point. (b) The Königsberg Bridge graph, formed by representing each of four land areas as a node and each of the city's seven bridges as an edge.|

## Euler's Theorem

Some definitions:

 * `Balanced node - a node where the number of incoming edges is equal to the number of outgoing edges` 
 * `Balanced graph - a graph where all nodes are balanced`
 * `Strongly connected graph - any node can be reached from any other node`

Euler's Theorem:

```
Every balanced, strongly connected directed graph is Eulerian.
```

## Finding Eulerian cycle

```
EulerianCycle(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking 
            Cycle ← Cycle’
        return Cycle
```

The figures below use Campeau and Pevzner's ant named _Leo_ to illustrate recursive nature of funding a Eulerian path:

![](http://www.bx.psu.edu/~anton/bioinf-images/4.22.png)
![](http://www.bx.psu.edu/~anton/bioinf-images/4.23.png)
![](http://www.bx.psu.edu/~anton/bioinf-images/4.24.png)
![](http://www.bx.psu.edu/~anton/bioinf-images/4.25.png)


