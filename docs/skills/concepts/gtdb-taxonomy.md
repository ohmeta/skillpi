---
title: GTDB 分类学框架
description: Genome Taxonomy Database - 基于基因组的标准化微生物分类体系
---

# GTDB 分类学框架

> **GTDB** (Genome Taxonomy Database) 是基于全基因组系统发育的标准化原核生物分类框架，正在逐步取代传统的 16S rRNA 分类体系。

## 为什么需要 GTDB？

传统分类学存在几个问题：
- **16S rRNA 分辨率不足**: 无法区分属/种级别（如大肠杆菌和志贺氏菌 16S 相似度 >99%）
- **分类不一致**: 不同数据库的分类标准不统一
- **未培养微生物缺失**: 传统分类依赖纯培养

GTDB 通过全基因组平均核苷酸一致性 (ANI) 和系统发育分析解决这些问题。

## GTDB 的核心概念

### 分类框架

| 级别 | 命名规则 | 说明 |
|------|----------|------|
| 领 (Domain) | 标准命名 | 细菌/古菌 |
| 门 (Phylum) | 标准命名 | |
| 纲 (Class) | 标准命名 | |
| 目 (Order) | 标准命名 | |
| 科 (Family) | 标准命名 | |
| 属 (Genus) | 标准命名 | |
| **物种 (Species)** | **ANI ≥ 95%** | 基于基因组相似度定义 |

### 物种定义：ANI

GTDB 使用 **平均核苷酸一致性 (ANI)** 定义物种边界：

```
ANI ≥ 95% → 同一物种
ANI < 95% → 不同物种
```

这比传统 DDH（DNA-DNA 杂交）的 70% 标准更精确。

### 命名规则

- GTDB 使用占位符名称 (placeholder names) 标记未正式命名的分类单元
- 格式：`g__` (属) `s__` (种)
- 例如：`s__GGB12345` 表示一个未命名的物种

## GTDB-Tk 使用

### 基本流程

```bash
# 1. 下载 GTDB 参考数据 (~85GB)
gtdbtk classify_wf --genome_dir genomes/ --out_dir output/ --cpus 16

# 2. 或分步运行
gtdbtk identify --genome_dir genomes/ --out_dir identify/
gtdbtk align --identify_dir identify/ --out_dir align/
gtdbtk classify --align_dir align/ --out_dir classify/
```

### 输出解读

```
# 输出文件: gtdbtk.bac120.summary.tsv
user_genome           classification                                fastani_reference  fastani_ani  fastani_af
bin.1                 d__Bacteria;p__Firmicutes;c__Bacilli;...      GCF_00012345.1     98.5         0.95
bin.2                 d__Bacteria;p__Proteobacteria;...             GCF_00067890.1     97.2         0.90
```

## GTDB 版本

| 版本 | 日期 | 基因组数 | 物种数 |
|------|------|----------|--------|
| R220 | 2024-04 | 852,000+ | 121,000+ |
| R214 | 2023-04 | 400,000+ | 85,000+ |
| R207 | 2022-04 | 258,000+ | 65,000+ |

## 与 NCBI 分类的差异

| 特性 | GTDB | NCBI Taxonomy |
|------|------|---------------|
| 物种定义 | ANI ≥ 95% | 混合标准 |
| 基于 | 基因组系统发育 | 混合（16S + 基因组） |
| 未培养微生物 | 包含 | 部分包含 |
| 命名 | 占位符 | 标准命名 |
| 更新频率 | 每年 | 持续 |

## 相关概念

- [宏基因组组装基因组 (MAG)](metagenome-assembled-genomes)
- [GTDB-Tk](../tools/gtdb_tk)
- [CheckM2](../tools/checkm2)

## 参考文献

1. Parks et al. (2018) A standardized bacterial taxonomy based on genome phylogeny substantially revises the tree of life. *Nature Biotechnology*. DOI: 10.1038/nbt.4229
2. Chaumeil et al. (2022) GTDB-Tk v2: memory friendly classification with the Genome Taxonomy Database. *Bioinformatics*. DOI: 10.1093/bioinformatics/btac672

---

*最后更新: 2026-03-30*
