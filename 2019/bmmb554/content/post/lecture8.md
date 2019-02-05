---
date: "2019-02-04"
tags: ["python", "seaborn","motplotlib","plotting"]
title: "Lecture 8: Plotting in Python"
---


<div class="alert alert-info" role="alert">
  This lecture draws extensively from <a href="https://seaborn.pydata.org/tutorial.html">Seaborn tutorials</a>.
</div>

# A primer of plotting with Python


```python
# If running in colaboratory uncomment and run the folliwing command
#!pip install seaborn --upgrade
```


```python
import seaborn as sns
sns.set(style="ticks")

import pandas as pd
import matplotlib.pyplot as plt
```

# Why plotting?
We will use [Ascombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) build into Seaborn to answer this questions


```python
# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")
```


```python
df
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
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dataset</th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>I</td>
      <td>10.0</td>
      <td>8.04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I</td>
      <td>8.0</td>
      <td>6.95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>I</td>
      <td>13.0</td>
      <td>7.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>I</td>
      <td>9.0</td>
      <td>8.81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>I</td>
      <td>11.0</td>
      <td>8.33</td>
    </tr>
    <tr>
      <th>5</th>
      <td>I</td>
      <td>14.0</td>
      <td>9.96</td>
    </tr>
    <tr>
      <th>6</th>
      <td>I</td>
      <td>6.0</td>
      <td>7.24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>I</td>
      <td>4.0</td>
      <td>4.26</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I</td>
      <td>12.0</td>
      <td>10.84</td>
    </tr>
    <tr>
      <th>9</th>
      <td>I</td>
      <td>7.0</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>10</th>
      <td>I</td>
      <td>5.0</td>
      <td>5.68</td>
    </tr>
    <tr>
      <th>11</th>
      <td>II</td>
      <td>10.0</td>
      <td>9.14</td>
    </tr>
    <tr>
      <th>12</th>
      <td>II</td>
      <td>8.0</td>
      <td>8.14</td>
    </tr>
    <tr>
      <th>13</th>
      <td>II</td>
      <td>13.0</td>
      <td>8.74</td>
    </tr>
    <tr>
      <th>14</th>
      <td>II</td>
      <td>9.0</td>
      <td>8.77</td>
    </tr>
    <tr>
      <th>15</th>
      <td>II</td>
      <td>11.0</td>
      <td>9.26</td>
    </tr>
    <tr>
      <th>16</th>
      <td>II</td>
      <td>14.0</td>
      <td>8.10</td>
    </tr>
    <tr>
      <th>17</th>
      <td>II</td>
      <td>6.0</td>
      <td>6.13</td>
    </tr>
    <tr>
      <th>18</th>
      <td>II</td>
      <td>4.0</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>19</th>
      <td>II</td>
      <td>12.0</td>
      <td>9.13</td>
    </tr>
    <tr>
      <th>20</th>
      <td>II</td>
      <td>7.0</td>
      <td>7.26</td>
    </tr>
    <tr>
      <th>21</th>
      <td>II</td>
      <td>5.0</td>
      <td>4.74</td>
    </tr>
    <tr>
      <th>22</th>
      <td>III</td>
      <td>10.0</td>
      <td>7.46</td>
    </tr>
    <tr>
      <th>23</th>
      <td>III</td>
      <td>8.0</td>
      <td>6.77</td>
    </tr>
    <tr>
      <th>24</th>
      <td>III</td>
      <td>13.0</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>25</th>
      <td>III</td>
      <td>9.0</td>
      <td>7.11</td>
    </tr>
    <tr>
      <th>26</th>
      <td>III</td>
      <td>11.0</td>
      <td>7.81</td>
    </tr>
    <tr>
      <th>27</th>
      <td>III</td>
      <td>14.0</td>
      <td>8.84</td>
    </tr>
    <tr>
      <th>28</th>
      <td>III</td>
      <td>6.0</td>
      <td>6.08</td>
    </tr>
    <tr>
      <th>29</th>
      <td>III</td>
      <td>4.0</td>
      <td>5.39</td>
    </tr>
    <tr>
      <th>30</th>
      <td>III</td>
      <td>12.0</td>
      <td>8.15</td>
    </tr>
    <tr>
      <th>31</th>
      <td>III</td>
      <td>7.0</td>
      <td>6.42</td>
    </tr>
    <tr>
      <th>32</th>
      <td>III</td>
      <td>5.0</td>
      <td>5.73</td>
    </tr>
    <tr>
      <th>33</th>
      <td>IV</td>
      <td>8.0</td>
      <td>6.58</td>
    </tr>
    <tr>
      <th>34</th>
      <td>IV</td>
      <td>8.0</td>
      <td>5.76</td>
    </tr>
    <tr>
      <th>35</th>
      <td>IV</td>
      <td>8.0</td>
      <td>7.71</td>
    </tr>
    <tr>
      <th>36</th>
      <td>IV</td>
      <td>8.0</td>
      <td>8.84</td>
    </tr>
    <tr>
      <th>37</th>
      <td>IV</td>
      <td>8.0</td>
      <td>8.47</td>
    </tr>
    <tr>
      <th>38</th>
      <td>IV</td>
      <td>8.0</td>
      <td>7.04</td>
    </tr>
    <tr>
      <th>39</th>
      <td>IV</td>
      <td>8.0</td>
      <td>5.25</td>
    </tr>
    <tr>
      <th>40</th>
      <td>IV</td>
      <td>19.0</td>
      <td>12.50</td>
    </tr>
    <tr>
      <th>41</th>
      <td>IV</td>
      <td>8.0</td>
      <td>5.56</td>
    </tr>
    <tr>
      <th>42</th>
      <td>IV</td>
      <td>8.0</td>
      <td>7.91</td>
    </tr>
    <tr>
      <th>43</th>
      <td>IV</td>
      <td>8.0</td>
      <td>6.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('dataset').describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table class="table table-striped table-responsive">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">x</th>
      <th colspan="8" halign="left">y</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>dataset</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>I</th>
      <td>11.0</td>
      <td>9.0</td>
      <td>3.316625</td>
      <td>4.0</td>
      <td>6.5</td>
      <td>9.0</td>
      <td>11.5</td>
      <td>14.0</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>2.031568</td>
      <td>4.26</td>
      <td>6.315</td>
      <td>7.58</td>
      <td>8.57</td>
      <td>10.84</td>
    </tr>
    <tr>
      <th>II</th>
      <td>11.0</td>
      <td>9.0</td>
      <td>3.316625</td>
      <td>4.0</td>
      <td>6.5</td>
      <td>9.0</td>
      <td>11.5</td>
      <td>14.0</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>2.031657</td>
      <td>3.10</td>
      <td>6.695</td>
      <td>8.14</td>
      <td>8.95</td>
      <td>9.26</td>
    </tr>
    <tr>
      <th>III</th>
      <td>11.0</td>
      <td>9.0</td>
      <td>3.316625</td>
      <td>4.0</td>
      <td>6.5</td>
      <td>9.0</td>
      <td>11.5</td>
      <td>14.0</td>
      <td>11.0</td>
      <td>7.500000</td>
      <td>2.030424</td>
      <td>5.39</td>
      <td>6.250</td>
      <td>7.11</td>
      <td>7.98</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>IV</th>
      <td>11.0</td>
      <td>9.0</td>
      <td>3.316625</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>19.0</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>2.030579</td>
      <td>5.25</td>
      <td>6.170</td>
      <td>7.04</td>
      <td>8.19</td>
      <td>12.50</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None
           )
```




    <seaborn.axisgrid.FacetGrid at 0x7f6abe1548d0>




![png](/BMMB554/img/lecture8/output_7_1.png)


## Let's look at TnSeq data again


```bash
%%bash
wget https://nekrut.github.io/BMMB554/tnseq_untreated.txt.gz
wget https://nekrut.github.io/BMMB554/ta_gc.txt
```

    --2019-02-04 18:36:13--  https://nekrut.github.io/BMMB554/tnseq_untreated.txt.gz
    Resolving nekrut.github.io... 185.199.111.153, 185.199.109.153, 185.199.110.153, ...
    Connecting to nekrut.github.io|185.199.111.153|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 2012967 (1.9M) [application/gzip]
    Saving to: ‘tnseq_untreated.txt.gz’
    
    
    2019-02-04 18:36:14 (9.19 MB/s) - ‘tnseq_untreated.txt.gz.1’ saved [2012967/2012967]
    
    --2019-02-04 18:36:14--  https://nekrut.github.io/BMMB554/ta_gc.txt
    Resolving nekrut.github.io... 185.199.111.153, 185.199.109.153, 185.199.110.153, ...
    Connecting to nekrut.github.io|185.199.111.153|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 7315570 (7.0M) [text/plain]
    Saving to: ‘ta_gc.txt’
 


```python
data_file = 'tnseq_untreated.txt.gz'
```


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
# Reading TnSeq data into a dataframe

tnseq = pd.read_table('data.txt', header=None, names=['pos','blunt','cap','dual','erm','pen','tuf','gene'])
```


```python
# Reading GC content data

gc = pd.read_table('ta_gc.txt', header=None, names=['pos','gc'])
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
  <thead>
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
  <thead>
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
# Join tnseq and GC content data together

tn_gc = tnseq.merge(gc,left_on='pos',right_on='pos',how='left')
```


```python
tn_gc.head()
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
  <thead>
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
      <th>gc</th>
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
      <td>0.225490</td>
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
      <td>0.225490</td>
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
      <td>0.215686</td>
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
      <td>0.225490</td>
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
      <td>0.215686</td>
    </tr>
  </tbody>
</table>
</div>




```python
# This is the list of column containing construct data

list(tn_gc)[1:7]
```




    ['blunt', 'cap', 'dual', 'erm', 'pen', 'tuf']



## "Melting data"

Visualization work much better with so called [narrow data](https://en.wikipedia.org/wiki/Wide_and_narrow_data). To convert our existing dataset into "narrow" form we will melt it down:

![](https://pandas.pydata.org/pandas-docs/stable/_images/reshaping_melt.png)

(This image and a much more detailed explanation of dataframe reshaping can be found in [Pandas Doc Pages](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)).


```python
# Melt tn_gc in tdf

tdf = pd.melt(tn_gc, id_vars=['pos','gc','gene'],value_vars=list(tn_gc)[1:7],var_name="construct",value_name="count").sort_values(by='pos')
```


```python
tdf.head()
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
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pos</th>
      <th>gc</th>
      <th>gene</th>
      <th>construct</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>406329</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>cap</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1486729</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>tuf</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1216629</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>pen</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>676429</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>dual</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>136229</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>blunt</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Set genic and non-genic categories

tdf.loc[tdf['gene'] == 'intergenic','genic'] = 'no'
tdf.loc[tdf['gene'] != 'intergenic','genic'] = 'yes'
```


```python
tdf.head()
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
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pos</th>
      <th>gc</th>
      <th>gene</th>
      <th>construct</th>
      <th>count</th>
      <th>genic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>406329</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>cap</td>
      <td>1.0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1486729</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>tuf</td>
      <td>0.0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1216629</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>pen</td>
      <td>0.0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>676429</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>dual</td>
      <td>0.0</td>
      <td>no</td>
    </tr>
    <tr>
      <th>136229</th>
      <td>4</td>
      <td>0.339286</td>
      <td>intergenic</td>
      <td>blunt</td>
      <td>0.0</td>
      <td>no</td>
    </tr>
  </tbody>
</table>
</div>



# Visualizing the distribution of a dataset
When dealing with a set of data, often the first thing you’ll want to do is get a sense for how the variables are distributed. This chapter of the tutorial will give a brief introduction to some of the tools in seaborn for examining univariate and bivariate distributions. You may also want to look at the categorical plots chapter for examples of functions that make it easy to compare the distribution of a variable across levels of other variables.

These examples are taken from [official seaborn tutorials](https://seaborn.pydata.org/tutorial.html).

## Plotting univariate distributions
The most convenient way to take a quick look at a univariate distribution in seaborn is the [`distplot()`](https://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot) function. By default, this will draw a [histogram](https://en.wikipedia.org/wiki/Histogram) and fit a kernel density estimate [KDE](https://en.wikipedia.org/wiki/Kernel_density_estimation)




```python
# Distribution of GC content 

sns.distplot(tdf['gc'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f6abd8dc8d0>




![png](/BMMB554/img/lecture8/output_26_1.png)



```python
# Distribution of read counts is a bit gloomy

sns.distplot(tdf['count'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f6ab8c66748>




![png](/BMMB554/img/lecture8/output_27_1.png)



```python
# We can narrow it down

sns.distplot(tdf['count'][(tdf['count']>6)&(tdf['count']<100)])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f6abd82e668>




![png](/BMMB554/img/lecture8/output_28_1.png)



```python
# Or increase the number of bins and change the scale

g=sns.distplot(tdf['count'],bins=10000)
g.set(xscale="log")
```




    [None]




![png](/BMMB554/img/lecture8/output_29_1.png)



```python
# And also get rid of zero counts

g=sns.distplot(tdf['count'][tdf['count']>0],bins=10000)
g.set(xscale="log")

```




    [None]




![png](/BMMB554/img/lecture8/output_30_1.png)



```python
# Plotting the relationship between GC count and insertion frequency

sns.jointplot(x="count", y="gc", data=tdf[tdf['count']>10]);
```


![png](/BMMB554/img/lecture8/output_31_0.png)


# Visualizing statistical relationships
Statistical analysis is a process of understanding how variables in a dataset relate to each other and how those relationships depend on other variables. Visualization can be a core component of this process because, when data are visualized properly, the human visual system can see trends and patterns that indicate a relationship.

We will discuss three seaborn functions in this tutorial. The one we will use most is [ `relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot). This is a [figure-level function](https://seaborn.pydata.org/introduction.html#intro-func-types) for visualizing statistical relationships using two common approaches: scatter plots and line plots. [ `relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot) combines a [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid) with one of two axes-level functions:

 - [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot) (with `kind="scatter"`; the default)
 - [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot) (with `kind="line"`)
 
As we will see, these functions can be quite illuminating because they use simple and easily-understood representations of data that can nevertheless represent complex dataset structures. They can do so because they plot two-dimensional graphics that can be enhanced by mapping up to three additional variables using the semantics of hue, size, and style.

## Relating variables with scatter plots
The scatter plot is a mainstay of statistical visualization. It depicts the joint distribution of two variables using a cloud of points, where each point represents an observation in the dataset. This depiction allows the eye to infer a substantial amount of information about whether there is any meaningful relationship between them.

There are several ways to draw a scatter plot in seaborn. The most basic, which should be used when both variables are numeric, is the [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot) function. The [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot) is the default kind in [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot) (it can also be forced by setting `kind="scatter"`):


```python
sns.relplot(x='gc',y='count',data=tdf[tdf['count']>100])
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa132ae80>




![png](/BMMB554/img/lecture8/output_34_1.png)


While the points are plotted in two dimensions, another dimension can be added to the plot by coloring the points according to a third variable. In seaborn, this is referred to as using a “hue semantic”, because the color of the point gains meaning:


```python
sns.relplot(x='gc',y='count',data=tdf[tdf['count']>100],hue='construct')
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa10d68d0>




![png](/BMMB554/img/lecture8/output_36_1.png)



```python
# Here we change y axis to log scale

g = sns.relplot(x='gc',y='count',data=tdf[tdf['count']>100],hue='construct')
g.set(yscale="log")
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0ec19e8>




![png](/BMMB554/img/lecture8/output_37_1.png)


To emphasize the difference between the classes, and to improve accessibility, you can use a different marker style for each class:


```python
sns.relplot(x='gc',y='count',data=tdf[tdf['count']>100],hue='construct',style='genic')
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0a590f0>




![png](/BMMB554/img/lecture8/output_39_1.png)


# Categorical scatterplots
The default representation of the data in [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot) uses a scatterplot. There are actually two different categorical scatter plots in seaborn. They take different approaches to resolving the main challenge in representing categorical data with a scatter plot, which is that all of the points belonging to one category would fall on the same position along the axis corresponding to the categorical variable. The approach used by [`stripplot()`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot), which is the default “kind” in [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot) is to adjust the positions of points on the categorical axis with a small amount of random “jitter”:


```python
sns.catplot(x="construct", y="count", data=tdf[tdf['count']>100]);
```


![png](/BMMB554/img/lecture8/output_41_0.png)


The `jitter` parameter controls the magnitude of jitter or disables it altogether:


```python
sns.catplot(x="construct", y="count", data=tdf[tdf['count']>100],jitter=False);
```


![png](/BMMB554/img/lecture8/output_43_0.png)


The second approach adjusts the points along the categorical axis using an algorithm that prevents them from overlapping. It can give a better representation of the distribution of observations, although it only works well for relatively small datasets. This kind of plot is sometimes called a “beeswarm” and is drawn in seaborn by [`swarmplot()`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot), which is activated by setting `kind="swarm"` in [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot):


```python
sns.catplot(x="construct", y="count", data=tdf[tdf['count']>100],kind="swarm")
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0df8cc0>




![png](/BMMB554/img/lecture8/output_45_1.png)


Similar to the relational plots, it’s possible to add another dimension to a categorical plot by using a `hue` semantic. (The categorical plots do not currently support `size` or `style` semantics). Each different categorical plotting function handles the `hue` semantic differently. For the scatter plots, it is only necessary to change the color of the points:


```python
sns.catplot(x="construct", y="count", data=tdf[tdf['count']>100],kind="swarm",hue='genic')
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0ee0e48>




![png](/BMMB554/img/lecture8/output_47_1.png)


We’ve referred to the idea of “categorical axis”. In these examples, that’s always corresponded to the horizontal axis. But it’s often helpful to put the categorical variable on the vertical axis (particularly when the category names are relatively long or there are many categories). To do this, swap the assignment of variables to axes:


```python
sns.catplot(x="count", y="construct", data=tdf[tdf['count']>100],kind="swarm",hue='genic')
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0df8898>




![png](/BMMB554/img/lecture8/output_49_1.png)


## Distributions of observations within categories
As the size of the dataset grows,, categorical scatter plots become limited in the information they can provide about the distribution of values within each category. When this happens, there are several approaches for summarizing the distributional information in ways that facilitate easy comparisons across the category levels.



### Boxplots
The first is the familiar [`boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot). This kind of plot shows the three quartile values of the distribution along with extreme values. The “whiskers” extend to points that lie within 1.5 IQRs of the lower and upper quartile, and then observations that fall outside this range are displayed independently. This means that each value in the boxplot corresponds to an actual observation in the data.


```python
sns.catplot(x="construct", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<100)],kind="box")
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0f97a58>




![png](/BMMB554/img/lecture8/output_52_1.png)


When adding a `hue` semantic, the box for each level of the semantic variable is moved along the categorical axis so they don’t overlap:


```python
sns.catplot(x="construct", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<100)],kind="box",hue='genic')
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa1054e80>




![png](/BMMB554/img/lecture8/output_54_1.png)


A related function, [`boxenplot()`](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot), draws a plot that is similar to a box plot but optimized for showing more information about the shape of the distribution. It is best suited for larger datasets:



```python
sns.catplot(x="construct", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<100)],kind="boxen")
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa132ad68>




![png](/BMMB554/img/lecture8/output_56_1.png)


### Violinplots
A different approach is a [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot), which combines a boxplot with the kernel density estimation procedure:




```python
sns.catplot(x="construct", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<100)],kind="violin")
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa144b320>




![png](/BMMB554/img/lecture8/output_58_1.png)



```python
sns.catplot(x="construct", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<100)],kind="violin",hue='genic')
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa159e358>




![png](/BMMB554/img/lecture8/output_59_1.png)


It’s also possible to “split” the violins when the hue parameter has only two levels, which can allow for a more efficient use of space:


```python
sns.catplot(x="construct", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<100)],kind="violin",hue='genic',split=True)
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa145efd0>




![png](/BMMB554/img/lecture8/output_61_1.png)


Finally, there are several options for the plot that is drawn on the interior of the violins, including ways to show each individual observation instead of the summary boxplot values:

## Statistical estimation within categories
For other applications, rather than showing the distribution within each category, you might want to show an estimate of the central tendency of the values. Seaborn has two main ways to show this information. Importantly, the basic API for these functions is identical to that for the ones discussed above.



### Bar plots
A familiar style of plot that accomplishes this goal is a bar plot. In seaborn, the [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot) function operates on a full dataset and applies a function to obtain the estimate (taking the mean by default). When there are multiple observations in each category, it also uses bootstrapping to compute a confidence interval around the estimate and plots that using error bars:


```python
sns.catplot(x="construct",y="count",hue="genic",kind="bar",data=tdf)
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa167ea90>




![png](/BMMB554/img/lecture8/output_65_1.png)


A special case for the bar plot is when you want to show the number of observations in each category rather than computing a statistic for a second variable. This is similar to a histogram over a categorical, rather than quantitative, variable. In seaborn, it’s easy to do so with the [`countplot()`](https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot) function:


```python
sns.catplot(x="genic",kind="count",data=tdf)
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa1340ef0>




![png](/BMMB554/img/lecture8/output_67_1.png)


## Showing multiple relationships with facets
Just like [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot), the fact that [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot) is built on a [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid) means that it is easy to add faceting variables to visualize higher-dimensional relationships:


```python
sns.catplot(x="genic", y="count", data=tdf[(tdf['count']>10) & (tdf['count']<1000)],kind="boxen",col='construct',col_wrap=2)
```




    <seaborn.axisgrid.FacetGrid at 0x7f6aa0d0b588>




![png](/BMMB554/img/lecture8/output_69_1.png)

