# Lastz and Minimap2

## A bit abouytr lastz


## A bit about minimap

The first step in Minimap2's algorithm is seeding, which involves identifying short, exact matches between the query and the reference sequences. To achieve this efficiently, Minimap2 employs the concept of minimizers.2 A minimizer is defined as the lexicographically smallest k-mer within a window of w consecutive k-mers in a given sequence.11 This method provides a way to sample representative k-mers from the sequences, significantly reducing the number of k-mers that need to be considered for indexing and searching.
Two key parameters govern the minimizer selection process: -k, which sets the length of the k-mer, and -w, which determines the size of the window. These parameters directly influence the density of minimizers extracted from a sequence. A smaller k-mer length or a smaller window size will result in a higher density of minimizers, potentially increasing the sensitivity of the alignment but also increasing the computational cost. Conversely, larger values for these parameters will lead to a sparser set of minimizers, which can improve speed at the expense of potentially missing some matches.
Minimap2 also offers the option to use homopolymer-compressed (HPC) k-mers for indexing, activated by the -H flag. HPC sequences are created by collapsing consecutive identical bases (homopolymers) into a single base. This strategy has been shown to be particularly beneficial for aligning PacBio reads, which are known to have a higher frequency of homopolymer-related errors. By indexing fewer minimizers using HPC compression, Minimap2 can improve overlap sensitivity for these types of reads.
The seeding process begins by extracting minimizers from both the reference genome and the query sequences based on the chosen values for k and w. For the reference genome, these minimizers are then organized into an index using a hash table. In this hash table, each unique minimizer from the reference serves as a key, and its corresponding value is a list of the genomic locations where that minimizer occurs. This indexing step allows for rapid lookup of any minimizer present in a query sequence.
To enhance the specificity of the seeding step and reduce the number of spurious matches, Minimap2 incorporates a filtering mechanism for highly frequent minimizers using the -f option. Minimizers that occur exceedingly often in the reference genome are likely to arise by chance and can lead to a large number of non-informative hits. By setting a threshold, either as a fraction of the total minimizers or as an absolute count, Minimap2 can ignore these overly common minimizers during the subsequent mapping of query sequences, thereby improving the efficiency and accuracy of the alignment process.

### Identifying Potential Mapping Locations (Seeds or Anchors)

Once the reference genome has been indexed, Minimap2 processes each query sequence. For every minimizer identified in the query, the algorithm queries the reference index (the hash table) to find all occurrences of that specific minimizer in the reference. Each match between a minimizer in the query and a minimizer in the reference represents a potential mapping location and is termed a "seed" or "anchor".
Each anchor is essentially a short, exact match between a subsequence of the query and a subsequence of the reference. It can be represented as a 3-tuple (x, y, w), where x and y denote the ending positions of the matching interval on the reference and query sequences, respectively, and w represents the length of the match, which is equal to the k-mer length. These anchors serve as the foundational elements for constructing longer alignments.
Following the identification of all anchors for a given query sequence, Minimap2 sorts these anchors based on their position in the reference genome. This sorting step is crucial for the efficiency of the subsequent chaining process, as it allows the algorithm to consider the relative order and proximity of the matches along the reference sequence.

### Chaining the Seeds (Minihits)

The next phase in the Minimap2 algorithm is chaining, where the individual, short anchors (often referred to as minihits) are connected to form longer, collinear chains. This process utilizes a dynamic programming approach to find the optimal set of anchors that are consistent with a potential alignment between the query and the reference sequences. The goal is to identify a series of anchors that appear in the same relative order and orientation on both the query and the reference, while allowing for gaps and mismatches between them.
The dynamic programming algorithm calculates a "chaining score" for each anchor, which reflects the quality of the chain ending at that anchor. This score is determined by considering the number of matching bases contributed by the anchors in the chain and by applying a penalty for the gaps between consecutive anchors. The gap cost function used in Minimap2 penalizes gaps based on their length, with different penalties for opening and extending a gap. Specifically, a gap of length l incurs a cost defined by a function that considers both the length of the gap and the average seed length.
To improve the computational efficiency of the chaining process, which can have a time complexity of O(N²) in the number of anchors, Minimap2 employs a heuristic to accelerate the dynamic programming calculation. This heuristic involves limiting the number of predecessor anchors considered when extending a chain, effectively reducing the average time complexity to O(hN), where h is a small constant.
After computing the chaining scores for all anchors, a backtracking step is performed to identify the actual chains that yield the highest scores.2 This involves tracing back through the predecessor information stored during the dynamic programming process to reconstruct the sequence of anchors that form the optimal chains.
In scenarios where multiple chains might overlap on the query sequence, particularly in repetitive regions of the genome, Minimap2 distinguishes between primary and secondary chains. The algorithm identifies the highest-scoring chain as the primary alignment. Other chains that overlap significantly with the primary chain on the query are marked as secondary alignments. This distinction is crucial for downstream analyses, as it provides information about the most likely mapping location while also indicating potential alternative mappings. The criteria for determining whether a chain is secondary are based on the extent of its overlap with a higher-scoring chain and the ratio of their chaining scores. Finally, for each primary chain, Minimap2 estimates a mapping quality score, which reflects the confidence in the alignment based on the score of the best secondary chain and the number of anchors in the primary chain.

### Base-Level Alignment

Following the chaining step, Minimap2 performs a more detailed base-level alignment to refine the identified chains of anchors.2 This step aims to fill in the gaps between consecutive anchors within a chain and to extend the alignment from the ends of the chains, ultimately producing a precise alignment that includes information about matches, mismatches, insertions, and deletions, typically represented in the form of a CIGAR string.2
This base-level alignment is also carried out using dynamic programming.2 For aligning genomic DNA, Minimap2 often employs an affine gap cost model, which uses separate penalties for opening a gap and for extending an existing gap.2 This model is biologically more realistic than a simple linear gap cost, as it accounts for the fact that the initiation of a gap is often more costly than extending it. Minimap2 specifically uses a 2-piece affine gap cost function for genomic DNA alignment, applying different gap open and extension costs based on the length of the gap.2
To optimize the speed of this base-level alignment, especially when dealing with very long sequences, Minimap2 utilizes the Suzuki–Kasahara formulation.2 This approach is a difference-based method that overcomes certain limitations associated with traditional implementations of the Smith-Waterman algorithm, allowing for efficient Single Instruction Multiple Data (SIMD) vectorization, regardless of the peak alignment score.2
For aligning spliced sequences, such as mRNA reads, the base-level alignment algorithm in Minimap2 is adapted to account for the presence of introns.2 The gap costs during chaining and the gap cost function used for the dynamic programming alignment are modified to differentiate between insertions and deletions relative to the reference sequence.2 Additionally, Minimap2 incorporates a reference-dependent cost to penalize non-canonical splicing junctions, using a modified dynamic programming equation that considers the presence of canonical splice signals (e.g., GT-AG) and less frequent splice signals in the reference genome.2 In the spliced alignment mode, Minimap2 typically increases the density of minimizers and disables banded alignment, which can make it slower than genomic DNA alignment but improves accuracy in identifying splice junctions.2
3. Input and Output Formats
Minimap2 is designed to be compatible with standard bioinformatics file formats for both input and output. For input, it commonly accepts sequence data in FASTA (.fa,.fna,.fasta) and FASTQ (.fq,.fastq) formats.2 These formats are widely used to store nucleotide sequences, with FASTQ also including quality scores for each base. Minimap2 can process both the reference genome and the query sequences provided in these formats.
The default output format for Minimap2 is PAF (Pairwise mApping Format).5 PAF is a tab-separated text format where each line represents a single alignment between a query and a target sequence. A standard PAF line contains at least 12 mandatory fields, providing essential information about the alignment 18:
Query sequence name: The identifier of the query sequence.
Query sequence length: The total length of the query sequence in bases.
Query start coordinate (0-based): The starting position of the alignment on the query sequence.
Query end coordinate (0-based): The ending position of the alignment on the query sequence.
Strand: Indicates the strand of the query sequence relative to the target sequence ('+' for same strand, '-' for opposite strand).
Target sequence name: The identifier of the target (reference) sequence.
Target sequence length: The total length of the target sequence in bases.
Target start coordinate on the original strand (0-based): The starting position of the alignment on the target sequence.
Target end coordinate on the original strand: The ending position of the alignment on the target sequence.
Number of matching bases in the mapping: The count of identical bases in the aligned region.
Number of bases, including gaps, in the mapping: The total number of bases involved in the alignment, including matches, mismatches, insertions, and deletions.
Mapping quality: A Phred-scaled estimate of the probability that the mapping position of the query sequence is incorrect (values range from 0 to 255, with 255 indicating a missing value).
In addition to PAF, Minimap2 can also output alignments in the more comprehensive SAM (Sequence Alignment/Map) format if the -a option is specified.5 SAM is a widely adopted format in the bioinformatics community that includes a header section with metadata and an alignment section with 11 mandatory fields followed by optional tags providing additional information about the alignment.18 Some important optional tags that Minimap2 might include in the SAM output are: SA (list of other supplementary alignments), ms (DP score of the max scoring segment), NM (number of mismatches and gaps), MD (string for generating the reference sequence in the alignment), and CIGAR string (representing the alignment operations).18 In PAF format, the CIGAR string can be included in a custom tag cg when the -c option is used.18
Table 1: Key Fields in PAF and SAM Formats
Field Name (PAF)
Description (PAF)
Corresponding Field(s) (SAM)
Description (SAM)
Query sequence name
Identifier of the query sequence
QNAME
Query template name
Query sequence length
Total length of the query sequence
TLEN
Template length (sum of segment lengths)
Query start coordinate (0-based)
Start position of the alignment on the query
POS
1-based leftmost mapping position on the reference sequence
Query end coordinate (0-based)
End position of the alignment on the query
POS + length of alignment
Implied by POS and CIGAR
Strand
Strand of the query relative to the target ('+' or '-')
FLAG (bit 4)
Bitwise flag indicating various alignment properties, including strand (read reverse complemented)
Target sequence name
Identifier of the target (reference) sequence
RNAME
Reference sequence name
Target sequence length
Total length of the target sequence
RNEXT (if unmapped '*')
Reference name of the mate/next read
Target start coordinate (0-based)
Start position of the alignment on the target
POS
1-based leftmost mapping position on the reference sequence
Target end coordinate on the original strand
End position of the alignment on the target
POS + length of alignment
Implied by POS and CIGAR
Number of matching bases in the mapping
Count of identical bases in the aligned region
CIGAR (M operators)
String representing the alignment operations (e.g., M for match/mismatch)
Number of bases, including gaps, in the mapping
Total bases in the alignment (matches, mismatches, insertions, deletions)
CIGAR (sum of lengths)
Total length of the alignment as indicated by the CIGAR string
Mapping quality
Phred-scaled probability of incorrect mapping (0-255)
MAPQ
Mapping quality (Phred-scaled confidence score)

4. Key Features and Advantages of Minimap2
Minimap2 boasts several key features and advantages that have contributed to its widespread adoption in the bioinformatics community.2 One of its most notable strengths is its exceptional speed, particularly when aligning long reads. It has been reported to be significantly faster than many other mainstream aligners, often achieving speedups of 3-4 times compared to short-read mappers and 30 times or more compared to other long-read aligners.2 This speed advantage is crucial for handling the large volumes of data produced by modern sequencing technologies within a reasonable timeframe.
In addition to its speed, Minimap2 also offers high accuracy across a variety of sequencing data types.2 It performs well with accurate short reads, long reads with error rates up to 15%, full-length noisy RNA or cDNA reads, and assembly contigs. Its accuracy in splicing alignment, a critical aspect for RNA-seq analysis, is also noteworthy.2
Minimap2 is particularly adept at handling the noisy long reads generated by technologies like Oxford Nanopore, which often have higher error rates compared to short reads.2 Its algorithm, especially the seeding and chaining steps, is designed to be robust to these errors, allowing for accurate mapping of even highly error-prone reads.
The aligner also supports split-read alignment, a fundamental requirement for analyzing RNA sequencing data where reads may span exon-intron junctions.2 This capability allows Minimap2 to accurately align transcripts to a reference genome, identifying splice sites and enabling the study of gene expression and transcript isoforms.
While performance can be influenced by specific parameters and data characteristics, Minimap2 is generally considered to be memory-efficient, making it suitable for use on standard computing infrastructure.5 It can handle large genomes and read datasets without requiring excessive computational resources.
Furthermore, Minimap2 is a versatile tool capable of performing various types of alignments beyond simple read mapping. It can be used for finding overlaps between long reads, which is a crucial step in de novo genome assembly.2 It can also be used to align a complete genome assembly to a reference genome, facilitating comparative genomics studies.2 This flexibility makes Minimap2 an invaluable tool in a wide range of bioinformatics applications.
5. Important Parameters and Options
Minimap2 offers a wide array of parameters and options that allow users to fine-tune its behavior for specific data types and analysis goals.18 These options can be broadly categorized into those affecting indexing, mapping, alignment, input/output, and presets.
Indexing Options: Key parameters include -k (k-mer length), which influences sensitivity; -w (window size), which affects minimizer density; -I (index batch size), important for memory management; -d (index output file), for saving the index; and -H (use HPC minimizers), beneficial for PacBio data.18
Mapping Options: Important parameters in this category are -f (filter frequent minimizers), which helps with repetitive regions; -U (k-mer occurrence bounds), for finer control over filtering; -g (chain elongation gap), controlling the gap between anchors; -r (chaining/alignment bandwidth), affecting gap sizes; -n (minimum minimizers in a chain) and -m (minimum chaining score), for filtering short/low-quality chains; -p (secondary-to-primary score ratio) and -N (max secondary alignments), controlling secondary alignments; -G (max reference gap for splicing); and the --splice and --sr flags for enabling specific alignment modes.18
Alignment Options: These parameters govern the scoring of matches, mismatches, and gaps during the base-level alignment. Key options include -A (match score), -B (mismatch penalty), -O (gap open penalty), -E (gap extension penalty), -J (splice model), -C (non-canonical splice cost), -z (Z-dropoff value for alignment termination), and -s (minimum alignment score to output).18
Input/Output Options: Essential parameters here include -a (output in SAM format), -o (output file), -Q (ignore base quality), -L (long CIGAR for compatibility), -R (SAM read group), -c (output CIGAR in PAF), --cs (output difference string), --MD (output MD tag in SAM), -t (number of threads), and -K (mini-batch size for processing).18
Preset Options: Minimap2 provides several presets via the -x option, which automatically adjust multiple parameters for common use cases.18 These include map-ont and map-pb for mapping noisy long reads (ONT and PacBio, respectively), map-hifi for accurate PacBio HiFi reads, splice for long-read spliced alignment, sr for short-read alignment, asm5 for assembly-to-reference mapping (low divergence), and ava-pb and ava-ont for all-vs-all overlap mapping of PacBio and ONT reads.18 These presets offer a convenient starting point for many analyses.
Table 2: Key Minimap2 Parameters and Their Effects
Parameter
Default Value
Description
Effect on Alignment Process
-k
15
Minimizer k-mer length
Smaller values increase sensitivity but may decrease speed.
-w
10
Minimizer window size
Larger values result in fewer minimizers (lower density), potentially increasing speed but decreasing sensitivity.
-f
0.0002
Filter out top fraction of frequent minimizers
Helps to reduce spurious matches, especially in repetitive regions.
-g
10k
Stop chain elongation if no minimizers within NUM bp
Controls the maximum gap allowed between consecutive anchors in a chain.
-r
500,20k
Bandwidth for chaining and base alignment
Affects the maximum gap size considered during chaining and alignment.
-p
0.8
Minimal secondary-to-primary score ratio to output secondary mappings
Determines how similar a secondary alignment must be to the primary alignment to be reported.
-N
5
Outputs at most INT secondary alignments
Limits the number of alternative alignments reported for a query sequence.
-a
PAF (default)
Output in SAM format
Changes the output format from the default PAF to the more widely used SAM format.
-t
3 (indexing)
Number of threads to use
Increases processing speed by utilizing multiple CPU cores.
-x
(none)
Apply a preset of options (e.g., map-ont, splice, sr)
Simplifies parameter setting by applying pre-optimized configurations for specific data types and analysis tasks.

6. Conclusion
In summary, Minimap2 is a powerful and versatile sequence alignment program that has become a cornerstone of modern bioinformatics, particularly with the rise of long-read sequencing technologies. Its efficient seed-chain-align algorithm, based on the concept of minimizers, allows for rapid and accurate mapping of various types of nucleotide sequences against large reference databases.5 The program's speed, accuracy, ability to handle noisy long reads, and support for split-read alignment make it an indispensable tool for a wide range of applications in genomics and transcriptomics. While generally robust, it is worth noting potential limitations such as possible suboptimal alignments in long low-complexity regions or the occasional missing of small exons.5 Furthermore, earlier versions had some issues with repetitive regions, which have been addressed in subsequent updates.30 Overall, Minimap2's performance and flexibility have established it as a significant contributor to the efficiency and accuracy of bioinformatics analysis pipelines.
Works cited
Minimap2: pairwise alignment for nucleotide sequences - PubMed, accessed April 8, 2025, https://pubmed.ncbi.nlm.nih.gov/29750242/
Minimap2: pairwise alignment for nucleotide sequences | Bioinformatics - Oxford Academic, accessed April 8, 2025, https://academic.oup.com/bioinformatics/article/34/18/3094/4994778
Minimap2: Pairwise alignment for nucleotide sequences - ResearchGate, accessed April 8, 2025, https://www.researchgate.net/publication/325106640_Minimap2_Pairwise_alignment_for_nucleotide_sequences
Minimap2: pairwise alignment for nucleotide sequences - Oxford Nanopore Technologies, accessed April 8, 2025, https://nanoporetech.com/resource-centre/minimap2-pairwise-alignment-nucleotide-sequences
lh3/minimap2: A versatile pairwise aligner for genomic and spliced nucleotide sequences - GitHub, accessed April 8, 2025, https://github.com/lh3/minimap2
Minimap2: pairwise alignment for nucleotide sequences - PMC, accessed April 8, 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC6137996/
Accelerating Minimap2 for Accurate Long Read Alignment on GPUs - ResearchGate, accessed April 8, 2025, https://www.researchgate.net/publication/367338181_Accelerating_Minimap2_for_Accurate_Long_Read_Alignment_on_GPUs
Accelerating Minimap2 for accurate long read alignment on GPUs - bioRxiv, accessed April 8, 2025, https://www.biorxiv.org/content/10.1101/2022.03.09.483575v4.full.pdf
Accelerating minimap2 for long-read sequencing applications on modern CPUs - Department of Computational and Data Sciences, accessed April 8, 2025, http://cds.iisc.ac.in/faculty/chirag/pubs/2022_kalikar_mm2fast.pdf
Long-Read Alignment - OmicsBox User Manual - BioBam, accessed April 8, 2025, https://docs.omicsbox.biobam.com/latest/Long-Read-Alignment/
Common Alignment Tools. A small summary of common alignment… | by Anuradha Wickramarachchi | The Computational Biology Magazine | Medium, accessed April 8, 2025, https://medium.com/computational-biology/common-alignment-tools-25e283290ae4
(PDF) When less is more: sketching with minimizers in genomics - ResearchGate, accessed April 8, 2025, https://www.researchgate.net/publication/384898331_When_less_is_more_sketching_with_minimizers_in_genomics
Improved design and analysis of practical minimizers | Bioinformatics - Oxford Academic, accessed April 8, 2025, https://academic.oup.com/bioinformatics/article/36/Supplement_1/i119/5870484
Sequence-specific minimizers via polar sets | Bioinformatics - Oxford Academic, accessed April 8, 2025, https://academic.oup.com/bioinformatics/article/37/Supplement_1/i187/6319665
Lecture 1: Minimizers, accessed April 8, 2025, https://www.cs.helsinki.fi/group/gsa/book/teaching/aga2023_lecture1-minimizers.pdf
Application of minimizers in read alignment. A typical read aligner... - ResearchGate, accessed April 8, 2025, https://www.researchgate.net/figure/Application-of-minimizers-in-read-alignment-A-typical-read-aligner-that-follows-the_fig4_384898331
Creating and Using Minimizer Sketches in Computational Genomics - PMC, accessed April 8, 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC11082048/
Manual Reference Pages - minimap2 (1), accessed April 8, 2025, https://lh3.github.io/minimap2/minimap2.html
minimap2 2.26 - CQLS Software Update List, accessed April 8, 2025, https://software.cqls.oregonstate.edu/updates/minimap2-2.26/
Adapting the GACT-X Aligner to Accelerate Minimap2 in an FPGA Cloud Instance - MDPI, accessed April 8, 2025, https://www.mdpi.com/2076-3417/13/7/4385
Minimap2 - Docs CSC, accessed April 8, 2025, https://docs.csc.fi/apps/minimap2/
Minimap2 Tutorial - How To Use tiny intern, accessed April 8, 2025, https://docs.tinybio.cloud/docs/minimap2-tutorial
minimap2 - NVIDIA Docs, accessed April 8, 2025, https://docs.nvidia.com/clara/parabricks/4.3.2/documentation/tooldocs/man_minimap2.html
Description of file formats used in D-Genies - INRAE, accessed April 8, 2025, https://dgenies.toulouse.inra.fr/documentation/formats
Feature request: SAM input · Issue #870 · lh3/minimap2 - GitHub, accessed April 8, 2025, https://github.com/lh3/minimap2/issues/870
Figure 1 from Minimap2: pairwise alignment for nucleotide sequences | Semantic Scholar, accessed April 8, 2025, https://www.semanticscholar.org/paper/Minimap2%3A-pairwise-alignment-for-nucleotide-Li/a47483dca56d93dabc54c8d49a5d03c6fb1e9771/figure/0
Accurate spliced alignment of long RNA sequencing reads - Oxford Academic, accessed April 8, 2025, https://academic.oup.com/bioinformatics/article/37/24/4643/6327681
Minimap2 transcriptome mapping - Jan's Blog of Bioinformatics Bits, accessed April 8, 2025, https://janbio.home.blog/2020/07/14/minimap2-transcriptome-mapping/
Genome Assembly with Minimap2 and Miniasm | Long-Read, long reach Bioinformatics Tutorials - GitHub Pages, accessed April 8, 2025, https://timkahlke.github.io/LongRead_tutorials/ASS_M.html
New strategies to improve minimap2 alignment accuracy - PMC, accessed April 8, 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC8652018/
