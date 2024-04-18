![](https://i.imgur.com/2dwPOHb.png)

# Sequence alignment

In the previous lecture we have seen the principle behind dynamic programming. This approach is extremely useful for comparing biological sequences, which is coincidentally one of the main points of this course. This lecture explain how this is done. In writing this text I heavily relied on wonderful [course](http://www.langmead-lab.org/teaching-materials/) taught by Ben Langmead at Johns Hopkins. The cover image shows pairwise alignments for human, mouse, and dog *KIF3* locus from [Dubchak et al. 2000](http://genome.cshlp.org/content/10/9/1304.long).

## How different are two sequences?

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

the vertical lines above indicate positions that are identical between the two sequences, while asterisks show differences. It will take six substitutions to turn one sequence into the other. This number -- six substitutions -- is called [*Hamming distance*](https://en.wikipedia.org/wiki/Hamming_distance) or the *minimal* number of substitutions required to turn one string into another. 

Now in addition to *substitutions* (i.e., changing one character into another) let's allow **insertions** and **deletions**. This will essentially allow us to insert dashes (gaps) between characters:

```
A C A T G C C T A -
| | * | | | | | | *
A C - T G C C T A C
```

In this case the [**edit distance**](https://en.wikipedia.org/wiki/Edit_distance) between two sequences is 2. It is defined as the minimum number of operations (substitutions, insertions, and deletions) requited to turn one string into another. The compared strings do not have to be of the same length to be able to compute the edit distance as we can compensate for length differences using deletions and insertions. While the situation above (where we inserted two dashes) is biologically much more meaningful (and realistic), it is much more difficult to find. 

# Generalizing the problem

Before we can develop an algorithm that will help us to compute the edit distance let's develop a general framework that would allow us to think about the problem in exact terms. Let's look at a pair of VERY long sequences. So long, that we do not even see the left end -- it disappears into $\infty$:

$$
		\color{red}{\texttt{.....A C T G C C T A}}\texttt{ G}\\
		\color{red}{\texttt{.....A C T G C C T A}}\texttt{ C}\\
$$

the red parts of the two sequences represent **prefixes** for the last nucleotides shown in black. Let's assume that the edit distance between the two prefixes is known (don't ask how we know, we just do). For simplicity let's "compact" the prefix of the first sequence into $\alpha$ and the prefix of the second sequence into $\beta$:


$$
		\alpha \texttt{G}\\
	    \beta  \texttt{C}
$$


again, the edit distance between $\alpha$ and $\beta$ is known to us. The three possibilities for computing the edit distance between $\alpha G$ and $\beta C$ are:



$$Edit\ Distance(\alpha\texttt{G},\beta\texttt{C})  = min\begin{cases} 
					Edit\ Distance(\alpha,\beta) + 1 \leftarrow\ because\ they\ do\ not\ match& \\
					Edit\ Distance(\alpha\texttt{G},\beta) + 1 \leftarrow\ because\ we\ are\ adding\ a\ gap& \\
					Edit\ Distance(\alpha,\beta\texttt{C}) + 1 \leftarrow\ because\ we\ are\ adding\ a\ gap
             \end{cases}$$



but we not always have $\texttt{G}$ and $\texttt{C}$ as two last nucleotiodes, so for the general case:



$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					Edit\ Distance(\alpha,\beta) + \delta(x,y) & \\
					Edit\ Distance(\alpha\texttt{x},\beta) + 1 & \\
					Edit\ Distance(\alpha,\beta\texttt{y}) + 1
             \end{cases}$$


where $\delta(x,y) = 0$ if $x = y$ (nucleotides match) and $\delta(x,y) = 1$ if $x \neq y$ (nucleotides do not match). The $\delta(x,y)$ has a particular meaning. If the two nucleotides at the end are equal to each other, there is nothing to be done -- no substitution operation is necessary. If a substitution is necessary however, we will record this by adding 1. When we will be talking about global and local alignment below the power of $\delta(x,y)$ will become even more clear. We can write an algorithm that would exhaustively evaluate the above expression for all possible suffixes. It will take roughly ~30 seconds to find the edit distance between the two sequences used in the beginning of this lecture.

The take-home-message here is that it takes a very long time to compute the edit distance between two sequences that are only **nine** nucleotides long! Why is this happening? Figure 1 below shows a small subset of situations the algorithm is evaluating for two very short strings $\texttt{TAG}$ and $\texttt{TAC}$: 

![image](https://github.com/nekrut/BMMB554/assets/4291636/399468e5-cc12-4a84-969e-ce4c1e5186a4)

<small>**Figure 1** | A fraction of situations evaluated by the naïve algorithm for computing the edit distance. Just like in the case of the change problem discussed in the previous lecture a lot of time is wasted on computing distances between suffixes that has been seen more than once (shown in red).</small>

While this approach to the edit distance problem is correct, it will hardly help us on the genome-wide scale. Just like in case of the change problem and Manhattan tourist problem dynamic programming is going to save the day.

# Dynamic programming to the rescue

It turns out that in order to find the alignment we first need to learn how to compute edit distances between sequences efficiently. So, suppose we have two sequences that deliberately have different lengths:

$\texttt{G C T A T A C}$

and 

$\texttt{G C G T A T G C}$

Let's represent them as the following matrix where the first character $\epsilon$ represents an empty string:

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
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$

Let's fill the first column and first row of the matrix. Because the distance between a string and an empty string is equal to the length of the string (e.g., a distance between string $\texttt{TCG}$ and an empty string is 3) this resulting matrix will look like this:

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
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$

Now, let's fill in the cell between $\texttt{G}$ and $\texttt{G}$. Recall that:

$$
Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					\color{red}{Edit\ Distance(\alpha,\beta) + \delta(x,y)} & \\
					\color{blue}{Edit\ Distance(\alpha\texttt{x},\beta) + 1} & \\
					\color{green}{Edit\ Distance(\alpha,\beta\texttt{y}) + 1}
             \end{cases}
$$

where $\delta(x,y) = 0$ if $x = y$ and $\delta(x,y) = 1$ if $x \neq y$. And now let's color each of the cells corresponding to each part of the above expression:

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
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$

In this specific case:

$$Edit\ Distance(\epsilon\texttt{G},\epsilon\texttt{G}) = min\begin{cases} 
					\color{red}{Edit\ Distance(\epsilon,\epsilon) + \delta(G,G)\ or\ 0\ +\ 0\ =\ 0} & \\
					\color{blue}{Edit\ Distance(\epsilon\texttt{G},\epsilon) + 1\ or\ 1\ +\ 1\ =\ 2} & \\
					\color{green}{Edit\ Distance(\epsilon,\epsilon\texttt{G}) + 1\ or\ 1\ +\ 1\ =\ 2}
             \end{cases}
$$

This minimum of 0, 2, and 2 will be 0, so we are putting zero into that cell:

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
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$

Using this uncomplicated logic we can fill the entire matrix like this:

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
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$

The lower rightmost cell highlighted in red is special. It contains the value for the edit distance between the two strings. 

# From edit distance to alignment

In the previous section we have filled the dynamic programming matrix to find out that the edit distance between the sequences is 2. But in biological applications we are most often interested not in edit distance *per se* but in the actual **alignment** between two sequences. 

## The traceback

We can use the dynamic programming matrix to reconstruct the alignment. This is done using **traceback** procedure. Let's look at the rightmost bottom cell of the matrix highlighted in **bold**:

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
G & 7 & 6 & 5 & 4 & 3 & 2 & \color{red}2 & \color{green}3\\
\hline
C & 8 & 7 & 6 & 5 & 4 & 3 & \color{blue}3 & \textbf{2}
\end{array}
$$

When we were filling this matrix did we come to this point from above ($\color{green}3$), from the left ($\color{blue}3$), or diagonally ($\color{red}2$):

$$
	\begin{array}{ | c | c }
	            \hline
				   \color{red}2 & \color{green}3\\
				\hline
				   \color{blue}3 & \textbf{2}
	\end{array}
$$


Remembering the fact that when filling the matrix we are trying to minimize the expression for edit distance, we clearly arrived to this point diagonally from $\color{red}2$. This because arriving from top ($\color{green}3$) or left ($\color{blue}3$) would add 1. So we highlight diagonal cell in red:


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
G & 7 & 6 & 5 & 4 & 3 & 2 & \color{red}2 & 3\\
\hline
C & 8 & 7 & 6 & 5 & 4 & 3 & 3 & \color{red}2
\end{array}
$$


Continuing this idea we will draw a trace like the one below until we hit an interesting point:

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
G & 3 & 2 & \color{red}1 & 1 & 2 & 3 & 4 & 5\\
\hline
T & 4 & 3 & 2 & \color{red}1 & 2 & 2 & 3 & 4\\
\hline
A & 5 & 4 & 3 & 2 & \color{red}1 & 2 & 2 & 3\\
\hline
T & 6 & 5 & 4 & 3 & 2 & \color{red}1 & 2 & 3\\
\hline
G & 7 & 6 & 5 & 4 & 3 & 2 & \color{red}2 & 3\\
\hline
C & 8 & 7 & 6 & 5 & 4 & 3 & 3 &\color{red}2
\end{array}
$$


At this point we have arrived to this value from the top because 0 + 1 = 1. If we were arriving diagonally it would be 1 + 1 = 2 since $\texttt{G}\ \neq\ \texttt{C}$, so we are turning traceback upward and then again diagonally:


$$
\begin{array}{ c | c | c | c | c | c | c}
& \epsilon & G & C & T & A & T & A & C\\
\hline
\epsilon & \color{red}0 & 1 & 2 & 3 & 4 & 5 & 6 & 7\\
\hline
G & 1 & \color{red}0 & 1 & 2 & 3 & 4 & 5 & 6\\
\hline
C & 2 & 1 & \color{red}0 & 1 & 2 & 3 & 4 & 5\\
\hline
G & 3 & 2 & \color{red}1 & 1 & 2 & 3 & 4 & 5\\
\hline
T & 4 & 3 & 2 & \color{red}1 & 2 & 2 & 3 & 4\\
\hline
A & 5 & 4 & 3 & 2 & \color{red}1 & 2 & 2 & 3\\
\hline
T & 6 & 5 & 4 & 3 & 2 & \color{red}1 & 2 & 3\\
\hline
G & 7 & 6 & 5 & 4 & 3 & 2 & \color{red}2 & 3\\
\hline
C & 8 & 7 & 6 & 5 & 4 & 3 & 3 & \color{red}2
\end{array}
$$


Now going through traceback line from the top we are getting the following alignment between two two sequences:

```
G C - T A T A C
| | * | | | * |
G C G T A T G C
```

## Approximate matching

Let's now get a bit more practical. In many real biological applications we are trying to see if one sequence is contained within another. So, how can we use dynamic programming to find if there is an approximate match between two sequences $\it\texttt{P}$ and $\texttt{T}$?

Suppose we have two strings:

$\it{T} = \texttt{A A C C C T A T G T C A T G C C T T G G A}$

and

$\it{P} = \texttt{T A C G T C A G C}$

Let's construct the following matrix:

$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
& \epsilon & A & A & C & C & C & T & A & T & G & T & C & A & T & G & C & C & T & T & G & G & A\\
\hline
\\
\hline
T\\
\hline
 A\\
\hline
C\\
\hline
G\\
\hline
T\\
\hline
C\\
\hline
A\\
\hline
G\\
\hline
C\\
\end{array}
\\
\textbf{Note}: sequence\ \texttt{T}\ is\ horizontal\ while\ \texttt{P}\ is\ vertical.
$$

Let me remind you that our goal is to find where $\it\texttt{P}$ matches $\texttt{T}$. *A priori* we do not know when it may be, so we will start by filling the entire first row with zeroes. This is because the match between $\it\texttt{P}$ and $\texttt{T}$ may start at any point up there. The first column we will initialize the same way we did previously: with increasing sequence of numbers:


$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
& \epsilon & A & A & C & C & C & T & A & T & G & T & C & A & T & G & C & C & T & T & G & G & A\\
\hline
& 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
\hline
T & 1\\
\hline
 A & 2\\
\hline
C & 3\\
\hline
G & 4\\
\hline
T & 5\\
\hline
C & 6\\
\hline
A & 7\\
\hline
G & 8\\
\hline
C & 9\\
\end{array}
$$
Now let's fill this matrix in using the same logic we used before:
$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
& \epsilon & A & A & C & C & C & T & A & T & G & T & C & A & T & G & C & C & T & T & G & G & A\\
\hline
& 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
\hline
T & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 1\\
\hline
A & 2 & 1 & 1 & 2 & 2 & 2 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 2 & 2 & 1 & 1 & 1 & 2 & 1\\
\hline
C & 3 & 2 & 2 & 1 & 2 & 2 & 2 & 1 & 1 & 2 & 2 & 1 & 2 & 2 & 2 & 1 & 2 & 2 & 2 & 2 & 2 & 2\\
\hline
G & 4 & 3 & 3 & 2 & 2 & 3 & 3 & 2 & 2 & 1 & 2 & 2 & 2 & 3 & 2 & 2 & 2 & 3 & 3 & 2 & 2 & 3\\
\hline
T & 5 & 4 & 4 & 3 & 3 & 3 & 3 & 3 & 2 & 2 & 1 & 2 & 3 & 2 & 3 & 3 & 3 & 2 & 3 & 3 & 3 & 3\\
\hline
C & 6 & 5 & 5 & 4 & 3 & 3 & 4 & 4 & 3 & 3 & 2 & 1 & 2 & 3 & 3 & 3 & 3 & 3 & 3 & 4 & 4 & 4\\
\hline
A & 7 & 6 & 5 & 5 & 4 & 4 & 4 & 4 & 4 & 4 & 3 & 2 & 1 & 2 & 3 & 4 & 4 & 4 & 4 & 4 & 5 & 4\\
\hline
G & 8 & 7 & 6 & 6 & 5 & 5 & 5 & 5 & 5 & 4 & 4 & 3 & 2 & 2 & 2 & 3 & 4 & 5 & 5 & 4 & 4 & 5\\
\hline
C & 9 & 8 & 7 & 6 & 6 & 5 & 6 & 6 & 6 & 5 & 5 & 4 & 3 & 3 & 3 & 2 & 3 & 4 & 5 & 5 & 5 & 5
\end{array}
$$

Now that we have filled in the complete matrix let's look at the bottom row. Instead of using the rightmost cell we will find a cell with the lowest number. That would be 2 (highlighted in red):

$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					& \epsilon & A & A & C & C & C & T & A & T & G & T & C & A & T & G & C & C & T & T & G & G & A\\
  					\hline
  					         & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
  					\hline
 					       T & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 1\\
 					\hline
 					       A & 2 & 1 & 1 & 2 & 2 & 2 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 2 & 2 & 1 & 1 & 1 & 2 & 1\\
 					\hline
 					       C & 3 & 2 & 2 & 1 & 2 & 2 & 2 & 1 & 1 & 2 & 2 & 1 & 2 & 2 & 2 & 1 & 2 & 2 & 2 & 2 & 2 & 2\\
 					\hline
 					       G & 4 & 3 & 3 & 2 & 2 & 3 & 3 & 2 & 2 & 1 & 2 & 2 & 2 & 3 & 2 & 2 & 2 & 3 & 3 & 2 & 2 & 3\\
 					\hline
 					       T & 5 & 4 & 4 & 3 & 3 & 3 & 3 & 3 & 2 & 2 & 1 & 2 & 3 & 2 & 3 & 3 & 3 & 2 & 3 & 3 & 3 & 3\\
 					\hline
 					       C & 6 & 5 & 5 & 4 & 3 & 3 & 4 & 4 & 3 & 3 & 2 & 1 & 2 & 3 & 3 & 3 & 3 & 3 & 3 & 4 & 4 & 4\\
 					\hline
 					       A & 7 & 6 & 5 & 5 & 4 & 4 & 4 & 4 & 4 & 4 & 3 & 2 & 1 & 2 & 3 & 4 & 4 & 4 & 4 & 4 & 5 & 4\\
 					\hline
 					       G & 8 & 7 & 6 & 6 & 5 & 5 & 5 & 5 & 5 & 4 & 4 & 3 & 2 & 2 & 2 & 3 & 4 & 5 & 5 & 4 & 4 & 5\\
 					\hline
 						   C & 9 & 8 & 7 & 6 & 6 & 5 & 6 & 6 & 6 & 5 & 5 & 4 & 3 & 3 & 3 & \color{red}2 & 3 & 4 & 5 & 5 & 5 & 5
\end{array}$$

Starting already familiar traceback procedure at that cell we will get the following path through the matrix:

$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					& \epsilon & A & A & C & C & C & T & A & T & G & T & C & A & T & G & C & C & T & T & G & G & A\\
  					\hline
  					         & 0 & 0 & 0 & 0 & 0 & \color{red}0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
  					\hline
 					       T & 1 & 1 & 1 & 1 & 1 & 1 & \color{red}0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 & 1\\
 					\hline
 					       A & 2 & 1 & 1 & 2 & 2 & 2 & 1 & \color{red}0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 2 & 2 & 1 & 1 & 1 & 2 & 1\\
 					\hline
 					       C & 3 & 2 & 2 & 1 & 2 & 2 & 2 & 1 & \color{red}1 & 2 & 2 & 1 & 2 & 2 & 2 & 1 & 2 & 2 & 2 & 2 & 2 & 2\\
 					\hline
 					       G & 4 & 3 & 3 & 2 & 2 & 3 & 3 & 2 & 2 & \color{red}1 & 2 & 2 & 2 & 3 & 2 & 2 & 2 & 3 & 3 & 2 & 2 & 3\\
 					\hline
 					       T & 5 & 4 & 4 & 3 & 3 & 3 & 3 & 3 & 2 & 2 & \color{red}1 & 2 & 3 & 2 & 3 & 3 & 3 & 2 & 3 & 3 & 3 & 3\\
 					\hline
 					       C & 6 & 5 & 5 & 4 & 3 & 3 & 4 & 4 & 3 & 3 & 2 & \color{red}1 & 2 & 3 & 3 & 3 & 3 & 3 & 3 & 4 & 4 & 4\\
 					\hline
 					       A & 7 & 6 & 5 & 5 & 4 & 4 & 4 & 4 & 4 & 4 & 3 & 2 & \color{red}1 & \color{red}2 & 3 & 4 & 4 & 4 & 4 & 4 & 5 & 4\\
 					\hline
 					       G & 8 & 7 & 6 & 6 & 5 & 5 & 5 & 5 & 5 & 4 & 4 & 3 & 2 & 2 & \color{red}2 & 3 & 4 & 5 & 5 & 4 & 4 & 5\\
 					\hline
 						   C & 9 & 8 & 7 & 6 & 6 & 5 & 6 & 6 & 6 & 5 & 5 & 4 & 3 & 3 & 3 & \color{red}2 & 3 & 4 & 5 & 5 & 5 & 5
\end{array}
 $$

</div>

for a corresponding alignment:

```
A A C C C T A T G T C A T G C C T T G G A
          | | * | | | | * | | 
          T A C G T C A - G C
```

# Global alignment

So far in filling the dynamic programming matrix we were using the following expression to compute the number within each cell:

<div>

$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					\color{red}{Edit\ Distance(\alpha,\beta) + \delta(x,y)} & \\
					\color{blue}{Edit\ Distance(\alpha\texttt{x},\beta) + 1} & \\
					\color{green}{Edit\ Distance(\alpha,\beta\texttt{y}) + 1}
             \end{cases}$$

</div>

Basically we were adding 1 if there was a mismatch (the $\delta$ function) and also adding 1 for every gap. This however is not biologically realistic. If we look at the rates of different rates of mutations in the human genome we will see that they vary dramatically. Let's look at substitutions first:

![image](https://github.com/nekrut/BMMB554/assets/4291636/74f99a80-a4ca-4c66-a91a-a936b16830d7)

**Figure 2** | There are two kinds of nucleotide substitutions: Transitions and Transversions. Transitions are substitutions between nucleotides belonging to the same chemical group. For example, a substitution of Adenine, a purine, to Guanine, also a purine, is a transition. Transversions, on the other hand, occur between chemically dissimilar nucleotides. For example, any substitution of a purine to a pyrimidine and vice verse will be a transition. (Image from [Wikipedia](https://en.wikipedia.org/wiki/Transversion))

you can see that there are move ways in which we can have a transversion. Despite this fact transversions are significantly less frequent that transitions. In fact in human the so called *Transition/Transversion ratio* ($Ts:Tv$) is close to [2](http://www.pnas.org/content/107/3/961.long) (or even higher in [coding regions](http://genomebiology.biomedcentral.com/articles/10.1186/gb-2011-12-9-r84)).

The situation with insertions and deletions (that are often called *indels*) is similar in that are relatively rare and their rarity increases with size. A single nucleotide indel may occur every 1,000 bases on average, while a two-nucleotide deletion occurs every 3,000 bases and so on (see [Montgomery et al. 2013](http://genome.cshlp.org/content/23/5/749.abstract) for a more detailed statistics). 

As a result it is simply unrealistic to use "1" is all cases. Instead, we need to *penalize* rare events more than we penalize frequent, more probable events. Let's create a *penalty matrix* to achieve this goal:


$$
\begin{array}{ c | c  c  c  c  c }
				     & A & C & G & T & -\\
				  \hline
				   A & 0 & \color{blue}4 & \color{red}2 & \color{blue}4 & \color{orange}8\\  
				   C & \color{blue}4 & 0 & \color{blue}4 & \color{red}2 & \color{orange}8\\
				   G & \color{red}2 & \color{blue}4 & 0 & \color{blue}4 & \color{orange}8\\
				   T & \color{blue}4 & \color{red}2 & \color{blue}4 & 0 & \color{orange}8\\
				   - & \color{orange}8 & \color{orange}8 & \color{orange}8 & \color{orange}8 & \\
				\hline
\end{array}
$$


Here if two nucleotides match, the penalty is 0. For a transitional substitution we pay $\color{red}2$ and for a transversional we pay $\color{blue}4$. The gap is the most expensive at $\color{orange}8$. 

Now, let's align two sequences:

$\it{X} = \texttt{T A T G T C A T G C}$

and

$\it{Y} = \texttt{T A C G T C A G C}$

First, we need to fill the following dynamic programming matrix:


$$
\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & T & A & T & G & T & C & A & T & G & C\\
  					\hline
 					\epsilon \\
 					\hline
 					       T \\
 					\hline
 					       A \\
 					\hline
 					       C \\
 					\hline
 					       G \\
 					\hline
 					       T \\
 					\hline
 					       C \\
 					\hline
 					       A \\
 					\hline
 					       G \\
 				    \hline
 				    	   C 
\end{array}
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$


But now we using penalty matrix generated above to calculate values in each cell. Specifically, before we were using this expression:

<div>

$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					Edit\ Distance(\alpha,\beta) + \delta(x,y) & \\
					Edit\ Distance(\alpha\texttt{x},\beta) + 1 & \\
					Edit\ Distance(\alpha,\beta\texttt{y}) + 1
             \end{cases}$$
</div>

but now, we will change it into this:

<div>

$$D(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
					D(\alpha,\beta) + p\texttt{(x,y)} & \\
					D(\alpha\texttt{x},\beta) + p\texttt{(x,-)} & \\
					D(\alpha,\beta\texttt{y}) + p\texttt{(-,y)}
             \end{cases}$$

</div>

where $p\texttt{(x,y)}$, $p\texttt{(x,-)}$, and $p\texttt{(-,y)}$ are taken directly from penalty matrix. Let's start with the first row. In this row we can only fill from the left were we essentially inserting a gap every time. Since the gap penalty is 8 we will get:


$$
	\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & T & A & T & G & T & C & A & T & G & C\\
  					\hline
 				\epsilon & 0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 & 72 & 80\\
 					\hline
 					       T \\
 					\hline
 					       A \\
 					\hline
 					       C \\
 					\hline
 					       G \\
 					\hline
 					       T \\
 					\hline
 					       C \\
 					\hline
 					       A \\
 					\hline
 					       G \\
 				    \hline
 				    	   C 
\end{array}
\\
\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.
$$

Similarly, for the first column we get:

$$
\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & T & A & T & G & T & C & A & T & G & C\\
  					\hline
 				\epsilon & 0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 & 72 & 80\\
 					\hline
 					       T & 8\\
 					\hline
 					       A & 16\\
 					\hline
 					       C & 24\\
 					\hline
 					       G & 32\\
 					\hline
 					       T & 40\\
 					\hline
 					       C & 48\\
 					\hline
 					       A & 56\\
 					\hline
 					       G & 64\\
 				    \hline
 				    	   C & 72
\end{array}
$$

and finally the full matrix:


$$
\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & T & A & T & G & T & C & A & T & G & C\\
  					\hline
 				\epsilon & 0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 & 72 & 80\\
 					\hline
 					       T & 8 & 0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 & 72\\
 					\hline
 					       A & 16 & 8 & 0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64\\
 					\hline
 					       C & 24 & 16 & 8 & 2 & 10 & 18 & 24 & 32 & 40 & 48 & 56\\
 					\hline
 					       G & 32 & 24 & 16 & 10 & 2 & 10 & 18 & 26 & 34 & 40 & 48\\
 					\hline
 					       T & 40 & 32 & 24 & 16 & 10 & 2 & 10 & 18 & 26 & 34 & 42\\
 					\hline
 					       C & 48 & 40 & 32 & 24 & 18 & 10 & 2 & 10 & 18 & 26 & 34\\
 					\hline
 					       A & 56 & 48 & 40 & 32 & 26 & 18 & 10 & 2 & 10 & 18 & 26\\
 					\hline
 					       G & 64 & 56 & 48 & 40 & 32 & 26 & 18 & 10 & 6 & 10 & 18\\
 				    \hline
 				    	   C & 72 & 64 & 56 & 48 & 40 & 34 & 26 & 18 & 12 & 10 & 10
\end{array}
$$

Drawing a traceback through this matrix will give us:


$$
\begin{array}{ c | c | c | c | c | c | c}
  					 & \epsilon & T & A & T & G & T & C & A & T & G & C\\
  					\hline
 				\epsilon & \color{red}0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 & 72 & 80\\
 					\hline
 					       T & 8 & \color{red}0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64 & 72\\
 					\hline
 					       A & 16 & 8 & \color{red}0 & 8 & 16 & 24 & 32 & 40 & 48 & 56 & 64\\
 					\hline
 					       C & 24 & 16 & 8 & \color{red}2 & 10 & 18 & 24 & 32 & 40 & 48 & 56\\
 					\hline
 					       G & 32 & 24 & 16 & 10 & \color{red}2 & 10 & 18 & 26 & 34 & 40 & 48\\
 					\hline
 					       T & 40 & 32 & 24 & 16 & 10 & \color{red}2 & 10 & 18 & 26 & 34 & 42\\
 					\hline
 					       C & 48 & 40 & 32 & 24 & 18 & 10 & \color{red}2 & 10 & 18 & 26 & 34\\
 					\hline
 					       A & 56 & 48 & 40 & 32 & 26 & 18 & 10 & \color{red}2 & \color{red}{10} & 18 & 26\\
 					\hline
 					       G & 64 & 56 & 48 & 40 & 32 & 26 & 18 & 10 & 6 & \color{red}{10} & 18\\
 				    \hline
 				    	   C & 72 & 64 & 56 & 48 & 40 & 34 & 26 & 18 & 12 & 10 & \color{red}{10}
\end{array}
$$


This corresponds to the following alignment:

```
T A C G T C A - G C
| | * | | | | * | | 
T A T G T C A T G C
```

The following Python code implements Global alignment approach we have seen above. Note that the first function, `exampleCost`, can be changed to set different value for the penalty matrix. You can play with it here:

<iframe src="https://trinket.io/embed/python3/911a7ddd2e?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Local alignment

Global alignment discussed above works only in cases when we truly expect sequences to match across their entire lengths. In majority of biological application this is rarely the case. For instance, suppose you want to compare two bacterial genomes to figure out if they have matching sequences. Local alignment algorithm helps with this challenge. Surprisingly, it is almost identical to the approaches we used before. So here is our problem:

```
Sequence 1: ##################################################
                              |||||||||||||||||
Sequence 2:         #################################################
```

there are two sequences (shown with # characters) and they share a region of high similarity (indicated by vertical lines). How do we find this region? We cannot use global alignment logic here because across the majority of their lengths these sequences are dissimilar. 

To approach this problem we will change our penalty strategy. Instead of giving a high value for each mismatch we will instead give negative penalties. Only matches get positive rewards. Here is an example of such *scoring matrix* (as opposed to the *penalty matrix* we've used before):

$$
\begin{array}{ c | c  c  c  c  c }
				     & A & C & G & T & -\\
				  \hline
				   A & 2 & \color{blue}{-4} & \color{red}{-4} & \color{blue}{-4} & \color{orange}{-6}\\  
				   C & \color{blue}{-4} & 2 & \color{blue}{-4} & \color{red}{-4}  & \color{orange}{-6}\\
				   G & \color{red}{-4} & \color{blue}{-4} & 2 & \color{blue}{-4}  & \color{orange}{-6}\\
				   T & \color{blue}{-4} & \color{red}{-4} & \color{blue}{-4}  & 2 & \color{orange}{-6}\\
				   - & \color{orange}{-6} & \color{orange}{-6} & \color{orange}{-6} & \color{orange}{-6} & \\
				\hline
\end{array}
$$

Our scoring logic will also change:

$$D(\alpha\texttt{x},\beta\texttt{y}) = max\begin{cases} 
					D(\alpha,\beta) + s\texttt{(x,y)} & \\
					D(\alpha\texttt{x},\beta) + s\texttt{(x,-)} & \\
					D(\alpha,\beta\texttt{y}) + s\texttt{(-,y)} & \\
					0
             \end{cases}$$


We are now looking for **maximum** and use *0* to prevent having negative values in the matrix. This also implies that the first row and column will now be filled with zeros. Let apply this to two sequences:

Now, let's align two sequences:

$\texttt{T A T A T G C G G C G T T T}$

and

$\texttt{G G T A T G C T G G C G C T A}$

Dynamic programming matrix with initialized first row and column will look like this:

$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					 & \epsilon & T & A & T & A & T & G & C & G & G & C & G & T & T & T\\
  					 \hline
  			       \epsilon & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
  			        \hline
  			       		  G & 0\\
  			        \hline
  			        	  G & 0\\
  			        \hline
  			              T & 0\\
  			        \hline
  			              A & 0\\ 
  			        \hline
  			              T & 0\\
  			        \hline
  			              G & 0\\
  			        \hline
  			              C & 0\\
  			        \hline
  			              T & 0\\
  			        \hline
  			              G & 0\\
  			        \hline
  			              G & 0\\
  			        \hline
  			              C & 0\\
  			        \hline
  			              G & 0\\
  			        \hline
  			              C & 0\\
  			        \hline
  			              T & 0\\
  			        \hline
  			              A & 0\\
\end{array}
\\
\textbf{Remember}: sequence\ \texttt{X}\ is\ vertical\ while\ \texttt{Y}\ is\ horizontal.
$$

Filling it completely will yield the following matrix. Note that clues to where the local alignment may be are given off by positive numbers in the sea of 0s:

$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					 & \epsilon & T & A & T & A & T & G & C & G & G & C & G & T & T & T\\
  					 \hline
  			       \epsilon & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
  			        \hline
  			       		  G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 2 & 0 & 2 & 0 & 0 & 0\\
  			        \hline
  			        	  G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 4 & 0 & 2 & 0 & 0 & 0\\
  			        \hline
  			              T & 0 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 2 & 2\\
  			        \hline
  			              A & 0 & 0 & 4 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 
  			        \hline
  			              T & 0 & 2 & 0 & 6 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 2 & 2\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 2 & 0 & 8 & 2 & 2 & 2 & 0 & 2 & 0 & 0 & 0\\
  			        \hline
  			              C & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 10 & 4 & 0 & 4 & 0 & 0 & 0 & 0\\
  			        \hline
  			              T & 0 & 2 & 0 & 2 & 0 & 2 & 0 & 4 & 6 & 0 & 0 & 0 & 2 & 2 & 2\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 6 & 8 & 2 & 2 & 0 & 0 & 0\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 8 & 4 & 4 & 0 & 0 & 0\\
  			        \hline
  			              C & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 2 & 10 & 4 & 0 & 0 & 0\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 6 & 2 & 4 & \color{red}{12} & 6 & 0 & 0\\
  			        \hline
  			              C & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 2 & 4 & 6 & 8 & 2 & 0\\
  			        \hline
  			              T & 0 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 8 & 10 & 4\\
  			        \hline
  			              A & 0 & 0 & 4 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 4 & 6\\
  			       \end{array}
$$

To identify to boundary of the local alignment we need to identify the cell with the **highest** value. This cell has value of $\color{red}{12}$ and is highlighted above. Using traceback procedure we will find:

$$
\begin{array}{ c | c | c | c | c | c | c | c | c | c | c | c | c | c }
  					 & \epsilon & T & A & T & A & T & G & C & G & G & C & G & T & T & T\\
  					 \hline
  			       \epsilon & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
  			        \hline
  			       		  G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 2 & 0 & 2 & 0 & 0 & 0\\
  			        \hline
  			        	  G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 4 & 0 & 2 & 0 & 0 & 0\\
  			        \hline
  			              T & 0 & 2 & 0 & \color{red}2 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 2 & 2\\
  			        \hline
  			              A & 0 & 0 & 4 & 0 & \color{red}4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\ 
  			        \hline
  			              T & 0 & 2 & 0 & 6 & 0 & \color{red}6 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 2 & 2\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 2 & 0 & \color{red}8 & 2 & 2 & 2 & 0 & 2 & 0 & 0 & 0\\
  			        \hline
  			              C & 0 & 0 & 0 & 0 & 0 & 0 & 2 & \color{red}{10} & 4 & 0 & 4 & 0 & 0 & 0 & 0\\
  			        \hline
  			              T & 0 & 2 & 0 & 2 & 0 & 2 & 0 & \color{red}4 & 6 & 0 & 0 & 0 & 2 & 2 & 2\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & \color{red}6 & 8 & 2 & 2 & 0 & 0 & 0\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & \color{red}8 & 4 & 4 & 0 & 0 & 0\\
  			        \hline
  			              C & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 2 & \color{red}{10} & 4 & 0 & 0 & 0\\
  			        \hline
  			              G & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 6 & 2 & 4 & \color{red}{12} & 6 & 0 & 0\\
  			        \hline
  			              C & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 2 & 4 & 6 & 8 & 2 & 0\\
  			        \hline
  			              T & 0 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 8 & 10 & 4\\
  			        \hline
  			              A & 0 & 0 & 4 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 4 & 6\\
  			       \end{array}
$$

This corresponds to the best local alignment between the two sequences:

```
 T A T A T G C - G G C G T T T
     | | | | | * | | | |
 G G T A T G C T G G C G C T A
 ```

Here is a Python representation of this approach:

```python
import numpy

def exampleCost(xc, yc):
    ''' Cost function: 2 to match, -6 to gap, -4 to mismatch '''
    if xc == yc: return 2 # match
    if xc == '-' or yc == '-': return -6 # gap
    return -4

def smithWaterman(x, y, s):
    ''' Calculate local alignment values of sequences x and y using
        dynamic programming.  Return maximal local alignment value. '''
    V = numpy.zeros((len(x)+1, len(y)+1), dtype=int)
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            V[i, j] = max(V[i-1, j-1] + s(x[i-1], y[j-1]), # diagonal
                          V[i-1, j  ] + s(x[i-1], '-'),    # vertical
                          V[i  , j-1] + s('-',    y[j-1]), # horizontal
                          0)                               # empty
    argmax = numpy.where(V == V.max())
    return V, int(V[argmax])
    
def traceback(V, x, y, s):
    """ Trace back from given cell in local-alignment matrix V """
    # get i, j for maximal cell
    i, j = numpy.unravel_index(numpy.argmax(V), V.shape)
    xscript, alx, aly, alm = [], [], [], []
    while (i > 0 or j > 0) and V[i, j] != 0:
        diag, vert, horz = 0, 0, 0
        if i > 0 and j > 0:
            diag = V[i-1, j-1] + s(x[i-1], y[j-1])
        if i > 0:
            vert = V[i-1, j] + s(x[i-1], '-')
        if j > 0:
            horz = V[i, j-1] + s('-', y[j-1])
        if diag >= vert and diag >= horz:
            match = x[i-1] == y[j-1]
            xscript.append('M' if match else 'R')
            alm.append('|' if match else ' ')
            alx.append(x[i-1]); aly.append(y[j-1])
            i -= 1; j -= 1
        elif vert >= horz:
            xscript.append('D')
            alx.append(x[i-1]); aly.append('-'); alm.append(' ')
            i -= 1
        else:
            xscript.append('I')
            aly.append(y[j-1]); alx.append('-'); alm.append(' ')
            j -= 1
    xscript = (''.join(xscript))[::-1]
    alignment = '\n'.join(map(lambda x: ''.join(x), [alx[::-1], alm[::-1], aly[::-1]]))
    return xscript, alignment

x, y = 'GGTATGCTGGCGCTA', 'TATATGCGGCGTTT'
V, best = smithWaterman(x, y, exampleCost)
print(V)
print("Best score=%d, in cell %s" % (best, numpy.unravel_index(numpy.argmax(V), V.shape)))
print(traceback(V, x, y, exampleCost)[1])
```

This algorithm was developed by [Temple Smith and Michael Waterman](http://dornsife.usc.edu/assets/sites/516/docs/papers/msw_papers/msw-042.pdf) in 1981. This is why it is most often called Smith Waterman local alignment algorithm. 

## Alignment tools

### Lastz

https://github.com/lastz/lastz

### Minimap2

https://github.com/lh3/minimap2

## Multiple whole genome alignment approaches

### [MultiZ](https://genome.cshlp.org/content/14/4/708.short)

![](https://i.imgur.com/2KfKwk7.png)

A schematic representation of the multiZ pipeline. Blue bars represent analysis steps performed by distinct tools. The workflow begins by softmasking interspersed and tandem repeats in the genomes to be aligned. The genomes are then split into smaller segments for parallelization purposes and all segments of the reference are aligned against all segments of each genome using lastZ. The resulting alignments are combined (in non-reference genome bins), sorted, and split by reference chromosomes. They are then chained and the chains are used to create nets. These steps are performed in parallel for each reference/genome{1, 2, …, N} combination. Subsequently all reference/genome combinations are combined into multiple alignments with MultiZ. Resulting MAF datasets are used to define conserved regions identified by phastCons and to compute per-base phyloP values. Chain and nets are explained in 1.2. 2bit, lav, axt, psl, and MAF are various intermediate file formats (described in [87]). 

### [Progressive Cactus](https://www.nature.com/articles/s41586-020-2871-y)

![](https://i.imgur.com/xkq71l0.png)

 A schematic representation of steps involved in aligning four genomes using ProgressiveCactus. First, genomes to be aligned are softmasked: regions of the sequence corresponding to repetitive elements are converted to lowercase characters. During the pairwise alignment step lastZ does not use softmasked regions in the seeding but is allowed to extend matches to these regions. ProgressiveCactus splits the MSA task into smaller parallelizable subtasks using a guide tree. Here the ancestral genome E is first reconstructed by a process which aligns the ingroups A and B, using the outgroups C and D to determine orthology relationships within the alignment of A and B. The output of this process is a sub-alignment of A and B to their direct ancestor E and a reconstruction of the genome assembly of E. At each stage there are two computation steps: a local alignment step (lastZ) and a MSA step (CAF/BAR). Each of these can be run on a single compute node with sufficient resources. The local alignment step generates local alignments between the ingroup genomes (all against all), and between the in-group genomes and the outgroups (using an intelligent strategy to avoid aligning all ingroups to all outgroups). In the MSA step these local alignments are combined within a graph theoretic structure which initially represents the transitive closure of these alignments and which progressively cleans and then refines the resulting MSA to produce the final MSA for the node. This whole process is then repeated for internal nodes F and G and the resulting MSAs, represented using the flexible HAL format, are stitched together. The total number of individual steps is equal to two times the number of internal nodes in the tree plus a single post processing step that combines the resulting sub-MSAs to create the final alignment. Gray nodes on the tree represent ancestral genomes inferred by Progressive Cactus. CAF = Cactus alignment filter; BAR = base-level alignment refinement; MSA = multiple sequence alignment.
 
 ## Alignment and UCSC Genome Browser
 
 https://genome.ucsc.edu/
 
 






