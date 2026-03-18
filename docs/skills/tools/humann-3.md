# HUMAnN 3

用于从宏基因组或宏转录组数据中高效、准确地分析微生物群落通路存在/缺失和丰度的流程（功能分析）

## 基本信息

- **类别**: functional-profiling
- **版本**: 3.0
- **难度**: intermediate
- **最后更新**: 2026-03-18

## 链接

- [官方网站](https://github.com/biobakery/humann)
- [相关论文](https://doi.org/10.7554/eLife.65088)

## 安装

```bash
# 推荐安装
pip install humann

# 或从源码
git clone https://github.com/biobakery/humann
cd humann
python setup.py install
```

## 使用示例

# 基本运行
humann --input sample.fastq --output output_dir

# 使用特定数据库
humann --input sample.fastq --output output_dir --threads 8

# 标准化输出
humann_renorm_table --input sample_genefamilies.tsv \
    --output sample_genefamilies_relab.tsv --units relab

## 标签

`metagenomics` `functional-profiling` `pathway-analysis` `metatranscriptomics`
