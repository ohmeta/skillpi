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

## 使用示例

```bash
# 宏基因组组装（配对端）
megahit -1 R1.fq.gz -2 R2.fq.gz -o megahit_out --num-cpu-threads 16

# 交错配对模式
megahit --12 interleaved.fq.gz -o megahit_out -t 16

# 长读长组装
megahit --long long_reads.fq.gz -o megahit_out_lr

# 混合组装（短+长读长）
megahit -1 R1.fq.gz -2 R2.fq.gz --long long_reads.fq.gz -o megahit_out_hybrid

# 使用预设参数
megahit -1 R1.fq.gz -2 R2.fq.gz --presets meta-large -o megahit_out --min-contig-len 1000
```

## 关键参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-1 / -2` | 配对端输入 | 可选 |
| `--12` | 交错配对输入 | 可选 |
| `--long` | 长读长输入 | 可选 |
| `-o` | 输出目录 | megahit_out |
| `-t / --num-cpu-threads` | 线程数 | CPU 核心数 |
| `--min-contig-len` | 最小 contig 长度 | 200 |
| `--presets` | 预设 (meta-sensitive/meta-large) | meta |

## 参考资源

- 📖 **官方文档**: [https://github.com/voutcn/megahit/wiki](https://github.com/voutcn/megahit/wiki)
- 🎓 **教程**: [https://github.com/voutcn/megahit/wiki](https://github.com/voutcn/megahit/wiki)
- 📄 **论文**: Li et al. (2015) MEGAHIT: an ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph. *Bioinformatics*. DOI: [10.1093/bioinformatics/btv033](https://doi.org/10.1093/bioinformatics/btv033)

### 相关工具

- [metaSPAdes](./metaspades)
- [Flye](./flye)
- [Canu](./canu)

### 相关概念

- [Metagenome Assembled Genomes](../concepts/metagenome-assembled-genomes)
