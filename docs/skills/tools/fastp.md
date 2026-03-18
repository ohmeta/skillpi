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
