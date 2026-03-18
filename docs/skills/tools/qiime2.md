# QIIME2

强大的、可扩展的微生物组分析平台，支持从原始测序数据到统计分析和可视化的完整流程

## 基本信息

- **类别**: analysis
- **版本**: 2024.2
- **难度**: intermediate
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://qiime2.org/)
- [代码仓库](https://github.com/biocore/qiime2)
- [相关论文](https://www.nature.com/articles/nbt.4260)

## 安装

```bash
# 使用 conda 安装
conda install -c qiime2 -c conda-forge qiime2

# 或使用 Docker
docker pull qiime2/core:2024.2

```

## 使用示例

# 导入数据
qiime tools import \
  --type 'SampleData[SequencesWithQuality]' \
  --input-path demux \
  --output-path demux.qza

# 质量过滤和去噪
qiime dada2 denoise-paired \
  --i-demultiplexed-seqs demux.qza \
  --o-table table.qza \
  --o-representative-sequences rep-seqs.qza


## 标签

`16S` `metagenomics` `python` `denoising` `visualization`
