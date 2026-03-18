# 16S rRNA 测序

**难度**: ⭐ 入门

## 定义

16S rRNA 基因是原核生物核糖体小亚基的组成部分，长度约 1500bp，包含 9 个可变区（V1-V9）和保守区，广泛用于微生物分类和系统发育分析。

## 原理

1. **保守区** - 用于设计通用引物（如 27F/1492R）
2. **可变区** - 包含物种特异性序列
3. **系统发育** - 通过序列比对构建进化树

## 常用引物

- **V3-V4 区**: 341F-805R
- **V4 区**: 515F-806R (Earth Microbiome Project)

## 分析流程

```
质控 → 拼接 → 去噪/OTU 聚类 → 物种注释 → 多样性分析
```

## 相关工具

- [QIIME 2](../tools/qiime2-amplicon) - 扩增子分析平台
- [DADA2](../tools/dada2-pipeline) - ASV 去噪
- [mothur](../tools/mothur) - 16S 分析工具

## 相关概念

- [宏基因组测序](metagenomics-sequencing)
- [Alpha 多样性](alpha-diversity)
