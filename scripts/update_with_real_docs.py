#!/usr/bin/env python3
"""
从真实文档更新 SkillPI 技能数据

使用从 GitHub 和官方文档抓取的详细信息
"""

import json
from pathlib import Path
from datetime import datetime

from skillpi.models import Skill, SkillCategory, Tool, Workflow, Concept, SkillLevel

# 真实工具数据（从文档抓取）
REAL_TOOLS = [
    # bioBakery 套件
    {
        "id": "metaphlan-4",
        "name": "MetaPhlAn 4",
        "version": "4.2.4",
        "description": "用于从宏基因组鸟枪法测序数据中进行物种级微生物组成分析的工具（细菌、古菌、真核生物和病毒）",
        "category": "profiling",
        "url": "https://github.com/biobakery/metaphlan",
        "homepage": "https://segatalab.cibio.unitn.it/tools/metaphlan/",
        "paper_url": "https://www.nature.com/articles/s41587-023-01688-w",
        "installation": "conda install -c bioconda metaphlan",
        "usage_example": """# 基本运行
metaphlan input.fastq.gz --output_file profile.txt

# 使用病毒数据库
metaphlan input.fastq.gz --output_file profile.txt --input_type fastq --nproc 8

# 菌株级分析
metaphlan input.fastq.gz --output_file profile.txt --strain_profiler true""",
        "tags": ["metagenomics", "taxonomic-profiling", "species-level", "strain-level", "virus"],
        "skill_level": "beginner"
    },
    {
        "id": "humann-3",
        "name": "HUMAnN 3",
        "version": "3.0",
        "description": "用于从宏基因组或宏转录组数据中高效、准确地分析微生物群落通路存在/缺失和丰度的流程（功能分析）",
        "category": "functional-profiling",
        "url": "https://github.com/biobakery/humann",
        "homepage": "http://huttenhower.sph.harvard.edu/humann",
        "paper_url": "https://doi.org/10.7554/eLife.65088",
        "installation": """# 推荐安装
pip install humann

# 或从源码
git clone https://github.com/biobakery/humann
cd humann
python setup.py install""",
        "usage_example": """# 基本运行
humann --input sample.fastq --output output_dir

# 使用特定数据库
humann --input sample.fastq --output output_dir --threads 8

# 标准化输出
humann_renorm_table --input sample_genefamilies.tsv \\
    --output sample_genefamilies_relab.tsv --units relab""",
        "tags": ["metagenomics", "functional-profiling", "pathway-analysis", "metatranscriptomics"],
        "skill_level": "intermediate"
    },
    {
        "id": "biobakery-workflow",
        "name": "bioBakery Workflow",
        "description": "Huttenhower 实验室开发的微生物群落分析工具集和教程平台，提供 MetaPhlAn、HUMAnN 等工具的集成环境",
        "category": "workflow",
        "url": "https://github.com/biobakery/biobakery",
        "homepage": "https://huttenhower.sph.harvard.edu/biobakery",
        "paper_url": "https://doi.org/10.1093/bioinformatics/btx732",
        "installation": """# 使用 Docker
docker pull biobakery/biobakery

# 或使用 Vagrant
# 下载预构建的虚拟镜像

# 或单独安装各个工具
conda install -c bioconda metaphlan humann""",
        "usage_example": """# 完整工作流程
# 1. 分类谱分析
metaphlan input.fastq --output profile.txt

# 2. 功能谱分析
humann --input input.fastq --output output_dir

# 3. 下游统计分析
# 使用 R 包 microbiome 或 Python 工具""",
        "tags": ["workflow", "metagenomics", "integrated-platform", "tutorial"],
        "skill_level": "intermediate"
    },
    # QIIME 2
    {
        "id": "qiime2-amplicon",
        "name": "QIIME 2 (Amplicon)",
        "description": "强大的微生物组扩增子分析平台，支持从原始测序数据到统计分析和可视化的完整流程",
        "category": "amplicon-analysis",
        "url": "https://github.com/qiime2/qiime2",
        "homepage": "https://qiime2.org",
        "paper_url": "https://doi.org/10.1038/s41587-019-0209-9",
        "installation": """# Conda 安装（推荐）
conda install -c qiime2 -c conda-forge qiime2

# Docker 安装
docker pull qiime2/core:2024.2""",
        "usage_example": """# 导入数据
qiime tools import \\
  --type 'SampleData[SequencesWithQuality]' \\
  --input-path demux \\
  --output-path demux.qza

# DADA2 去噪
qiime dada2 denoise-paired \\
  --i-demultiplexed-seqs demux.qza \\
  --o-table table.qza \\
  --o-representative-sequences rep-seqs.qza \\
  --o-denoising-stats stats.qza

# 多样性分析
qiime diversity core-metrics-phylogenetic \\
  --i-phylogeny rooted-tree.qza \\
  --i-table table.qza \\
  --p-sampling-depth 10000 \\
  --output-dir core-metrics-results""",
        "tags": ["16S", "amplicon", "its", "analysis", "visualization", "reproducible"],
        "skill_level": "intermediate"
    },
    # DADA2
    {
        "id": "dada2-pipeline",
        "name": "DADA2",
        "version": "1.30",
        "description": "高分辨率的样本推断算法，可从扩增子测序数据中精确识别序列变异（ASV），替代传统的 OTU 聚类方法",
        "category": "denoising",
        "url": "https://github.com/benjjneb/dada2",
        "homepage": "https://benjjneb.github.io/dada2/",
        "paper_url": "https://doi.org/10.1038/nmeth.3869",
        "installation": """# R/Bioconductor 安装
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("dada2")

# 或使用 QIIME 2 插件
qiime dada2 denoise-paired ...""",
        "usage_example": """# R 代码示例
library(dada2)

# 1. 过滤和截断
filtFs <- filterAndTrim(fnFs, filtFs, truncLen=c(240,0))

# 2. 学习错误率
errF <- learnErrors(filtFs)

# 3. 去噪
dadaFs <- dada(filtFs, err=errF)

# 4. 合并双端 reads
mergers <- mergePairs(dadaFs, filtFs, dadaRs, filtRs)

# 5. 构建 ASV 表
seqtab <- makeSequenceTable(mergers)""",
        "tags": ["16S", "denoising", "ASV", "amplicon", "R", "bioconductor"],
        "skill_level": "intermediate"
    },
    # mothur
    {
        "id": "mothur",
        "version": "1.48.5",
        "description": "用于微生物生态学分析的综合工具，专注于 16S rRNA 基因序列分析和微生物群落多样性研究",
        "category": "amplicon-analysis",
        "url": "https://github.com/mothur/mothur",
        "homepage": "https://www.mothur.org",
        "paper_url": "https://doi.org/10.1128/AEM.01541-09",
        "installation": """# Ubuntu/Debian
sudo apt-get install mothur

# Conda
conda install -c bioconda mothur

# 源码编译
git clone https://github.com/mothur/mothur.git
cd mothur
make -j""",
        "usage_example": """# 标准 MiSeq SOP
mothur > make.contigs(file=stability.files, processors=8)
mothur > screen.seqs(fasta=current, maxambig=0, maxlength=275)
mothur > unique.seqs(fasta=current)
mothur > align.seqs(fasta=current, reference=silva.v4.fasta)
mothur > filter.seqs(fasta=current, vertical=T, trump=.)
mothur > pre.cluster(fasta=current, diffs=2)
mothur > chimera.vsearch(fasta=current)
mothur > classify.seqs(fasta=current, reference=trainset9_032012.pds.fasta)
mothur > cluster.split(fasta=current, count=current, splitmethod=classify)""",
        "tags": ["16S", "amplicon", "OTU", "diversity", "SOP"],
        "skill_level": "intermediate"
    },
    # 质控工具
    {
        "id": "fastp",
        "version": "1.0",
        "description": "超快速的 FASTQ 数据预处理和质量控制工具，集成了质量分析、过滤、修剪、去重等多种功能",
        "category": "quality-control",
        "url": "https://github.com/OpenGene/fastp",
        "homepage": "http://opengene.org/fastp/",
        "paper_url": "https://doi.org/10.1002/IMT2.107",
        "installation": """# Conda
conda install -c bioconda fastp

# Docker
docker pull opengene/fastp

# 预编译二进制
wget http://opengene.org/fastp/fastp
chmod a+x ./fastp""",
        "usage_example": """# 双端数据质控
fastp -i in.R1.fq.gz -I in.R2.fq.gz \\
  -o out.R1.fq.gz -O out.R2.fq.gz \\
  -h report.html -j report.json \\
  -w 8

# 自动接头检测
fastp -i input.fq -o output.fq --detect_adapter_for_pe

# UMI 处理
fastp -i input.fq -o output.fq -U index1""",
        "tags": ["QC", "fastq", "adapter-trimming", "filtering", "ultra-fast"],
        "skill_level": "beginner"
    },
    # 组装工具
    {
        "id": "megahit",
        "version": "1.2.9",
        "description": "超快速且内存高效的 NGS 组装器，主要针对宏基因组优化，基于简洁 de Bruijn 图技术",
        "category": "assembly",
        "url": "https://github.com/voutcn/megahit",
        "homepage": "https://github.com/voutcn/megahit",
        "paper_url": "https://doi.org/10.1093/bioinformatics/btv033",
        "installation": """# Conda
conda install -c bioconda megahit

# Docker
docker run -v $(pwd):/workspace vout/megahit

# 预编译二进制
wget https://github.com/voutcn/megahit/releases/download/v1.2.9/MEGAHIT-1.2.9-Linux-x86_64-static.tar.gz
tar xvzf MEGAHIT-*.tar.gz""",
        "usage_example": """# 宏基因组组装
megahit -1 pe_1.fq -2 pe_2.fq -o output_dir

# 大型复杂宏基因组
megahit -1 reads_1.fq -2 reads_2.fq \\
  --presets meta-large -o output_dir

# 从中间结果继续
megahit --continue -o output_dir""",
        "tags": ["metagenomics", "assembly", "de-bruijn-graph", "memory-efficient"],
        "skill_level": "advanced"
    },
    # 概念
    {
        "id": "16s-rrna-sequencing",
        "name": "16S rRNA 测序",
        "definition": "16S rRNA 基因是原核生物核糖体小亚基的组成部分，长度约 1500bp，包含 9 个可变区（V1-V9）和保守区，广泛用于微生物分类和系统发育分析",
        "explanation": """16S rRNA 基因测序是微生物组研究中最常用的方法：

**原理**：
1. 保守区用于设计通用引物（如 27F/1492R）
2. 可变区包含物种特异性序列
3. 通过序列比对构建系统发育树

**常用引物**：
- V3-V4 区：341F-805R
- V4 区：515F-806R（Earth Microbiome Project）

**分析流程**：
质控 → 拼接 → 去噪/OTU 聚类 → 物种注释 → 多样性分析""",
        "related_concepts": ["扩增子测序", "OTU", "ASV", "系统发育树", "Alpha 多样性", "Beta 多样性"],
        "examples": [
            "Illumina MiSeq 2x250bp 测序 V3-V4 区",
            "使用 DADA2 进行去噪获得 ASV",
            "使用 QIIME 2 进行多样性分析"
        ],
        "tags": ["16S", "sequencing", "taxonomy", "amplicon", "basics"],
        "skill_level": "beginner"
    },
    {
        "id": "metagenomics-sequencing",
        "name": "宏基因组测序",
        "definition": "宏基因组测序（鸟枪法测序）是对环境样本中所有微生物的总 DNA 进行测序，不依赖 PCR 扩增，可获得物种组成和功能基因信息",
        "explanation": """**与 16S 测序的比较**：

| 特征 | 16S 测序 | 宏基因组测序 |
|------|----------|--------------|
| 目标区域 | 16S rRNA 基因 | 全基因组 |
| 物种分辨率 | 属/种水平 | 种/菌株水平 |
| 功能信息 | 无 | 有（基因、通路） |
| 成本 | 低 | 高 |
| 数据量 | 1-5M reads | 20-100M reads |

**典型应用**：
- 物种组成分析（MetaPhlAn）
- 功能谱分析（HUMAnN）
- 基因组组装（MEGAHIT）
- 菌株追踪""",
        "related_concepts": ["鸟枪法测序", "功能分析", "基因组组装", "分箱"],
        "examples": [
            "Illumina NovaSeq 2x150bp 测序",
            "使用 MetaPhlAn 进行物种分析",
            "使用 HUMAnN 进行通路分析"
        ],
        "tags": ["metagenomics", "shotgun", "sequencing", "functional-analysis"],
        "skill_level": "intermediate"
    }
]

def create_skills():
    """创建技能对象"""
    skills = []
    
    for tool_data in REAL_TOOLS:
        # 确保有 name 字段
        if "name" not in tool_data:
            tool_data["name"] = tool_data["id"].replace("-", " ").title()
        
        if "definition" in tool_data:
            # 这是概念
            concept = Concept(
                name=tool_data["name"],
                definition=tool_data["definition"],
                explanation=tool_data.get("explanation"),
                related_concepts=tool_data.get("related_concepts", []),
                examples=tool_data.get("examples", []),
                tags=tool_data.get("tags", []),
                skill_level=SkillLevel(tool_data.get("skill_level", "beginner"))
            )
            skill = Skill(
                id=tool_data["id"],
                type=SkillCategory.CONCEPT,
                data=concept
            )
        elif "workflow" in tool_data.get("category", "").lower() or "workflow" in tool_data.get("tags", []):
            # 这是工作流
            workflow = Workflow(
                name=tool_data["name"],
                description=tool_data["description"],
                steps=[
                    "1. 质量控制（fastp）",
                    "2. 物种分类谱分析（MetaPhlAn）",
                    "3. 功能谱分析（HUMAnN）",
                    "4. 下游统计分析"
                ],
                tools_used=["MetaPhlAn", "HUMAnN", "fastp"],
                input_format="FASTQ (宏基因组或宏转录组)",
                output_format="物种丰度表、通路丰度表",
                documentation_url=tool_data.get("homepage"),
                tags=tool_data.get("tags", []),
                skill_level=SkillLevel(tool_data.get("skill_level", "intermediate"))
            )
            skill = Skill(
                id=tool_data["id"],
                type=SkillCategory.WORKFLOW,
                data=workflow
            )
        else:
            # 这是工具
            tool = Tool(
                name=tool_data["name"],
                version=tool_data.get("version"),
                description=tool_data["description"],
                category=tool_data["category"],
                url=tool_data.get("url"),
                homepage=tool_data.get("homepage"),
                paper_url=tool_data.get("paper_url"),
                installation=tool_data.get("installation"),
                usage_example=tool_data.get("usage_example"),
                tags=tool_data.get("tags", []),
                skill_level=SkillLevel(tool_data.get("skill_level", "intermediate"))
            )
            skill = Skill(
                id=tool_data["id"],
                type=SkillCategory.TOOL,
                data=tool
            )
        
        skills.append(skill)
    
    return skills

def main():
    """主函数"""
    print("="*70)
    print("从真实文档创建 SkillPI 技能数据")
    print("="*70)
    
    skills = create_skills()
    
    # 保存为 JSON
    data = [skill.model_dump(mode="json") for skill in skills]
    
    output_file = Path("data/skills/curated_tools.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ 成功创建 {len(skills)} 个技能")
    print(f"  工具：{sum(1 for s in skills if s.type == SkillCategory.TOOL)}")
    print(f"  工作流：{sum(1 for s in skills if s.type == SkillCategory.WORKFLOW)}")
    print(f"  概念：{sum(1 for s in skills if s.type == SkillCategory.CONCEPT)}")
    print(f"\n✓ 保存到：{output_file}")
    
    # 生成文档
    print(f"\n生成文档网站...")
    from skillpi.generators import MkDocsGenerator
    generator = MkDocsGenerator(str(output_file.parent), ".")
    generator.generate()
    
    print(f"✓ 文档生成完成")
    print(f"  查看：npm run dev")
    print("="*70)

if __name__ == "__main__":
    main()
