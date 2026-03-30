# Fastp

超快速的 FASTQ 数据预处理和质量控制工具，集成了质量分析、过滤、修剪、去重等多种功能

## 基本信息

- **类别**: quality-control
- **版本**: 1.0
- **难度**: beginner
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/OpenGene/fastp)
- [相关论文](https://doi.org/10.1002/IMT2.107)

## 安装

```bash
# Conda
conda install -c bioconda fastp

# Docker
docker pull opengene/fastp

# 预编译二进制
wget http://opengene.org/fastp/fastp
chmod a+x ./fastp
```

## 使用示例

# 双端数据质控
fastp -i in.R1.fq.gz -I in.R2.fq.gz \
  -o out.R1.fq.gz -O out.R2.fq.gz \
  -h report.html -j report.json \
  -w 8

# 自动接头检测
fastp -i input.fq -o output.fq --detect_adapter_for_pe

# UMI 处理
fastp -i input.fq -o output.fq -U index1

## 标签

`QC` `fastq` `adapter-trimming` `filtering` `ultra-fast`

## 使用示例

```bash
# 基本质控
fastp -i input_R1.fq.gz -I input_R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz

# 单端数据
fastp -i input.fq.gz -o clean.fq.gz

# 自动检测适配器 + HTML 报告
fastp -i R1.fq.gz -I R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz --html report.html --json report.json

# 低质量碱基修剪
fastp -i R1.fq.gz -I R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz --qualified_quality_phred 20 --length_required 50

# UMI 处理
fastp -i R1.fq.gz -I R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz --umi --umi_loc read1 --umi_len 8
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-i / -I` | 输入 R1 / R2 | 必需 |
| `-o / -O` | 输出 R1 / R2 | 必需 |
| `--qualified_quality_phred` | 质量阈值 | 20 |
| `--unqualified_percent_limit` | 允许的低质量碱基占比 | 40 |
| `--length_required` | 最短读长 | 15 |
| `--adapter_sequence` | 适配器序列 | 自动检测 |
| `--html` | HTML 报告 | 无 |
| `--json` | JSON 报告 | 无 |
| `--thread` | 线程数 | 2 |
