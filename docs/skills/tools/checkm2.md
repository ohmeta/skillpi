---
title: CheckM2
description: Assessing the quality of metagenome-derived genome bins using machine learning
---

# CheckM2

> Assessing the quality of metagenome-derived genome bins using machine learning

## 基本信息

| 属性 | 值 |
|------|-----|
| **类别** | quality-assessment |
| **难度** | ⭐⭐ 中级 |
| **语言** | Scilab |
| **GitHub Stars** | 252 |
| **标签** | quality-assessment, MAG, machine-learning, completeness |

## 链接

- 📦 **代码仓库**: [https://github.com/chklovski/CheckM2](https://github.com/chklovski/CheckM2)
- 📄 **论文**: [https://doi.org/10.1038/s41592-023-01940-w](https://doi.org/10.1038/s41592-023-01940-w)

## 安装

```bash
conda install -c bioconda checkm2
```

## 简介

Assessing the quality of metagenome-derived genome bins using machine learning

## 使用示例


## 使用示例

```bash
# 预测基因组质量
checkm2 predict --threads 8 --input bins/ --output-directory checkm2_output

# 指定输出格式
checkm2 predict --threads 8 --input bins/ --output-directory checkm2_output --output-format tab

# 使用 Diamond 而非 MMseqs2（更快）
checkm2 predict --threads 8 --input bins/ --output-directory checkm2_output --database_path /path/to/CheckM2_database

# 查看结果
cat checkm2_output/quality_report.tsv
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | MAG 目录或文件列表 | 必需 |
| `--output-directory` | 输出目录 | 必需 |
| `--threads` | 线程数 | 1 |
| `--output_format` | 输出格式 (tab/csv) | tab |
| `--database_path` | CheckM2 数据库路径 | 内置 |
| `--extension` | 基因组文件扩展名 | fasta |

> 📝 更多详细参数请参考官方文档。

---

*最后更新: 2026-03-30*
