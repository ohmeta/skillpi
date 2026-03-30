---
title: 微生物组网络分析
description: 共现网络推断微生物间相互作用关系
---

# 微生物组网络分析

> 通过共现（co-occurrence）和相关性分析，推断微生物之间的潜在相互作用关系。

## 为什么做网络分析？

微生物群落不是随机聚集的 — 物种之间存在：
- **互利共生**: 交叉喂养、代谢互补
- **竞争排斥**: 争夺相同资源
- **捕食关系**: 噬菌体-宿主

网络分析帮助我们可视化和量化这些关系。

## 方法对比

| 方法 | 原理 | 处理组成性 | 计算成本 | 参考 |
|------|------|-----------|---------|------|
| **Spearman** | 秩相关 | ❌ | 低 | — |
| **SparCC** | 对数比相关 | ✅ | 中 | Friedman & Alm 2012 |
| **SPIEC-EASI** | 稀疏逆协方差 | ✅ | 高 | Kurtz et al. 2015 |
| **FlashWeave** | 条件互信息 | ✅ | 高 | Tackmann et al. 2019 |
| **SECOM** | 偏相关 | ✅ | 中 | 2024 |

### 为什么普通相关不行？

由于组成性偏差，物种间会出现 **虚假负相关**（见 [组成性数据分析](compositional-data-analysis)）。必须使用校正方法。

## 实操流程

### R 语言 (SpiecEasi)

```r
library(SpiecEasi)

# 构建网络
se <- spiec.easi(ps, method = "mb", lambda.min.ratio = 1e-2,
                  nlambda = 20, icov.select.params = list(rep.num = 50))

# 提取邻接矩阵
adj <- as.matrix(getRefit(se))

# 转换为 igraph 对象
library(igraph)
g <- graph_from_adjacency_matrix(adj, mode = "undirected", diag = FALSE)

# 可视化
plot(g, vertex.size = 5, vertex.label.cex = 0.7)
```

### Python (SparCC)

```python
from pysurvey import SparCC

sparcc = SparCC()
sparcc.fit(otu_table)
correlations = sparcc.correlations
pvalues = sparcc.pvalues
```

## 网络指标

| 指标 | 含义 | 生物学意义 |
|------|------|-----------|
| **度 (Degree)** | 连接数 | 关联多的"核心"物种 |
| **介数中心性** | 桥梁作用 | 关键"枢纽"物种 |
| **模块 (Module)** | 紧密连接的子群 | 功能群落/代谢网络 |
| **负边比例** | 负相关占比 | 竞争强度 |

## 注意事项

1. **相关 ≠ 因果**: 共现不等于相互作用
2. **样本量**: 网络推断需要较大样本量（建议 n > 50）
3. **过滤稀有 OTU**: 出现频率 < 10% 的 OTU 应过滤
4. **组成性校正**: 必须使用 SparCC/SPIEC-EASI 等方法

## 参考文献

1. Friedman & Alm (2012) Inferring Correlation Networks from Genomic Survey Data. *PLOS Computational Biology*. DOI: 10.1371/journal.pcbi.1002687
2. Kurtz et al. (2015) Sparse and Compositionally Robust Inference of Microbial Ecological Networks. *PLOS Computational Biology*. DOI: 10.1371/journal.pcbi.1004226
3. Tackmann et al. (2019) Rapid Inference of Direct Interactions in Large-Scale Ecological Networks from Conditional Independence. *Cell Systems*. DOI: 10.1016/j.cels.2019.08.002

---

*最后更新: 2026-03-30*
