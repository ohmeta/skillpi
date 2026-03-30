#!/usr/bin/env python3
"""
Deep enrichment of ALL tool docs:
- Add official documentation links
- Add tutorial/getting-started links
- Add paper references
- Add related tools section
- Improve descriptions
"""

import json
import re
from pathlib import Path

# Official docs, tutorials, papers for each tool
TOOL_REFERENCES = {
    "metaphlan-4": {
        "official_docs": "https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4",
        "tutorial": "https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4#quick-start",
        "paper": "Blanco-Míguez et al. (2023) Extending and improving metagenomic taxonomic profiling with uncharacterized species using MetaPhlAn 4. *Nature Biotechnology*. DOI: [10.1038/s41587-023-01688-w](https://doi.org/10.1038/s41587-023-01688-w)",
        "related": ["HUMAnN 3", "StrainPhlAn", "Kraken 2"],
    },
    "humann-3": {
        "official_docs": "https://github.com/biobakery/humann/wiki",
        "tutorial": "https://github.com/biobakery/humann/wiki/HUMAnN-User-Guide",
        "paper": "Beghini et al. (2021) Integrating taxonomic, functional, and strain-level profiling of diverse microbial communities with bioBakery 3. *eLife*. DOI: [10.7554/eLife.65088](https://doi.org/10.7554/eLife.65088)",
        "related": ["MetaPhlAn 4", "StrainPhlAn", "LEfSe"],
    },
    "qiime2-amplicon": {
        "official_docs": "https://docs.qiime2.org/",
        "tutorial": "https://docs.qiime2.org/2024.5/tutorials/overview/",
        "paper": "Bolyen et al. (2019) Reproducible, interactive, scalable and extensible microbiome data science using QIIME 2. *Nature Biotechnology*. DOI: [10.1038/s41587-019-0209-9](https://doi.org/10.1038/s41587-019-0209-9)",
        "related": ["DADA2", "mothur", "phyloseq"],
    },
    "dada2-pipeline": {
        "official_docs": "https://benjjneb.github.io/dada2/",
        "tutorial": "https://benjjneb.github.io/dada2/tutorial.html",
        "paper": "Callahan et al. (2016) DADA2: High-resolution sample inference from Illumina amplicon data. *Nature Methods*. DOI: [10.1038/nmeth.3869](https://doi.org/10.1038/nmeth.3869)",
        "related": ["QIIME 2", "DEBLUR", "UNOISE3"],
    },
    "mothur": {
        "official_docs": "https://mothur.org/wiki/",
        "tutorial": "https://mothur.org/wiki/miseq_sop/",
        "paper": "Schloss et al. (2009) Introducing mothur: Open-Source, Platform-Independent, Community-Supported Software for Describing and Comparing Microbial Communities. *Applied and Environmental Microbiology*. DOI: [10.1128/AEM.01541-09](https://doi.org/10.1128/AEM.01541-09)",
        "related": ["QIIME 2", "DADA2", "phyloseq"],
    },
    "fastp": {
        "official_docs": "https://github.com/OpenGene/fastp",
        "tutorial": "https://github.com/OpenGene/fastp#all-options",
        "paper": "Chen et al. (2018) fastp: an ultra-fast all-in-one FASTQ preprocessor. *Bioinformatics*. DOI: [10.1093/bioinformatics/bty560](https://doi.org/10.1093/bioinformatics/bty560)",
        "related": ["Trimmomatic", "Cutadapt", "BBDuk"],
    },
    "megahit": {
        "official_docs": "https://github.com/voutcn/megahit/wiki",
        "tutorial": "https://github.com/voutcn/megahit/wiki",
        "paper": "Li et al. (2015) MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph. *Bioinformatics*. DOI: [10.1093/bioinformatics/btv033](https://doi.org/10.1093/bioinformatics/btv033)",
        "related": ["metaSPAdes", "Flye", "Canu"],
    },
    "kraken2": {
        "official_docs": "https://github.com/DerrickWood/kraken2/wiki",
        "tutorial": "https://github.com/DerrickWood/kraken2/wiki/Manual",
        "paper": "Wood et al. (2019) Improved metagenomic analysis with Kraken 2. *Genome Biology*. DOI: [10.1186/s13059-019-1891-0](https://doi.org/10.1186/s13059-019-1891-0)",
        "related": ["Bracken", "MetaPhlAn 4", "Centrifuge"],
    },
    "bracken": {
        "official_docs": "https://github.com/jenniferlu717/Bracken",
        "tutorial": "https://ccb.jhu.edu/software/bracken/index.shtml?t=manual",
        "paper": "Lu et al. (2017) Bracken: estimating species abundance in metagenomics data. *PeerJ Computer Science*. DOI: [10.7717/peerj-cs.104](https://doi.org/10.7717/peerj-cs.104)",
        "related": ["Kraken 2", "MetaPhlAn 4"],
    },
    "centrifuge": {
        "official_docs": "https://github.com/DaehwanKimLab/centrifuge",
        "tutorial": "https://ccb.jhu.edu/software/centrifuge/manual.shtml",
        "paper": "Kim et al. (2016) Centrifuge: rapid and sensitive classification of metagenomic sequences. *Genome Research*. DOI: [10.1101/gr.210641.116](https://doi.org/10.1101/gr.210641.116)",
        "related": ["Kraken 2", "Kaiju", "MetaPhlAn 4"],
    },
    "kaiju": {
        "official_docs": "https://github.com/bioinformatics-centre/kaiju",
        "tutorial": "https://kaiju.binf.ku.dk/tutorial",
        "paper": "Menzel et al. (2016) Fast and sensitive taxonomic classification for metagenomics with Kaiju. *Nature Communications*. DOI: [10.1038/ncomms11257](https://doi.org/10.1038/ncomms11257)",
        "related": ["Kraken 2", "Centrifuge", "MetaPhlAn 4"],
    },
    "metaspades": {
        "official_docs": "https://github.com/ablab/spades#metaspades",
        "tutorial": "https://github.com/ablab/spades/blob/spades_3.15.5/metaspades/README.md",
        "paper": "Nurk et al. (2017) metaSPAdes: a new versatile metagenomic assembler. *Genome Research*. DOI: [10.1101/gr.213959.116](https://doi.org/10.1101/gr.213959.116)",
        "related": ["MEGAHIT", "Flye", "Unicycler"],
    },
    "flye": {
        "official_docs": "https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md",
        "tutorial": "https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md",
        "paper": "Kolmogorov et al. (2019) Assembly of long, error-prone reads using repeat graphs. *Nature Biotechnology*. DOI: [10.1038/s41587-019-0072-8](https://doi.org/10.1038/s41587-019-0072-8)",
        "related": ["Canu", "MEGAHIT", "metaSPAdes"],
    },
    "canu": {
        "official_docs": "https://github.com/marbl/canu",
        "tutorial": "https://canu.readthedocs.io/en/latest/",
        "paper": "Koren et al. (2017) Canu: scalable and accurate long-read assembly via adaptive k-mer weighting and repeat separation. *Genome Research*. DOI: [10.1101/gr.215087.116](https://doi.org/10.1101/gr.215087.116)",
        "related": ["Flye", "metaSPAdes"],
    },
    "unicycler": {
        "official_docs": "https://github.com/rrwick/Unicycler",
        "tutorial": "https://github.com/rrwick/Unicycler#usage",
        "paper": "Wick et al. (2017) Unicycler: Resolving bacterial genome assemblies from short and long sequencing reads. *PLOS Computational Biology*. DOI: [10.1371/journal.pcbi.1005595](https://doi.org/10.1371/journal.pcbi.1005595)",
        "related": ["Flye", "metaSPAdes", "MEGAHIT"],
    },
    "metabat2": {
        "official_docs": "https://github.com/BinPro/MetaBAT2/wiki",
        "tutorial": "https://bitbucket.org/berkeleylab/metabat/src/master/",
        "paper": "Kang et al. (2019) MetaBAT 2: an adaptive binning algorithm for robust and efficient genome reconstruction from metagenome assemblies. *PeerJ*. DOI: [10.7717/peerj.7359](https://doi.org/10.7717/peerj.7359)",
        "related": ["MaxBin 2", "CONCOCT", "DAS Tool", "CheckM2"],
    },
    "maxbin2": {
        "official_docs": "https://github.com/kylebittinger/maxbin2",
        "tutorial": "https://sourceforge.net/projects/maxbin2/files/",
        "paper": "Wu et al. (2015) MaxBin 2.0: an automated binning algorithm to recover genomes from multiple metagenomic datasets. *Bioinformatics*. DOI: [10.1093/bioinformatics/btv638](https://doi.org/10.1093/bioinformatics/btv638)",
        "related": ["MetaBAT 2", "CONCOCT", "DAS Tool"],
    },
    "concoct": {
        "official_docs": "https://github.com/BinPro/CONCOCT",
        "tutorial": "https://concoct.readthedocs.io/en/latest/",
        "paper": "Alneberg et al. (2014) Binning metagenomic contigs by coverage and composition. *Nature Methods*. DOI: [10.1038/nmeth.2835](https://doi.org/10.1038/nmeth.2835)",
        "related": ["MetaBAT 2", "MaxBin 2", "DAS Tool"],
    },
    "das_tool": {
        "official_docs": "https://github.com/cmks/DAS_Tool",
        "tutorial": "https://github.com/cmks/DAS_Tool#usage",
        "paper": "Sieber et al. (2018) Recovery of genomes from metagenomes via a dereplication, aggregation and scoring strategy. *Nature Microbiology*. DOI: [10.1038/s41564-018-0171-1](https://doi.org/10.1038/s41564-018-0171-1)",
        "related": ["MetaBAT 2", "MaxBin 2", "CONCOCT", "CheckM2"],
    },
    "checkm2": {
        "official_docs": "https://github.com/chklovski/CheckM2",
        "tutorial": "https://github.com/chklovski/CheckM2/wiki",
        "paper": "Chklovski et al. (2023) CheckM2: a rapid, scalable and accurate tool for assessing microbial genome quality using machine learning. *Nature Methods*. DOI: [10.1038/s41592-023-01940-w](https://doi.org/10.1038/s41592-023-01940-w)",
        "related": ["CheckM", "MetaBAT 2", "GTDB-Tk"],
    },
    "gtdb_tk": {
        "official_docs": "https://github.com/Ecogenomics/GTDBTk",
        "tutorial": "https://ecogenomics.github.io/GTDBTk/commands/classify_wf.html",
        "paper": "Chaumeil et al. (2022) GTDB-Tk v2: memory friendly classification with the Genome Taxonomy Database. *Bioinformatics*. DOI: [10.1093/bioinformatics/btac672](https://doi.org/10.1093/bioinformatics/btac672)",
        "related": ["CheckM2", "MetaBAT 2", "anvi'o"],
    },
    "strainphlan": {
        "official_docs": "https://github.com/biobakery/MetaPhlAn/wiki/StrainPhlAn-4",
        "tutorial": "https://github.com/biobakery/MetaPhlAn/wiki/StrainPhlAn-4",
        "paper": "Truong et al. (2015) MetaPhlAn2 for enhanced metagenomic taxonomic profiling. *Nature Methods*. DOI: [10.1038/nmeth.3589](https://doi.org/10.1038/nmeth.3589)",
        "related": ["MetaPhlAn 4", "inStrain"],
    },
    "instrain": {
        "official_docs": "https://github.com/MrOlm/inStrain",
        "tutorial": "https://instrain.readthedocs.io/en/latest/",
        "paper": "Olm et al. (2021) inStrain profiles population microdiversity from metagenomic data and sensitively detects shared microbial strains. *Nature Biotechnology*. DOI: [10.1038/s41587-020-00797-0](https://doi.org/10.1038/s41587-020-00797-0)",
        "related": ["StrainPhlAn", "MetaPhlAn 4"],
    },
    "eggnog_mapper": {
        "official_docs": "https://github.com/eggnogdb/eggnog-mapper/wiki",
        "tutorial": "https://github.com/eggnogdb/eggnog-mapper/wiki",
        "paper": "Cantalapiedra et al. (2021) eggNOG-mapper v2: functional annotation of genomes using eggNOG orthologs. *Molecular Biology and Evolution*. DOI: [10.1093/molbev/msab293](https://doi.org/10.1093/molbev/msab293)",
        "related": ["Prokka", "Bakta", "DRAM"],
    },
    "prokka": {
        "official_docs": "https://github.com/tseemann/prokka",
        "tutorial": "https://github.com/tseemann/prokka#usage",
        "paper": "Seemann (2014) Prokka: rapid prokaryotic genome annotation. *Bioinformatics*. DOI: [10.1093/bioinformatics/btu153](https://doi.org/10.1093/bioinformatics/btu153)",
        "related": ["Bakta", "eggNOG-mapper", "DRAM"],
    },
    "bakta": {
        "official_docs": "https://github.com/oschwengers/bakta",
        "tutorial": "https://github.com/oschwengers/bakta#usage",
        "paper": "Schwengers et al. (2021) Bakta: rapid and standardized annotation of bacterial genomes. *Microbial Genomics*. DOI: [10.1099/mgen.0.000685](https://doi.org/10.1099/mgen.0.000685)",
        "related": ["Prokka", "eggNOG-mapper", "DRAM"],
    },
    "antismash": {
        "official_docs": "https://docs.antismash.secondarymetabolites.org/",
        "tutorial": "https://docs.antismash.secondarymetabolites.org/getting_started/",
        "paper": "Blin et al. (2021) antiSMASH 6.0: improving cluster detection and comparison capabilities. *Nucleic Acids Research*. DOI: [10.1093/nar/gkab335](https://doi.org/10.1093/nar/gkab335)",
        "related": ["PRISM", "BiG-SCAPE", "Prokka"],
    },
    "dram": {
        "official_docs": "https://github.com/WrightonLabCSU/DRAM",
        "tutorial": "https://github.com/WrightonLabCSU/DRAM/wiki",
        "paper": "Shaffer et al. (2020) DRAM for distilling microbial metabolism to automate the curation of microbiome function. *Nucleic Acids Research*. DOI: [10.1093/nar/gkaa621](https://doi.org/10.1093/nar/gkaa621)",
        "related": ["eggNOG-mapper", "Prokka", "Bakta"],
    },
    "bowtie2": {
        "official_docs": "http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml",
        "tutorial": "http://bowtie-bio.sourceforge.net/bowtie2/index.shtml",
        "paper": "Langmead & Salzberg (2012) Fast gapped-read alignment with Bowtie 2. *Nature Methods*. DOI: [10.1038/nmeth.1923](https://doi.org/10.1038/nmeth.1923)",
        "related": ["BWA-MEM2", "minimap2", "HISAT2"],
    },
    "minimap2": {
        "official_docs": "https://github.com/lh3/minimap2",
        "tutorial": "https://github.com/lh3/minimap2#usage",
        "paper": "Li (2018) Minimap2: pairwise alignment for nucleotide sequences. *Bioinformatics*. DOI: [10.1093/bioinformatics/bty191](https://doi.org/10.1093/bioinformatics/bty191)",
        "related": ["Bowtie 2", "BWA-MEM2", "NGMLR"],
    },
    "bwa_mem2": {
        "official_docs": "https://github.com/bwa-mem2/bwa-mem2",
        "tutorial": "https://github.com/bwa-mem2/bwa-mem2#usage",
        "paper": "Vasimuddin et al. (2019) Efficient Architecture-Aware Acceleration of BWA-MEM for Multicore Systems. *IEEE IPDPS*. DOI: [10.1109/IPDPS.2019.00041](https://doi.org/10.1109/IPDPS.2019.00041)",
        "related": ["Bowtie 2", "minimap2"],
    },
    "anvio": {
        "official_docs": "https://anvio.org/",
        "tutorial": "https://merenlab.org/2016/06/22/anvio-tutorial-v2/",
        "paper": "Eren et al. (2021) Community-led, integrated, reproducible multi-omics with anvi'o. *Nature Microbiology*. DOI: [10.1038/s41564-020-00743-5](https://doi.org/10.1038/s41564-020-00743-5)",
        "related": ["CheckM2", "GTDB-Tk", "Prokka"],
    },
    "pavian": {
        "official_docs": "https://github.com/fbreitwieser/pavian",
        "tutorial": "https://github.com/fbreitwieser/pavian/wiki",
        "paper": "Breitwieser & Salzberg (2020) Pavian: interactive analysis of metagenomics data. *Briefings in Bioinformatics*. DOI: [10.1093/bib/bbz155](https://doi.org/10.1093/bib/bbz155)",
        "related": ["Kraken 2", "Centrifuge", "Krona"],
    },
    "krona": {
        "official_docs": "https://github.com/marbl/Krona/wiki",
        "tutorial": "https://github.com/marbl/Krona/wiki/KronaTools",
        "paper": "Ondov et al. (2011) Interactive Metagenomic Visualization in a Web Browser. *BMC Bioinformatics*. DOI: [10.1186/1471-2105-12-355](https://doi.org/10.1186/1471-2105-12-355)",
        "related": ["Pavian", "MetaPhlAn 4", "Kraken 2"],
    },
    "phyloseq": {
        "official_docs": "https://joey711.github.io/phyloseq/",
        "tutorial": "https://joey711.github.io/phyloseq/phyloseq-quick-start-demo.html",
        "paper": "McMurdie & Holmes (2013) phyloseq: An R Package for Reproducible Interactive Analysis and Graphics of Microbiome Census Data. *PLOS ONE*. DOI: [10.1371/journal.pone.0061217](https://doi.org/10.1371/journal.pone.0061217)",
        "related": ["DESeq2", "ANCOM-BC", "microeco"],
    },
    "deseq2": {
        "official_docs": "https://bioconductor.org/packages/release/bioc/html/DESeq2.html",
        "tutorial": "https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html",
        "paper": "Love et al. (2014) Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. *Genome Biology*. DOI: [10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8)",
        "related": ["ANCOM-BC", "ALDEx2", "edgeR"],
    },
    "lefse": {
        "official_docs": "https://huttenhower.sph.harvard.edu/galaxy/",
        "tutorial": "https://huttenhower.sph.harvard.edu/galaxy/",
        "paper": "Segata et al. (2011) Metagenomic biomarker discovery and explanation. *Genome Biology*. DOI: [10.1186/gb-2011-12-6-r60](https://doi.org/10.1186/gb-2011-12-6-r60)",
        "related": ["ANCOM-BC", "DESeq2", "phyloseq"],
    },
    "ancom_bc": {
        "official_docs": "https://bioconductor.org/packages/release/bioc/html/ANCOMBC.html",
        "tutorial": "https://bioconductor.org/packages/release/bioc/vignettes/ANCOMBC/inst/doc/ANCOMBC.html",
        "paper": "Lin et al. (2020) Analysis of compositions of microbiomes with bias correction. *Nature Communications*. DOI: [10.1038/s41467-020-17041-7](https://doi.org/10.1038/s41467-020-17041-7)",
        "related": ["ALDEx2", "DESeq2", "LEfSe"],
    },
    "microeco": {
        "official_docs": "https://github.com/ChiLiubio/microeco",
        "tutorial": "https://chiliubio.github.io/microeco_tutorial/",
        "paper": "Liu et al. (2025) Protocol for using the R microeco package. *Nature Protocols*. DOI: [10.1038/s41596-025-01239-4](https://doi.org/10.1038/s41596-025-01239-4)",
        "related": ["phyloseq", "ANCOM-BC", "vegan"],
    },
    "nanoplot": {
        "official_docs": "https://github.com/wdecoster/NanoPlot",
        "tutorial": "https://github.com/wdecoster/NanoPlot#usage",
        "paper": "De Coster et al. (2018) NanoPlot: plot quality statistics and filtering for long read sequencing data. *Source Code for Biology and Medicine*. DOI: [10.1186/s13029-018-0073-4](https://doi.org/10.1186/s13029-018-0073-4)",
        "related": ["Filtlong", "Chopper", "FastQC"],
    },
    "filtlong": {
        "official_docs": "https://github.com/rrwick/Filtlong",
        "tutorial": "https://github.com/rrwick/Filtlong#usage",
        "paper": None,
        "related": ["NanoPlot", "fastp", "Chopper"],
    },
    "clair3": {
        "official_docs": "https://github.com/HKU-BAL/Clair3",
        "tutorial": "https://github.com/HKU-BAL/Clair3#quick-demo",
        "paper": "Zheng et al. (2022) Symphonizing pileup and full-alignment for deep and polymorphic nanopore variant calling. *Nature Methods*. DOI: [10.1038/s41587-021-01138-1](https://doi.org/10.1038/s41587-021-01138-1)",
        "related": ["DeepVariant", "Medaka", "PEPPER-Margin-DeepVariant"],
    },
    "salmon": {
        "official_docs": "https://salmon.readthedocs.io/en/latest/",
        "tutorial": "https://salmon.readthedocs.io/en/latest/salmon.html",
        "paper": "Patro et al. (2017) Salmon provides fast and bias-aware quantification of transcript expression. *Nature Methods*. DOI: [10.1038/nmeth.4197](https://doi.org/10.1038/nmeth.4197)",
        "related": ["Kallisto", "STAR", "featureCounts"],
    },
    "featurecounts": {
        "official_docs": "https://subread.sourceforge.net/featureCounts.html",
        "tutorial": "https://subread.sourceforge.net/SubreadUsersGuide.pdf",
        "paper": "Liao et al. (2014) featureCounts: an efficient general purpose program for assigning sequence reads to genomic features. *Bioinformatics*. DOI: [10.1093/bioinformatics/btt656](https://doi.org/10.1093/bioinformatics/btt656)",
        "related": ["HTSeq", "Salmon", "Kallisto"],
    },
    "nextflow": {
        "official_docs": "https://www.nextflow.io/docs/latest/index.html",
        "tutorial": "https://training.nextflow.io/",
        "paper": "Di Tommaso et al. (2017) Nextflow enables reproducible computational workflows. *Nature Biotechnology*. DOI: [10.1038/nbt.3820](https://doi.org/10.1038/nbt.3820)",
        "related": ["Snakemake", "nf-core/mag", "WDL"],
    },
    "nf_core_mag": {
        "official_docs": "https://nf-co.re/mag",
        "tutorial": "https://nf-co.re/mag/usage",
        "paper": "Ewels et al. (2020) nf-core: Community curated bioinformatics pipelines. *Nature Biotechnology*. DOI: [10.1038/s41587-020-0439-x](https://doi.org/10.1038/s41587-020-0439-x)",
        "related": ["Nextflow", "MEGAHIT", "MetaBAT 2"],
    },
    "virsorter2": {
        "official_docs": "https://github.com/jiarong/VirSorter2",
        "tutorial": "https://github.com/jiarong/VirSorter2/wiki",
        "paper": "Guo et al. (2021) VirSorter2: a multi-classifier, expert-guided approach to detect diverse DNA and RNA viruses. *Microbiome*. DOI: [10.1186/s40168-020-00990-y](https://doi.org/10.1186/s40168-020-00990-y)",
        "related": ["PHASTER", "Pharokka", "CheckV"],
    },
    "pharokka": {
        "official_docs": "https://github.com/gbouras13/pharokka",
        "tutorial": "https://pharokka.readthedocs.io/en/latest/",
        "paper": "Bouras et al. (2023) Pharokka: a fast scalable bacteriophage annotation tool. *Bioinformatics*. DOI: [10.1093/nargab/lqad054](https://doi.org/10.1093/nargab/lqad054)",
        "related": ["VirSorter 2", "PHASTER", "CheckV"],
    },
}

# Concept link mappings
CONCEPT_LINKS = {
    "quality-control": "quality-control",
    "taxonomic-classification": "functional-vs-taxonomic",
    "assembly": "metagenome-assembled-genomes",
    "binning": "metagenome-assembled-genomes",
    "binning-refinement": "metagenome-assembled-genomes",
    "quality-assessment": "metagenome-assembled-genomes",
    "strain-analysis": "metagenome-assembled-genomes",
    "functional-annotation": "functional-vs-taxonomic",
    "genome-annotation": "functional-vs-taxonomic",
    "alignment": "quality-control",
    "visualization": "functional-vs-taxonomic",
    "downstream-analysis": "compositional-data-analysis",
    "variant-calling": "genome-resolved-metagenomics",
    "quantification": "metatranscriptomics",
    "viral-analysis": "genome-resolved-metagenomics",
    "pipeline-framework": "quality-control",
}


def generate_references_section(refs: dict, category: str) -> str:
    """Generate the references markdown section."""
    lines = []
    lines.append("## 参考资源")
    lines.append("")

    if refs.get("official_docs"):
        lines.append(f"- 📖 **官方文档**: [{refs['official_docs']}]({refs['official_docs']})")
    if refs.get("tutorial"):
        lines.append(f"- 🎓 **教程**: [{refs['tutorial']}]({refs['tutorial']})")
    if refs.get("paper"):
        lines.append(f"- 📄 **论文**: {refs['paper']}")

    # Related tools
    related = refs.get("related", [])
    if related:
        lines.append("")
        lines.append("### 相关工具")
        lines.append("")
        for tool in related:
            tid = tool.lower().replace(" ", "_").replace("'", "").replace("-", "_")
            # Find matching tool id
            lines.append(f"- [{tool}](./{tid})")

    # Related concept
    concept = CONCEPT_LINKS.get(category)
    if concept:
        lines.append("")
        lines.append(f"### 相关概念")
        lines.append("")
        lines.append(f"- [{concept.replace('-', ' ').title()}](../concepts/{concept})")

    lines.append("")
    return "\n".join(lines)


def enrich_tool_doc(tool_id: str, md_content: str, refs: dict, category: str) -> str:
    """Enrich a tool doc with reference links."""
    # Check if already enriched (has "参考资源" section)
    if "## 参考资源" in md_content:
        return md_content

    ref_section = generate_references_section(refs, category)

    # Insert before the final separator
    if "---\n\n*最后更新" in md_content:
        md_content = md_content.replace(
            "---\n\n*最后更新",
            ref_section + "\n---\n\n*最后更新"
        )
    else:
        md_content += "\n" + ref_section

    return md_content


def main():
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs" / "skills" / "tools"
    data_file = project_root / "data" / "skills" / "curated_tools.json"

    # Load tool data for categories
    tool_categories = {}
    if data_file.exists():
        with open(data_file) as f:
            tools = json.load(f)
            for t in tools:
                d = t.get("data", {})
                tool_categories[t["id"]] = d.get("category", "unknown")

    enriched = 0
    skipped = 0
    for md_file in sorted(docs_dir.glob("*.md")):
        tool_id = md_file.stem
        refs = TOOL_REFERENCES.get(tool_id)
        if not refs:
            skipped += 1
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        category = tool_categories.get(tool_id, "unknown")
        enriched_content = enrich_tool_doc(tool_id, content, refs, category)

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(enriched_content)

        print(f"  ✅ {tool_id}")
        enriched += 1

    print(f"\n🎉 Enriched {enriched} tools, skipped {skipped} (no reference data)")


if __name__ == "__main__":
    main()
