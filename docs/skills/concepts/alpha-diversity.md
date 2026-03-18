# Alpha 多样性

**难度**: ⭐⭐ 中级

## 定义

衡量单个样本内微生物群落多样性的指标，包括丰富度（物种数量）和均匀度（物种分布的均匀程度）。

## 常用指数

| 指数 | 描述 | 公式 |
|------|------|------|
| **Observed OTUs/ASVs** | 观测到的物种数量 | - |
| **Shannon 指数** | 同时考虑丰富度和均匀度 | H' = -Σ(pi × ln(pi)) |
| **Simpson 指数** | 衡量优势物种的集中程度 | D = 1 - Σ(pi²) |
| **Pielou 均匀度** | 物种分布的均匀程度 | J = H'/ln(S) |
| **Faith's PD** | 考虑系统发育关系的多样性 | - |

## 相关工具

- [QIIME 2](../tools/qiime2-amplicon) - 多样性分析
- [mothur](../tools/mothur) - 多样性计算

## 相关概念

- [16S rRNA 测序](16s-rrna-sequencing)
- [宏基因组测序](metagenomics-sequencing)
