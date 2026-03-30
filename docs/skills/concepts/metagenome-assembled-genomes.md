---
title: 宏基因组组装基因组 (MAG)
description: Metagenome-Assembled Genomes 的概念、方法和应用
---

# 宏基因组组装基因组 (MAG)

> **MAG** = Metagenome-Assembled Genome，从宏基因组数据中通过组装和分箱获得的微生物基因组。

## 为什么 MAG 重要？

传统微生物学只能研究约 **1%** 可培养的微生物。MAG 技术使我们能够：
- 直接从环境样本获取未培养微生物的基因组
- 发现新的物种、门和代谢途径
- 构建更完整的微生物基因组目录

## MAG 构建流程

```
原始读段 → 质量控制 → 组装 → 分箱 → 质量评估 → 分类注释
              ↓         ↓       ↓        ↓          ↓
           fastp    MEGAHIT  MetaBAT2  CheckM2   GTDB-Tk
                  metaSPAdes MaxBin2
                    Flye    CONCOCT
```

### 关键步骤

| 步骤 | 工具 | 说明 |
|------|------|------|
| **组装** | MEGAHIT, metaSPAdes, Flye | 将短/长读段组装成 contigs |
| **分箱** | MetaBAT 2, MaxBin 2, CONCOCT | 将 contigs 分组为单个基因组 |
| **优化** | DAS Tool | 整合多个分箱工具的结果 |
| **评估** | CheckM2, CheckM | 评估完整性和污染度 |
| **分类** | GTDB-Tk | 基于 GTDB 分类框架注释 |

## 质量标准 (MIMAG 标准)

基于 [Bowers et al., 2017](https://doi.org/10.1038/nbt.3893) 的最低信息标准：

| 质量等级 | 完整性 | 污染度 |
|----------|--------|--------|
| **高质量 (HQ)** | ≥ 90% | ≤ 5% |
| **中质量 (MQ)** | ≥ 50% | ≤ 10% |

> 💡 高质量 MAG 还要求：含有 23S、16S、5S rRNA 基因和 ≥18 个 tRNA 基因。

## MAG 数据库

| 数据库 | 规模 | 说明 |
|--------|------|------|
| **GTDB** | 400,000+ 物种 | 基因组分类数据库，标准化分类框架 |
| **UHGG** | 200,000+ 基因组 | 人类肠道微生物基因组 |
| **HRGM2** | 155,000+ 基因组 | 跨 41 国的人类肠道 MAG 目录 (2025) |
| **gcMeta** | 持续更新 | 全球 MAG 资源库 (2025 NAR) |

## 最新进展 (2025-2026)

- **长读长 MAG**: PacBio HiFi + nanoMDBG 可获得数百个环化完整基因组 ([Nature Methods, 2024](https://doi.org/10.1038/s41587-023-01983-6))
- **LorBin**: 专为长读长设计的分箱工具 ([Nature Communications, 2025](https://doi.org/10.1038/s41467-025-64916-8))
- **分箱工具 Benchmark**: 13 种工具在短读长/长读长/混合数据上的比较 ([Nature Communications, 2025](https://doi.org/10.1038/s41467-025-57957-6))

## 相关概念

- [宏基因组测序](metagenomics-sequencing)
- [GTDB 分类学](gtdb-taxonomy)
- [CheckM2](../tools/checkm2)
- [MetaBAT 2](../tools/metabat2)
- [DAS Tool](../tools/das_tool)

## 参考文献

1. Bowers et al. (2017) Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG). *Nature Biotechnology*. DOI: 10.1038/nbt.3893
2. Parks et al. (2020) A standardized bacterial taxonomy based on genome phylogeny substantially revises the tree of life. *Nature Biotechnology*. DOI: 10.1038/nbt.4229
3. Chen et al. (2025) Metagenome-Assembled Genomes (MAGs): Advances, Challenges, and Opportunities. *Microorganisms*. DOI: 10.3390/microorganisms13050985

---

*最后更新: 2026-03-30*
