![](https://i.imgur.com/phZHgSu.png)

# Assembly

$k$-mer composition

Genomes are strings of text. When we sequence genomes we use sequencing machines that generate reads. For now let's assume that all reads have the same length $k$ and every $k$-mer is sequenced only once. We will relax these assumptions later in this lecture. Thus sequencing a genome generates a large list of $k$-mers.  

Suppose we are dealing with a *very* short genome `TATGGGGTGC`. Its $k$-mer composition (note the subscript) $Composition_k(Text)$ is the collection of all $k$-mer substrings (including repeated ones). When $k$ = 3 we get (basically we split sequence into windows of length 3 sliding window by 1 base every time):

$$
Composition_3(\texttt{TATGGGGTGC}) = \texttt{ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
$$

Note that we have listed *k*-mers in lexicographic order (i.e., how they would appear in a dictionary) rather than in the order of their appearance in $\texttt{TATGGGGTGC}$. We have done this because the correct ordering of the reads is unknown when they are generated (i.e., a sequencing machine does not generate reads in any particular order). 

## Assembly by overlap

In the example above we know what the "genome" sequence is. In real life we don't know that and our goal is to determine genome sequence given a scrambled collection of $k$-mers. Let's consider the following collection of 3-mers representing a hypothetical genome:

$$
\texttt{AAT ATG GTT TAA TGT}
$$

Let's "tile" $k$-mers if they overlap in $k-1$ nucleotides:


```
TAA
 AAT
  ATG
   TGT
    GTT
-------
TAATGTT
```

Now let's apply it to slightly longer "genome" with the following 3-mer composition sorted in a lexicographic order:

$$
  \texttt{AAT ATG ATG ATG CAT CCA GAT GCC GGA GGG GTT TAA TGC TGG TGT}
$$

`TAA` looks like a great beginning and we are continuing:
```
1 TAA
2  AAT
3   ATG
4    TGT
5     GTT
  -------
  TAATGTT
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
   ----------------
   TAATGCCATGGATGTT
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

## The First and the Second laws of assembly

The goal of assembly process is to reconstruct an unknown genome sequence given a collection of scrambled sequencing reads:

-----

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

**The goal of assembly process**. Given sequencing reads reconstruct underlying genome sequence.

-----

 We've seen that this can (in principle) be accomplished by finding overlaps. We also discussed the concept of the coverage.  We can now formulate the two first assembly laws.

### The First Assembly Law: Overlaps imply co-location

Let's define terms **Prefix** and **Suffix** using string $\texttt{TAA}$ as an example:

 * $Prefix(\texttt{TAA}) = \texttt{TA}$
 * $Suffix(\texttt{TAA}) = \texttt{AA}$

The First law states that if a *suffix* of one read is similar to a *prefix* of another read ...

```
TCTATATCTCGGCTCTAGG    <- read 1
    ||||||| ||||||| 
    TATCTCGACTCTAGGCC  <- read 2
```

... then they may overlap (may be derived from the same location) within the genome.

```
      TCTATATCTCGGCTCTAGG                  <- read 1
 -------------------------------------
 AGCGTTCTATATCTCGGCTCTAGGCCGTGCAGGACGT     <- genome
 -------------------------------------
          TATCTCGACTCTAGGCC                <- read 2
```

Note that in the above example suffix of the first read is *not* exactly identical to the prefix of the second read: they differ by a G-to-A substitution. Such differences are quite common in real life and may be caused by:

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

## Solving assembly problem with graphs

We can solve assembly challenge using overlaps between sequencing reads. However, to solve this problem effectively we need to first represent all overlaps in a way that would facilitate further analysis. *Directed graphs* help achieving this. 

### Directed graphs 

Finding overlaps is identical to building a *directed graph* where directed *edges* connect *nodes* representing overlapping reads:

------

![](https://i.imgur.com/TeoO58f.png)

**Directed graph** representing overlapping reads. (Image from [Ben Langmead](http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_scs.pdf))

------

For example, the string reconstruction we have seen earlier (with the difference of inserting `GGG` in line 10):

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
10          GGG
11           GGA
12            GAT
13             ATG
14              TGT
15               GTT
   -----------------
   TAATGCCATGGGATGTT
```

can be represented as a following directed graph (or genome path):

-----

![](https://i.imgur.com/yLV2ywo.png)


**Genome path**. Trimers composing the $\texttt{TAATGCCATGGGATGTT}$ sequence represented as the "genome" path. (Fig. 4.6 from CP). In this path a suffix of a 3-mer is equal to prefix of the next 3-mer.


-----

**However**, we do not know the actual genome! All we have in real life is a collection of reads. Let's first build an overlap graph by connecting two 3-mers if suffix of one is equal to the prefix of the other:

------

![](https://i.imgur.com/QMDqdT3.png)

**Overlap graph**. All possible overlap connections for our 3-mer collection. (Adopted from Fig. 4.7 from CP)</small>

------

So to determine the sequence of the underlying genome we are looking a path in this graph that visits every node (3-mer) once. Such path is called [Hamiltonial path](https://en.wikipedia.org/wiki/Hamiltonian_path) and it may not be unique. For example for our 3-mer collection there two possible Hamiltonian paths:

------
Path 1:

![](https://i.imgur.com/XX6iLya.png)



Path 2:

![](https://i.imgur.com/qKjciNl.png)


**Two Hamiltonian paths for the 15 3-mers**. Edges spelling "genomes" $\texttt{TAATGCCATGGGATGTT}$ and $\texttt{TAATGGGATGCCATGTT}$ are highlighted in black. (Adopted Fig. 4.9. from CP)

------

The reason for this "duality" is the fact that we have a *repeat*: 3-mer $\texttt{ATG}$ is present three times in our data (<font color="green">green</font>, <font color="red">red</font>, and <font color="blue">blue</font>). As we will see later repeats cause a lot of trouble in genome assembly.

## The Third Law of Assembly: Repeats are Evil!

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

-----

![](https://i.imgur.com/B1HhK6L.png)


**An overlap graph** for with overlap length $\geq 3$.

------

If we try to maximimize the overlap we will get this:

-----

![](https://i.imgur.com/2qCFl0c.png)

To make things even clearer let's isolate the path:

![](https://i.imgur.com/67Y0tcb.png)

The total overlap here (the sum of edge weights) is $4+5+5+5+5+5+5+5+5=44$

------

The problem is that $4+5+5+5+5+5+5+5+5=44$ gives us `a_long_long_time` as the shortest superstring:

```
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


We are missing one instance of `long` in this string. The following graph shows the path that would return the *correct* string:

-----

![](https://i.imgur.com/xjRznUF.png)

A path yielding the correct string with three repeats. The total overlap here is $5+3+3+5+4+4+5+5+5=39$

-----

The above graph with overlap $5+3+3+5+4+4+5+5+5=39$ is actually *worse* than the previous path if our goal is to find the shortest superstring:

```
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


## de Bruijn graphs

[Nicolaas de Bruijn](https://en.wikipedia.org/wiki/Nicolaas_Govert_de_Bruijn) had a purely theoretical interest of constructing $k$-universal strings for an arbitrary value of $k$. A $k$-universal string contains every possible $k$-mer only once:

------

![](https://i.imgur.com/ya9yVT1.png)


**de Bruijn graph**. From [Compeau:2011](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html)

------

This problem is equivalent to a string reconstruction problem we have been talking about above: finding a $k$-universal string is equivalent to finding a Hamiltonian path in an overlap graph constructed from all $k$-mers. Yet finding a Hamiltonian path in a really large graph (representing a real genome) is not a tractable problem as we have seen. Instead de Bruijn decided to represent $k$-mer composition in a graph using a slightly different logic. Again, suppose we have a "genome" $\texttt{TAATGCCATGGGATGTT}$ split in a collection of 3-mers:

```
TAA AAT ATG TGC GCC CCA CAT ATG TGG GGG GGA GAT ATG TGT GTT
```

We will assign 3-mers to _edges_ instead or _nodes_:

-----

![](https://i.imgur.com/p3ZaiGA.png)


**$k$-mers as edges**. Edges represented by 3-mers connect nodes representing the overlaps. (Adopted from Fig. 4.12 from CP).

------

This graph can be simplified by gluing identical nodes together:

-----

![](https://i.imgur.com/tIEATZQ.png)
![](https://i.imgur.com/E3xLpHk.png)

Here the complexity of the graph is reduced by first gluing redundant <font color="red">`AT`</font> nodes

![](https://i.imgur.com/k4PK6Os.png)
![](https://i.imgur.com/nFCwH2F.png)


Next, <font color="blue">`TG`</font> nodes are merged

![](https://i.imgur.com/25mq4mc.png)
![](https://i.imgur.com/PCk9xcU.png)

And, finally the two <font color="green">`GG`</font> nodes are resolved. (Adopted from Fig. 4.13 from CP)

------


Because we now represent _k_-mers as edges (rather than nodes), our problem has morphed into finding a path that visits every _edge_ once, or an [Eulerian Path](https://en.wikipedia.org/wiki/Eulerian_path):

------

![](https://i.imgur.com/2rGUmCi.png)

**Eulerian paths for the 15 3-mers**. Numbering of edges provides a way to reconstruct the original "genome". (Adopted from Fig. 4.15 from CP)

------

## Euler's Theorem

Some definitions:

 * **Balanced node** - a node where the number of incoming edges is equal to the number of outgoing edges
 * **Balanced graph** - a graph where all nodes are balanced
 * **Strongly connected graph** - any node can be reached from any other node

**Euler's Theorem**:

>Every balanced, strongly connected directed graph is Eulerian.

Let's apply Euler's Theorem to a classical problem: The bridges of Köninsberg problem. Here the question is: *Can you walk through all of Köninsberg traversing every bridge exactly one time?* In other words: *Is there a Eulerian path through the city of Köninsberg?*

-----

![](https://i.imgur.com/QzmL8g4.png)

**Köninsberg and Euler's Theorem**. (a) A map of old Königsberg, in which each area of the city is labeled with a different color point. (b) The Königsberg Bridge graph, formed by representing each of four land areas as a node and each of the city's seven bridges as an edge. (From [Campeau:2011](http://www.nature.com/nbt/journal/v29/n11/abs/nbt.2023.html#close))

------

By looking at this graph we can see that it is *unblanaced*. If one arrives to, say, the <font color="orange">orange</font> node from the <font color="blue">blue</font> node there are two ways to get out. Thus there is no way to see all of the city and traverse every bridge once!

----

<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d73747.90922499954!2d20.451778999511713!3d54.71627037775103!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNTTCsDQzJzAwLjAiTiAyMMKwMzEnMDAuMCJF!5e0!3m2!1sen!2sus!4v1615904421852!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>

Another problem with bridges of Köninsberg, is that Köninsberg no longer exists.

-----

## Repeats are still a challenge

Let's look at the de Bruijn graph from above again. But this time let's drop edge numbering and pretend that the genome is not really known to us (as is usually the case in real life):

------

![](https://i.imgur.com/pYXzYox.png)

**Eulerian paths for the 15 3-mers**.

------

In the original sequence `TAATGCCATGGGATGTT` $k$-mer <font color="red">`AT`</font> is present 3 times and $k$-mer <font color="blue">`TG`</font> is found twice. Thus *multiple* Eulerian walks are now possible like this:

------

![](https://i.imgur.com/Ruv2DPV.png)

**Possible path #1**. Here after we reach <font color="blue">`TG`</font> node we turn **up**.

-------

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

------

![](https://i.imgur.com/TvUb8Se.png)

**Possible path #2**. Here after we reach <font color="blue">`TG`</font> node we turn **dow**.

-------

Which spells:

```
TAA
 AAT
  ATG
   TGG
    GGG
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
-----------------
TAATGGGATGCCATGTT
```

Note how different these are (`|` = same; `*` = different):

```
TAATGCCATGGGATGTT
|||||**|||**|||||
TAATGGGATGCCATGTT
```

and only one of them is correct. <font color="orange">Repeats are evil!</font>

## $k$-mer size affects repeat resolution

In the above example we have used $k$-mer size of 3. But what if we try 4 or 5? Below are DeBruijn graphs for different values of $k$:

------
$k = 3$:

![image](https://github.com/user-attachments/assets/5e4d2858-72ef-4026-b004-f52e580f6f5d)


This :point_up: is our original graph.

$k = 4$:

![image](https://github.com/user-attachments/assets/68bf7fec-06e6-46bd-b33a-29dbd19c60f1)

Here complexity is decreasing, but we still have the problem with having `ATG` twice.

$k = 5$:

![image](https://github.com/user-attachments/assets/72da830f-3fb6-4065-8b03-c5080985b8d2)

In this case there is only one path. This because our $k$ is larger that the repeat size, so we can resolve it accurately.

------

This is why technologies producing long sequencing reads stimulate so much enthusiasm - they will allow to resolve and produce accurate assembly of large genomes. 

## Overlap Graphs versus deBruijn graphs:

The **fundamental difference** between **de Bruijn graphs** and **overlap graphs** in genome assembly lies in **how they represent relationships between sequencing reads**:

### 1. **Unit of Representation**

- **Overlap Graphs**:
  - Nodes represent **entire sequencing reads**.
  - Edges represent **overlaps** between the suffix of one read and the prefix of another (typically ≥ a certain length).

- **de Bruijn Graphs**:
  - Nodes represent **k-mers** (short substrings of length *k* extracted from reads).
  - Edges represent **(k+1)-mers**, connecting two k-mers if one shifts into the other by one nucleotide.



### 2. **Graph Construction Philosophy**

- **Overlap Graph**:
  - Based on **explicit pairwise comparison** of reads to find overlaps.
  - Scales poorly with large numbers of reads: **O(n²)** comparisons.

- **de Bruijn Graph**:
  - Based on **k-mer decomposition**, avoiding pairwise comparisons.
  - Scales well for large datasets; efficient to construct using **hash tables** or **Bloom filters**.



### 3. **Handling of Repeats**

- **Overlap Graph**:
  - Better preserves **long-range information**, so can help resolve longer repeats if coverage and read length are sufficient.
  
- **de Bruijn Graph**:
  - More prone to **collapse repeats** shorter than the k-mer size; choice of *k* is critical.
  - Sensitive to sequencing errors — can fragment the graph if *k* is too large or introduce bubbles if too small.



### 4. **Assembly Use Case Suitability**

| Use Case        | Overlap Graphs           | de Bruijn Graphs             |
|-----------------|--------------------------|------------------------------|
| Long reads      | ✅ Ideal                  | ❌ Inefficient               |
| Short reads     | ❌ Memory-intensive       | ✅ Efficient and compact     |
| Error tolerance | ✅ Better error modeling  | ❌ Needs error correction    |





