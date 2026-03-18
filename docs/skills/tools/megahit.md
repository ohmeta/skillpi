# Megahit

超快速且内存高效的 NGS 组装器，主要针对宏基因组优化，基于简洁 de Bruijn 图技术

## 基本信息

- **类别**: assembly
- **版本**: 1.2.9
- **难度**: advanced
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/voutcn/megahit)
- [相关论文](https://doi.org/10.1093/bioinformatics/btv033)

## 安装

```bash
# Conda
conda install -c bioconda megahit

# Docker
docker run -v $(pwd):/workspace vout/megahit

# 预编译二进制
wget https://github.com/voutcn/megahit/releases/download/v1.2.9/MEGAHIT-1.2.9-Linux-x86_64-static.tar.gz
tar xvzf MEGAHIT-*.tar.gz
```

## 使用示例

# 宏基因组组装
megahit -1 pe_1.fq -2 pe_2.fq -o output_dir

# 大型复杂宏基因组
megahit -1 reads_1.fq -2 reads_2.fq \
  --presets meta-large -o output_dir

# 从中间结果继续
megahit --continue -o output_dir

## 标签

`metagenomics` `assembly` `de-bruijn-graph` `memory-efficient`
