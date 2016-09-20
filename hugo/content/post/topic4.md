+++
categories = []
date = "2016-09-19T10:12:04-04:00"
#draft = true
featureimage = ""
menu = ""
tags = []
title = "topic4"

+++

# Sequence alignment

This lecture closely follows Ben Langmead's tutorial on edit distance and dynamic programming. 

# How different are two sequnces?

Suppose you have two sequences of the same length:


```
A C A T G C C T A
A C T G C C T A C
```

How different are they? In other words, how many bases should be change to turn one sequence onto the other:


```
A C A T G C C T A
| | * * * | * * *
A C T G C C T A C
```

the vertical lines above indicate positions that are identical between the two sequences, while asterisks show differences. It will take six substitutions to turn one sequence into the other. This is so called [*Hamming distance*](https://en.wikipedia.org/wiki/Hamming_distance) or the *minimal* number of substitutions required to turn one string into another. The code below computes the Hamming distance:


<iframe src="https://trinket.io/embed/python/99a02b790a?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Now in addition to *substitutions* (i.e., changing one character into another) let's allow **instertions** and **deletions**. This essentially will allow us insert dashes between characters:

```
A C A T G C C T A -
| | * | | | | | | *
A C - T G C C T A C
```

In this case the [**Edit distance**](https://en.wikipedia.org/wiki/Edit_distance) between two sequences is 2. It is defined as the minimum number of operations (substitutions, insertions, and develetions) requited to turn one string into another. The comparted strings do not have to be of the same length to be able to compute the edit distance as we can compensate for this using deletions and insertions. While the situation above (where we instert two dashes) is biologically much more meangful (and realistic) it is much more difficult to find. 

# Generalizing the problem

Before we can develop an algorithm that will help us to compute the edit distance let's develop a general framework that would allow us to think about the problem in exact terms. Let's look at a pair of VERY long sequences. So long, that we do not even see the left end - it disappears into infinity:

<div>
	$$
		\texttt{.....a c t g c c t a G}\\
		\texttt{.....a c t g c c t a C}
	$$
</div>

the lowercase parts of the two sequences represent **prefixes** for the last nucleotides shown in the uppercase. Let's assume that the edit distance between the two prefixes is known (don't ask how we know, we just do). For simplicity let's "compact" the prefix of the first sequence into $\alpha$ and the prefix of the second sequence into $\beta$:

<div>
	$$
		\alpha \texttt{G}\\
	    \beta  \texttt{C}
	$$
</div>

again, the edit distance between $\alpha$ and $\beta$ are know to us. So now the edit distance between the two sequence can be computed using the following expression:

<div>

$$Edit\ Distance(\alpha\texttt{G},\beta\texttt{C})  = min\begin{cases} 
					Edit\ Distance(\alpha,\beta) + 1 & \\
					Edit\ Distance(\alpha\texttt{G},\beta) + 1 & \\
					Edit\ Distance(\alpha,\beta\texttt{C}) + 1
             \end{cases}$$

</div>

but we not always have $\texttt{G}$ and $\texttt{C}$ as two last nucleotiodes, so for the general case:

<div>

$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					Edit\ Distance(\alpha,\beta) + \delta(x,y) & \\
					Edit\ Distance(\alpha\texttt{x},\beta) + 1 & \\
					Edit\ Distance(\alpha,\beta\texttt{y}) + 1
             \end{cases}$$

</div>

where $\delta(x,y) = 0$ if $x = y$ and $\delta(x,y) = 1$ if $x \neq y$. The $\delta(x,y)$ has a particular meaning. If the two nucleotides at the end are equal to each other, there is nothing to be done - no substitution operation is necessary. If a substitution is neecessary however, we will record this by adding 1. 

Recall the change problem from the previous lecture. We can write an algorithm that would exhaustively evaluate the above axtression for all possible suffixes. This algorithm is below. Try executing it. It will take roughly 30 seconds to find teh edit distance between the two sequences used in the beginning of this lecture:

<iframe src="https://trinket.io/embed/python/eff3a798bf?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Again, don't worry if Python looks scary to you. The take-home-message here is that it takes a very long time to compute the edit distance between two sequences that are only **nine** nucleotides long. Why is this happeining? Figure below shows a small subset of situations the algorithm is evaluating for two very short strings $\texttt{TAG}$ and $\texttt{TAC}$: 

> ![](http://www.bx.psu.edu/~anton/bioinf-images/editDist.png)
>
> **Figure 1** | A fraction of situations evaluated by the naïve algorithm for computing the edit distance. Just like in the case of the change problem discussed in the previous lecture a lot of time is wasted on computing distances between suffixes that has been seen more than once (shown in red).

To understand the magnitude of this problem let's look at slightly modified version of the previous Python code shown below. All we do here is keeping track how many times a particular pair of suffixes (in this case $\texttt{AC}$ and $\texttt{AC}$) are seen by the program. The number is staggering: 48,639. So this algorithm is **extremely** wasteful. 

<iframe src="https://trinket.io/embed/python/8994bfe46e?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So this approach to the edit distance problem will hardly help us on the genome-wide scale. Just like in case of the change proglem and Manhattan tourist problem dynamic programming is going to help us. 

# Dynamic programming to the rescue

Let's recall Manhattan tourist problem. The objective of the problem was to find a path through Manhattant that visits the highest number of langdmarks. If you remember, we represented mahattan as a matrix where each edge was representing a block and was lebelled with the number of landmarks within that block. Here, we will use a similar idea to find an optimal **alignment** between two sequences. Note that so far this is the first time we use the term **alignment** in this section. It turns out that in order to find the alignemnt we first need to learn how to compute edit distances between sequences efficiently. So, suppose we have two sequences that deliberately have different lenghts:

$\texttt{G C T A T A C}$

and 

$\texttt{G C G T A T G C}$

Let's represent them as the following matrix where the first character $\epsilon$ represents an empty string:


<div>
	$$
	\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & G & C & T & A & T & A & C\\
  					\hline
 					\epsilon\\
 					\hline
 					G\\
 					\hline
 					C\\
 					\hline
 					G\\
 					\hline
 					T\\
 					\hline
 					A\\
 					\hline
 					T\\
 					\hline
 					G\\
 					\hline
 					C

 \end{array}
  	$$
</div>

Let's fill the first column and first raw of the matrix. Because the distance between a string and an empty string is equal to the length of the string (e.g., a distance between string $\texttt{TAG}$ and an empty string is 3) this resulting matrix will look like this:

<div>
	$$
	\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & G & C & T & A & T & A & C\\
  					\hline
 					\epsilon & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7\\
 					\hline
 					G & 1\\
 					\hline
 					C & 2\\
 					\hline
 					G & 3\\
 					\hline
 					T & 4\\
 					\hline
 					A & 5\\
 					\hline
 					T & 6\\
 					\hline
 					G & 7\\
 					\hline
 					C & 8

 \end{array}
  	$$
</div>

Now, let's fill in the cell between $\texttt{G}$ and $\texttt{G}$. Let's recall that:

<div>

$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					\color{red}{Edit\ Distance(\alpha,\beta) + \delta(x,y)} & \\
					\color{blue}{Edit\ Distance(\alpha\texttt{x},\beta) + 1} & \\
					\color{green}{Edit\ Distance(\alpha,\beta\texttt{y}) + 1}
             \end{cases}$$

</div>

where $\delta(x,y) = 0$ if $x = y$ and $\delta(x,y) = 1$ if $x \neq y$. And now let's color each of the cells correspoinding to each part of the above expression:

<div>
	$$
	\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & G & C & T & A & T & A & C\\
  					\hline
 					\epsilon & \color{red}0 & \color{green}1 & 2 & 3 & 4 & 5 & 6 & 7\\
 					\hline
 					G & \color{blue}1\\
 					\hline
 					C & 2\\
 					\hline
 					G & 3\\
 					\hline
 					T & 4\\
 					\hline
 					A & 5\\
 					\hline
 					T & 6\\
 					\hline
 					G & 7\\
 					\hline
 					C & 8

 \end{array}
  	$$
</div>

In this specific case:

<div>

$$Edit\ Distance(\epsilon\texttt{G},\epsilon\texttt{G}) = min\begin{cases} 
					\color{red}{Edit\ Distance(\epsilon,\epsilon) + \delta(G,G)\ or\ 0\ +\ 0\ =\ 0} & \\
					\color{blue}{Edit\ Distance(\epsilon\texttt{G},\epsilon) + 1\ or\ 1\ +\ 1\ =\ 2} & \\
					\color{green}{Edit\ Distance(\epsilon,\epsilon\texttt{G}) + 1\ or\ 1\ +\ 1\ =\ 2}
             \end{cases}$$

</div>

This minimum of 0, 2, and 2 will be 0, so we are putting zero into that cell:

<div>
	$$
	\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & G & C & T & A & T & A & C\\
  					\hline
 					\epsilon & \color{red}0 & \color{green}1 & 2 & 3 & 4 & 5 & 6 & 7\\
 					\hline
 					G & \color{blue}1 & \color{red}0\\
 					\hline
 					C & 2\\
 					\hline
 					G & 3\\
 					\hline
 					T & 4\\
 					\hline
 					A & 5\\
 					\hline
 					T & 6\\
 					\hline
 					G & 7\\
 					\hline
 					C & 8

 \end{array}
  	$$
</div>

Using this uncomplicated logic we can fill the entire matrix like this:

<div>
	$$
	\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & G & C & T & A & T & A & C\\
  					\hline
 					\epsilon & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7\\
 					\hline
 					       G & 1 & 0 & 1 & 2 & 3 & 4 & 5 & 6\\
 					\hline
 					       C & 2 & 1 & 0 & 1 & 2 & 3 & 4 & 5\\
 					\hline
 					       G & 3 & 2 & 1 & 1 & 2 & 3 & 4 & 5\\
 					\hline
 					       T & 4 & 3 & 2 & 1 & 2 & 2 & 3 & 4\\
 					\hline
 					       A & 5 & 4 & 3 & 2 & 1 & 2 & 2 & 3\\
 					\hline
 					       T & 6 & 5 & 4 & 3 & 2 & 1 & 2 & 3\\
 					\hline
 					       G & 7 & 6 & 5 & 4 & 3 & 2 & 2 & 3\\
 					\hline
 					       C & 8 & 7 & 6 & 5 & 4 & 3 & 3 & \color{red}2

 \end{array}
  	$$
</div>

The lower rightmost cell highlighted in red is special. It contains the value for the edit distance between the two strings. The following Python script implements this idea. You can see that it is essentially instantaneous:

<iframe src="https://trinket.io/embed/python3/1bec8f9150?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# From edit distance to alignment

In the previous lectures we have spent time talking about sequencing technologies and then suddenly jumped to algorithms. Why? Well, with sequecning technologies we have seen how to generate impressive amounts of data. In many cases the way this data is analyzed is by aligning reads produced by NGS machines against existing genomic assemblies. Although, as we will see in the future lectures, modern high performance read aligners/mappers use approaches we have not yet discussed, dynamic programming offers powerful framework for finding if one sequence matches another. In fact, a lot of practical things that we will be doing in this course will involve aligning a short sequence (an NGS read) against a much larger genomic sequence. So, how can we use dynamic programming to find an approximate match between two sequences $\it\texttt{P}$ and $\texttt{T}$?

Suppose we have two strings:

$\it{T} = \texttt{T A T T G G C T A T A C G G T T}$

and

$\it{P} = \texttt{G C G T A T G C}$

Let's construct the following matrix:

<div>
$$
	\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					\epsilon & T & A & T & T & G & G & C & T & A & T & A & C & G & G & T & T\\
  					\hline
  					           \\
  					\hline
 					          G\\
 					\hline
 					          C\\
 					\hline
 					          G\\
 					\hline
 					          T\\
 					\hline
 					          A\\
 					\hline
 					          T\\
 					\hline
 					          G\\
 					\hline
 					          C\\

 \end{array}
 $$

</div>

Let me remind you that our goal is to find where $\it\texttt{P}$ matches $\texttt{T}$. *A priori* we do not know when it may be, so will start by filling the entire first row with zeroes. The first column we will initialize the same way we did previously: with increasing sequence of numbers:

<div>
$$
	\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					\epsilon & T & A & T & T & G & G & C & T & A & T & A & C & G & G & T & T\\
  					\hline
 					          G & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
 					\hline
 					          C & 1\\
 					\hline
 					          G & 2\\
 					\hline
 					          T & 3\\
 					\hline
 					          A & 4\\
 					\hline
 					          T & 5\\
 					\hline
 					          G & 6\\
 					\hline
 					          C & 7\\

 \end{array}
 $$

</div>

Now let's fill this matrix in using the same logic we used before:

<div>
$$
	\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					\epsilon & T & A & T & T & G & G & C & T & A & T & A & C & G & G & T & T\\
  					\hline
 					          G & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
 					\hline
 					          C & 1 1 1 1 1 0 1 0 1 0 1 1 0 1 1 1 0 0 1 1 1
 					\hline
 					          G & 1 1 2 2 2 1 0 1 1 1 1 1 1 1 2 2 1 1 1 2 1
 					\hline
 					          T & 2 2 1 2 2 2 1 1 2 2 1 2 2 2 1 2 2 2 2 2 2
 					\hline
 					          A & 3 3 2 2 3 3 2 2 1 2 2 2 3 2 2 2 3 3 2 2 3
 					\hline
 					          T & 4 4 3 3 3 3 3 2 2 1 2 3 2 3 3 3 2 3 3 3 3
 					\hline
 					          G & 5 5 4 3 3 4 4 3 3 2 1 2 3 3 3 3 3 3 4 4 4
 					\hline
 					          C & 6 5 5 4 4 4 4 4 4 3 2 1 2 3 4 4 4 4 4 5 4

 					          7 6 6 5 5 5 5 5 4 4 3 2 2 2 3 4 5 5 4 4 5

 					          8 7 6 6 5 6 6 6 5 5 4 3 3 3 2 3 4 5 5 5 5

 \end{array}
 $$

</div>


