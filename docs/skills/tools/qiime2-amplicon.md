# QIIME 2 (Amplicon)

强大的微生物组扩增子分析平台，支持从原始测序数据到统计分析和可视化的完整流程

## 基本信息

- **类别**: amplicon-analysis
- **版本**: N/A
- **难度**: intermediate
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/qiime2/qiime2)
- [相关论文](https://doi.org/10.1038/s41587-019-0209-9)

## 安装

```bash
# Conda 安装（推荐）
conda install -c qiime2 -c conda-forge qiime2

# Docker 安装
docker pull qiime2/core:2024.2
```

## 使用示例

# 导入数据
qiime tools import \
  --type 'SampleData[SequencesWithQuality]' \
  --input-path demux \
  --output-path demux.qza

# DADA2 去噪
qiime dada2 denoise-paired \
  --i-demultiplexed-seqs demux.qza \
  --o-table table.qza \
  --o-representative-sequences rep-seqs.qza \
  --o-denoising-stats stats.qza

# 多样性分析
qiime diversity core-metrics-phylogenetic \
  --i-phylogeny rooted-tree.qza \
  --i-table table.qza \
  --p-sampling-depth 10000 \
  --output-dir core-metrics-results

## 标签

`16S` `amplicon` `its` `analysis` `visualization` `reproducible`

## 使用示例

```bash
# 导入数据
qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path manifest.csv \
  --output-path paired-end-demux.qza \
  --input-format PairedEndFastqManifestPhred33

# DADA2 去噪
qiime dada2 denoise-paired \
  --i-demultiplexed-seqs paired-end-demux.qza \
  --p-trunc-len-f 240 \
  --p-trunc-len-r 200 \
  --o-table table.qza \
  --o-representative-sequences rep-seqs.qza \
  --o-denoising-stats stats.qza

# Alpha/Beta 多样性
qiime diversity core-metrics-phylogenetic \
  --i-phylogeny rooted-tree.qza \
  --i-table table.qza \
  --p-sampling-depth 10000 \
  --output-dir core-metrics-results

# 分类注释
qiime feature-classifier classify-sklearn \
  --i-classifier classifier.qza \
  --i-reads rep-seqs.qza \
  --o-classification taxonomy.qza
```

## 关键参数

| 命令 | 说明 |
|------|------|
| `qiime tools import` | 导入数据 |
| `qiime dada2 denoise-paired` | DADA2 去噪 |
| `qiime diversity core-metrics-phylogenetic` | 多样性分析 |
| `qiime feature-classifier classify-sklearn` | 分类注释 |
| `qiime taxa barplot` | 分类柱状图 |
| `qiime emperor plot` | PCoA 3D 可视化 |
