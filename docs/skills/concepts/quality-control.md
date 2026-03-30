---
title: 测序质量控制
description: 微生物组测序数据的质量评估和质控流程
---

# 测序质量控制

> 质量控制 (QC) 是任何生物信息分析的第一步，也是最重要的一步。"Garbage in, garbage out."

## QC 流程

```
原始 FASTQ → 质量评估 → 适配器去除 → 低质量修剪 → 过短过滤 → 污染去除 → 清洁数据
              ↓           ↓            ↓           ↓           ↓
           FastQC     fastp/       fastp/     fastp/     Bowtie2/
           MultiQC    Cutadapt     Trimmomatic Trimmomatic Kraken 2
```

## 质量评估工具

### FastQC

```bash
# 单个样本
fastqc input.fastq.gz -o qc_reports/ -t 8

# 批量
fastqc *.fastq.gz -o qc_reports/ -t 8
```

关键指标：
- **Per base quality**: Phred score ≥20 为合格，≥30 为优秀
- **Adapter content**: 应 <5%
- **GC content**: 应与参考基因组一致
- **Sequence duplication**: 过高可能表示 PCR 过度扩增

### MultiQC

```bash
# 汇总多个 FastQC 报告
multiqc qc_reports/ -o multiqc_output/
```

## 质控工具对比

| 工具 | 速度 | 特点 | 推荐场景 |
|------|------|------|---------|
| **fastp** | ⚡⚡⚡ | 自动检测适配器，HTML 报告，UMI 支持 | **首选** |
| **Trimmomatic** | ⚡⚡ | 经典工具，功能全面 | 需要精细控制 |
| **Cutadapt** | ⚡⚡ | 精确适配器去除 | 特殊适配器 |
| **Sickle** | ⚡ | 轻量级质量修剪 | 快速简单任务 |
| **BBDuk** | ⚡⚡⚡ | BBMap 套件，功能丰富 | 大规模数据 |

## fastp 最佳实践

```bash
# 推荐参数（宏基因组）
fastp \
  -i sample_R1.fq.gz \
  -I sample_R2.fq.gz \
  -o clean_R1.fq.gz \
  -O clean_R2.fq.gz \
  --qualified_quality_phred 20 \
  --unqualified_percent_limit 40 \
  --length_required 50 \
  --detect_adapter_for_pe \
  --correction \
  --html sample_qc.html \
  --json sample_qc.json \
  --thread 8

# 参数说明:
# --qualified_quality_phred 20 : 质量分 ≥20 视为合格
# --unqualified_percent_limit 40 : 允许 40% 碱基低于阈值
# --length_required 50 : 过滤 <50bp 的读段
# --detect_adapter_for_pe : 自动检测配对端适配器
# --correction : 配对端重叠区域纠错
```

## QC 检查清单

- [ ] 原始 reads 数量统计
- [ ] FastQC 报告：per-base quality
- [ ] 适配器含量检查
- [ ] GC 含量分布
- [ ] 序列重复水平
- [ ] 质控后 reads 数量和比例
- [ ] 配对端 reads 匹配率
- [ ] 污染检查（可选，低生物量样本必做）

## 参考文献

1. Chen et al. (2018) fastp: an ultra-fast all-in-one FASTQ preprocessor. *Bioinformatics*. DOI: 10.1093/bioinformatics/bty560
2. Ewels et al. (2016) MultiQC: summarize analysis results for multiple tools and samples in a single report. *Bioinformatics*. DOI: 10.1093/bioinformatics/btw354

---

*最后更新: 2026-03-30*
