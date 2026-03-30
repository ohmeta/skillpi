---
title: 宏转录组学
description: Metatranscriptomics — 研究微生物群落的基因表达
---

# 宏转录组学

> **宏转录组学 (Metatranscriptomics)** 通过分析环境样本中的 RNA，研究微生物群落中哪些基因正在被表达。与宏基因组（"能做什么"）互补，宏转录组揭示"正在做什么"。

## 宏基因组 vs 宏转录组

| 维度 | 宏基因组 | 宏转录组 |
|------|---------|---------|
| **分子** | DNA | RNA (主要是 mRNA) |
| **反映** | 功能潜力 | 实际表达 |
| **挑战** | DNA 稳定 | RNA 不稳定，易降解 |
| **rRNA 占比** | 低 | **高（可达 90%+）** |
| **数据分析** | 成熟 | 更复杂 |

## 宏转录组特殊挑战

### rRNA 去除

测序中 80-95% 的 reads 是 rRNA，必须去除：

| 工具 | 方法 | 速度 |
|------|------|------|
| **SortMeRNA** | 参考比对 | 中 |
| **Barrnap** | HMM | 快 |
| **riboDetector** | 深度学习 | 快 |
| **SILVA db** | 参考数据库 | — |

```bash
# SortMeRNA
sortmerna --ref silva-bac-16s-id90.fasta \
          --reads sample.fq \
          --aligned rRNA \
          --other mRNA \
          --threads 8
```

### 定量分析

```bash
# 功能定量 (HUMAnN 3, 同时支持宏基因组和宏转录组)
humann --input mRNA.fq --output humann_out/ --threads 8

# 基因表达定量
salmon quant -i index -l A -1 R1.fq -2 R2.fq -o quant_out
```

## 典型流程

```
原始 RNA-seq → rRNA 去除 → QC → 比对/定量 → 功能注释 → 差异表达
                ↓          ↓      ↓            ↓           ↓
             SortMeRNA   fastp  Salmon      HUMAnN 3    DESeq2
             riboDetector       Bowtie2     eggNOG     ANCOM-BC
```

## 实践建议

1. **RNA 保存**: 采集后立即稳定 RNA（RNAlater 或冻存 -80°C）
2. **rRNA 去除**: 必做，否则分析空间被 rRNA 占据
3. **批次效应**: 宏转录组的批次效应比宏基因组更严重
4. **技术重复**: 建议生物学重复 ≥3，技术重复 ≥2

## 参考文献

1. Bashiardes et al. (2016) Metatranscriptomics for the Human Microbiome. *Annual Review of Microbiology*. DOI: 10.1146/annurev-micro-102215-095407
2. Shakya et al. (2019) Comparative Metagenomic and RRNA Microbiome Profiling. *Microbiome*. DOI: 10.1186/s40168-019-0658-4

---

*最后更新: 2026-03-30*
