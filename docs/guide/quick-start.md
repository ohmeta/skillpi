# 快速开始

## 🎯 选择你的学习路径

### 路径 1: 扩增子分析 (16S/ITS)

适合研究细菌、真菌群落组成。

```
1. 学习 16S rRNA 测序概念
   ↓
2. 使用 fastp 进行质量控制
   ↓
3. 使用 QIIME 2 或 DADA2 分析
   ↓
4. 多样性分析和可视化
```

**推荐工具**:
- [QIIME 2](/skills/tools/qiime2-amplicon) - 完整分析平台
- [DADA2](/skills/tools/dada2-pipeline) - ASV 去噪
- [fastp](/skills/tools/fastp) - 质量控制

### 路径 2: 宏基因组分析

适合研究微生物群落的基因和功能。

```
1. 学习宏基因组测序概念
   ↓
2. 使用 fastp 进行质量控制
   ↓
3. 使用 MEGAHIT 进行组装
   ↓
4. 使用 MetaPhlAn 进行物种分析
   ↓
5. 使用 HUMAnN 进行功能分析
```

**推荐工具**:
- [MetaPhlAn 4](/skills/tools/metaphlan-4) - 物种分析
- [HUMAnN 3](/skills/tools/humann-3) - 功能分析
- [MEGAHIT](/skills/tools/megahit) - 组装
- [fastp](/skills/tools/fastp) - 质量控制

### 路径 3: 完整工作流程

使用集成平台，一站式分析。

**推荐**:
- [bioBakery Workflow](/skills/workflows/biobakery-workflow) - Huttenhower 实验室集成平台

## 📚 前置知识

### 必需
- 基础生物学知识
- 命令行基础 (Linux/Mac)
- 统计学基础

### 推荐
- Python 或 R 编程基础
- 高通量测序原理
- 微生物学基础

## 🛠️ 环境准备

### 基础环境
```bash
# 安装 Conda (推荐)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# 或安装 Mamba (更快)
conda install -c conda-forge mamba
```

### 常用工具安装
```bash
# fastp
conda install -c bioconda fastp

# MetaPhlAn
conda install -c bioconda metaphlan

# HUMAnN
pip install humann
```

## 📖 学习资源

### 官方文档
- [QIIME 2 教程](https://docs.qiime2.org/)
- [bioBakery Wiki](https://github.com/biobakery/biobakery/wiki)
- [DADA2 教程](https://benjjneb.github.io/dada2/tutorial.html)

### 社区论坛
- [QIIME 2 论坛](https://forum.qiime2.org/)
- [bioBakery 论坛](https://forum.biobakery.org/)

### 书籍
- 《微生物组分析》
- 《Macro-omics: Techniques and Applications》

## 💡 下一步

- 查看 [工具列表](/skills/tools) 了解所有工具
- 学习 [核心概念](/skills/concepts) 理解基本原理
- 探索 [工作流](/skills/workflows) 获取完整分析方案
