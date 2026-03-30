---
title: 数据标准化与归一化
description: 微生物组数据的标准化方法：rarefaction、CSS、TMM、CLR 等
---

# 数据标准化与归一化

> 测序深度差异是微生物组分析的核心技术挑战之一。不同样本的 reads 数量可能相差数十倍，直接比较丰度会产生偏差。

## 为什么需要标准化？

```
样本A: 总 reads = 50,000  → OTU_X = 500 reads (1%)
样本B: 总 reads = 500,000 → OTU_X = 2000 reads (0.4%)

OTU_X 在样本B中 reads 数是A的4倍，但相对丰度反而更低！
```

## 主要方法对比

| 方法 | 原理 | 优点 | 缺点 | 适用场景 |
|------|------|------|------|----------|
| **Rarefaction** | 随机抽样到最小深度 | 简单直观 | 丢弃数据，统计效力降低 | Alpha 多样性 |
| **CSS** (Cumulative Sum Scaling) | 累积求和缩放 | 保留零值 | 对假阳性敏感 | QIIME / metagenomeSeq |
| **TMM** (Trimmed Mean of M-values) | 修剪均值 | 适用于 RNA-seq | 假设大部分特征不变 | edgeR |
| **CLR** (Centered Log-Ratio) | 几何均值为中心的对数比 | 组成性数据分析 | 不能处理零值 | ANCOM-BC, ALDEx2 |
| **RLE** (Relative Log Expression) | 相对对数表达 | 稳健 | 假设大部分特征不变 | DESeq2 |
| **CPM** (Counts Per Million) | 简单比例缩放 | 快速 | 不校正组成性偏差 | 初步探索 |

## Rarefaction（稀释）

最直观的方法：将所有样本随机抽样到相同深度。

```r
# R (phyloseq)
ps_rare <- rarefy_even_depth(ps, sample.size = 10000, rngseed = 42)

# Python (scikit-biomove)
from biomove import rarefy
rarefied = rarefy(table, depth=10000)
```

**⚠️ 注意**: Rarefaction 会丢弃数据，且每次结果不同（需设随机种子）。不推荐用于差异丰度分析。

## CLR 变换

CoDA 方法的核心：

```r
# R (microbiome package)
clr_transformed <- microbiome::transform(ps, "clr")

# Python
import numpy as np
def clr(x):
    log_x = np.log(x + 1e-6)  # 伪计数
    return log_x - np.mean(log_x)
```

## 实践建议

1. **Alpha 多样性**: 使用 rarefaction 统一深度
2. **差异丰度分析**: 使用方法内置的标准化（ANCOM-BC, DESeq2, ALDEx2 各自处理）
3. **可视化**: 探索性分析可简单用比例（percentages）
4. **不要叠加**: 不要先 rarefy 再用 DESeq2 — 选一种方法坚持到底

## 参考文献

1. McMurdie & Holmes (2014) Waste not, want not: why rarefying microbiome data is inadmissible. *PLOS Computational Biology*. DOI: 10.1371/journal.pcbi.1003531
2. Gloor et al. (2017) Microbiome Datasets Are Compositional. *Frontiers in Microbiology*. DOI: 10.3389/fmicb.2017.02224
3. Weiss et al. (2017) Normalization and microbial differential abundance strategies depend upon data characteristics. *Microbiome*. DOI: 10.1186/s40168-017-0237-y

---

*最后更新: 2026-03-30*
