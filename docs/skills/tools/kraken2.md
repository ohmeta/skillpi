---
title: Kraken 2
description: The second version of the Kraken taxonomic sequence classification system 
---

# Kraken 2

> The second version of the Kraken taxonomic sequence classification system 

## 基本信息

| 属性 | 值 |
|------|-----|
| **类别** | taxonomic-classification |
| **难度** | ⭐⭐ 中级 |
| **语言** | C++ |
| **GitHub Stars** | 887 |
| **标签** | taxonomic-classification, kmer, metagenomics, fast |

## 链接

- 📦 **代码仓库**: [https://github.com/DerrickWood/kraken2](https://github.com/DerrickWood/kraken2)
- 📄 **论文**: [https://doi.org/10.1186/s13059-019-1891-0](https://doi.org/10.1186/s13059-019-1891-0)

## 安装

```bash
conda install -c bioconda kraken 2
```

## 简介

The second version of the Kraken taxonomic sequence classification system 

## 使用示例


## 使用示例

```bash
# 基本分类
kraken2 --db /path/to/kraken2_db --output result.kreport --report result.report input_1.fastq input_2.fastq

# 使用预建数据库
kraken2 --db /path/to/kraken2_db --paired --output result.kreport --report result.report sample_1.fq.gz sample_2.fq.gz

# 多线程加速
kraken2 --db /path/to/kraken2_db --threads 16 --output result.kreport --report result.report input.fastq

# 与 Bracken 配合估算丰度
bracken -d /path/to/kraken2_db -i result.report -o result.bracken -r 150 -l S
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--db` | Kraken2 数据库路径 | 必需 |
| `--output` | Kraken 格式输出 | 必需 |
| `--report` | 报告文件 | 必需 |
| `--threads` | 线程数 | 1 |
| `--paired` | 配对模式 | 关闭 |
| `--confidence` | 分类置信度阈值 | 0.05 |
| `--minimum-hit-groups` | 最小命中组数 | 2 |

> 📝 更多详细参数请参考官方文档。

## 参考资源

- 📖 **官方文档**: [https://github.com/DerrickWood/kraken2/wiki](https://github.com/DerrickWood/kraken2/wiki)
- 🎓 **教程**: [https://github.com/DerrickWood/kraken2/wiki/Manual](https://github.com/DerrickWood/kraken2/wiki/Manual)
- 📄 **论文**: Wood et al. (2019) Improved metagenomic analysis with Kraken 2. *Genome Biology*. DOI: [10.1186/s13059-019-1891-0](https://doi.org/10.1186/s13059-019-1891-0)

### 相关工具

- [Bracken](./bracken)
- [MetaPhlAn 4](./metaphlan-4)
- [Centrifuge](./centrifuge)

### 相关概念

- [Functional Vs Taxonomic](../concepts/functional-vs-taxonomic)

---

*最后更新: 2026-03-30*
