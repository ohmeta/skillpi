# SkillPI 真实世界数据更新报告

## 🎉 概述

SkillPI 已从**真实世界文档**更新了微生物组信息学工具目录，包含来自官方 GitHub 仓库、文档网站和论文的详细、准确信息。

---

## 📊 更新统计

| 类别 | 数量 | 详情 |
|------|------|------|
| **工具** | 7 个 | MetaPhlAn 4, HUMAnN 3, QIIME 2, DADA2, mothur, fastp, MEGAHIT |
| **工作流** | 1 个 | bioBakery 集成分析流程 |
| **概念** | 2 个 | 16S rRNA 测序，宏基因组测序 |
| **总计** | 10 个 | 涵盖微生物组分析全流程 |

---

## 🛠️ 新增工具详解

### 1. MetaPhlAn 4 ⭐

**来源**: [GitHub - biobakery/metaphlan](https://github.com/biobakery/metaphlan)

| 属性 | 详情 |
|------|------|
| **版本** | 4.2.4 (2025-10-21) |
| **用途** | 物种级微生物组成分析（细菌、古菌、真核生物、病毒） |
| **安装** | `conda install -c bioconda metaphlan` |
| **难度** | ⭐ 入门 |
| **论文** | Nature Biotechnology 2023 |

**关键特性**:
- ✅ 物种级分辨率
- ✅ 菌株级分析 (StrainPhlAn)
- ✅ 病毒模块支持
- ✅ 快速准确（基于标记基因）

**使用示例**:
```bash
# 基本运行
metaphlan input.fastq.gz --output_file profile.txt

# 菌株级分析
metaphlan input.fastq.gz --output_file profile.txt --strain_profiler true
```

---

### 2. HUMAnN 3 ⭐

**来源**: [GitHub - biobakery/humann](https://github.com/biobakery/humann)

| 属性 | 详情 |
|------|------|
| **版本** | 3.0 |
| **用途** | 宏基因组/宏转录组功能谱分析 |
| **安装** | `pip install humann` |
| **难度** | ⭐⭐ 中级 |
| **论文** | eLife 2021 |

**关键特性**:
- ✅ 基因家族丰度分析
- ✅ 代谢通路丰度分析
- ✅ 自动整合 MetaPhlAn 分类信息
- ✅ 支持宏转录组数据

**使用示例**:
```bash
# 基本运行
humann --input sample.fastq --output output_dir

# 标准化输出
humann_renorm_table --input sample_genefamilies.tsv \
    --output sample_genefamilies_relab.tsv --units relab
```

---

### 3. QIIME 2 (Amplicon)

**来源**: [GitHub - qiime2/qiime2](https://github.com/qiime2/qiime2)

| 属性 | 详情 |
|------|------|
| **用途** | 扩增子测序数据分析平台 |
| **安装** | `conda install -c qiime2 qiime2` |
| **难度** | ⭐⭐ 中级 |
| **论文** | Nature Biotechnology 2019 |

**关键特性**:
- ✅ 完整分析流程（质控→去噪→注释→多样性）
- ✅ 插件系统（DADA2, Deblur, etc.）
- ✅ 可重复性保证
- ✅ 交互式可视化

---

### 4. DADA2

**来源**: [GitHub - benjjneb/dada2](https://github.com/benjjneb/dada2)

| 属性 | 详情 |
|------|------|
| **版本** | 1.30 |
| **用途** | 扩增子去噪，精确识别 ASV |
| **安装** | Bioconductor: `BiocManager::install("dada2")` |
| **难度** | ⭐⭐ 中级 |
| **论文** | Nature Methods 2016 |

**关键特性**:
- ✅ 单核苷酸分辨率
- ✅ 替代传统 OTU 聚类
- ✅ 错误率学习模型
- ✅ 双端 reads 合并

---

### 5. mothur

**来源**: [GitHub - mothur/mothur](https://github.com/mothur/mothur)

| 属性 | 详情 |
|------|------|
| **版本** | 1.48.5 (2026-01-13) |
| **用途** | 16S rRNA 基因序列分析 |
| **安装** | `conda install -c bioconda mothur` |
| **难度** | ⭐⭐ 中级 |
| **论文** | AEM 2009 |

**关键特性**:
- ✅ 标准操作程序 (SOP)
- ✅ OTU 聚类
- ✅ 多样性分析
- ✅ 与 SILVA、Greengenes 集成

---

### 6. fastp

**来源**: [GitHub - OpenGene/fastp](https://github.com/OpenGene/fastp)

| 属性 | 详情 |
|------|------|
| **版本** | 1.0 |
| **用途** | FASTQ 质量控制和预处理 |
| **安装** | `conda install -c bioconda fastp` |
| **难度** | ⭐ 入门 |
| **论文** | iMeta 2025 |

**关键特性**:
- ✅ 超快速（优于 FASTQC+Trimmomatic）
- ✅ 自动接头检测
- ✅ HTML + JSON 报告
- ✅ UMI 处理、去重、合并

---

### 7. MEGAHIT

**来源**: [GitHub - voutcn/megahit](https://github.com/voutcn/megahit)

| 属性 | 详情 |
|------|------|
| **版本** | 1.2.9 |
| **用途** | 宏基因组 de novo 组装 |
| **安装** | `conda install -c bioconda megahit` |
| **难度** | ⭐⭐⭐ 高级 |
| **论文** | Bioinformatics 2015 |

**关键特性**:
- ✅ 简洁 de Bruijn 图
- ✅ 内存高效
- ✅ 适用于大型复杂宏基因组
- ✅ 支持多种文库类型

---

## 🔄 新增工作流

### bioBakery Workflow

**来源**: [GitHub - biobakery/biobakery](https://github.com/biobakery/biobakery)

**完整分析流程**:

```
1. 质量控制（fastp）
   ↓
2. 物种分类谱分析（MetaPhlAn）
   ↓
3. 功能谱分析（HUMAnN）
   ↓
4. 下游统计分析（R/Python）
```

**部署方式**:
- Docker 容器
- Vagrant 虚拟机
- Google Cloud 镜像
- Galaxy 服务器

---

## 📖 新增概念

### 1. 16S rRNA 测序

**定义**: 16S rRNA 基因是原核生物核糖体小亚基的组成部分，长度约 1500bp，包含 9 个可变区（V1-V9），广泛用于微生物分类和系统发育分析。

**常用引物**:
- V3-V4 区：341F-805R
- V4 区：515F-806R（Earth Microbiome Project）

**分析流程**:
```
质控 → 拼接 → 去噪/OTU 聚类 → 物种注释 → 多样性分析
```

---

### 2. 宏基因组测序

**定义**: 宏基因组测序（鸟枪法测序）是对环境样本中所有微生物的总 DNA 进行测序，不依赖 PCR 扩增，可获得物种组成和功能基因信息。

**与 16S 的比较**:

| 特征 | 16S 测序 | 宏基因组测序 |
|------|----------|--------------|
| 目标区域 | 16S rRNA 基因 | 全基因组 |
| 物种分辨率 | 属/种水平 | 种/菌株水平 |
| 功能信息 | 无 | 有（基因、通路） |
| 成本 | 低 | 高 |
| 数据量 | 1-5M reads | 20-100M reads |

---

## 📈 覆盖的分析流程

SkillPI 现在涵盖了完整的微生物组分析流程：

```
样本采集
   ↓
DNA 提取
   ↓
文库制备
   ↓
测序 (Illumina/Nanopore)
   ↓
┌──────────────────────────────────────┐
│         SkillPI 覆盖区域             │
│                                      │
│  1. 质量控制 → fastp                 │
│  2. 物种分析 → MetaPhlAn, QIIME 2   │
│  3. 功能分析 → HUMAnN                │
│  4. 组装 → MEGAHIT                   │
│  5. 统计分析 → bioBakery             │
└──────────────────────────────────────┘
```

---

## 🔍 数据来源验证

所有工具信息均来自**官方来源**：

| 工具 | 数据来源 |
|------|----------|
| MetaPhlAn 4 | GitHub + Nature Biotechnology |
| HUMAnN 3 | GitHub + eLife |
| QIIME 2 | GitHub + Nature Biotechnology |
| DADA2 | GitHub + Nature Methods |
| mothur | GitHub + AEM |
| fastp | GitHub + iMeta |
| MEGAHIT | GitHub + Bioinformatics |
| bioBakery | GitHub + Bioinformatics |

---

## 🚀 使用方法

### 查看文档网站

```bash
# 本地预览
mkdocs serve

# 访问 http://localhost:8000
```

### 查看原始数据

```bash
# 查看精选工具数据
cat data/skills/curated_tools.json

# 查看生成的文档
cat docs/skills/tools/metaphlan-4.md
cat docs/skills/concepts/16s-rrna-sequencing.md
```

### 更新工具数据

```bash
# 运行更新脚本
python scripts/update_with_real_docs.py
```

---

## 📊 文档统计

| 文件类型 | 数量 | 位置 |
|---------|------|------|
| 工具文档 | 10 | `docs/skills/tools/` |
| 工作流文档 | 2 | `docs/skills/workflows/` |
| 概念文档 | 4 | `docs/skills/concepts/` |
| 索引页面 | 3 | `docs/skills/*.md` |

---

## 🎯 下一步计划

### 短期优化
1. 添加更多工具（Kraken2, Bracken, CheckM, etc.）
2. 实现自动更新机制（定期抓取 GitHub）
3. 添加工具比较功能
4. 集成用户评分和评论

### 长期规划
1. 添加视频教程链接
2. 创建交互式学习路径
3. 实现工具推荐系统
4. 建立社区贡献机制

---

## 📚 相关资源

- **bioBakery 论坛**: https://forum.biobakery.org
- **QIIME 2 论坛**: https://forum.qiime2.org
- **微生物组分析教程**: https://github.com/microbiome/tutorials

---

**更新时间**: 2026-03-18  
**数据来源**: GitHub 官方仓库、论文、文档网站  
**验证状态**: ✅ 已验证
