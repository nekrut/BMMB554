# Class project for BMMB554

## Groups

### Group 1

- sfh5867@psu.edu
- apk6356@psu.edu
- drr5496@psu.edu
- kkr5509@psu.edu
- ybw5455@psu.edu
- jmn6161@psu.edu
- emk5806@psu.edu

---

### Group 2

- mrs6995@psu.edu
- wbw5279@psu.edu
- hpz5226@psu.edu
- rvd5580@psu.edu
- dns5447@psu.edu
- ssb5724@psu.edu

---

### Group 3

- jal7297@psu.edu
- zxx5155@psu.edu
- msy5129@psu.edu
- lps5778@psu.edu
- evm5863@psu.edu
- mmn5745@psu.edu
- tmh6573@psu.edu

---

### Group 4

- pky5070@psu.edu
- nhk5073@psu.edu
- evw11@psu.edu
- jdd5984@psu.edu
- szb5297@psu.edu
- smh7874@psu.edu

## The problem

Despite the rapidly increasing number of fully assembled genomes few genomes are well annotated. This is especially true for large eukaryotic genomes with their complex gene structure and abundance of pseudogenes. And of course do not forget about the [Murphy’s](https://en.wikipedia.org/wiki/Murphy%27s_law) law: if you are interested in a particular gene the chances are that it will not be annotated in your genome of interest. So …

## What you need to do

### Genes of interest:

- Group 1: _XBP-1_ [UCSC](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr22%3A28794560%2D28800569) [NCBI](https://www.ncbi.nlm.nih.gov/gene/7494/)
- Group 2: _GNAS1_ [UCSC](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr20%3A58839748%2D58911192) [NCBI](https://www.ncbi.nlm.nih.gov/gene/2778)
- Group 3: _Ink4a_ [UCSC](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr9%3A21967752%2D21995323) [NCBI](https://www.ncbi.nlm.nih.gov/gene/1029/)
- Group 4: _LRTOMT_ [UCSC](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr11%3A72080850%2D72110782) [NCBI](https://www.ncbi.nlm.nih.gov/gene/220074/)

### Import a history with your gene

- Group 1: [_XBP-1_](https://usegalaxy.org/u/cartman/h/xbp1) [paper](https://pubmed.ncbi.nlm.nih.gov/17034899/)
- Group 2: [_GNAS1_](https://usegalaxy.org/u/cartman/h/gnas) 
- Group 3: [_Ink4a_](https://usegalaxy.org/u/cartman/h/ink4a) 
- Group 4: [_LRTOMT_](https://usegalaxy.org/u/cartman/h/lrtomt)

### Run analysis workflow

Run the following workflow: https://usegalaxy.org/u/cartman/w/copy-of-comparative-gene-analysis-v3

## Interpreting the results

### Workflow outputs

If all goes well you should get two output datasets in your history:

![image](https://github.com/user-attachments/assets/20080aab-8d94-4fcf-9ee0-0e7485b185ad)

#### Trees

This is a collection of [neghbor-joining](https://doi.org/10.1093/oxfordjournals.molbev.a040454) trees for each input sequence you provided. For example, in the case of *Ink4a* you will get this:

![image](https://github.com/user-attachments/assets/74a9e6e7-04c0-4746-8d33-0014e3ccc281)

If you expand each dataset by clicking on it, you will get access to additional buttons:

![image](https://github.com/user-attachments/assets/64c40f12-fc58-48b1-9aaa-cd593e94902e)

If you click on the "graph" button - the last button in this row:

![image](https://github.com/user-attachments/assets/f2735c15-ec13-401d-ae9d-a5de72574531)

you will see a series of options in the center pane of Galaxy interface:

![image](https://github.com/user-attachments/assets/593ff784-28ec-4fb8-bdfd-9bf20089e716)

If you click on the "Phylogenetic Tree Visualization" you will see the tree:

![image](https://github.com/user-attachments/assets/0d52d967-2601-4b7e-a814-1233c1619f93)

or this:

![image](https://github.com/user-attachments/assets/ef5fd899-4431-4dca-ad3b-c798d6cb53ac)

#### Protting Data

"Plotting Data" is a single dataset containing data that can be visualized using this [notebook](https://colab.research.google.com/drive/1smTpRejBb7c02LiIxMPNVDjOucLAsD81?usp=sharing).  

To generate visualization, simple replace this line:

```python
# Paste link to the dataset here
dataset_url = "https://usegalaxy.org/api/datasets/f9cad7b01a472135a9e7130a8002d909/display?to_ext=tabular"
```

with URL of your dataset, then go to "Runtime" and click "Run all":

![image](https://github.com/user-attachments/assets/528c9233-854e-4871-a6b2-80d38fd2f522)





  


