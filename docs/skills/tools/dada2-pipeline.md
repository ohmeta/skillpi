# DADA2

高分辨率的样本推断算法，可从扩增子测序数据中精确识别序列变异（ASV），替代传统的 OTU 聚类方法

## 基本信息

- **类别**: denoising
- **版本**: 1.30
- **难度**: intermediate
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/benjjneb/dada2)
- [相关论文](https://doi.org/10.1038/nmeth.3869)

## 安装

```bash
# R/Bioconductor 安装
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("dada2")

# 或使用 QIIME 2 插件
qiime dada2 denoise-paired ...
```

## 使用示例

# R 代码示例
library(dada2)

# 1. 过滤和截断
filtFs <- filterAndTrim(fnFs, filtFs, truncLen=c(240,0))

# 2. 学习错误率
errF <- learnErrors(filtFs)

# 3. 去噪
dadaFs <- dada(filtFs, err=errF)

# 4. 合并双端 reads
mergers <- mergePairs(dadaFs, filtFs, dadaRs, filtRs)

# 5. 构建 ASV 表
seqtab <- makeSequenceTable(mergers)

## 标签

`16S` `denoising` `ASV` `amplicon` `R` `bioconductor`
