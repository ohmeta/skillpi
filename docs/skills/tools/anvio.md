---
title: anvi'o
description: An analysis and visualization platform for 'omics data
---

# anvi'o

> An analysis and visualization platform for 'omics data

## 基本信息

| 属性 | 值 |
|------|-----|
| **类别** | visualization |
| **难度** | ⭐⭐⭐ 高级 |
| **语言** | Python |
| **GitHub Stars** | 510 |
| **标签** | visualization, interactive, comparative-genomics, binning, MAG, metagenomics, metatranscriptomics, pangenomics, science, bioinformatics, phylogenomics, population-genetics, python, javascript, anvio |

## 链接

- 📦 **代码仓库**: [https://github.com/merenlab/anvio](https://github.com/merenlab/anvio)
- 🏠 **主页**: [http://merenlab.org/software/anvio](http://merenlab.org/software/anvio)
- 📄 **论文**: [https://doi.org/10.1038/s41564-020-00743-5](https://doi.org/10.1038/s41564-020-00743-5)

## 安装

```bash
pip install anvi'o
```

## 简介

An analysis and visualization platform for 'omics data

## 使用示例


## 使用示例

```bash
# 从 FASTA 创建 Contigs DB
anvi-gen-contigs-database -f contigs.fa -o CONTIGS.db -n 'My project'

# 运行 HMMs
anvi-run-hmms -c CONTIGS.db -T 8

# 运行 NCBI COGs
anvi-run-ncbi-cogs -c CONTIGS.db -T 8

# 导入 BAM 文件
anvi-init-bam -b mapped.bam -o mapped-processed.bam
anvi-profile -i mapped-processed.bam -c CONTIGS.db -o PROFILE -T 8

# 合并多个样本
anvi-merge */PROFILE/PROFILE.db -o MERGED -c CONTIGS.db

# 交互式可视化
anvi-interactive -p MERGED/PROFILE.db -c CONTIGS.db

# 分箱和精炼
anvi-cluster-contigs -p MERGED/PROFILE.db -c CONTIGS.db -C CONCOCT --driver concoct
anvi-refine -p MERGED/PROFILE.db -c CONTIGS.db -C CONCOCT -b Bin_1
```

## 关键参数

| 命令 | 说明 |
|------|------|
| `anvi-gen-contigs-database` | 创建 Contigs 数据库 |
| `anvi-run-hmms` | 运行 HMM 搜索 |
| `anvi-profile` | 生成样本 profile |
| `anvi-merge` | 合并多个样本 |
| `anvi-interactive` | 启动交互式界面 |
| `anvi-cluster-contigs` | 自动分箱 |
| `anvi-refine` | 手动精炼分箱 |
| `anvi-export-gene-calls` | 导出基因预测 |

> 📝 更多详细参数请参考官方文档。

## 参考资源

- 📖 **官方文档**: [https://anvio.org/](https://anvio.org/)
- 🎓 **教程**: [https://merenlab.org/2016/06/22/anvio-tutorial-v2/](https://merenlab.org/2016/06/22/anvio-tutorial-v2/)
- 📄 **论文**: Eren et al. (2021) Community-led, integrated, reproducible multi-omics with anvi'o. *Nature Microbiology*. DOI: [10.1038/s41564-020-00743-5](https://doi.org/10.1038/s41564-020-00743-5)

### 相关工具

- [CheckM2](./checkm2)
- [GTDB-Tk](./gtdb_tk)
- [Prokka](./prokka)

### 相关概念

- [Functional Vs Taxonomic](../concepts/functional-vs-taxonomic)

---

*最后更新: 2026-03-30*
