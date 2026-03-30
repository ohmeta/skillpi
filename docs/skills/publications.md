---
title: 最新文献
description: 2025-2026 微生物组信息学重要文献和工具评测
---

# 最新文献 (2025-2026)

本页追踪微生物组信息学领域的最新重要文献，重点关注新工具、方法评测和综述。

---

## 📖 综述类

### 长读长宏基因组计算工具综述

**"Computational Tools and Resources for Long-read Metagenomic Sequencing"**
- 作者: Zhang et al.
- 期刊: *Genomics, Proteomics & Bioinformatics* (2025)
- DOI: [PMC12631790](https://pmc.ncbi.nlm.nih.gov/articles/PMC12631790/)
- 内容: 系统综述了长读长（Nanopore/PacBio）宏基因组的分类、组装、分箱工具
- 亮点: 工具 GitHub 资源库 [LongMetagenome](https://github.com/zhangtianyuan666/LongMetagenome)

### 宏基因组组装基因组 (MAG) 综述

**"Metagenome-Assembled Genomes (MAGs): Advances, Challenges, and Opportunities"**
- 作者: Chen et al.
- 期刊: *Microorganisms* (2025)
- DOI: [10.3390/microorganisms13050985](https://www.mdpi.com/2076-2607/13/5/985)
- 内容: MAG 构建的最新进展、挑战和机遇

### 长读长宏基因组计算方法综述

**"A review of computational approaches for metagenomics by long-read sequencing"**
- 期刊: *Science China Life Sciences* (2025)
- DOI: [10.1007/s11427-025-3133-3](https://link.springer.com/article/10.1007/s11427-025-3133-3)
- 内容: 分类策略、组装和分箱方法、遗传元件检测的系统综述

---

## 🧪 方法评测

### 分箱工具 Benchmark

**"Benchmarking metagenomic binning tools on real datasets"**
- 期刊: *Nature Communications* (2025)
- DOI: [10.1038/s41467-025-57957-6](https://www.nature.com/articles/s41467-025-57957-6)
- 内容: 13 种分箱工具在短读长/长读长/混合数据下的全面比较
- 关键发现: 不同数据类型的最佳工具不同；长读长需要专门的分箱方法

### Nanopore 宏基因组工具 Benchmark

**"Benchmarking of analysis tools and pipeline development for nanopore long-read metagenomics"**
- 作者: Peng et al.
- 期刊: (2025)
- DOI: [PubMed 40189999](https://pubmed.ncbi.nlm.nih.gov/40189999/)
- 内容: 长读长宏基因组分析工具的系统评测和流程开发

### 差异丰度方法比较

**"Microbiome differential abundance methods produce different results"**
- 期刊: *Nature Communications* (2022, 持续引用)
- DOI: [10.1038/s41467-022-28034-z](https://www.nature.com/articles/s41467-022-28034-z)
- 内容: 14 种方法在 38 个数据集上的比较
- 结论: ALDEx2 和 ANCOM-II 产生最一致的结果

### Web 工具 Benchmark

**"A comprehensive comparison of web-based tools for amplicon analysis"**
- 期刊: *Frontiers in Microbiology* (2025)
- DOI: [10.3389/fmicb.2025.1711000](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2025.1711000/full)

---

## 🔬 新工具

### nanoMDBG — 长读长宏基因组组装

**"High-quality metagenome assembly from nanopore reads with nanoMDBG"**
- 期刊: *Nature Communications* (2026)
- DOI: [10.1038/s41467-026-69760-y](https://www.nature.com/articles/s41467-026-69760-y)
- 内容: 基于 minimizer 的长读长宏基因组组装器
- 亮点: ONT 数据可产出接近 PacBio HiFi 质量的 MAG

### LorBin — 长读长分箱

**"LorBin: efficient binning of long-read metagenomes"**
- 期刊: *Nature Communications* (2025)
- DOI: [10.1038/s41467-025-64916-8](https://www.nature.com/articles/s41467-025-64916-8)
- 内容: 无监督长读长宏基因组分箱工具
- 亮点: 提升高质量 MAG 恢复率，发现新分类单元

### dar — 共识差异丰度

**"dar: Consensus-based differential abundance analysis"**
- 预印本: *bioRxiv* (2025)
- DOI: [10.1101/2025.02.07.637000](https://www.biorxiv.org/content/10.1101/2025.02.07.637000v1)
- 内容: 整合 DESeq2、ALDEx2、ANCOM-BC 等方法的共识框架

### Metagenomics-Toolkit

**"Metagenomics-Toolkit: the flexible and efficient cloud-based workflow"**
- 期刊: *NAR Genomics and Bioinformatics* (2025)
- DOI: [10.1093/nargab/lqaf093](https://academic.oup.com/nargab/article/7/3/lqaf093/8204052)
- 内容: 基于 Nextflow 的可扩展宏基因组分析流程

---

## 📊 数据库更新

### HRGM2 — 人类肠道 MAG 目录

**"A human gut metagenome-assembled genome catalogue spanning 41 countries"**
- 期刊: *Nature Microbiology* (2025)
- DOI: [10.1038/s41564-025-02206-1](https://www.nature.com/articles/s41564-025-02206-1)
- 内容: 155,211 个高质量 MAG，覆盖 41 个国家

### gcMeta 2025

**"gcMeta 2025: a global repository of metagenome-assembled genomes"**
- 期刊: *Nucleic Acids Research* (2025)
- DOI: [10.1093/nar/gkae1085](https://academic.oup.com/nar/article/54/D1/D724/8307362)

### MAGdb

**"MAGdb: a comprehensive high quality MAGs repository"**
- 期刊: *Genome Biology* (2025)
- DOI: [10.1186/s13059-025-03711-6](https://link.springer.com/article/10.1186/s13059-025-03711-6)

### Kraken 2 数据库更新

- 2026 年 1 月：**PrackenDB** 发布，包含所有 NCBI RefSeq 细菌、古菌、原生生物和真菌

---

## 📈 可视化与分析平台

### MicrobiomeStatPlots

**"MicrobiomeStatPlots: Microbiome statistics plotting gallery"**
- 期刊: *iMeta* (2025)
- DOI: [10.1002/imt2.70002](https://onlinelibrary.wiley.com/doi/full/10.1002/imt2.70002)
- 内容: 综合微生物组统计分析和可视化平台

### microeco 包

**"Protocol for using the R microeco package"**
- 期刊: *Nature Protocols* (2025)
- DOI: [10.1038/s41596-025-01239-4](https://www.nature.com/articles/s41596-025-01239-4)
- 内容: R microeco 包的详细操作协议，支持扩增子和宏基因组

---

## 🔄 持续更新

本文献列表定期更新。如果您有推荐的新文献，请在 GitHub 上提交 Issue 或 Pull Request。

*最后更新: 2026-03-30*
