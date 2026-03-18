# Tools

本页面包含所有微生物组分析工具，按类别组织。

## 🔬 核心工具 (Core Tools)

| 工具 | 用途 | 难度 | 来源 |
|------|------|------|------|
| [**MetaPhlAn 4**](tools/metaphlan-4.md) | 物种级分类分析 | ⭐ 入门 | bioBakery |
| [**HUMAnN 3**](tools/humann-3.md) | 功能谱分析 | ⭐⭐ 中级 | bioBakery |
| [**QIIME 2**](tools/qiime2-amplicon.md) | 扩增子分析平台 | ⭐⭐ 中级 | QIIME 2 |
| [**DADA2**](tools/dada2-pipeline.md) | ASV 去噪 | ⭐⭐ 中级 | Bioconductor |
| [**mothur**](tools/mothur.md) | 16S rRNA 分析 | ⭐⭐ 中级 | mothur.org |
| [**fastp**](tools/fastp.md) | 序列质量控制 | ⭐ 入门 | OpenGene |
| [**MEGAHIT**](tools/megahit.md) | 宏基因组组装 | ⭐⭐⭐ 高级 | MEGAHIT |

## 📦 其他工具 (Additional Tools)

| 工具 | 用途 | 难度 |
|------|------|------|
| [Emperor](tools/emperor.md) | 微生物组可视化 | ⭐⭐ 中级 |
| [microbiome](tools/microbiome.md) | R 语言分析包 | ⭐⭐ 中级 |
| [scikit-bio](tools/scikit-bio.md) | Python 生物信息库 | ⭐⭐ 中级 |
| [biom-format](tools/biom-format.md) | BIOM 格式支持 | ⭐ 入门 |

## 🔍 按类别筛选

### 物种分析 (Taxonomic Profiling)
- [MetaPhlAn 4](tools/metaphlan-4.md) - 物种级分析
- [QIIME 2](tools/qiime2-amplicon.md) - 扩增子分析
- [mothur](tools/mothur.md) - 16S 分析

### 功能分析 (Functional Analysis)
- [HUMAnN 3](tools/humann-3.md) - 通路和基因功能

### 质量控制 (Quality Control)
- [fastp](tools/fastp.md) - FASTQ 质控和预处理

### 组装 (Assembly)
- [MEGAHIT](tools/megahit.md) - 宏基因组组装

### 可视化 (Visualization)
- [Emperor](tools/emperor.md) - 微生物组数据可视化

### 编程库 (Libraries)
- [scikit-bio](tools/scikit-bio.md) - Python 库
- [microbiome](tools/microbiome.md) - R 包
- [biom-format](tools/biom-format.md) - BIOM 格式

---

## 📊 工具统计

- **核心工具**: 7 个
- **其他工具**: 4 个
- **总计**: 11 个工具

## 🎯 选择工具的建议

### 如果你是初学者
从 **[fastp](tools/fastp.md)** 和 **[MetaPhlAn 4](tools/metaphlan-4.md)** 开始

### 如果你做 16S 分析
使用 **[QIIME 2](tools/qiime2-amplicon.md)** 或 **[DADA2](tools/dada2-pipeline.md)**

### 如果你做宏基因组
使用 **[MEGAHIT](tools/megahit.md)** + **[MetaPhlAn 4](tools/metaphlan-4.md)** + **[HUMAnN 3](tools/humann-3.md)**

### 如果你需要完整流程
参考 **[bioBakery Workflow](workflows/biobakery-workflow.md)**
