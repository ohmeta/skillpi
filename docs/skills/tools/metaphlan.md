# MetaPhlAn

用于从宏基因组测序数据中快速准确地进行微生物组谱分析的超快工具

## 基本信息

- **类别**: profiling
- **版本**: 4.0
- **难度**: beginner
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://huttenhower.sph.harvard.edu/metaphlan/)
- [代码仓库](https://github.com/biobakery/metaphlan)
- [相关论文](https://www.nature.com/articles/nmeth.3317)

## 安装

```bash
# 使用 pip 安装
pip install metaphlan

# 下载数据库
metaphlan --install

```

## 使用示例

# 运行 MetaPhlAn
metaphlan metagenome.fastq \
  --input_type fastq \
  --output_file profile.txt \
  --nproc 8


## 标签

`metagenomics` `profiling` `taxonomic` `python`
