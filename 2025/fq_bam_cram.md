# Class Notes: FASTQ, SAM/BAM, and CRAM Formats

## 1. FASTQ Format

FASTQ is a text-based format for storing biological sequence data along with associated quality scores.

### FASTQ Structure
Each record consists of four lines:
1. **Sequence Identifier** (starts with `@`)
2. **Nucleotide Sequence**
3. **Quality Score Identifier** (starts with `+`)
4. **Quality Scores** (ASCII-encoded Phred scores)

Example:
```plaintext
@SEQ_ID
GATTTGGGGTTTCCCAGTCACGAC
+
!''*((((***+))%%%++)(%%%%).1
```

### Handling FASTQ Files with `samtools`
Although `samtools` is mainly for BAM/CRAM handling, it can be used to convert FASTQ to SAM:
```sh
samtools import reference.fasta reads.fastq reads.sam
```
Alternatively, `seqtk` can be used for FASTQ manipulation:
```sh
seqtk seq -A reads.fastq > reads.fasta
```

#### Real Example with Small Files
Create a small FASTQ file:
```sh
echo -e "@read1\nACGTACGTACGT\n+\nIIIIIIIIIIII" > small.fastq
```
Convert FASTQ to SAM:
```sh
samtools import reference.fasta small.fastq small.sam
```

---

## 2. SAM/BAM Format

SAM (Sequence Alignment/Map) and BAM (Binary Alignment/Map) store sequence alignment data against a reference genome.

### SAM Format Structure
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

### Handling BAM Files with `samtools`
#### Convert SAM to BAM
```sh
samtools view -b -o reads.bam reads.sam
```
#### Sort BAM
```sh
samtools sort -o reads.sorted.bam reads.bam
```
#### Index BAM
```sh
samtools index reads.sorted.bam
```
#### View BAM Content
```sh
samtools view reads.sorted.bam | head -10
```

#### Real Example with Small Files
Create a small SAM file:
```sh
echo -e "@SQ\tSN:chr1\tLN:1000\nread1\t0\tchr1\t100\t60\t10M\t*\t0\t0\tACGTACGTAC\tIIIIIIIIII" > small.sam
```
Convert to BAM:
```sh
samtools view -b -o small.bam small.sam
```
Sort and index BAM:
```sh
samtools sort -o small.sorted.bam small.bam
samtools index small.sorted.bam
```

---

## 3. BAM vs. CRAM: Comparison and Advantages

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

---

## 4. CRAM Format

[CRAM Format Specification](https://samtools.github.io/hts-specs/CRAMv3.pdf)

### Handling CRAM Files with `samtools`
#### Convert BAM to CRAM
```sh
samtools view -C -T reference.fasta -o reads.cram reads.bam
```
#### Convert CRAM to BAM
```sh
samtools view -b -o reads.bam reads.cram
```
#### View CRAM Content
```sh
samtools view reads.cram | head -10
```
#### Index CRAM
```sh
samtools index reads.cram
```

#### Real Example with Small Files
Convert BAM to CRAM:
```sh
samtools view -C -T reference.fasta -o small.cram small.bam
```
View CRAM content:
```sh
samtools view small.cram
```

---

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
