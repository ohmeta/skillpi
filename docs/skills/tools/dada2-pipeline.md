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

## 使用示例

```bash
# R 语言使用
library(dada2)

# 1. 读取文件路径
fnFs <- sort(list.files("fastq/", pattern="_R1_001.fastq.gz", full.names=TRUE))
fnRs <- sort(list.files("fastq/", pattern="_R2_001.fastq.gz", full.names=TRUE))

# 2. 质量过滤
filtered <- filterAndTrim(fnFs, filtFs, fnRs, filtRs,
                          truncLen=c(240,200),
                          maxN=0, maxEE=c(2,2),
                          truncQ=2, rm.phix=TRUE,
                          compress=TRUE, multithread=TRUE)

# 3. 学习错误模型
errF <- learnErrors(filtFs, multithread=TRUE)
errR <- learnErrors(filtRs, multithread=TRUE)

# 4. 去重
derepFs <- derepFastq(filtFs)
derepRs <- derepFastq(filtRs)

# 5. 去噪
dadaFs <- dada(derepFs, err=errF, multithread=TRUE)
dadaRs <- dada(derepRs, err=errR, multithread=TRUE)

# 6. 合并配对
mergers <- mergePairs(dadaFs, derepFs, dadaRs, derepRs)

# 7. 构建 ASV 表
seqtab <- makeSequenceTable(mergers)

# 8. 去嵌合体
seqtab.nochim <- removeBimeraDenovo(seqtab, method="consensus")

# 9. 分类注释
taxa <- assignTaxonomy(seqtab.nochim, "silva_nr99_v138.1_train_set.fa.gz")
```

## 关键参数

| 函数 | 说明 |
|------|------|
| `filterAndTrim()` | 质量过滤和修剪 |
| `learnErrors()` | 学习测序错误模型 |
| `derepFastq()` | 快速去重 |
| `dada()` | 核心去噪算法 |
| `mergePairs()` | 合并配对端 |
| `makeSequenceTable()` | 构建 ASV 表 |
| `removeBimeraDenovo()` | 去嵌合体 |
| `assignTaxonomy()` | 分类注释 |
