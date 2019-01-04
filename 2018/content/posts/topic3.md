+++
#categories = []
date = "2018-01-31"
#draft = true
featureimage = "img/nyc.jpg"
menu = ""
tags = ['dynamic programming','global alignment','local alignment','Smith-Waterman']
title = "Sequence alignment: Introductory concepts"

+++

![](/img/topic4_cover.jpg)

<small>The cover image shows pairwise alignments for human, mouse, and dog *KIF3* locus from [Dubchak et al. 2000](http://genome.cshlp.org/content/10/9/1304.long).</small>

----

# Introduction to dynamic programming

<small>(Based on dynamic programming example from [InteractivePython](http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html)).</small>


In the previous lecture we have seen several ways in which DNA sequence data can be accumulated. Because sequencing machines (especially the ones made by Illumina) generate billions of sequences (called reads) from every run, the real challenge is what one does with all this data once sequencing is done. So before we get into applications of sequencing technologies we need to introduce some basic algorithmic concepts related to sequence alignment. Today we will start with **dynamic programming**. 

Suppose you are a cashier who's job is, generally speaking, to receive money and to give out change. Suppose that someone buys something that costs \$9.37 and gives you a 10 dollar bill. You need to give \$0.63 back in smallest possible number of coins. The US coin denominations are:

 * 100 (1 dollar)
 * 50 (half-dollar)
 * 25 (quarter)
 * 10 (dime)
 * 5 (nickel)
 * 1 (penny)

So, given these coins you will:

1.  start with the largest coin smaller than the amount you need to give back = **50 Cents**
2.  repeat for the remaining $0.13 and select **10 Cents**  (**NOTE**: this is recursion happening)
3.  finish with three 1 cent counts thus you ended up with 5 (**50** + **10** +  3 &times; **1**) coins.

### Solving problem exhaustively

Now (as suggested [here](http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html)) suppose you are a cashier in a strange country where there is also a **21** cent coin in circulation. By using the algorithm above, you will still give your customer <font color="red">five</font> coins, while the "correct" solution will certainly be giving him/her <font color="green">three</font> **21** cent coins. So the algorithm we used above simply does not work. 

Let's rephrase the problem. The smallest number of coins summing up to $0.63 cents (in our strange country with a **21** cent coin) will be:

 * a minimal collection of coins summing up to $0.62 plus a **1** cent coin
 * a minimal collection of coins summing up to $0.58 plus a **5** cent coin
 * a minimal collection of coins summing up to $0.53 plus a **10** cent coin
 * a minimal collection of coins summing up to $0.42 plus a **21** cent coin
 * a minimal collection of coins summing up to $0.38 plus a **25** cent coin
 * a minimal collection of coins summing up to $0.13 plus a **50** cent coin

|                 |
|-----------------|
|![](/img/change1.png)|
|<small>**1. First iteration**</small>|

Next, for each of these possibilities we will repeat this again. For example for $0.62 will consider:

 * a minimal collection of coins summing up to $0.61 plus a **1** cent coin
 * a minimal collection of coins summing up to $0.57 plus a **5** cent coin
 * a minimal collection of coins summing up to $0.52 plus a **10** cent coin
 * a minimal collection of coins summing up to $0.41 plus a **21** cent coin
 * a minimal collection of coins summing up to $0.37 plus a **25** cent coin
 * a minimal collection of coins summing up to $0.12 plus a **50** cent coin

|                 |
|-----------------|
|![](/img/change2.png)
| <small>**2. Second iteration**</small>|

 And again. For $0.58 we will have:

|                 |
|-----------------|
|![](/img/change3.png)
|<small>**3. Third iteration**. Note that amounts highlighted in red are repeated. Below we explain why this is **really bad**. </small>|

 and so on. Basically, as every iteration we are trying to find:


<div>

$$numCoins = min\begin{cases} 1 + numCoins(original\_amount - 1) 
                         & \\ 1 + numCoins(original\_amount - 5) 
                         & \\ 1 + numCoins(original\_amount - 10) 
                         & \\ 1 + numCoins(original\_amount - 21) 
                         & \\ 1 + numCoins(original\_amount - 25) 
                         & \\ 1 + numCoins(original\_amount - 50) 
                 \end{cases}$$

</div>


While this algorithm will find us the smallest number of coins necessary to give out a particular amount in change, it does this at a horrific price: it is extremely inefficient as it recomputes all possibilities at every iteration. For instance, if we ask the algorithm to compute the minimal number of coins necessary to give out 63 cents in change in a country with only four coins (1, 5, 10, and 25 cents) it will take **67,716,925** iterations (recursive calls). As a result you will probably loose all of your customers while they are waiting for the change.

The code snippet below implements this algorithm (do not worry if you don't quire understand python. It is OK for now). If you execute it (press the play button) your browser will likely crash as it will get tired waiting for result to come back (try it anyway):


<iframe src="https://trinket.io/embed/python/a74fb5b988?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Caching helps a bit

One potential way to solve our problem in a reasonable amount of time is to take advantage of red nodes shown in Figure 3. What if before calling the function we check if a minimum number of coins for a particular amount was already computed? Apparently this speeds things up quite dramatically:

<iframe src="https://trinket.io/embed/python/efcc5b3667?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Now you can see that it takes under a second to find that it takes 3 coins to give 63 cents in change in a country with 1, 5, 10, 21, and 25 cent coins. Yet this script still makes 221 calls (better than 67,716,925, but still a lot) for find the answer. 


### Introducing dynamic programming

Let's flip things around. Instead of starting from **63** cents and going down through the tree as shown in Figs 1 - 3 we will instead compute the minimal number of coins for every value from 1 to 63. To save space, let's instead assume that we need to give 11 cents in change. Let's compute a dynamic programming array for minimal number of coins between 1 and 11 (you may need to scroll sideways if your screen is small):

| Amount | Minimal Number of Coins |
|:-------:|:------------------------:|
|  0 |  0 |
|  1 |  1 |
|  2 |  2 |
|  3 |  3 |
|  4 |  4 |
|  5 |  1 |
|  6 |  2 |
|  7 |  3 |
|  8 |  4 |
|  9 |  5 |
| 10 |  1 | 
| 11 |  2 |


for amounts between **1** and **4**, we have no choice, since we have only pennies. At **5** we can either use 5 pennies or 1 nickel. According to this strategy (for a country with 1, 5, 10, and 25 cent coins):

<div>

$$numCoins = min\begin{cases} 1 + numCoins(original\_amount - 1) 
                         & \\ 1 + numCoins(original\_amount - 5) 
                         & \\ 1 + numCoins(original\_amount - 10) 
                         & \\ 1 + numCoins(original\_amount - 25) 
                                         \end{cases}$$

</div>

nickel wins (needs just 1 coin). From **6** to **9** we can either use all pennies (values will be 6, 7, 8, and 9) or a combination of nickel and pennies (values will be 2, 3, 4, 5). Again, smaller values win.

Let's now use this table to decide what is the minimum number of coins necessary to give 11 cents in change:

|                 |
|-----------------|
|![](/img/change4.png)
|<small>**4. Making change for 11 cents**. Let's look at leftmost branch. If you give 1 cent in change, you are left with 10 more to give. You consult Table 1 above and see that 10 cents can be given with 1 coin, so it will be 1 + 1 = 2 coins. In the center branch we give 5 cents in one coin and have 6 more cents to give. Looking at Table 1 tells us that 6 cents can be given in 2 coins, so 1 + 2 = 3 coins. Finally, in the rightmost branch giving 10 cents as one coin leaves 1 cent to give in change, which is also 1 coin, so 1 + 1 = 2. Thus we can either give 10 cents + 1 cent or 1 cent + 10 cents, which is equivalent since in both cases we give only 2 coins.</small>|

The following python code implements a function called `dynamicCoinChange` which computes a table (like Table 1) for any amount. In line 20 of the script we print a value corresponding to the amount we need to give back. That value is the minimum number of coins. Note that this program takes virtually no time to run.

<iframe src="https://trinket.io/embed/python/81c07a3750?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**So**, dynamic programming is a methodology where complex problems are broken down to simple subproblems, that are computed just once and then used to solve the complete problem. In this example, we first pre-compute the number of coins needed to make change for any amount up to the required one, and then produce the answer. 

# Sequence alignment

We have just seen the principle behind dynamic programming. This approach is also extremely useful for comparing biological sequences, which is coincidentally one of the main points of this course. This lecture explain how this is done. In writing this text I heavily relied on wonderful [course](http://www.langmead-lab.org/teaching-materials/) taught by Ben Langmead at Johns Hopkins. 

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

the vertical lines above indicate positions that are identical between the two sequences, while asterisks show differences. It will take six substitutions to turn one sequence into the other. This number -- six substitutions -- is called [*Hamming distance*](https://en.wikipedia.org/wiki/Hamming_distance) or the *minimal* number of substitutions required to turn one string into another. The code below computes the Hamming distance. Try it. You can change `seq1` and `seq2` into whatever you want except that they should have the same length.


<iframe src="https://trinket.io/embed/python/99a02b790a?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Now in addition to *substitutions* (i.e., changing one character into another) let's allow **instertions** and **deletions**. This will essentially allow us to insert dashes (gaps) between characters:

```
A C A T G C C T A -
| | * | | | | | | *
A C - T G C C T A C
```

In this case the [**edit distance**](https://en.wikipedia.org/wiki/Edit_distance) between two sequences is 2. It is defined as the minimum number of operations (substitutions, insertions, and deletions) requited to turn one string into another. The compared strings do not have to be of the same length to be able to compute the edit distance as we can compensate for length differences using deletions and insertions. While the situation above (where we inserted two dashes) is biologically much more meaningful (and realistic), it is much more difficult to find. 

## Generalizing the problem

Before we can develop an algorithm that will help us to compute the edit distance let's develop a general framework that would allow us to think about the problem in exact terms. Let's look at a pair of VERY long sequences. So long, that we do not even see the left end -- it disappears into $\infty$:

<div>
        $$
                \color{red}{\texttt{.....A C T G C C T A}}\texttt{ G}\\
                \color{red}{\texttt{.....A C T G C C T A}}\texttt{ C}\\
        $$
</div>

the red parts of the two sequences represent **prefixes** for the last nucleotides shown in black. Let's assume that the edit distance between the two prefixes is known (don't ask how we know, we just do). For simplicity let's "compact" the prefix of the first sequence into $\alpha$ and the prefix of the second sequence into $\beta$:

<div>
        $$
                \alpha \texttt{G}\\
            \beta  \texttt{C}
        $$
</div>

again, the edit distance between $\alpha$ and $\beta$ is known to us. The three possibilities for computing the edit distance between $\alpha G$ and $\beta C$ are:

<div>

$$Edit\ Distance(\alpha\texttt{G},\beta\texttt{C})  = min\begin{cases} 
                                        Edit\ Distance(\alpha,\beta) + 1 \leftarrow\ because\ they\ do\ not\ match& \\
                                        Edit\ Distance(\alpha\texttt{G},\beta) + 1 \leftarrow\ because\ we\ are\ adding\ a\ gap& \\
                                        Edit\ Distance(\alpha,\beta\texttt{C}) + 1 \leftarrow\ because\ we\ are\ adding\ a\ gap
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

where $\delta(x,y) = 0$ if $x = y$ (nucleotides match) and $\delta(x,y) = 1$ if $x \neq y$ (nucleotides do not match). The $\delta(x,y)$ has a particular meaning. If the two nucleotides at the end are equal to each other, there is nothing to be done -- no substitution operation is necessary. If a substitution is necessary however, we will record this by adding 1. When we will be talking about global and local alignment below the power of $\delta(x,y)$ will become even more clear.

Recall the change problem from the previous lecture. We can write an algorithm that would exhaustively evaluate the above expression for all possible suffixes. This algorithm is below. Try executing it. It will take roughly ~30 seconds to find the edit distance between the two sequences used in the beginning of this lecture:

<iframe src="https://trinket.io/embed/python/eff3a798bf?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Again, don't worry if Python looks scary to you. The take-home-message here is that it takes a very long time to compute the edit distance between two sequences that are only **nine** nucleotides long! Why is this happening? Figure 5 below shows a small subset of situations the algorithm is evaluating for two very short strings $\texttt{TAG}$ and $\texttt{TAC}$: 

|                 |
|-----------------|
|![](/img/editDist.png)|
|<small>**5**. A fraction of situations evaluated by the naïve algorithm for computing the edit distance. Just like in the case of the change problem discussed in the previous lecture a lot of time is wasted on computing distances between suffixes that has been seen more than once (shown in red).</small>|

To understand the magnitude of this problem let's look at slightly modified version of the previous Python code below. All we do here is keeping track how many times a particular pair of suffixes (in this case $\texttt{AC}$ and $\texttt{AC}$) are seen by the program. The number is staggering: 48,639. So this algorithm is **extremely** wasteful. 

<iframe src="https://trinket.io/embed/python/8994bfe46e?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

While this approach to the edit distance problem is correct, it will hardly help us on the genome-wide scale. Just like in case of the change problem dynamic programming is going to save the day.

## Dynamic programming to the rescue

Our goal is to find an optimal **alignment** between two sequences. Note that so far this is the first time we use the term **alignment** in this section. It turns out that in order to find the alignment we first need to learn how to compute edit distances between sequences efficiently. So, suppose we have two sequences that deliberately have different lengths:

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

  \\

\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.

        $$
</div>

Let's fill the first column and first raw of the matrix. Because the distance between a string and an empty string is equal to the length of the string (e.g., a distance between string $\texttt{TCG}$ and an empty string is 3) this resulting matrix will look like this:

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

  \\

\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.

        $$
</div>

Now, let's fill in the cell between $\texttt{G}$ and $\texttt{G}$. Recall that:

<div>

$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
                                        \color{red}{Edit\ Distance(\alpha,\beta) + \delta(x,y)} & \\
                                        \color{blue}{Edit\ Distance(\alpha\texttt{x},\beta) + 1} & \\
                                        \color{green}{Edit\ Distance(\alpha,\beta\texttt{y}) + 1}
             \end{cases}$$

</div>

where $\delta(x,y) = 0$ if $x = y$ and $\delta(x,y) = 1$ if $x \neq y$. And now let's color each of the cells corresponding to each part of the above expression:

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

  \\

\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.

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
                                         & \epsilon & G & C & T & A & T & A & C \\
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

 \\

\textbf{Note}: sequence\ \texttt{X}\ is\ vertical\ and\ sequence\ \texttt{Y}\ is\ horizontal.

        $$
</div>

The lower rightmost cell highlighted in red is special. It contains the value for the edit distance between the two strings. The following Python script implements this idea. You can see that it is essentially instantaneous:

<iframe src="https://trinket.io/embed/python3/1bec8f9150?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## From edit distance to alignment

In the previous section we have filled the dynamic programming matrix to find out that the edit distance between the sequences is 2. But in biological applications we are most often interested not in edit distance *per se* but in the actual **alignment** between two sequences. 

### The traceback

We can use the dynamic programming matrix to reconstruct the alignment. This is done using **traceback** procedure. Let's look at the rightmost bottom cell of the matrix highlighted in **bold**:

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
                                               C & 8 & 7 & 6 & 5 & 4 & 3 & 3 & \textbf{2}

 \end{array}

        $$
</div>

When we were filling this matrix did we come to this point from above ($\color{green}3$), from the left ($\color{blue}3$), or diagonally ($\color{red}2$):

<div>
        $$
        \begin{array}{ | c | c }
                    \hline
                                   \color{red}2 & \color{green}3\\
                                \hline
                                   \color{blue}3 & \textbf{2}
        \end{array}
        $$
</div>

Remembering the fact that when filling the matrix we are trying to minimize the expression for edit distance, we clearly arrived to this point diagonally from $\color{red}2$. This because arriving from top ($\color{green}3$) or left ($\color{blue}3$) would add 1. So we highlight diagonal cell in red:

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
                                               G & 7 & 6 & 5 & 4 & 3 & 2 & \color{red}2 & 3\\
                                        \hline
                                               C & 8 & 7 & 6 & 5 & 4 & 3 & 3 & \color{red}2

 \end{array}
        $$
</div>

Continuing this idea we will draw a trace like the one below until we hit an interesting point:

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
</div>

At this point we have arrived to this value from the top because 0 + 1 = 1. If we were arriving diagonally it would be 1 + 1 = 2 since $\texttt{G}\ \neq\ \texttt{C}$, so we are turning traceback upward and then again diagonally:


<div>
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
</div>

Now going through traceback line from the top we are getting the following alignment between two two sequences:

```
G C - T A T A C
| | * | | | * |
G C G T A T G C
```

### Approximate matching

Let's now get a bit more practical. In many real biological applications we are trying to see if one sequence is contained within another. So, how can we use dynamic programming to find if there is an approximate match between two sequences $\it\texttt{P}$ and $\texttt{T}$?

Suppose we have two strings:

$\it{T} = \texttt{A A C C C T A T G T C A T G C C T T G G A}$

and

$\it{P} = \texttt{T A C G T C A G C}$

Let's construct the following matrix:

<div>
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

</div>

Let me remind you that our goal is to find where $\it\texttt{P}$ matches $\texttt{T}$. *A priori* we do not know when it may be, so we will start by filling the entire first row with zeros. This is because the match between $\it\texttt{P}$ and $\texttt{T}$ may start at any point up there. The first column we will initialize the same way we did previously: with increasing sequence of numbers:

<div>
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

</div>

Now let's fill this matrix in using the same logic we used before:

<div>
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

</div>

Now that we have filled in the complete matrix let's look at the bottom row. Instead of using the rightmost cell we will find a cell with the lowest number. That would be 2 (highlighted in red):


<div>
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

 \end{array}
 $$

</div>

Starting already familiar traceback procedure at that cell we will get the following path through the matrix:

<div>
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

------

## Global alignment

So far in filling the dynamic programming matrix we were using the following expression to compute the number within each cell:

<div>

$$Edit\ Distance(\alpha\texttt{x},\beta\texttt{y}) = min\begin{cases} 
                                        \color{red}{Edit\ Distance(\alpha,\beta) + \delta(x,y)} & \\
                                        \color{blue}{Edit\ Distance(\alpha\texttt{x},\beta) + 1} & \\
                                        \color{green}{Edit\ Distance(\alpha,\beta\texttt{y}) + 1}
             \end{cases}$$

</div>

Basically we were adding 1 if there was a mismatch (the $\delta$ function) and also adding 1 for every gap. This however is not biologically realistic. If we look at the rates of different rates of mutations in the human genome we will see that they vary dramatically. Let's look at substitutions first:

|     |
|-----|
|![](/img/TsTv.png)|
| <small>**6**. There are two kinds of nucleotide substitutions: Transitions and Transversions. Transitions are substitutions between nucleotides belonging to the same chemical group. For example, a substitution of Adenine, a purine, to Guanine, also a purine, is a transition. Transversions, on the other hand, occur between chemically dissimilar nucleotides. For example, any substitution of a purine to a pyrimidine and vice verse will be a transition. (Image from [Wikipedia](https://en.wikipedia.org/wiki/Transversion))</small>|

you can see that there are move ways in which we can have a transversion. Despite this fact transversions are significantly less frequent that transitions. In fact in human the so called *Transition/Transversion ratio* ($Ts:Tv$) is close to [2](http://www.pnas.org/content/107/3/961.long) (or even higher in [coding regions](http://genomebiology.biomedcentral.com/articles/10.1186/gb-2011-12-9-r84)).

The situation with insertions and deletions (that are often called *indels*) is similar in that are relatively rare and their rarity increases with size. A single nucleotide indel may occur every 1,000 bases on average, while a two-nucleotide deletion occurs every 3,000 bases and so on (see [Montgomery et al. 2013](http://genome.cshlp.org/content/23/5/749.abstract) for a more detailed statistics). 

As a result it is simply unrealistic to use "1" is all cases. Instead, we need to *penalize* rare events more than we penalize frequent, more probable events. Let's create a *penalty matrix* to achieve this goal:


<div>
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
</div>

Here if two nucleotides match, the penalty is 0. For a transitional substitution we pay $\color{red}2$ and for a transversional we pay $\color{blue}4$. The gap is the most expensive at $\color{orange}8$. 

Now, let's align two sequences:

$\it{X} = \texttt{T A T G T C A T G C}$

and

$\it{Y} = \texttt{T A C G T C A G C}$

First, we need to fill the following dynamic programming matrix:

<div>
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
</div>

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

<div>
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
</div>

Similarly, for the first column we get:

<div>
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
</div>

and finally the full matrix:

<div>
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
</div>

Drawing a traceback through this matrix will give us:

<div>
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
</div>

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

<div>
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
</div>

Our scoring logic will also change:

<div>

$$D(\alpha\texttt{x},\beta\texttt{y}) = max\begin{cases} 
                                        D(\alpha,\beta) + s\texttt{(x,y)} & \\
                                        D(\alpha\texttt{x},\beta) + s\texttt{(x,-)} & \\
                                        D(\alpha,\beta\texttt{y}) + s\texttt{(-,y)} & \\
                                        0
             \end{cases}$$

</div>

We are now looking for **maximum** and use *0* to prevent having negative values in the matrix. This also implies that the first row and column will now be filled with zeros. Let apply this to two sequences:

Now, let's align two sequences:

$\texttt{T A T A T G C G G C G T T T}$

and

$\texttt{G G T A T G C T G G C G C T A}$

Dynamic programming matrix with initialized first row and column will look like this:


<div>
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
</div>

Filling it completely will yield the following matrix. Note that clues to where the local alignment may be are given off by positive numbers in the sea of 0s:

<div>
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
</div>

To identify to boundary of the local alignment we need to identify the cell with the **highest** value. This cell has value of $\color{red}{12}$ and is highlighted above. Using traceback procedure we will find:

<div>
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
</div>

This corresponds to the best local alignment between the two sequences:

```
 T A T A T G C - G G C G T T T
     | | | | | * | | | |
 G G T A T G C T G G C G C T A
 ```

Here is a Python representation of this approach:

<iframe src="https://trinket.io/embed/python3/aa05b81499?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This algorithm was developed by [Temple Smith and Michael Waterman](http://dornsife.usc.edu/assets/sites/516/docs/papers/msw_papers/msw-042.pdf) in 1981. This is why it is most often called Smith Waterman local alignment algorithm. 

