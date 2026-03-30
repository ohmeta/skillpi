---
title: 批次效应
description: 微生物组研究中的批次效应识别和校正
---

# 批次效应

> **批次效应** (Batch Effect) 是由技术因素（非生物因素）引入的系统性变异，可能严重干扰微生物组分析结果。

## 批次效应的来源

| 来源 | 示例 | 影响 |
|------|------|------|
| **DNA 提取** | 不同试剂盒、提取日期 | 物种组成偏移 |
| **测序批次** | 不同 flow cell、运行日期 | 深度和质量差异 |
| **引物批次** | 不同合成批次 | 扩增偏好性变化 |
| **存储条件** | -80°C vs -20°C | DNA 降解差异 |
| **操作人员** | 不同实验员 | 污染模式不同 |

## 如何识别批次效应

### 可视化方法

```r
library(phyloseq)
library(ggplot2)

# PCA/PCoA 着色批次
plot_ordination(ps, ordinate(ps, "PCoA"), color = "batch")

# 热图聚序
pheatmap(otu_table(ps), annotation_col = sample_data(ps)["batch"])
```

### 统计检验

```r
# PERMANOVA 检验批次对组成的影响
library(vegan)
adonis2(otu_table(ps) ~ batch + condition, data = sample_data(ps))

# 如果 batch 的 R² 很大且 p < 0.05，说明存在显著批次效应
```

## 批次效应校正方法

### 1. 实验设计层面（首选）

**最佳策略是在实验设计阶段预防**：

- **平衡设计**: 每个批次包含所有实验组的样本
- **随机化**: 样本处理顺序随机
- **批次内对照**: 每批次加入阳性/阴性对照
- **同时处理**: 尽量在同一批次处理所有样本

### 2. 统计校正

#### 协变量方法

在统计模型中加入批次作为协变量：

```r
# ANCOM-BC: 直接在公式中加入
result <- ancombc2(ps, fix_formula = "group + batch")

# DESeq2: 加入设计矩阵
dds <- DESeqDataSetFromMatrix(countData, colData, ~ batch + group)
```

#### ComBat / ComBat-seq

```r
library(sva)

# 对丰度矩阵校正
adjusted <- ComBat_seq(counts, batch = sample_data$batch, 
                        group = sample_data$group)
```

#### limma::removeBatchEffect

```r
library(limma)

# 对 log 转换后的数据校正
corrected <- removeBatchEffect(log_abundance, batch = metadata$batch)
```

### 3. 工具特定方法

| 工具 | 方法 | 适用场景 |
|------|------|----------|
| **ANCOM-BC** | 协变量调整 | 差异丰度分析 |
| **SVA** | 代理变量 | 未知混杂因素 |
| **RUV** | 负对照基因 | RNA-seq 类数据 |
| **MMUPHin** | 元分析校正 | 多队列整合 |

## 关键原则

1. ⚠️ **永远不要**在不考虑批次的情况下比较组间差异
2. ✅ **实验设计 > 统计校正** — 预防优于补救
3. ✅ **平衡设计** — 批次和实验组交叉
4. ✅ **保留批次信息** — 在结果中报告批次效应
5. ✅ **敏感性分析** — 校正前后结果一致性检验

## 相关概念

- [组成性数据分析 (CoDA)](compositional-data-analysis)
- [Alpha 多样性](alpha-diversity)
- [ANCOM-BC](../tools/ancom_bc)

## 参考文献

1. Leek et al. (2010) Tackling the widespread and critical impact of batch effects in high-throughput data. *Nature Reviews Genetics*. DOI: 10.1038/nrg2825
2. Gibbons et al. (2018) Correcting for batch effects in case-control microbiome studies. *PLOS Computational Biology*. DOI: 10.1371/journal.pcbi.1006102
3. Dai et al. (2022) MMUPHin: meta-analysis framework with community heterogeneity control. *Nature Communications*. DOI: 10.1038/s41467-022-29587-9

---

*最后更新: 2026-03-30*
