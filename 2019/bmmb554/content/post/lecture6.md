---
date: "2019-01-28"
tags: ["python", "pandas"]
title: "Lecture 6: Pandas 1"
---

# Prep

 - Point your browser to http://colab.research.google.com
 - Open notebook `2019/ipynb/tnseq_with_pandas.ipynb` from `https://github.com/nekrut/BMMB554`


# Introduction to Pandas : Part 1
-------
This tutorial is heavily based on [Pandas in 10 min](https://pandas.pydata.org/pandas-docs/stable/10min.html). The original material waas modified by adding TnSeq data as examples. 


## Get datasets to play with


```bash
%%bash
wget https://nekrut.github.io/BMMB554/tnseq_untreated.txt.gz
wget https://nekrut.github.io/BMMB554/ta_gc.txt
```

    2019-01-28 13:53:53 (2.53 MB/s) - 'tnseq_untreated.txt.gz' saved [2012967/2012967]
 
    2019-01-28 13:53:56 (2.96 MB/s) - 'ta_gc.txt' saved [7315570/7315570] 



```python
data_file = 'tnseq_untreated.txt.gz'
```

The first dataset lists coordinates of `TA` sites and counts of reads for TnSeq constructs 'blunt', 'cap', 'dual', 'erm', 'pen', and 'tuf':


```python
!gunzip -c {data_file} | head
```

    2400002	0.0	0.0	1.0	0.0	0.0	1.0	.
    2400004	1.0	0.0	5.0	0.0	0.0	1.0	.
    2400006	1.0	0.0	5.0	1.0	0.0	1.0	.
    2400009	2.0	2.0	8.0	1.0	0.0	0.0	.
    2400029	6.0	1.0	0.0	1.0	0.0	1.0	.
    2400038	4.0	2.0	0.0	3.0	3.0	2.0	.
    2400047	22.0	4.0	2.0	3.0	4.0	5.0	.
    2400061	25.0	3.0	3.0	2.0	2.0	9.0	.
    2400065	3.0	0.0	1.0	1.0	1.0	5.0	.
    2400072	8.0	5.0	28.0	10.0	7.0	9.0	.
    



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
!wc -l data.txt
```

      270100 data.txt



```python
!head data.txt
```

    2400002	0.0	0.0	1.0	0.0	0.0	1.0	intergenic
    2400004	1.0	0.0	5.0	0.0	0.0	1.0	intergenic
    2400006	1.0	0.0	5.0	1.0	0.0	1.0	intergenic
    2400009	2.0	2.0	8.0	1.0	0.0	0.0	intergenic
    2400029	6.0	1.0	0.0	1.0	0.0	1.0	intergenic
    2400038	4.0	2.0	0.0	3.0	3.0	2.0	intergenic
    2400047	22.0	4.0	2.0	3.0	4.0	5.0	intergenic
    2400061	25.0	3.0	3.0	2.0	2.0	9.0	intergenic
    2400065	3.0	0.0	1.0	1.0	1.0	5.0	intergenic
    2400072	8.0	5.0	28.0	10.0	7.0	9.0	intergenic



```python
!gunzip -c {data_file} | wc -l
```

      270100



```python
import pandas as pd

tnseq = pd.read_table('data.txt', header=None, names=['pos','blunt','cap','dual','erm','pen','tuf','gene'])
```


```python
# Let's create a small subset of this dataset
df = tnseq[tnseq['blunt'] > 200]
```


```python
df.head()
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
      <th>469</th>
      <td>2404930</td>
      <td>283.0</td>
      <td>65.0</td>
      <td>109.0</td>
      <td>94.0</td>
      <td>47.0</td>
      <td>128.0</td>
      <td>gene2465</td>
    </tr>
    <tr>
      <th>470</th>
      <td>2404933</td>
      <td>284.0</td>
      <td>67.0</td>
      <td>108.0</td>
      <td>94.0</td>
      <td>55.0</td>
      <td>128.0</td>
      <td>gene2465</td>
    </tr>
    <tr>
      <th>471</th>
      <td>2404937</td>
      <td>353.0</td>
      <td>79.0</td>
      <td>115.0</td>
      <td>122.0</td>
      <td>80.0</td>
      <td>173.0</td>
      <td>gene2465</td>
    </tr>
    <tr>
      <th>20753</th>
      <td>511019</td>
      <td>7399.0</td>
      <td>2021.0</td>
      <td>1933.0</td>
      <td>9207.0</td>
      <td>1860.0</td>
      <td>3141.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>20754</th>
      <td>511024</td>
      <td>7390.0</td>
      <td>2017.0</td>
      <td>1925.0</td>
      <td>9168.0</td>
      <td>1857.0</td>
      <td>3130.0</td>
      <td>intergenic</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index
```




    Int64Index([   469,    470,    471,  20753,  20754,  20755,  26131,  26436,
                 26437,  26438,
                ...
                245491, 245492, 245493, 252032, 252850, 252851, 254003, 255351,
                260067, 267395],
               dtype='int64', length=104)




```python
df.describe()
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1.040000e+02</td>
      <td>104.000000</td>
      <td>104.000000</td>
      <td>104.000000</td>
      <td>104.000000</td>
      <td>104.000000</td>
      <td>104.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.295009e+06</td>
      <td>473.000000</td>
      <td>145.307692</td>
      <td>141.394231</td>
      <td>428.307692</td>
      <td>134.855769</td>
      <td>221.884615</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.859577e+05</td>
      <td>1200.109048</td>
      <td>328.880097</td>
      <td>319.687360</td>
      <td>1525.561454</td>
      <td>303.135217</td>
      <td>510.726083</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.068300e+04</td>
      <td>202.000000</td>
      <td>27.000000</td>
      <td>18.000000</td>
      <td>35.000000</td>
      <td>16.000000</td>
      <td>37.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.110228e+05</td>
      <td>217.750000</td>
      <td>51.750000</td>
      <td>43.750000</td>
      <td>73.000000</td>
      <td>49.500000</td>
      <td>76.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.046223e+06</td>
      <td>248.000000</td>
      <td>77.000000</td>
      <td>64.500000</td>
      <td>116.500000</td>
      <td>71.500000</td>
      <td>116.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.105208e+06</td>
      <td>312.750000</td>
      <td>123.000000</td>
      <td>108.250000</td>
      <td>204.500000</td>
      <td>107.000000</td>
      <td>183.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.726151e+06</td>
      <td>7399.000000</td>
      <td>2021.000000</td>
      <td>1933.000000</td>
      <td>9207.000000</td>
      <td>1860.000000</td>
      <td>3141.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df.sort_values(by=['pos'])
```


```python
df = df.set_index('pos')
```


```python
df.head()
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
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
      <td>140.0</td>
      <td>362.0</td>
      <td>128.0</td>
      <td>253.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>141343</th>
      <td>419.0</td>
      <td>185.0</td>
      <td>214.0</td>
      <td>421.0</td>
      <td>179.0</td>
      <td>380.0</td>
      <td>intergenic</td>
    </tr>
  </tbody>
</table>
</div>



## Selection
-------
**Note**: While standard Python / Numpy expressions for selecting and setting are intuitive and come in handy for interactive work, for production code, we recommend the optimized pandas data access methods, `.at`, `.iat`, `.loc` and `.iloc`.

See the indexing documentation:
 - [Indexing and Selecting Data](https://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing)
 - [MultiIndex / Advanced Indexing](https://pandas.pydata.org/pandas-docs/stable/advanced.html#advanced)

### Getting

Selecting via `[]`, which slices the rows.


```python
df[0:3]
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
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
    </tr>
  </tbody>
</table>
</div>



Selecting a single column, a `series` can be done in two ways:


```python
df.gene.head()
```




    pos
    40683         gene35
    103869        gene90
    132578       gene116
    141339    intergenic
    141343    intergenic
    Name: gene, dtype: object



or


```python
df['gene'].head()
```




    pos
    40683         gene35
    103869        gene90
    132578       gene116
    141339    intergenic
    141343    intergenic
    Name: gene, dtype: object



### Selection by label
See more in [Selection by Label](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-label).

For getting a cross section using a label:


```python
df.loc[2404930]
```




    blunt         283
    cap            65
    dual          109
    erm            94
    pen            47
    tuf           128
    gene     gene2465
    Name: 2404930, dtype: object




```python
df.loc[2404930,['erm','pen']]
```




    erm    94
    pen    47
    Name: 2404930, dtype: object




```python
df.loc[2404930:2404937,['erm','pen']]
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
      <th>erm</th>
      <th>pen</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2404930</th>
      <td>94.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>2404933</th>
      <td>94.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>2404937</th>
      <td>122.0</td>
      <td>80.0</td>
    </tr>
  </tbody>
</table>
</div>



### Selection by position
See more in [Selection by Position](https://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-integer)

Select via the position of the passed integers:


```python
df.iloc[3]
```




    blunt           348
    cap             136
    dual            140
    erm             362
    pen             128
    tuf             253
    gene     intergenic
    Name: 141339, dtype: object



By integer slices, acting similar to numpy/python:


```python
df.iloc[3:5,0:2]
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
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
    </tr>
    <tr>
      <th>141343</th>
      <td>419.0</td>
      <td>185.0</td>
    </tr>
  </tbody>
</table>
</div>



By lists of integer position locations, similar to the numpy/python style:


```python
df.iloc[[1,2,4],[0,2]]
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
      <th>dual</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>141343</th>
      <td>419.0</td>
      <td>214.0</td>
    </tr>
  </tbody>
</table>
</div>



For slicing rows explicitly:


```python
df.iloc[100:,1:5]
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
      <th>cap</th>
      <th>dual</th>
      <th>erm</th>
      <th>pen</th>
    </tr>
    <tr>
      <th>pos</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2663073</th>
      <td>141.0</td>
      <td>61.0</td>
      <td>137.0</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>2703968</th>
      <td>57.0</td>
      <td>51.0</td>
      <td>70.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>2726139</th>
      <td>107.0</td>
      <td>542.0</td>
      <td>155.0</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>2726151</th>
      <td>111.0</td>
      <td>545.0</td>
      <td>156.0</td>
      <td>89.0</td>
    </tr>
  </tbody>
</table>
</div>



For getting a value explicitly:


```python
df.iloc[1,1]
```




    42.0



For getting fast access to a scalar (equivalent to the prior method):


```python
df.iat[1,1]
```




    42.0



### Selecting based on condition (boolean indexing)

Using a single column’s values to select data:


```python
df[df.gene != 'intergenic'].head()
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
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
    </tr>
    <tr>
      <th>203828</th>
      <td>287.0</td>
      <td>45.0</td>
      <td>35.0</td>
      <td>72.0</td>
      <td>84.0</td>
      <td>223.0</td>
      <td>gene172</td>
    </tr>
    <tr>
      <th>203830</th>
      <td>287.0</td>
      <td>45.0</td>
      <td>35.0</td>
      <td>73.0</td>
      <td>84.0</td>
      <td>223.0</td>
      <td>gene172</td>
    </tr>
  </tbody>
</table>
</div>



Selecting values from a DataFrame where a boolean condition is met:


```python
df[df > 0].head()
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
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
      <td>140.0</td>
      <td>362.0</td>
      <td>128.0</td>
      <td>253.0</td>
      <td>intergenic</td>
    </tr>
    <tr>
      <th>141343</th>
      <td>419.0</td>
      <td>185.0</td>
      <td>214.0</td>
      <td>421.0</td>
      <td>179.0</td>
      <td>380.0</td>
      <td>intergenic</td>
    </tr>
  </tbody>
</table>
</div>



Using the [`isin()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.isin.html#pandas.Series.isin) method for filtering:


```python
df.gene.unique()
```




    array(['gene35', 'gene90', 'gene116', 'intergenic', 'gene172', 'gene176',
           'gene206', 'gene233', 'gene275', 'gene297', 'gene313', 'gene443',
           'gene528', 'gene533', 'gene673', 'gene688', 'gene929', 'gene932',
           'gene1016', 'gene1342', 'gene1364', 'gene1469', 'gene1516',
           'gene1751', 'gene1753', 'gene1833', 'gene2010', 'gene2134',
           'gene2176', 'gene2195', 'gene2209', 'gene2233', 'gene2321',
           'gene2390', 'gene2465', 'gene2664', 'gene2707', 'gene2764',
           'gene2787'], dtype=object)




```python
df[df['gene'].isin(['gene2465','gene206'])]
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
      <th>242376</th>
      <td>229.0</td>
      <td>31.0</td>
      <td>56.0</td>
      <td>63.0</td>
      <td>44.0</td>
      <td>69.0</td>
      <td>gene206</td>
    </tr>
    <tr>
      <th>242378</th>
      <td>204.0</td>
      <td>31.0</td>
      <td>48.0</td>
      <td>60.0</td>
      <td>39.0</td>
      <td>42.0</td>
      <td>gene206</td>
    </tr>
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
  </tbody>
</table>
</div>



### Setting

Setting a new column automatically aligns the data by the indexes:


```python
gc = pd.read_table('ta_gc.txt', header=None, names=['pos','gc'])
```


```python
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




```python
df['gc'] = gc
```


```python
df.head()
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
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
      <td>140.0</td>
      <td>362.0</td>
      <td>128.0</td>
      <td>253.0</td>
      <td>intergenic</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>141343</th>
      <td>419.0</td>
      <td>185.0</td>
      <td>214.0</td>
      <td>421.0</td>
      <td>179.0</td>
      <td>380.0</td>
      <td>intergenic</td>
      <td>0.323529</td>
    </tr>
  </tbody>
</table>
</div>



Setting values by label:


```python
df.at[2,'erm'] = 0
```


```python
df.loc[2]
```




    blunt    NaN
    cap      NaN
    dual     NaN
    erm        0
    pen      NaN
    tuf      NaN
    gene     NaN
    gc       NaN
    Name: 2, dtype: object




```python
df = df.sort_index()
```


```python
df.head()
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
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
      <td>140.0</td>
      <td>362.0</td>
      <td>128.0</td>
      <td>253.0</td>
      <td>intergenic</td>
      <td>0.333333</td>
    </tr>
  </tbody>
</table>
</div>



## Missing data
-------
pandas primarily uses the value `np.nan` to represent missing data. It is by default not included in computations. See the [Missing Data section](https://pandas.pydata.org/pandas-docs/stable/missing_data.html#missing-data).

To drop any rows that have missing data:


```python
df.dropna(how='any').head()
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
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
      <td>140.0</td>
      <td>362.0</td>
      <td>128.0</td>
      <td>253.0</td>
      <td>intergenic</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>141343</th>
      <td>419.0</td>
      <td>185.0</td>
      <td>214.0</td>
      <td>421.0</td>
      <td>179.0</td>
      <td>380.0</td>
      <td>intergenic</td>
      <td>0.323529</td>
    </tr>
  </tbody>
</table>
</div>



Filling missing data


```python
df.fillna(value='0').head()
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
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>40683</th>
      <td>211</td>
      <td>80</td>
      <td>91</td>
      <td>68.0</td>
      <td>81</td>
      <td>67</td>
      <td>gene35</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214</td>
      <td>42</td>
      <td>50</td>
      <td>155.0</td>
      <td>31</td>
      <td>69</td>
      <td>gene90</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202</td>
      <td>70</td>
      <td>99</td>
      <td>194.0</td>
      <td>107</td>
      <td>157</td>
      <td>gene116</td>
      <td>0.27451</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348</td>
      <td>136</td>
      <td>140</td>
      <td>362.0</td>
      <td>128</td>
      <td>253</td>
      <td>intergenic</td>
      <td>0.333333</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isna().head()
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
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>40683</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



## Operations
-------
See the [Basic section on Binary Ops](https://pandas.pydata.org/pandas-docs/stable/basics.html#basics-binop).

### Stats

Operations in general exclude missing data.

Performing a descriptive statistic:


```python
df.mean()
```




    blunt    473.000000
    cap      145.307692
    dual     141.394231
    erm      424.228571
    pen      134.855769
    tuf      221.884615
    gc         0.316365
    dtype: float64



Same operation on the other axis:


```python
df.mean(1).head()
```




    pos
    2           0.000000
    40683      85.466387
    103869     80.180672
    132578    118.467787
    141339    195.333333
    dtype: float64



### Apply
Apply functions to the data:


```python
df.head()
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
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
      <td>gene35</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>214.0</td>
      <td>42.0</td>
      <td>50.0</td>
      <td>155.0</td>
      <td>31.0</td>
      <td>69.0</td>
      <td>gene90</td>
      <td>0.264706</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>202.0</td>
      <td>70.0</td>
      <td>99.0</td>
      <td>194.0</td>
      <td>107.0</td>
      <td>157.0</td>
      <td>gene116</td>
      <td>0.274510</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>348.0</td>
      <td>136.0</td>
      <td>140.0</td>
      <td>362.0</td>
      <td>128.0</td>
      <td>253.0</td>
      <td>intergenic</td>
      <td>0.333333</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
df.loc[:,'blunt':'tuf'].apply(np.cumsum).head()
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
      <th>pos</th>
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
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40683</th>
      <td>211.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>68.0</td>
      <td>81.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>103869</th>
      <td>425.0</td>
      <td>122.0</td>
      <td>141.0</td>
      <td>223.0</td>
      <td>112.0</td>
      <td>136.0</td>
    </tr>
    <tr>
      <th>132578</th>
      <td>627.0</td>
      <td>192.0</td>
      <td>240.0</td>
      <td>417.0</td>
      <td>219.0</td>
      <td>293.0</td>
    </tr>
    <tr>
      <th>141339</th>
      <td>975.0</td>
      <td>328.0</td>
      <td>380.0</td>
      <td>779.0</td>
      <td>347.0</td>
      <td>546.0</td>
    </tr>
  </tbody>
</table>
</div>



### Hostogramming
See more at [Histogramming and Discretization](https://pandas.pydata.org/pandas-docs/stable/basics.html#basics-discretization):


```python
df['gene'].value_counts()
```




    intergenic    30
    gene2134       7
    gene929        5
    gene2010       5
    gene176        4
    gene1016       3
    gene533        3
    gene2390       3
    gene172        3
    gene1342       3
    gene2465       3
    gene1753       2
    gene2233       2
    gene2787       2
    gene2195       2
    gene206        2
    gene1469       2
    gene673        2
    gene1833       1
    gene297        1
    gene116        1
    gene90         1
    gene2321       1
    gene932        1
    gene1516       1
    gene313        1
    gene1751       1
    gene35         1
    gene2764       1
    gene688        1
    gene2664       1
    gene2707       1
    gene275        1
    gene233        1
    gene1364       1
    gene528        1
    gene2176       1
    gene2209       1
    gene443        1
    Name: gene, dtype: int64




```python
%matplotlib inline
df.loc[:,'blunt':'tuf'].hist(bins=100, sharex=True, sharey=True)
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x1230fa908>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x123146fd0>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x12317b400>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x12319f7f0>],
           [<matplotlib.axes._subplots.AxesSubplot object at 0x1231c8be0>,
            <matplotlib.axes._subplots.AxesSubplot object at 0x1231c8c18>]],
          dtype=object)




![png](/BMMB554/img/output_77_1.png)


### String Methods
Series is equipped with a set of string processing methods in the str attribute that make it easy to operate on each element of the array, as in the code snippet below. Note that pattern-matching in str generally uses [regular expressions](https://docs.python.org/3/library/re.html) by default (and in some cases always uses them). See more at [Vectorized String Methods](https://pandas.pydata.org/pandas-docs/stable/text.html#text-string-methods):


```python
df['gene'].str.upper().head()
```




    pos
    2                NaN
    40683         GENE35
    103869        GENE90
    132578       GENE116
    141339    INTERGENIC
    Name: gene, dtype: object



In the next lecture we will learn how to process data in a number of interesting ways
