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
