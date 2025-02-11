# Reading and writing files in Python

First let's download a file we will be using in your notebooks:

```python
!wget https://raw.githubusercontent.com/nekrut/BMMB554/master/2023/data/l9/mt_cds.fa
```

In Python, you can handle files using the built-in `open` function. The `open` function creates a file object, which you can use to read, write, or modify the file.

Here's an example of how to open a file for reading:

```python
f = open("mt_cds.fa", "r")
```

After you've opened the file, you can read its contents using the read method:

```python
contents = f.read()
print(contents)
```

You can also read the file line by line using the readline method:

```python
line = f.readline()
print(line)
```

When you're done reading the file, you should close it using the close method:

```python
f.close()
```

You can also use the `with` statement to automatically close the file when you're done:

```python
with open("mt_cds.fa", "r") as f:
    contents = f.read()
    print(contents)
```

You can also write to files using `write` method (note the "w" mode):

```python
f = open("sample.txt", "w")
f.write("This is a new line.")
f.close()
```

If you open an existing file in write mode, its contents will be overwritten. If you want to append to an existing file instead, you can use the "a" mode:

```python
f = open("sample.txt", "a")
f.write("This is another line.")
f.close()
```

## [Fasta](https://en.wikipedia.org/wiki/FASTA_format)

```python
sequences = {}
with open("mt_cds.fa", "r") as file:
  header = ""
  sequence = ""
  for line in file:
    line=line.rstrip()
    if line.startswith('>'):
      if header != "":
        sequences[header] = sequence
        sequence = ""
      header = line[1:]
    else:
      sequence += line
  if header != "":
    sequences[header] = sequence
```

## [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format)

```python
!wget https://raw.githubusercontent.com/nekrut/BMMB554/master/2023/data/l9/reads.fq
```

```python
def read_fastq(file_path):
    records = []
    with open(file_path, "r") as f:
        while True:
            header = f.readline().strip()
            if header == "":
                break
            sequence = f.readline().strip()
            quality_header = f.readline().strip()
            quality = f.readline().strip()
            records.append((header, sequence, quality))
    return records
```

```python
records = read_fastq("reads.fq")
for header, sequence, quality_header, quality in records:
    print(header)
    print(sequence)
    print(quality_header)
    print(quality)
```

## [SAM](https://en.wikipedia.org/wiki/SAM_(file_format))

```python
!wget https://raw.githubusercontent.com/nekrut/BMMB554/master/2023/data/l9/sam_example.sam
```

```python
def read_sam(file_path):
    records = []
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("@"):
                continue
            fields = line.strip().split("\t")
            records.append(fields)
    return records
```

```python
records = read_sam("sam_example.sam")
for fields in records:
    print(fields)

## SAM/BAM/CRAM trifecta

### SAM (Sequence Alignment/Map) and BAM (Binary Alignment/Map) store sequence alignment data against a reference genome.

#### SAM Format Structure
- **Header** (optional, starts with `@`)
- **Alignment Records** with fields like:
  - Query name
  - Flag
  - Reference name
  - Position
  - Mapping quality
  - CIGAR string
  - Sequence and quality scores

Example SAM entry:
```plaintext
@SQ	SN:chr1	LN:248956422
read1	0	chr1	100	60	50M	*	0	0	ACGTACGT...	IIIIIIII...
```

### BAM Format
BAM is the compressed binary equivalent of SAM.

[BAM Format Specification](https://samtools.github.io/hts-specs/SAMv1.pdf)

### CRAM Format Overview
CRAM is a highly compressed format for storing sequencing alignments. Unlike BAM, which compresses reads independently, CRAM achieves better compression by leveraging an external reference genome.

### Key Differences Between BAM and CRAM
| Feature | BAM | CRAM |
|---------|-----|------|
| Compression | Moderate (Gzip-like) | High (Reference-based) |
| Reference Required for Decoding | No | Yes |
| Storage Space | Larger | Smaller |
| Lossless/Lossy | Always Lossless | Can be Lossless or Lossy |
| Indexing | Required for random access | Required for random access |

### Advantages of CRAM Over BAM
1. **Smaller File Sizes:** CRAM files can be up to 50% smaller than BAM due to reference-based compression.
2. **Better Storage Efficiency:** Useful for large-scale sequencing projects.
3. **Flexible Compression Modes:** Users can choose between lossless and lossy compression.
4. **Faster Transfer Times:** Smaller files reduce data transfer times.

### When to Use BAM vs. CRAM
- Use **BAM** when the reference genome is unavailable or when you need a standalone format.
- Use **CRAM** for efficient storage and archiving of aligned reads when the reference is accessible.

## 5. Compression Comparison: BAM vs. CRAM

### Example Using *E. coli* K12 Genome
Download reference genome:
```sh
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz
gzip -d GCF_000005845.2_ASM584v2_genomic.fna.gz
```

Simulate sequencing reads:
```sh
wgsim -N 100000 -1 150 -2 150 GCF_000005845.2_ASM584v2_genomic.fna reads_1.fastq reads_2.fastq
```

Align to reference:
```sh
bwa index GCF_000005845.2_ASM584v2_genomic.fna
bwa mem GCF_000005845.2_ASM584v2_genomic.fna reads_1.fastq reads_2.fastq | samtools view -bS -o reads.bam
```

Convert to CRAM:
```sh
samtools view -C -T GCF_000005845.2_ASM584v2_genomic.fna -o reads.cram reads.bam
```

Compare file sizes:
```sh
ls -lh reads.bam reads.cram
```
Expected result: CRAM file should be significantly smaller than BAM due to reference-based compression.
