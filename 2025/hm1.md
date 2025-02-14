# Home work 1
Feb 14 - Feb 20, 2025

## What do you need to do?

You need to repeat analysis of SRA accessions for your organism of intereset. Do do this follow these steps:

### Run through the example

1. Go to "[Pandas + Altair](https://colab.research.google.com/github/nekrut/BMMB554/blob/master/notebooks/pandas.ipynb#scrollTo=390d708a-156d-43bf-845c-014612abb8e4)" cell on the notebook from the previous class.
2. Run through it to understand how it works.

### Think of which organism you want to do analsys with

The organism choice is really up to you but you need to know `taxId` of your organism. To get `taxId`:

To retrieve the NCBI TaxID for the Somali wild ass using the NCBI Taxonomy website, follow these steps:

1. **Access the NCBI Taxonomy Browser:**  
   Open your web browser and navigate to the [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi).

2. **Enter the Organism's Name:**  
   In the search box, type the scientific name of the Somali wild ass, for example,  
   ```
   Equus africanus somaliensis
   ```
   or simply “Somali wild ass”.

3. **Submit Your Search:**  
   Press the “Search” button or hit Enter to submit your query.

4. **Review the Search Results:**  
   The search results will display entries that match your query. Look for the entry corresponding to the Somali wild ass.

5. **Locate the TaxID:**  
   Click on the relevant entry. On the detail page, you will see the organism’s information, including the NCBI Taxonomy ID (TaxID). For the Somali wild ass, the TaxID is typically listed as **9838**.

By following these steps, you can easily find the NCBI TaxID for the Somali wild ass or any other organism.

### Retrieve a list of SRA datasets for this organism

You can retrieve SRA accessions for an organism using its TaxID by following these steps on the NCBI SRA website:

1. **Go to the NCBI SRA Website:**  
   Open your web browser and navigate to the [NCBI SRA homepage](https://www.ncbi.nlm.nih.gov/sra).

2. **Enter the TaxID Query:**  
   In the search bar, type a query that specifies the TaxID. The typical format is:
   ```
   txid[TAXID][Organism]
   ```
   For example, if you're interested in the Somali wild ass (TaxID 9838), you would enter:
   ```
   txid9838[Organism]
   ```

3. **Execute the Search:**  
   Press Enter or click the search icon. This will return a list of SRA records (studies, experiments, runs, etc.) associated with the specified TaxID.

4. **Review the Results:**  
   The results page will display various SRA records. You’ll see accession numbers such as SRP (study), SRX (experiment), and SRR (run). These are the accessions related to your organism.

5. **Download list of SRA accessions and associated metadata:**
   Click "Send to:" and choose "File" and "RunInfo" as Format:
   ![image](https://github.com/user-attachments/assets/a672336e-a184-4f0e-ad0b-a5acc281d11c)
   Click "Create file"

   This will download a csv file that you need to analyze. It should look like this:

``` Run,ReleaseDate,LoadDate,spots,bases,spots_with_mates,avgLength,size_MB,AssemblyName,download_path,Experiment,LibraryName,LibraryStrategy,LibrarySelection,LibrarySource,LibraryLayout,InsertSize,InsertDev,Platform,Model,SRAStudy,BioProject,Study_Pubmed_id,ProjectID,Sample,BioSample,SampleType,TaxID,ScientificName,SampleName,g1k_pop_code,source,g1k_analysis_group,Subject_ID,Sex,Disease,Tumor,Affection_Status,Analyte_Type,Histological_Type,Body_Site,CenterName,Submission,dbgap_study_accession,Consent,RunHash,ReadHash
ERR6892499,2021-12-19 22:35:26,,0,0,0,0,0,,,ERX6515857,unspecified,WGS,unspecified,GENOMIC,PAIRED,271,0,ILLUMINA,HiSeq X Ten,ERP131944,PRJEB47650,,791274,ERS7664783,SAMEA9986517,simple,9838,Camelus dromedarius,19,,,,,,,no,,,,,HUSSAIN,ERA6520238,,public,,
ERR6892494,2021-12-19 22:35:26,,0,0,0,0,0,,,ERX6515852,unspecified,WGS,unspecified,GENOMIC,PAIRED,271,0,ILLUMINA,HiSeq X Ten,ERP131944,PRJEB47650,,791274,ERS7664778,SAMEA9986512,simple,9838,Camelus dromedarius,2,,,,,,,no,,,,,HUSSAIN,ERA6520238,,public,,
```

### Use notebook to analyze this file using 

Analyze this datasert as described in [Pandas + Altair](https://colab.research.google.com/github/nekrut/BMMB554/blob/master/notebooks/pandas.ipynb#scrollTo=390d708a-156d-43bf-845c-014612abb8e4). For this simply replace the filke in [this cell](https://colab.research.google.com/github/nekrut/BMMB554/blob/master/notebooks/pandas.ipynb#scrollTo=aed2724a-99a8-4f83-8f22-125808852ae3&line=2&uniqifier=1) using your new file. Of coursem, you will need to change settings appropriately.

## How to submit it?

Use [this form](https://forms.gle/qDJvn3FDcrb9e1r67) to submit a link to your colab notebook. ⚠️ You need to be logged into Google with **your psu account** to us e this form.





 
