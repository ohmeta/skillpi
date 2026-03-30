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

## 使用示例

```bash
# 基本物种分类
metaphlan input.fastq --bowtie2db /path/to/db --nproc 8 --output_file profiled.txt

# 配对端数据
metaphlan sample_1.fq.gz,sample_2.fq.gz --bowtie2db /path/to/db --nproc 8 --input_type fastq --output_file profile.txt

# 生成 Bowtie2 比对文件（可复用）
metaphlan input.fastq --bowtie2db /path/to/db --bowtie2out mapped.bz2 --nproc 8 --input_type fastq --output_file profile.txt

# 批量处理 + 合并
merge_metaphlan_tables.py sample1_profile.txt sample2_profile.txt > merged_abundance_table.txt

# 菌株水平分析 (StrainPhlAn)
strainphlan -s SRS014464.bz2 --output_dir output --nprocs 4 --marker_in_n_markers 50 --sample_with_n_markers 50
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--bowtie2db` | 数据库路径 | 必需 |
| `--nproc` | 线程数 | 1 |
| `--input_type` | 输入格式 (fastq/fasta/bowtie2out) | 自动检测 |
| `--output_file` | 输出文件 | stdout |
| `--tax_lev` | 分类级别 (t/p/c/o/f/g/s) | 'a' (all) |
| `--unclassified_estimation` | 估算未分类比例 | 关闭 |
