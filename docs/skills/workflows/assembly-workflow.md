# 宏基因组组装工作流

从原始宏基因组测序数据到完整基因组的完整分析流程

## 基本信息

- **输入格式**: Illumina paired-end FASTQ
- **输出格式**: MAGs (Metagenome-Assembled Genomes) in FASTA format
- **难度**: advanced

## 使用工具

- FastQC
- Trimmomatic
- MEGAHIT
- Prodigal
- MetaBAT2
- CheckM

## 步骤

1. 1. 质量控制：使用 FastQC 和 MultiQC 评估数据质量
2. 2. 预处理：使用 Trimmomatic 或 fastp 去除低质量 reads 和 adapter
3. 3. 组装：使用 MEGAHIT 或 metaSPAdes 进行 de novo 组装
4. 4. 基因预测：使用 Prodigal 预测开放阅读框
5. 5. 分箱：使用 MetaBAT2 或 MaxBin2 进行基因组分箱
6. 6. 质量评估：使用 CheckM 评估 MAG 质量
7. 7. 注释：使用 eggNOG-mapper 或 DRAM 进行功能注释
