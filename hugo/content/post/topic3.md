+++
#categories = []
date = "2017-01-25T10:43:18-04:00"
#draft = true
featureimage = "img/nyc.jpg"
menu = ""
tags = []
title = "3. Sequence alignment: Introductory concepts"
description = "**Topic 3** | Aligning DNA sequences: An introduction to algorithmic principles"

+++

![](/BMMB554/img/nyc.jpg)

# Introduction

In the previous lecture we have seen several ways in which DNA sequence data can be accumulated (the reason for having Manhattan in the figure above will be apparent a bit later). Because sequencing machines (especially the ones made by Illumina) generate billions of sequences (called reads) from every run, the real challenge is what one does with all this data once sequencing is done. So before we get into details of technology and its application we need to introduce some basic algorithmic concepts related to sequence analysis. Today we will start with **dynamic programming**. 

## Dynamic programming for the change problem

When introducing algorithmic concepts to biological audience it often becomes critical to use good examples. One of the people who probably succeeded most in this endeavor is [Pavel Pevzner](http://cseweb.ucsd.edu/~ppevzner/), a Ronald R. Taylor Professor of Computer Science at UCSD, who (together with [Phillip Compeau](http://compeau.cbd.cmu.edu/)) published a very informatics (and entertaining) [book](https://www.amazon.com/Bioinformatics-Algorithms-Active-Learning-Approach/dp/0990374602) on the subject of computational biology. The example I use below comes from this book.

-----

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
3.  finish with three 1 cent counts thus you ended up with 5 (**50** + **10** + 3x**1**) coins.

### Solving problem exhaustively

Now (as suggested [here](http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html)) suppose you are a cashier in a strange country where there is also a **21** cent coin in circulation. By using the algorithm above you will still give your customer 5 coins, while the "correct" solution will certainly be giving him/her 3 **21** cent coins. So the algorithm we used above simply does not work. 

Let's rephrase the problem. The smallest number of coins summing up to $0.63 cents (in our strange country with a **21** cent coin) will be:

 * a minimal collection of coins summing up to $0.62 plus a **1** cent coin
 * a minimal collection of coins summing up to $0.58 plus a **5** cent coin
 * a minimal collection of coins summing up to $0.53 plus a **10** cent coin
 * a minimal collection of coins summing up to $0.42 plus a **21** cent coin
 * a minimal collection of coins summing up to $0.38 plus a **25** cent coin
 * a minimal collection of coins summing up to $0.13 plus a **50** cent coin

> ![](http://www.bx.psu.edu/~anton/bioinf-images/change1.png)
>
> **Figure 1** | First iteration

Next, for each of these possibilities we will repeat this again. For example for $0.62 will consider:

 * a minimal collection of coins summing up to $0.61 plus a **1** cent coin
 * a minimal collection of coins summing up to $0.57 plus a **5** cent coin
 * a minimal collection of coins summing up to $0.52 plus a **10** cent coin
 * a minimal collection of coins summing up to $0.41 plus a **21** cent coin
 * a minimal collection of coins summing up to $0.37 plus a **25** cent coin
 * a minimal collection of coins summing up to $0.12 plus a **50** cent coin

> ![](http://www.bx.psu.edu/~anton/bioinf-images/change2.png)
>
> **Figure 2** | Second iteration 

 And again. For $0.58 we will have:

> ![](http://www.bx.psu.edu/~anton/bioinf-images/change3.png)
>
> **Figure 3** | Note that amounts highlighted in red are repeated. Below we explain why this is **really bad**

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

> ```
> Amount                   0  1  2  3  4  5  6  7  8  9 10 11
> Minimum number of coins  0  1  2  3  4  1  2  3  4  5  1  2
> ```
> **Table 1**

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

> ![](http://www.bx.psu.edu/~anton/bioinf-images/change4.png)
>
> **Figure 4** | Making change for 11 cents. Let's look at leftmost branch. If you give 1 cent in change, you are left with 10 more to give. You consult Table 1 above and see that 10 cents can be given with 1 coin, so it will be 1 + 1 = 2 coins. In the center branch we give 5 cents in one coin and have 6 more cents to give. Looking at Table 1 tells us that 6 cents can be given in 2 coins, so 1 + 2 = 3 coins. Finally, in the rightmost branch giving 10 cents as one coin leaves 1 cent to give in change, which is also 1 coin, so 1 + 1 = 2. Thus we can either give 10 cents + 1 cent or 1 cent + 10 cents, which is equivalent since in both cases we give only 2 coins. 

The following python code implements a function called `dynamicCoinChange` which computes a table (like Table 1) for any amount. In line 20 of the script we print a value corresponding to the amount we need to give back. That value is the minimum number of coins. Note that this program takes virtually no time to run.

<iframe src="https://trinket.io/embed/python/81c07a3750?toggleCode=true" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**So**, dynamic programming is a methodology where complex problems are broken down to simple subproblems, that are computed just once and then used to solve the complete problem. In this example, we first pre-compute the number of coins needed to make change for any amount up to the required one, and then produce the answer. 

## Dynamic programming for Manhattan tourist problem 

Now let's get into a multi(2)-dimensional world beautifully elaborated in Jones and Pevzner ([2004](http://www.amazon.com/Introduction-Bioinformatics-Algorithms-Computational-Molecular/dp/0262101068/)) book:

>![](http://www.bx.psu.edu/~anton/bioinf-images/6.3.png)|
>
> **Figure 5** | Reproduced from [JP](http://www.amazon.com/Introduction-Bioinformatics-Algorithms-Computational-Molecular/dp/0262101068/)

The goal of this game is to visit the **maximum number** of attractions along a stroll across Manhattan.
Let's formalize this a bit:

 * city = _n_ x _m_ directed graph
 * node = intersection
 * edge = block
 * edge weight = number of attractions along a city block
 * start node = source
 * end node = sink

|  |  |
|------:|:------:|
|![](http://www.bx.psu.edu/~anton/bioinf-images/6.4a.png)|![](http://www.bx.psu.edu/~anton/bioinf-images/6.4b.png)|
|The city | and a path through it (Figure 6.4 from [JP](http://www.amazon.com/Introduction-Bioinformatics-Algorithms-Computational-Molecular/dp/0262101068/))|

The figure above provides a path from source to the sink, yet this path is not the longest. We can identify the optimal path recursively, but just like in the case if the change problem we will end up with a very inefficient code. Let's instead pre-fill our matrix using the following logic:


<div>

$$s_i,_j = max\begin{cases} s_{i-1,j} + weight\ of\ the\ edge\ between\ (i - 1, j)\ and\ (i,j)
                         & \\ s_{i,j-1} + weight\ of\ the\ edge\ between\ (i, j - 1)\ and\ (i,j)
                 
                 \end{cases}$$

</div>

This will result in the following progression:

|  |  |
|-----------|-------------|
|![](http://www.bx.psu.edu/~anton/bioinf-images/grid1.png)|![](http://www.bx.psu.edu/~anton/bioinf-images/grid2.png)|
|![](http://www.bx.psu.edu/~anton/bioinf-images/grid2.png)|![](http://www.bx.psu.edu/~anton/bioinf-images/grid4.png)|
|![](http://www.bx.psu.edu/~anton/bioinf-images/grid3.png)|![](http://www.bx.psu.edu/~anton/bioinf-images/grid6.png)|
|From [JP](http://www.amazon.com/Introduction-Bioinformatics-Algorithms-Computational-Molecular/dp/0262101068/)| |

You can see that wandering from the source may get us into a dead end. However, backtracking from the sink will always get us to source along the longest path! This by pre-computing the matrix we can easily solve the Manhattan tourist problem. Now we are ready to tackle sequence alignment problems.

# Video

{{< vimeo 182594750 >}}




