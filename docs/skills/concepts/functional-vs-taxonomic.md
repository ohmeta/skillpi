---
title: 功能谱分析 vs 分类谱分析
description: 宏基因组分析的两种核心策略对比
---

# 功能谱分析 vs 分类谱分析

> 宏基因组数据可从两个维度分析：**"谁在那里"（分类谱）** 和 **"它们在做什么"（功能谱）**。

## 两种策略对比

| 维度 | 分类谱 (Taxonomic Profiling) | 功能谱 (Functional Profiling) |
|------|------|------|
| **问题** | 样本中有哪些物种？ | 样本中有哪些代谢通路/基因？ |
| **工具** | MetaPhlAn, Kraken 2 | HUMAnN 3, eggNOG-mapper |
| **数据库** | 标记基因/基因组参考 | UniRef, KEGG, MetaCyc |
| **输出** | 物种丰度表 | 通路/基因家族丰度表 |
| **计算成本** | 较低 | 较高 |
| **生物学洞察** | 群落组成 | 群落功能潜力 |

## 分类谱分析

### 原理

将 reads 映射到已知物种的标记基因或基因组：

```
Reads → 比对到参考 → 物种分类 → 丰度估计
```

### 工具选择

| 工具 | 方法 | 速度 | 准确度 | 内存 |
|------|------|------|--------|------|
| **MetaPhlAn 4** | 标记基因 | 快 | 高 | 中 |
| **Kraken 2** | k-mer | 最快 | 中 | 高 |
| **Centrifuge** | FM-index | 快 | 中 | 低 |
| **Kaiju** | 蛋白质比对 | 慢 | 高（远缘） | 中 |

### 典型流程

```bash
# MetaPhlAn
metaphlan input.fastq --bowtie2db /db --nproc 8 --output_file profile.txt

# Kraken 2 + Bracken
kraken2 --db /db --output kraken.out --report kraken.report input.fastq
bracken -d /db -i kraken.report -o bracken.out -r 150 -l S
```

## 功能谱分析

### 原理

将 reads 映射到蛋白质数据库，然后映射到代谢通路：

```
Reads → 翻译 → 比对到 UniRef → 映射到通路 → 通路丰度
```

### 核心工具：HUMAnN 3

```bash
# 基本使用
humann --input input.fastq --output humann_out/ --threads 8

# 输出文件：
# - genefamilies.tsv  (基因家族丰度)
# - pathcoverage.tsv  (通路覆盖度)
# - pathabundance.tsv (通路丰度)
```

### 通路数据库

| 数据库 | 说明 | 适用 |
|------|------|------|
| **UniRef50/90** | 蛋白质聚类 | 通用 |
| **KEGG** | 代谢通路 | 代谢分析 |
| **MetaCyc** | 代谢通路 | 替代 KEGG |
| **eggNOG** | 直系同源组 | 功能注释 |

## 整合分析

最佳实践是同时做分类和功能分析：

```bash
# bioBakery 流程
metaphlan input.fastq --bowtie2out mapped.bz2 --output profile.txt
humann --input input.fastq --output humann_out/
```

然后用 MaAsLin2 做统计关联：

```bash
# 分类关联
maaslin2 -i abundance.tsv -m metadata.tsv -o results_taxonomy/

# 功能关联
maaslin2 -i pathabundance.tsv -m metadata.tsv -o results_functional/
```

## 参考文献

1. Beghini et al. (2021) Integrating taxonomic, functional, and strain-level profiling of diverse microbial communities with bioBakery 3. *eLife*. DOI: 10.7554/eLife.65088
2. Franzosa et al. (2018) Species-level functional profiling of metagenomes and metatranscriptomes. *Nature Methods*. DOI: 10.1038/s41592-018-0176-y

---

*最后更新: 2026-03-30*
