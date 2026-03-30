---
title: 组成性数据分析 (CoDA)
description: 微生物组数据的组成性特征及其分析方法
---

# 组成性数据分析 (CoDA)

> **CoDA** = Compositional Data Analysis，专门处理总和为常数（如100%）的数据的统计框架。微生物组丰度数据天然是组成性的。

## 为什么微生物组数据是组成性的？

测序仪报告的是**相对丰度**（reads 数量），而非绝对丰度：

```
实际绝对丰度:  A=1000, B=500, C=500   → 总数=2000
测到的 reads:  A=500,  B=250, C=250   → 总数=1000

如果 A 的绝对丰度翻倍:
实际绝对丰度:  A=2000, B=500, C=500   → 总数=3000
测到的 reads:  A=667,  B=167, C=167   → 总数=1000

B 和 C 的"丰度"下降了，但它们的绝对丰度没变！
```

这就是**组成性偏差 (compositional bias)**：一个物种的丰度变化会影响其他所有物种的相对丰度。

## 问题的本质

### 闭合效应 (Closure Effect)

测序数据经过"闭合"处理（除以总 reads 数），导致：
- **负相关伪影**: 即使物种间完全独立，也会出现负相关
- **虚假差异**: 一个物种的真实变化会"传染"给其他物种
- **标准方法失效**: t 检验、DESeq2 等假设独立性的方法不再适用

### 对比率空间 (Ratio Space)

CoDA 的核心思想：不看绝对值，看**比率**

```
CLR 变换: clr(x_i) = log(x_i / g(x))
其中 g(x) = (x_1 * x_2 * ... * x_D)^(1/D)  # 几何均值
```

CLR (Centered Log-Ratio) 变换将组成性数据转换到欧几里得空间。

## 微生物组 CoDA 方法对比

| 方法 | 原理 | 优点 | 缺点 |
|------|------|------|------|
| **ANCOM-BC** | 偏差校正 + 线性模型 | 控制 FDR，支持多组比较 | 需要较大样本量 |
| **ALDEx2** | 贝叶斯 Dirichlet-multinomial | 鲁棒性好，假阳性低 | 计算较慢 |
| **ANCOM** | 对比率检验 | 理论优雅 | 不报告效应量 |
| **DESeq2** | 负二项分布 | 广泛使用，文档丰富 | 对组成性数据假阳性高 |
| **LEfSe** | LDA + Kruskal-Wallis | 直观可视化 | 统计基础较弱 |

### Benchmark 结论 (Naylor et al., 2022)

> 在 38 个 16S 数据集上比较 14 种方法：**ALDEx2** 和 **ANCOM-II** 产生最一致的结果。

## 实践建议

### 推荐流程

```r
library(ANCOMBC)
library(phyloseq)

# 1. 准备 phyloseq 对象
ps <- phyloseq(otu_table, sample_data, tax_table)

# 2. ANCOM-BC 分析
result <- ancombc2(
  data = ps,
  fix_formula = "Group + Age + Sex",  # 固定效应
  p_adj_method = "BH",                 # FDR 校正
  lib_cut = 1000,                      # 最低 reads 数
  group = "Group"                       # 分组变量
)

# 3. 查看结果
result$res  # log fold change, SE, W-stat, p-value
```

### 注意事项

1. **过滤稀有 OTU**: 移除出现在 <10% 样本中的 OTU
2. **添加伪计数**: 处理零值（CoDA 方法通常内置处理）
3. **考虑混杂因素**: 在模型中加入批次、年龄等协变量
4. **多方法验证**: 至少用 2 种方法确认结果
5. **报告效应量**: 不只看 p 值，也要看 log fold change

## 2025 新工具：dar 包

[dar R 包](https://doi.org/10.1101/2025.02.07.637000) 将 DESeq2、ALDEx2、ANCOM-BC、metagenomeSeq 整合为一个共识框架：

```r
library(dar)
result <- differential_abundance(ps, method = "consensus")
```

## 相关概念

- [Alpha 多样性](alpha-diversity)
- [ANCOM-BC](../tools/ancom_bc)
- [LEfSe](../tools/lefse)
- [DESeq2](../tools/deseq2)
- [phyloseq](../tools/phyloseq)

## 参考文献

1. Gloor et al. (2017) Microbiome Datasets Are Compositional: And This Is Not Optional. *Frontiers in Microbiology*. DOI: 10.3389/fmicb.2017.02224
2. Lin et al. (2020) Analysis of compositions of microbiomes with bias correction. *Nature Communications*. DOI: 10.1038/s41467-020-17041-7
3. Naylor et al. (2022) Microbiome differential abundance methods produce different results across 38 datasets. *Nature Communications*. DOI: 10.1038/s41467-022-28034-z
4. Lin & Peddada (2024) Multigroup analysis of compositions of microbiomes with covariate adjustments and structural zeros. *Nature Methods*. DOI: 10.1038/s41592-023-02092-7

---

*最后更新: 2026-03-30*
