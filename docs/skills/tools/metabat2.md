---
title: MetaBAT 2
description: 基于丰度和四核苷酸频率的宏基因组分箱工具，恢复高质量 MAG
---

# MetaBAT 2

> 基于丰度和四核苷酸频率的宏基因组分箱工具，恢复高质量 MAG

## 基本信息

| 属性 | 值 |
|------|-----|
| **类别** | binning |
| **难度** | ⭐⭐⭐ 高级 |
| **语言** | N/A |
| **GitHub Stars** | 0 |
| **标签** | binning, MAG, metagenomics, abundance |

## 链接

- 📦 **代码仓库**: [https://github.com/BinPro/MetaBAT2](https://github.com/BinPro/MetaBAT2)
- 📄 **论文**: [https://doi.org/10.7554/eLife.45092](https://doi.org/10.7554/eLife.45092)

## 安装

```bash
conda install -c bioconda metabat 2
```

## 简介

基于丰度和四核苷酸频率的宏基因组分箱工具，恢复高质量 MAG

## 使用示例


## 使用示例

```bash
# 1. 先生成深度文件
jgi_summarize_bam_contig_depths --outputDepth depth.txt assembly.bam

# 2. 基本分箱
metabat2 -i assembly.fa -a depth.txt -o bins/bin -t 8

# 敏感模式（适合低覆盖数据）
metabat2 -i assembly.fa -a depth.txt -o bins/bin --sensitive

# 最小 contig 长度
metabat2 -i assembly.fa -a depth.txt -o bins/bin --minContig 2500

# 与多个 BAM 合并深度
jgi_summarize_bam_contig_depths --outputDepth depth.txt sample1.bam sample2.bam sample3.bam
metabat2 -i assembly.fa -a depth.txt -o bins/bin
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-i` | 组装 FASTA | 必需 |
| `-a` | 深度文件 | 必需 |
| `-o` | 输出前缀 | 必需 |
| `-t` | 线程数 | 0 (全部) |
| `--minContig` | 最小 contig 长度 | 2500 |
| `--sensitive` | 敏感模式 | 关闭 |
| `--maxP` | 最大分箱数 | 自动 |
| `--seed` | 随机种子 | 不固定 |

> 📝 更多详细参数请参考官方文档。

## 参考资源

- 📖 **官方文档**: [https://github.com/BinPro/MetaBAT2/wiki](https://github.com/BinPro/MetaBAT2/wiki)
- 🎓 **教程**: [https://bitbucket.org/berkeleylab/metabat/src/master/](https://bitbucket.org/berkeleylab/metabat/src/master/)
- 📄 **论文**: Kang et al. (2019) MetaBAT 2: an adaptive binning algorithm for robust and efficient genome reconstruction from metagenome assemblies. *PeerJ*. DOI: [10.7717/peerj.7359](https://doi.org/10.7717/peerj.7359)

### 相关工具

- [MaxBin 2](./maxbin_2)
- [CONCOCT](./concoct)
- [DAS Tool](./das_tool)
- [CheckM2](./checkm2)

### 相关概念

- [Metagenome Assembled Genomes](../concepts/metagenome-assembled-genomes)

---

*最后更新: 2026-03-30*
