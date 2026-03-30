# 工具

本页面包含所有 51 个微生物组分析工具。

## 🔗 比对

| 工具 | 用途 | 难度 |
|------|------|------|
| [Bowtie 2](tools/bowtie2) | A fast and sensitive gapped read aligner | ⭐ 初级 |
| [minimap2](tools/minimap2) | A versatile pairwise aligner for genomic and spliced nucleot | ⭐ 初级 |
| [BWA-MEM2](tools/bwa_mem2) | BWA-MEM 的加速版本，利用 SIMD 指令提升比对速度 2-3 倍 | ⭐ 初级 |

## 🧪 扩增子分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [QIIME 2 (Amplicon)](tools/qiime2-amplicon) | 强大的微生物组扩增子分析平台，支持从原始测序数据到统计分析和可视化的完整流程 | ⭐⭐ 中级 |
| [Mothur](tools/mothur) | 用于微生物生态学分析的综合工具，专注于 16S rRNA 基因序列分析和微生物群落多样性研究 | ⭐⭐ 中级 |

## 🧩 组装

| 工具 | 用途 | 难度 |
|------|------|------|
| [Megahit](tools/megahit) | 超快速且内存高效的 NGS 组装器，主要针对宏基因组优化，基于简洁 de Bruijn 图技术 | ⭐⭐⭐ 高级 |
| [metaSPAdes](tools/metaspades) | 专门为宏基因组数据设计的 de novo 组装器，基于 SPAdes 引擎 | ⭐⭐ 中级 |
| [Flye](tools/flye) | De novo assembler for single molecule sequencing reads using | ⭐⭐⭐ 高级 |
| [Canu](tools/canu) | A single molecule sequence assembler for genomes large and s | ⭐⭐⭐ 高级 |
| [Unicycler](tools/unicycler) | hybrid assembly pipeline for bacterial genomes | ⭐⭐ 中级 |

## 📦 分箱 (Binning)

| 工具 | 用途 | 难度 |
|------|------|------|
| [MetaBAT 2](tools/metabat2) | 基于丰度和四核苷酸频率的宏基因组分箱工具，恢复高质量 MAG | ⭐⭐⭐ 高级 |
| [MaxBin 2](tools/maxbin2) | 自动化宏基因组分箱工具，利用序列组成和丰度信息 | ⭐⭐⭐ 高级 |
| [CONCOCT](tools/concoct) | Clustering cONtigs with COverage and ComposiTion | ⭐⭐⭐ 高级 |

## ✨ 分箱优化

| 工具 | 用途 | 难度 |
|------|------|------|
| [DAS Tool](tools/das_tool) | 通过集成多个分箱工具结果来恢复高质量 MAG 的整合框架 | ⭐⭐⭐ 高级 |

## 📖 概念

| 工具 | 用途 | 难度 |
|------|------|------|
| [16S rRNA 测序](tools/16s-rrna-sequencing) |  | ⭐ 初级 |
| [宏基因组测序](tools/metagenomics-sequencing) |  | ⭐⭐ 中级 |

## 🔊 去噪

| 工具 | 用途 | 难度 |
|------|------|------|
| [DADA2](tools/dada2-pipeline) | 高分辨率的样本推断算法，可从扩增子测序数据中精确识别序列变异（ASV），替代传统的 OTU 聚类方法 | ⭐⭐ 中级 |

## 📈 下游分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [phyloseq](tools/phyloseq) | phyloseq is a set of classes, wrappers, and tools (in R) to  | ⭐⭐ 中级 |
| [DESeq2](tools/deseq2) | Differential expression of RNA-seq data using the Negative B | ⭐⭐ 中级 |
| [LEfSe](tools/lefse) | 线性判别分析效应量工具，用于高维生物数据的类间差异分析 | ⭐⭐ 中级 |
| [ANCOM-BC](tools/ancom_bc) | 基于偏差校正的组成数据分析方法，用于微生物组差异丰度分析 | ⭐⭐⭐ 高级 |
| [microeco](tools/microeco) | R 包，用于微生物组数据的统计分析和可视化，支持多种数据类型 | ⭐⭐ 中级 |

## 📝 功能注释

| 工具 | 用途 | 难度 |
|------|------|------|
| [eggNOG-mapper](tools/eggnog_mapper) | Fast genome-wide functional annotation through orthology ass | ⭐⭐ 中级 |
| [antiSMASH](tools/antismash) | 微生物次级代谢产物生物合成基因簇（BGC）的全面识别和分析工具 | ⭐⭐⭐ 高级 |
| [DRAM](tools/dram) | Distilled and Refined Annotation of Metabolism: A tool for t | ⭐⭐⭐ 高级 |

## 🔬 功能分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [HUMAnN 3](tools/humann-3) | 用于从宏基因组或宏转录组数据中高效、准确地分析微生物群落通路存在/缺失和丰度的流程（功能分析） | ⭐⭐ 中级 |

## 🧬 基因组注释

| 工具 | 用途 | 难度 |
|------|------|------|
| [Prokka](tools/prokka) | :zap: :aquarius: Rapid prokaryotic genome annotation | ⭐⭐ 中级 |
| [Bakta](tools/bakta) | Rapid & standardized annotation of bacterial genomes, MAGs & | ⭐⭐ 中级 |

## ⚙️ 流程框架

| 工具 | 用途 | 难度 |
|------|------|------|
| [Nextflow](tools/nextflow) | 用于可扩展和可复现计算工作流的框架，支持 Docker/Singularity 容器化 | ⭐⭐⭐ 高级 |

## 🧬 分类分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [MetaPhlAn 4](tools/metaphlan-4) | 用于从宏基因组鸟枪法测序数据中进行物种级微生物组成分析的工具（细菌、古菌、真核生物和病毒） | ⭐ 初级 |

## ✅ 质量评估

| 工具 | 用途 | 难度 |
|------|------|------|
| [CheckM2](tools/checkm2) | Assessing the quality of metagenome-derived genome bins usin | ⭐⭐ 中级 |

## 🔬 质量控制

| 工具 | 用途 | 难度 |
|------|------|------|
| [Fastp](tools/fastp) | 超快速的 FASTQ 数据预处理和质量控制工具，集成了质量分析、过滤、修剪、去重等多种功能 | ⭐ 初级 |
| [NanoPlot](tools/nanoplot) | Oxford Nanopore 测序数据质量控制和可视化工具 | ⭐ 初级 |
| [Filtlong](tools/filtlong) | 长读长序列质量过滤工具，基于质量分数和读长长度 | ⭐ 初级 |

## 📊 定量分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [Salmon](tools/salmon) | 超快速转录本定量工具，支持映射和无比对模式 | ⭐⭐ 中级 |
| [featureCounts](tools/featurecounts) | 高效的读段计数工具，支持基因/外显子/转录本水平的定量 | ⭐ 初级 |

## 🦠 菌株分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [StrainPhlAn](tools/strainphlan) | MetaPhlAn is a computational tool for profiling the composit | ⭐⭐⭐ 高级 |
| [inStrain](tools/instrain) | 基于读段比较分析宏基因组中的群体基因组学，包括 SNV、微多样性、菌株验证 | ⭐⭐⭐ 高级 |

## 🧬 分类鉴定

| 工具 | 用途 | 难度 |
|------|------|------|
| [Kraken 2](tools/kraken2) | The second version of the Kraken taxonomic sequence classifi | ⭐⭐ 中级 |
| [Bracken](tools/bracken) | Bracken (Bayesian Reestimation of Abundance with KrakEN) is  | ⭐⭐ 中级 |
| [Centrifuge](tools/centrifuge) | Classifier for metagenomic sequences | ⭐⭐ 中级 |
| [Kaiju](tools/kaiju) | Fast taxonomic classification of metagenomic sequencing read | ⭐⭐ 中级 |
| [GTDB-Tk](tools/gtdb_tk) | GTDB-Tk: a toolkit for assigning objective taxonomic classif | ⭐⭐ 中级 |

## 🎯 变异检测

| 工具 | 用途 | 难度 |
|------|------|------|
| [Clair3](tools/clair3) | 长读长（ONT/PacBio）快速准确的 SNP/Indel 变异检测工具 | ⭐⭐⭐ 高级 |

## 🧫 病毒分析

| 工具 | 用途 | 难度 |
|------|------|------|
| [VirSorter 2](tools/virsorter2) | 基于多分类器的病毒序列识别工具，从宏基因组中挖掘病毒序列 | ⭐⭐⭐ 高级 |
| [Pharokka](tools/pharokka) | 快速噬菌体基因组注释工具，自动检测 tRNA、tmRNA 和基因功能 | ⭐⭐ 中级 |

## 📊 可视化

| 工具 | 用途 | 难度 |
|------|------|------|
| [anvi'o](tools/anvio) | An analysis and visualization platform for 'omics data | ⭐⭐⭐ 高级 |
| [Pavian](tools/pavian) | 交互式宏基因组分类结果可视化工具，支持 Kraken/KrakenUniq/Centrifuge 输出 | ⭐ 初级 |
| [Krona](tools/krona) | Interactively explore metagenomes and more from a web browse | ⭐ 初级 |

## 🔄 工作流

| 工具 | 用途 | 难度 |
|------|------|------|
| [bioBakery Workflow](tools/biobakery-workflow) | Huttenhower 实验室开发的微生物群落分析工具集和教程平台，提供 MetaPhlAn、HUMAnN 等工具的集成 | ⭐⭐ 中级 |
| [nf-core/mag](tools/nf_core_mag) | nf-core 的宏基因组组装和分箱流程，支持短读长/长读长/混合数据 | ⭐⭐⭐ 高级 |

