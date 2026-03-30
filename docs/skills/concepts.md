# 核心概念

微生物组信息学的基础概念和术语。

## 📖 概念列表

### 基础概念

| 概念 | 难度 | 描述 |
|------|------|------|
| [16S rRNA 测序](concepts/16s-rrna-sequencing) | ⭐ 初级 | 基于 16S rRNA 基因的微生物分类分析 |
| [宏基因组测序](concepts/metagenomics-sequencing) | ⭐⭐ 中级 | 鸟枪法测序分析微生物群落功能 |
| [Alpha 多样性](concepts/alpha-diversity) | ⭐⭐ 中级 | 样本内微生物多样性指标 |

### 数据处理

| 概念 | 难度 | 描述 |
|------|------|------|
| [测序质量控制](concepts/quality-control) | ⭐ 初级 | QC 流程、FastQC、fastp 最佳实践 |
| [数据标准化与归一化](concepts/normalization) | ⭐⭐ 中级 | Rarefaction、CSS、TMM、CLR 方法对比 |
| [组成性数据分析 (CoDA)](concepts/compositional-data-analysis) | ⭐⭐⭐ 高级 | 处理相对丰度数据的统计框架 |
| [批次效应](concepts/batch-effects) | ⭐⭐ 中级 | 技术因素引入的系统性变异及其校正 |
| [样本污染与去污染](concepts/decontamination) | ⭐⭐ 中级 | 低生物量样本的污染检测与去除 |

### 分析策略

| 概念 | 难度 | 描述 |
|------|------|------|
| [功能谱 vs 分类谱](concepts/functional-vs-taxonomic) | ⭐⭐ 中级 | "谁在那里" vs "它们在做什么" |
| [宏转录组学](concepts/metatranscriptomics) | ⭐⭐⭐ 高级 | RNA 水平的微生物群落功能分析 |
| [微生物组网络分析](concepts/network-analysis) | ⭐⭐⭐ 高级 | 共现网络推断微生物相互作用 |

### 基因组学

| 概念 | 难度 | 描述 |
|------|------|------|
| [宏基因组组装基因组 (MAG)](concepts/metagenome-assembled-genomes) | ⭐⭐⭐ 高级 | 从宏基因组中重建微生物基因组 |
| [基因组解析宏基因组学](concepts/genome-resolved-metagenomics) | ⭐⭐⭐ 高级 | 从群落中解析单个基因组的完整流程 |
| [GTDB 分类学框架](concepts/gtdb-taxonomy) | ⭐⭐⭐ 高级 | 基于基因组的标准化微生物分类体系 |

## 🎯 学习路径

### 入门
[测序质量控制](concepts/quality-control) → [16S rRNA 测序](concepts/16s-rrna-sequencing) → [Alpha 多样性](concepts/alpha-diversity)

### 中级
[宏基因组测序](concepts/metagenomics-sequencing) → [功能谱 vs 分类谱](concepts/functional-vs-taxonomic) → [数据标准化](concepts/normalization) → [批次效应](concepts/batch-effects)

### 高级
[MAG](concepts/metagenome-assembled-genomes) → [基因组解析](concepts/genome-resolved-metagenomics) → [GTDB](concepts/gtdb-taxonomy) → [CoDA](concepts/compositional-data-analysis) → [网络分析](concepts/network-analysis)
