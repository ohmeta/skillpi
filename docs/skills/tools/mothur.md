# Mothur

用于微生物生态学分析的综合工具，专注于 16S rRNA 基因序列分析和微生物群落多样性研究

## 基本信息

- **类别**: amplicon-analysis
- **版本**: 1.48.5
- **难度**: intermediate
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/mothur/mothur)
- [相关论文](https://doi.org/10.1128/AEM.01541-09)

## 安装

```bash
# Ubuntu/Debian
sudo apt-get install mothur

# Conda
conda install -c bioconda mothur

# 源码编译
git clone https://github.com/mothur/mothur.git
cd mothur
make -j
```

## 使用示例

# 标准 MiSeq SOP
mothur > make.contigs(file=stability.files, processors=8)
mothur > screen.seqs(fasta=current, maxambig=0, maxlength=275)
mothur > unique.seqs(fasta=current)
mothur > align.seqs(fasta=current, reference=silva.v4.fasta)
mothur > filter.seqs(fasta=current, vertical=T, trump=.)
mothur > pre.cluster(fasta=current, diffs=2)
mothur > chimera.vsearch(fasta=current)
mothur > classify.seqs(fasta=current, reference=trainset9_032012.pds.fasta)
mothur > cluster.split(fasta=current, count=current, splitmethod=classify)

## 标签

`16S` `amplicon` `OTU` `diversity` `SOP`
