# MetaPhlAn 4

用于从宏基因组鸟枪法测序数据中进行物种级微生物组成分析的工具（细菌、古菌、真核生物和病毒）

## 基本信息

- **类别**: profiling
- **版本**: 4.2.4
- **难度**: beginner
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/biobakery/metaphlan)
- [相关论文](https://www.nature.com/articles/s41587-023-01688-w)

## 安装

```bash
conda install -c bioconda metaphlan
```

## 使用示例

# 基本运行
metaphlan input.fastq.gz --output_file profile.txt

# 使用病毒数据库
metaphlan input.fastq.gz --output_file profile.txt --input_type fastq --nproc 8

# 菌株级分析
metaphlan input.fastq.gz --output_file profile.txt --strain_profiler true

## 标签

`metagenomics` `taxonomic-profiling` `species-level` `strain-level` `virus`
