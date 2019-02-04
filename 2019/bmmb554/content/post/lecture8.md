---
date: "2019-02-04"
tags: ["python", "seaborn","motplotlib","plotting"]
title: "Lecture 8: Plotting in Python"
---

The lecture notes will be posted **after** the class. For now do this:

 - Point your browser to http://colab.research.google.com
 - Create a new Python3 notebbok
 - Execute the following commans:

 ```bash
 # Colaboratory has an old version of seaborn, so let's upgrade 
!pip install seaborn --upgrade
```

Import required libraries:

```python
import seaborn as sns
sns.set(style="ticks")

import pandas as pd
import matplotlib.pyplot as plt
```

Import TnSeq datasets:

```bash
%%bash
wget https://nekrut.github.io/BMMB554/tnseq_untreated.txt.gz
wget https://nekrut.github.io/BMMB554/ta_gc.txt
```

Set datafile name:

```python
data_file = 'tnseq_untreated.txt.gz'
```

Process the file:

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

Load dataframes:

```python
tnseq = pd.read_table('data.txt', header=None, names=['pos','blunt','cap','dual','erm','pen','tuf','gene'])

gc = pd.read_table('ta_gc.txt', header=None, names=['pos','gc'])
```

...
