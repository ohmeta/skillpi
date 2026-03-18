# DADA2

高分辨率的样本推断算法，可从扩增子测序数据中精确识别序列变异

## 基本信息

- **类别**: denoising
- **版本**: 1.30
- **难度**: intermediate
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://benjjneb.github.io/dada2/)
- [代码仓库](https://github.com/benjjneb/dada2)
- [相关论文](https://www.nature.com/articles/nmeth.3869)

## 安装

```bash
# 在 R 中安装
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("dada2")

```

## 使用示例

# R 代码示例
library(dada2)

# 过滤和截断
filtFs <- filterAndTrim(fnFs, filtFs, truncLen=c(240,0))

# 学习错误率
errF <- learnErrors(filtFs)

# 去噪
dadaFs <- dada(filtFs, err=errF)


## 标签

`16S` `denoising` `R` `ASV` `amplicon`
