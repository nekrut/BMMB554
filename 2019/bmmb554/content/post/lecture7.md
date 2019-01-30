---
date: "2019-01-30"
tags: ["python", "pandas"]
title: "Lecture 7: Pandas 2"
---

# Prep

 - Point your browser to http://colab.research.google.com
 - Open notebook `2019/ipynb/tnseq_with_pandas2.ipynb` from `https://github.com/nekrut/BMMB554`


# Introduction to Pandas : Part 1
-------
This tutorial is heavily based on [Pandas in 10 min](https://pandas.pydata.org/pandas-docs/stable/10min.html). The original material waas modified by adding TnSeq data as examples. 


# Introduction to Pandas : Part 2
------
This tutorial is heavily based on [Pandas in 10 min](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#). The original material waas modified by adding TnSeq data as examples.


```python
import pandas as pd
import numpy as np
%matplotlib inline  
```

## Get datasets to play with


```bash
%%bash
wget https://nekrut.github.io/BMMB554/tnseq_untreated.txt.gz
wget https://nekrut.github.io/BMMB554/ta_gc.txt
```


```python
data_file = 'tnseq_untreated.txt.gz'
```


```python
# Just two choices for beginning of of gene field
!gunzip -c {data_file} | cut -f 8 | cut -f 1 -d '=' | sort | uniq -c
```

    49898 .
    220202 ID



```python
# Process tnseq_untreated.txt.gz to correctly parse gene names

import os
f = open('data.txt','w')

with os.popen('gunzip -c {}'.format(data_file)) as stream:
  for line in stream:
    if line.split( '\t' )[7].startswith( '.' ):
      f.write( '{}\t{}\n'.format( '\t'.join( line.split( '\t' )[:7] ) , 'intergenic'  ) )
    elif line.split( '\t' )[7].startswith( 'ID' ):
      f.write( '{}\t{}\n'.format( '\t'.join( line.split( '\t' )[:7] ) , line.split( '\t' )[7].split(';')[0][3:] ) )
f.close()
```


```python
# Read from the file

tnseq = pd.read_table('data.txt', header=None, names=['pos','blunt','cap','dual','erm','pen','tuf','gene'])
```


```python
tnseq.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>pos</th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2400002</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2400004</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2400006</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2400009</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2400029</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Set position as index

tnseq = tnseq.set_index('pos')
```


```python
tnseq.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2400002</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>2400004</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>2400006</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>2400009</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>2400029</th>
      <td>6.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>intergenic</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading GC content data

gc = pd.read_table('ta_gc.txt', header=None, names=['pos','gc'])
```


```python
gc.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>pos</th>
      <th>gc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>0.339286</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>0.354839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16</td>
      <td>0.367647</td>
    </tr>
    <tr>
      <th>3</th>
      <td>42</td>
      <td>0.372340</td>
    </tr>
    <tr>
      <th>4</th>
      <td>79</td>
      <td>0.303922</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Set position as index as well

gc = gc.set_index('pos')
```


```python
gc.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>0.339286</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.354839</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.367647</td>
    </tr>
    <tr>
      <th>42</th>
      <td>0.372340</td>
    </tr>
    <tr>
      <th>79</th>
      <td>0.303922</td>
    </tr>
  </tbody>
</table>
</div>



## Joins of all sorts

![](http://kirillpavlov.com/images/join-types.png)

Image from Kirill Pavlov [blog](http://kirillpavlov.com/blog/2016/04/23/beyond-traditional-join-with-apache-spark/)

### Prepare sample data

To make things more digestable we will create twio dataframes, `df1` and `df2`, that are small subsets of `tnseq` and `gc` tables. In making them we will make sure that thay mostly overlap but also contain a few rows with indexes not present in the other dataframe.


```python
# Let's create a small subset of tnseq data:

df1 = tnseq[( tnseq['gene'] != 'intergenic' ) & ( tnseq['blunt']>100 ) ].head(10)
```


```python
# Create a numpy array contain index values from fd1

i = np.array(df1.index[1:])
```


```python
i
```




    array([2404933, 2404937, 2410079, 2410094, 2419997, 2430244, 2430254,
           2439462, 2439466])




```python
# Append a few gc index values to i, that are not present in df1

i = np.append(i,[2410079,2405277,2405301])
```


```python
i
```




    array([2404933, 2404937, 2410079, 2410094, 2419997, 2430244, 2430254,
           2439462, 2439466, 2410079, 2405277, 2405301])




```python
# ... and a subset of gc data

df2 = gc.loc[i]
```


```python
# This is what we have in df1

df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404930</th>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
    </tr>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ... and this is content of df2
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404933</th>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2405277</th>
      <td>0.303922</td>
    </tr>
    <tr>
      <th>2405301</th>
      <td>0.274510</td>
    </tr>
  </tbody>
</table>
</div>




### Inner join

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/SQL_Join_-_07_A_Inner_Join_B.svg/220px-SQL_Join_-_07_A_Inner_Join_B.svg.png)

Here **A** is `df1` and **B** is `df2`.

Image from [Wikipedia](https://en.wikipedia.org/wiki/Join_(SQL)).


```python
df1.join(df2, how = 'inner')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_index=True, right_index=True, how = 'inner')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>



### Left join

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/SQL_Join_-_01_A_Left_Join_B.svg/220px-SQL_Join_-_01_A_Left_Join_B.svg.png)

Here **A** is `df1` and **B** is `df2`.

Image from [Wikipedia](https://en.wikipedia.org/wiki/Join_(SQL)).


```python
df1.join(df2, how = 'left')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404930</th>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_index=True, right_index=True, how = 'left')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404930</th>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>



### Right join

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/SQL_Join_-_03_A_Right_Join_B.svg/220px-SQL_Join_-_03_A_Right_Join_B.svg.png)

Here **A** is `df1` and **B** is `df2`.

Image from [Wikipedia](https://en.wikipedia.org/wiki/Join_(SQL)).


```python
df1.join(df2, how = 'right')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2405277</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.303922</td>
    </tr>
    <tr>
      <th>2405301</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_index=True, right_index=True, how = 'right')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2405277</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.303922</td>
    </tr>
    <tr>
      <th>2405301</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>



### Full join

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/SQL_Join_-_05b_A_Full_Join_B.svg/220px-SQL_Join_-_05b_A_Full_Join_B.svg.png)

Here **A** is `df1` and **B** is `df2`.

> Image from [Wikipedia](https://en.wikipedia.org/wiki/Join_(SQL)).


```python
df1.join(df2, how = 'outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404930</th>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2405277</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.303922</td>
    </tr>
    <tr>
      <th>2405301</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1, df2, left_index=True, right_index=True, how = 'outer')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>gc</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404930</th>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2404933</th>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2405277</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.303922</td>
    </tr>
    <tr>
      <th>2405301</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410079</th>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>2410094</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2419997</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>2430244</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2430254</th>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2439462</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>2439466</th>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>



## Grouping

-------

By “group by” we are referring to a process involving one or more of the following steps:

 - Splitting the data into groups based on some criteria
 - Applying a function to each group independently
 - Combining the results into a data structure
See the [Grouping section](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby).


```python
df1.groupby(['gene']).sum()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
    </tr>
    <tr>
      <th>gene</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>gene2465</th>
      <td>920.0</td>
      <td>211.0</td>
      <td>332.0</td>
      <td>310.0</td>
      <td>182.0</td>
      <td>429.0</td>
    </tr>
    <tr>
      <th>gene2471</th>
      <td>387.0</td>
      <td>65.0</td>
      <td>52.0</td>
      <td>90.0</td>
      <td>38.0</td>
      <td>94.0</td>
    </tr>
    <tr>
      <th>gene2481</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>gene2491</th>
      <td>264.0</td>
      <td>173.0</td>
      <td>61.0</td>
      <td>95.0</td>
      <td>100.0</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>gene2499</th>
      <td>220.0</td>
      <td>65.0</td>
      <td>68.0</td>
      <td>149.0</td>
      <td>41.0</td>
      <td>101.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.groupby(['gene']).max()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
    </tr>
    <tr>
      <th>gene</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>gene2465</th>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
    </tr>
    <tr>
      <th>gene2471</th>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>gene2481</th>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>gene2491</th>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>gene2499</th>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
    </tr>
  </tbody>
</table>
</div>



## Actually using SQL

There is a great SQL-like interface for Pandas called [`pandasql`](https://github.com/yhat/pandasql):


```python
!pip install -U pandasql
```



```python
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
```


```python
## Aggregating

pysqldf("select gene, sum(blunt) as bl from df1 group by gene")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>gene</th>
      <th>bl</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>gene2465</td>
      <td>920.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>gene2471</td>
      <td>387.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>gene2481</td>
      <td>111.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gene2491</td>
      <td>264.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gene2499</td>
      <td>220.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Joining (left join)

pysqldf("select * from df1 left join df2 on df1.pos = df2.pos")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>pos</th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>pos</th>
      <th>gc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2404930</td>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2404933</td>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>2404933.0</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2404937</td>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>2404937.0</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2410079</td>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>2410079.0</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2410079</td>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>2410079.0</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2410094</td>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>2410094.0</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2419997</td>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>2419997.0</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2430244</td>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>2430244.0</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2430254</td>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>2430254.0</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2439462</td>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>2439462.0</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2439466</td>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>2439466.0</td>
      <td>0.313725</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Joining (inner join)

pysqldf("select * from df1 join df2 on df1.pos = df2.pos")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead class="thead-dark">
    <tr style="text-align: right;">
      <th></th>
      <th>pos</th>
      <th>blunt</th>
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
      <th>tuf</th>
      <th>gene</th>
      <th>pos</th>
      <th>gc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2404933</td>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
      <td>2404933</td>
      <td>0.284314</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2404937</td>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
      <td>2404937</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2410079</td>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>2410079</td>
      <td>0.352941</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2410094</td>
      <td>194.0</td>
      <td>33.0</td>
      <td>26.0</td>
      <td>46.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>2410094</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2419997</td>
      <td>111.0</td>
      <td>37.0</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>39.0</td>
      <td>66.0</td>
      <td>gene2481</td>
      <td>2419997</td>
      <td>0.343137</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2430244</td>
      <td>136.0</td>
      <td>90.0</td>
      <td>32.0</td>
      <td>61.0</td>
      <td>58.0</td>
      <td>47.0</td>
      <td>gene2491</td>
      <td>2430244</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2430254</td>
      <td>128.0</td>
      <td>83.0</td>
      <td>29.0</td>
      <td>34.0</td>
      <td>42.0</td>
      <td>38.0</td>
      <td>gene2491</td>
      <td>2430254</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2439462</td>
      <td>112.0</td>
      <td>35.0</td>
      <td>36.0</td>
      <td>93.0</td>
      <td>22.0</td>
      <td>56.0</td>
      <td>gene2499</td>
      <td>2439462</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2439466</td>
      <td>108.0</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>56.0</td>
      <td>19.0</td>
      <td>45.0</td>
      <td>gene2499</td>
      <td>2439466</td>
      <td>0.313725</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2410079</td>
      <td>193.0</td>
      <td>32.0</td>
      <td>26.0</td>
      <td>44.0</td>
      <td>19.0</td>
      <td>47.0</td>
      <td>gene2471</td>
      <td>2410079</td>
      <td>0.352941</td>
    </tr>
  </tbody>
</table>
</div>


