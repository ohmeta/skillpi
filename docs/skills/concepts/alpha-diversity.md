# Alpha 多样性

## 定义

衡量单个样本内微生物群落多样性的指标，包括丰富度（物种数量）和均匀度（物种分布的均匀程度）

## 解释

常用的 Alpha 多样性指数：

- **Observed OTUs/ASVs**: 观测到的物种数量
- **Shannon 指数**: 同时考虑丰富度和均匀度
- **Simpson 指数**: 衡量优势物种的集中程度
- **Pielou 均匀度**: 物种分布的均匀程度
- **Faith's PD**: 考虑系统发育关系的多样性


## 示例

- Shannon 指数计算：H' = -Σ(pi × ln(pi))
- QIIME2 命令：qiime diversity alpha

## 相关概念

- Beta 多样性
- Gamma 多样性
- 物种丰富度

