# 工具

本页面包含所有微生物组分析工具。

## 🔬 核心工具

| 工具 | 用途 | 难度 | 来源 |
|------|------|------|------|
| [MetaPhlAn 4](tools/metaphlan-4) | 物种级分类分析 | ⭐ 入门 | bioBakery |
| [HUMAnN 3](tools/humann-3) | 功能谱分析 | ⭐⭐ 中级 | bioBakery |
| [QIIME 2](tools/qiime2-amplicon) | 扩增子分析平台 | ⭐⭐ 中级 | QIIME 2 |
| [DADA2](tools/dada2-pipeline) | ASV 去噪 | ⭐⭐ 中级 | Bioconductor |
| [mothur](tools/mothur) | 16S rRNA 分析 | ⭐⭐ 中级 | mothur.org |
| [fastp](tools/fastp) | 序列质量控制 | ⭐ 入门 | OpenGene |
| [MEGAHIT](tools/megahit) | 宏基因组组装 | ⭐⭐⭐ 高级 | MEGAHIT |

## 🎯 工具选择建议

### 初学者
从 **[fastp](tools/fastp)** 和 **[MetaPhlAn 4](tools/metaphlan-4)** 开始

### 16S 分析
使用 **[QIIME 2](tools/qiime2-amplicon)** 或 **[DADA2](tools/dada2-pipeline)**

### 宏基因组
使用 **[MEGAHIT](tools/megahit)** + **[MetaPhlAn 4](tools/metaphlan-4)** + **[HUMAnN 3](tools/humann-3)**

### 完整流程
参考 **[bioBakery Workflow](workflows/biobakery-workflow)**
