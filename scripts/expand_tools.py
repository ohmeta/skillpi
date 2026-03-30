#!/usr/bin/env python3
"""
Expand SkillPI tool catalogue with more microbiome bioinformatics tools.

Fetches latest info from GitHub API and generates:
1. Updated curated_tools.json
2. Markdown docs for each tool
"""

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# ── Tool definitions: (id, name, category, github_url, description, tags, skill_level, paper_url) ──

NEW_TOOLS = [
    # ═══ Taxonomic Classification ═══
    {
        "id": "kraken2",
        "name": "Kraken 2",
        "category": "taxonomic-classification",
        "github": "DerrickWood/kraken2",
        "description": "超快速的宏基因组分类序列归类工具，基于 k-mer 匹配和最低共同祖先算法",
        "tags": ["taxonomic-classification", "kmer", "metagenomics", "fast"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1186/s13059-019-1891-0",
    },
    {
        "id": "bracken",
        "name": "Bracken",
        "category": "taxonomic-classification",
        "github": "jenniferlu717/Bracken",
        "description": "基于贝叶斯方法重新估计 Kraken 分类的物种丰度，支持种/属/科级别",
        "tags": ["abundance-estimation", "kraken", "bayesian"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.7554/eLife.39915",
    },
    {
        "id": "centrifuge",
        "name": "Centrifuge",
        "category": "taxonomic-classification",
        "github": "DaehwanKimLab/centrifuge",
        "description": "基于 FM-index 的超快速宏基因组分类工具，内存效率高",
        "tags": ["taxonomic-classification", "fm-index", "memory-efficient"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1101/gr.210641.116",
    },
    {
        "id": "kaiju",
        "name": "Kaiju",
        "category": "taxonomic-classification",
        "github": "bioinformatics-centre/kaiju",
        "description": "基于蛋白质比对的宏基因组分类工具，对远缘物种更敏感",
        "tags": ["taxonomic-classification", "protein", "sensitive"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1038/ncomms11257",
    },
    # ═══ Assembly ═══
    {
        "id": "metaspades",
        "name": "metaSPAdes",
        "category": "assembly",
        "github": "ablab/spades",
        "description": "专门为宏基因组数据设计的 de novo 组装器，基于 SPAdes 引擎",
        "tags": ["assembly", "metagenomics", "short-read", "de-bruijn"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1101/gr.213959.116",
    },
    {
        "id": "flye",
        "name": "Flye",
        "category": "assembly",
        "github": "fenderglass/Flye",
        "description": "用于长读长（PacBio/Nanopore）的 de novo 组装器，支持宏基因组组装",
        "tags": ["assembly", "long-read", "nanopore", "pacbio", "metagenomics"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41587-019-0072-8",
    },
    {
        "id": "canu",
        "name": "Canu",
        "category": "assembly",
        "github": "marbl/canu",
        "description": "长读长单分子序列组装器，源自 Celera Assembler，支持纠错+修剪+组装",
        "tags": ["assembly", "long-read", "pacbio", "nanopore"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1101/gr.215087.116",
    },
    {
        "id": "unicycler",
        "name": "Unicycler",
        "category": "assembly",
        "github": "rrwick/Unicycler",
        "description": "混合组装工具，结合短读长和长读长数据，适用于细菌基因组",
        "tags": ["assembly", "hybrid", "short-read", "long-read", "bacterial"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1371/journal.pcbi.1005595",
    },
    # ═══ Binning ═══
    {
        "id": "metabat2",
        "name": "MetaBAT 2",
        "category": "binning",
        "github": "BinPro/MetaBAT2",
        "description": "基于丰度和四核苷酸频率的宏基因组分箱工具，恢复高质量 MAG",
        "tags": ["binning", "MAG", "metagenomics", "abundance"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.7554/eLife.45092",
    },
    {
        "id": "maxbin2",
        "name": "MaxBin 2",
        "category": "binning",
        "github": "kylebittinger/maxbin2",
        "description": "自动化宏基因组分箱工具，利用序列组成和丰度信息",
        "tags": ["binning", "MAG", "metagenomics", "automated"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1093/bioinformatics/btv638",
    },
    {
        "id": "concoct",
        "name": "CONCOCT",
        "category": "binning",
        "github": "BinPro/CONCOCT",
        "description": "基于高斯混合模型的无监督宏基因组分箱，利用序列组成和覆盖度",
        "tags": ["binning", "MAG", "unsupervised", "gaussian-mixture"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/nmeth.2835",
    },
    {
        "id": "das_tool",
        "name": "DAS Tool",
        "category": "binning-refinement",
        "github": "cmks/DAS_Tool",
        "description": "通过集成多个分箱工具结果来恢复高质量 MAG 的整合框架",
        "tags": ["binning-refinement", "MAG", "ensemble", "quality-improvement"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41564-018-0171-1",
    },
    {
        "id": "checkm2",
        "name": "CheckM2",
        "category": "quality-assessment",
        "github": "chklovski/CheckM2",
        "description": "MAG 质量评估工具（CheckM 的继任者），使用机器学习预测基因组完整性和污染",
        "tags": ["quality-assessment", "MAG", "machine-learning", "completeness"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1038/s41592-023-01940-w",
    },
    {
        "id": "gtdb_tk",
        "name": "GTDB-Tk",
        "category": "taxonomic-classification",
        "github": "Ecogenomics/GTDBTk",
        "description": "基于 GTDB 分类框架对细菌和古菌基因组进行自动化分类注释",
        "tags": ["taxonomy", "MAG", "GTDB", "classification"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1038/s41587-020-0501-8",
    },
    # ═══ Strain-level Analysis ═══
    {
        "id": "strainphlan",
        "name": "StrainPhlAn",
        "category": "strain-analysis",
        "github": "biobakery/metaphlan",
        "description": "宏基因组菌株水平群体基因组学工具，可追踪菌株变异和系统发育关系",
        "tags": ["strain-level", "phylogenetics", "metagenomics", "biobakery"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/nmeth.3589",
    },
    {
        "id": "instrain",
        "name": "inStrain",
        "category": "strain-analysis",
        "github": "MrOlm/inStrain",
        "description": "基于读段比较分析宏基因组中的群体基因组学，包括 SNV、微多样性、菌株验证",
        "tags": ["strain-level", "SNV", "microdiversity", "population-genomics"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1186/s13059-020-02179-4",
    },
    # ═══ Functional Annotation ═══
    {
        "id": "eggnog_mapper",
        "name": "eggNOG-mapper",
        "category": "functional-annotation",
        "github": "eggnogdb/eggnog-mapper",
        "description": "基于 eggNOG 数据库的快速功能注释工具，使用预计算的直系同源组",
        "tags": ["functional-annotation", "orthologs", "GO", "KEGG"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1093/molbev/msab293",
    },
    {
        "id": "prokka",
        "name": "Prokka",
        "category": "genome-annotation",
        "github": "tseemann/prokka",
        "description": "快速原核生物基因组注释工具，自动化预测基因并分配功能",
        "tags": ["annotation", "prokaryotic", "gene-prediction", "rapid"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1093/bioinformatics/btu153",
    },
    {
        "id": "bakta",
        "name": "Bakta",
        "category": "genome-annotation",
        "github": "oschwengers/bakta",
        "description": "快速标准化原核生物基因组注释（Prokka 的继任者），使用 UniRef/Pfam/COG",
        "tags": ["annotation", "prokaryotic", "standardized", "UniRef"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1093/microbe/miac074",
    },
    {
        "id": "antismash",
        "name": "antiSMASH",
        "category": "functional-annotation",
        "github": "antismash/antismash",
        "description": "微生物次级代谢产物生物合成基因簇（BGC）的全面识别和分析工具",
        "tags": ["BGC", "secondary-metabolites", "natural-products", "genomics"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1093/nar/gkab335",
    },
    {
        "id": "dram",
        "name": "DRAM",
        "category": "functional-annotation",
        "github": "WrightonLabCSU/DRAM",
        "description": "Distilled and Refined Annotation of Metabolism — 代谢通路和基因功能的宏基因组注释",
        "tags": ["functional-annotation", "metabolism", "MAG", "distillation"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41587-020-0674-2",
    },
    # ═══ Alignment & Mapping ═══
    {
        "id": "bowtie2",
        "name": "Bowtie 2",
        "category": "alignment",
        "github": "BenLangmead/bowtie2",
        "description": "超快速高效的短读长序列比对工具，支持间隙比对，广泛用于宏基因组",
        "tags": ["alignment", "short-read", "indexing", "fast"],
        "skill_level": "beginner",
        "paper_url": "https://doi.org/10.1038/nmeth.1923",
    },
    {
        "id": "minimap2",
        "name": "minimap2",
        "category": "alignment",
        "github": "lh3/minimap2",
        "description": "多功能序列比对工具，支持全基因组、转录组和长读长比对",
        "tags": ["alignment", "long-read", "versatile", "fast"],
        "skill_level": "beginner",
        "paper_url": "https://doi.org/10.1093/bioinformatics/bty191",
    },
    {
        "id": "bwa_mem2",
        "name": "BWA-MEM2",
        "category": "alignment",
        "github": "bwa-mem2/bwa-mem2",
        "description": "BWA-MEM 的加速版本，利用 SIMD 指令提升比对速度 2-3 倍",
        "tags": ["alignment", "short-read", "SIMD", "accelerated"],
        "skill_level": "beginner",
        "paper_url": "https://doi.org/10.1109/IPDPS.2019.00041",
    },
    # ═══ Visualization ═══
    {
        "id": "anvio",
        "name": "anvi'o",
        "category": "visualization",
        "github": "merenlab/anvio",
        "description": "交互式可视化和分析平台，支持宏基因组组装、分箱、功能注释和比较基因组学",
        "tags": ["visualization", "interactive", "comparative-genomics", "binning", "MAG"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41564-020-00743-5",
    },
    {
        "id": "pavian",
        "name": "Pavian",
        "category": "visualization",
        "github": "fbreitwieser/pavian",
        "description": "交互式宏基因组分类结果可视化工具，支持 Kraken/KrakenUniq/Centrifuge 输出",
        "tags": ["visualization", "interactive", "classification", "R"],
        "skill_level": "beginner",
        "paper_url": "https://doi.org/10.1093/bioinformatics/btz510",
    },
    {
        "id": "krona",
        "name": "Krona",
        "category": "visualization",
        "github": "marbl/Krona",
        "description": "交互式多层级饼图可视化工具，支持分类层级数据展示",
        "tags": ["visualization", "hierarchical", "taxonomy", "interactive"],
        "skill_level": "beginner",
        "paper_url": "https://doi.org/10.1186/1471-2105-12-355",
    },
    # ═══ Downstream Analysis (R) ═══
    {
        "id": "phyloseq",
        "name": "phyloseq",
        "category": "downstream-analysis",
        "github": "joey711/phyloseq",
        "description": "R 包，用于微生物组丰度数据的导入、存储、分析和图形展示",
        "tags": ["R", "diversity", "visualization", "amplicon"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1371/journal.pone.0061217",
    },
    {
        "id": "deseq2",
        "name": "DESeq2",
        "category": "downstream-analysis",
        "github": "mikelove/DESeq2",
        "description": "基于负二项分布的差异丰度分析工具，广泛用于微生物组差异分析",
        "tags": ["R", "differential-abundance", "statistical", "negative-binomial"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1186/s13059-014-0550-8",
    },
    {
        "id": "lefse",
        "name": "LEfSe",
        "category": "downstream-analysis",
        "github": "biobakery/LEfSe",
        "description": "线性判别分析效应量工具，用于高维生物数据的类间差异分析",
        "tags": ["biomarker", "differential-abundance", "LDA", "biobakery"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1186/gb-2011-12-6-r60",
    },
    {
        "id": "ancom_bc",
        "name": "ANCOM-BC",
        "category": "downstream-analysis",
        "github": "frederick-huang-lin/ANCOMBC",
        "description": "基于偏差校正的组成数据分析方法，用于微生物组差异丰度分析",
        "tags": ["R", "differential-abundance", "compositionality", "bias-correction"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41467-020-17041-7",
    },
    {
        "id": "microeco",
        "name": "microeco",
        "category": "downstream-analysis",
        "github": "ChiLiubio/microeco",
        "description": "R 包，用于微生物组数据的统计分析和可视化，支持多种数据类型",
        "tags": ["R", "statistics", "visualization", "comprehensive"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1038/s41596-025-01239-4",
    },
    # ═══ Long-read QC ═══
    {
        "id": "nanoplot",
        "name": "NanoPlot",
        "category": "quality-control",
        "github": "wdecoster/NanoPlot",
        "description": "Oxford Nanopore 测序数据质量控制和可视化工具",
        "tags": ["QC", "nanopore", "long-read", "visualization"],
        "skill_level": "beginner",
        "paper_url": None,
    },
    {
        "id": "filtlong",
        "name": "Filtlong",
        "category": "quality-control",
        "github": "rrwick/Filtlong",
        "description": "长读长序列质量过滤工具，基于质量分数和读长长度",
        "tags": ["QC", "long-read", "filtering", "nanopore"],
        "skill_level": "beginner",
        "paper_url": None,
    },
    # ═══ Variant Calling ═══
    {
        "id": "clair3",
        "name": "Clair3",
        "category": "variant-calling",
        "github": "HKU-BAL/Clair3",
        "description": "长读长（ONT/PacBio）快速准确的 SNP/Indel 变异检测工具",
        "tags": ["variant-calling", "long-read", "SNP", "Indel", "nanopore"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41587-021-01138-1",
    },
    # ═══ Metatranscriptomics ═══
    {
        "id": "salmon",
        "name": "Salmon",
        "category": "quantification",
        "github": "COMBINE-lab/salmon",
        "description": "超快速转录本定量工具，支持映射和无比对模式",
        "tags": ["quantification", "transcriptomics", "metatranscriptomics", "fast"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1038/nmeth.4197",
    },
    {
        "id": "featurecounts",
        "name": "featureCounts",
        "category": "quantification",
        "github": "Shi-Lab/featureCounts",
        "description": "高效的读段计数工具，支持基因/外显子/转录本水平的定量",
        "tags": ["quantification", "read-counting", "fast", "multithreaded"],
        "skill_level": "beginner",
        "paper_url": "https://doi.org/10.1093/bioinformatics/btt656",
    },
    # ═══ Pipeline Frameworks ═══
    {
        "id": "nextflow",
        "name": "Nextflow",
        "category": "pipeline-framework",
        "github": "nextflow-io/nextflow",
        "description": "用于可扩展和可复现计算工作流的框架，支持 Docker/Singularity 容器化",
        "tags": ["workflow", "DSL", "reproducible", "scalable", "containers"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/nbt.3820",
    },
    {
        "id": "nf_core_mag",
        "name": "nf-core/mag",
        "category": "workflow",
        "github": "nf-core/mag",
        "description": "nf-core 的宏基因组组装和分箱流程，支持短读长/长读长/混合数据",
        "tags": ["workflow", "assembly", "binning", "nextflow", "nf-core"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1038/s41587-020-0439-x",
    },
    # ═══ Phage/Virus ═══
    {
        "id": "virsorter2",
        "name": "VirSorter 2",
        "category": "viral-analysis",
        "github": "jiarong/VirSorter2",
        "description": "基于多分类器的病毒序列识别工具，从宏基因组中挖掘病毒序列",
        "tags": ["virus", "phage", "identification", "metagenomics"],
        "skill_level": "advanced",
        "paper_url": "https://doi.org/10.1186/s13059-020-02181-w",
    },
    {
        "id": "pharokka",
        "name": "Pharokka",
        "category": "viral-analysis",
        "github": "gbouras13/pharokka",
        "description": "快速噬菌体基因组注释工具，自动检测 tRNA、tmRNA 和基因功能",
        "tags": ["phage", "annotation", "fast", "automated"],
        "skill_level": "intermediate",
        "paper_url": "https://doi.org/10.1093/nargab/lqad054",
    },
]


def fetch_github_info(owner_repo: str, token: str = None) -> dict:
    """Fetch repo info from GitHub API."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    url = f"https://api.github.com/repos/{owner_repo}"
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"  ⚠️  GitHub API {resp.status_code} for {owner_repo}")
            return {}
    except Exception as e:
        print(f"  ❌ Error fetching {owner_repo}: {e}")
        return {}


def fetch_topics(owner_repo: str, token: str = None) -> list:
    """Fetch repo topics from GitHub API."""
    headers = {
        "Accept": "application/vnd.github.mercy-preview+json",
    }
    if token:
        headers["Authorization"] = f"token {token}"

    url = f"https://api.github.com/repos/{owner_repo}/topics"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("names", [])
    except Exception:
        pass
    return []


def generate_install_cmd(language: str, full_name: str, name: str) -> str:
    """Generate installation command based on language."""
    if language == "Python":
        return f"pip install {name.lower()}"
    elif language == "R":
        return f"# R\nBiocManager::install('{name}')"
    elif language in ("Rust",):
        return f"cargo install {name.lower()}"
    elif language in ("Go",):
        return f"go install github.com/{full_name}@latest"
    elif language in ("C++", "C"):
        return f"conda install -c bioconda {name.lower()}"
    elif language == "Nextflow":
        return f"nextflow pull {full_name}"
    else:
        return f"conda install -c bioconda {name.lower()}"


def build_tool_entry(tool_def: dict, github_data: dict, github_topics: list) -> dict:
    """Build a SkillPI tool entry from definition + GitHub data."""
    name = tool_def["name"]
    description = tool_def["description"]

    # Enrich with GitHub data
    if github_data:
        gh_desc = github_data.get("description", "")
        if gh_desc and len(gh_desc) > len(description):
            description = gh_desc
        stars = github_data.get("stargazers_count", 0)
        language = github_data.get("language", "")
        homepage = github_data.get("homepage", "")
        full_name = github_data.get("full_name", "")
    else:
        stars = 0
        language = ""
        homepage = ""
        full_name = tool_def.get("github", "")

    # Merge tags
    tags = list(tool_def.get("tags", []))
    for t in github_topics:
        if t.lower() not in [x.lower() for x in tags]:
            tags.append(t)

    # Installation
    install = generate_install_cmd(language, full_name, name)

    # URL
    repo_url = f"https://github.com/{tool_def.get('github', '')}"
    url = homepage if homepage else repo_url

    return {
        "id": tool_def["id"],
        "type": "tool",
        "data": {
            "name": name,
            "version": github_data.get("default_branch", "").replace("main", "").replace("master", "") or None,
            "description": description,
            "category": tool_def["category"],
            "url": url,
            "repo_url": repo_url,
            "homepage": homepage or None,
            "paper_url": tool_def.get("paper_url"),
            "installation": install,
            "usage_example": None,
            "tags": tags,
            "skill_level": tool_def.get("skill_level", "intermediate"),
            "github_stars": stars,
            "language": language,
            "last_updated": datetime.now(timezone.utc).isoformat(),
        },
    }


def generate_markdown_doc(entry: dict) -> str:
    """Generate a VitePress markdown doc for a tool."""
    data = entry["data"]
    name = data["name"]
    desc = data["description"]
    category = data["category"]
    tags = ", ".join(data.get("tags", []))
    skill_level = data.get("skill_level", "intermediate")
    repo_url = data.get("repo_url", "")
    paper_url = data.get("paper_url", "")
    install = data.get("installation", "")
    stars = data.get("github_stars", 0)
    language = data.get("language", "")
    homepage = data.get("homepage", "")

    level_map = {
        "beginner": "⭐ 初级",
        "intermediate": "⭐⭐ 中级",
        "advanced": "⭐⭐⭐ 高级",
        "expert": "⭐⭐⭐⭐ 专家",
    }

    md = f"""---
title: {name}
description: {desc}
---

# {name}

> {desc}

## 基本信息

| 属性 | 值 |
|------|-----|
| **类别** | {category} |
| **难度** | {level_map.get(skill_level, skill_level)} |
| **语言** | {language or 'N/A'} |
| **GitHub Stars** | {stars:,} |
| **标签** | {tags} |

## 链接

"""
    if repo_url:
        md += f"- 📦 **代码仓库**: [{repo_url}]({repo_url})\n"
    if homepage:
        md += f"- 🏠 **主页**: [{homepage}]({homepage})\n"
    if paper_url:
        md += f"- 📄 **论文**: [{paper_url}]({paper_url})\n"

    md += f"""
## 安装

```bash
{install}
```

## 简介

{desc}

## 使用示例

> 📝 更多使用示例请参考官方文档。

---

*最后更新: {datetime.now().strftime('%Y-%m-%d')}*
"""
    return md


def main():
    # Config
    token = os.environ.get("GITHUB_TOKEN")
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data" / "skills"
    docs_dir = project_root / "docs" / "skills"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Load existing tools
    existing_file = data_dir / "curated_tools.json"
    existing_tools = []
    existing_ids = set()
    if existing_file.exists():
        with open(existing_file) as f:
            existing_tools = json.load(f)
            existing_ids = {t["id"] for t in existing_tools}
            print(f"📂 Loaded {len(existing_tools)} existing tools")

    new_entries = []
    for tool_def in NEW_TOOLS:
        tid = tool_def["id"]
        if tid in existing_ids:
            print(f"  ⏭️  {tool_def['name']} already exists, skipping")
            continue

        github_repo = tool_def.get("github", "")
        print(f"  🔍 Fetching {tool_def['name']} from {github_repo}...")

        github_data = {}
        github_topics = []
        if github_repo:
            github_data = fetch_github_info(github_repo, token)
            github_topics = fetch_topics(github_repo, token)
            time.sleep(0.5)  # Rate limit

        entry = build_tool_entry(tool_def, github_data, github_topics)
        new_entries.append(entry)
        print(f"  ✅ {tool_def['name']} ({entry['data']['category']}, ⭐{entry['data'].get('github_stars', 0)})")

    if not new_entries:
        print("\n✨ No new tools to add!")
        return

    # Merge and save
    all_tools = existing_tools + new_entries
    with open(existing_file, "w", encoding="utf-8") as f:
        json.dump(all_tools, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n💾 Saved {len(all_tools)} tools to {existing_file}")

    # Generate markdown docs
    tools_docs_dir = docs_dir / "tools"
    tools_docs_dir.mkdir(parents=True, exist_ok=True)

    for entry in new_entries:
        md = generate_markdown_doc(entry)
        md_file = tools_docs_dir / f"{entry['id']}.md"
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"  📝 Generated {md_file.name}")

    # Also generate tools index update
    print(f"\n🎉 Done! Added {len(new_entries)} new tools ({len(all_tools)} total)")
    print(f"   Data: {data_dir}")
    print(f"   Docs: {tools_docs_dir}")


if __name__ == "__main__":
    main()
