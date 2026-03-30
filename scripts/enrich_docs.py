#!/usr/bin/env python3
"""
Enrich tool docs with detailed usage examples.
Fecthes README content from GitHub and generates enriched markdown.
"""

import json
import re
import time
from pathlib import Path

import requests

# Tools to enrich with detailed examples (most commonly used)
ENRICH_TOOLS = {
    "kraken2": {
        "usage": """# 基本分类
kraken2 --db /path/to/kraken2_db --output result.kreport --report result.report input_1.fastq input_2.fastq

# 使用预建数据库
kraken2 --db /path/to/kraken2_db --paired --output result.kreport --report result.report sample_1.fq.gz sample_2.fq.gz

# 多线程加速
kraken2 --db /path/to/kraken2_db --threads 16 --output result.kreport --report result.report input.fastq

# 与 Bracken 配合估算丰度
bracken -d /path/to/kraken2_db -i result.report -o result.bracken -r 150 -l S""",
        "key_params": """| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--db` | Kraken2 数据库路径 | 必需 |
| `--output` | Kraken 格式输出 | 必需 |
| `--report` | 报告文件 | 必需 |
| `--threads` | 线程数 | 1 |
| `--paired` | 配对模式 | 关闭 |
| `--confidence` | 分类置信度阈值 | 0.05 |
| `--minimum-hit-groups` | 最小命中组数 | 2 |""",
    },
    "metaphlan-4": {
        "usage": """# 基本物种分类
metaphlan input.fastq --bowtie2db /path/to/db --nproc 8 --output_file profiled.txt

# 配对端数据
metaphlan sample_1.fq.gz,sample_2.fq.gz --bowtie2db /path/to/db --nproc 8 --input_type fastq --output_file profile.txt

# 生成 Bowtie2 比对文件（可复用）
metaphlan input.fastq --bowtie2db /path/to/db --bowtie2out mapped.bz2 --nproc 8 --input_type fastq --output_file profile.txt

# 批量处理 + 合并
merge_metaphlan_tables.py sample1_profile.txt sample2_profile.txt > merged_abundance_table.txt

# 菌株水平分析 (StrainPhlAn)
strainphlan -s SRS014464.bz2 --output_dir output --nprocs 4 --marker_in_n_markers 50 --sample_with_n_markers 50""",
        "key_params": """| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--bowtie2db` | 数据库路径 | 必需 |
| `--nproc` | 线程数 | 1 |
| `--input_type` | 输入格式 (fastq/fasta/bowtie2out) | 自动检测 |
| `--output_file` | 输出文件 | stdout |
| `--tax_lev` | 分类级别 (t/p/c/o/f/g/s) | 'a' (all) |
| `--unclassified_estimation` | 估算未分类比例 | 关闭 |""",
    },
    "fastp": {
        "usage": """# 基本质控
fastp -i input_R1.fq.gz -I input_R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz

# 单端数据
fastp -i input.fq.gz -o clean.fq.gz

# 自动检测适配器 + HTML 报告
fastp -i R1.fq.gz -I R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz --html report.html --json report.json

# 低质量碱基修剪
fastp -i R1.fq.gz -I R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz --qualified_quality_phred 20 --length_required 50

# UMI 处理
fastp -i R1.fq.gz -I R2.fq.gz -o clean_R1.fq.gz -O clean_R2.fq.gz --umi --umi_loc read1 --umi_len 8""",
        "key_params": """| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-i / -I` | 输入 R1 / R2 | 必需 |
| `-o / -O` | 输出 R1 / R2 | 必需 |
| `--qualified_quality_phred` | 质量阈值 | 20 |
| `--unqualified_percent_limit` | 允许的低质量碱基占比 | 40 |
| `--length_required` | 最短读长 | 15 |
| `--adapter_sequence` | 适配器序列 | 自动检测 |
| `--html` | HTML 报告 | 无 |
| `--json` | JSON 报告 | 无 |
| `--thread` | 线程数 | 2 |""",
    },
    "megahit": {
        "usage": """# 宏基因组组装（配对端）
megahit -1 R1.fq.gz -2 R2.fq.gz -o megahit_out --num-cpu-threads 16

# 交错配对模式
megahit --12 interleaved.fq.gz -o megahit_out -t 16

# 长读长组装
megahit --long long_reads.fq.gz -o megahit_out_lr

# 混合组装（短+长读长）
megahit -1 R1.fq.gz -2 R2.fq.gz --long long_reads.fq.gz -o megahit_out_hybrid

# 使用预设参数
megahit -1 R1.fq.gz -2 R2.fq.gz --presets meta-large -o megahit_out --min-contig-len 1000""",
        "key_params": """| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-1 / -2` | 配对端输入 | 可选 |
| `--12` | 交错配对输入 | 可选 |
| `--long` | 长读长输入 | 可选 |
| `-o` | 输出目录 | megahit_out |
| `-t / --num-cpu-threads` | 线程数 | CPU 核心数 |
| `--min-contig-len` | 最小 contig 长度 | 200 |
| `--presets` | 预设 (meta-sensitive/meta-large) | meta |""",
    },
    "qiime2-amplicon": {
        "usage": """# 导入数据
qiime tools import \\
  --type 'SampleData[PairedEndSequencesWithQuality]' \\
  --input-path manifest.csv \\
  --output-path paired-end-demux.qza \\
  --input-format PairedEndFastqManifestPhred33

# DADA2 去噪
qiime dada2 denoise-paired \\
  --i-demultiplexed-seqs paired-end-demux.qza \\
  --p-trunc-len-f 240 \\
  --p-trunc-len-r 200 \\
  --o-table table.qza \\
  --o-representative-sequences rep-seqs.qza \\
  --o-denoising-stats stats.qza

# Alpha/Beta 多样性
qiime diversity core-metrics-phylogenetic \\
  --i-phylogeny rooted-tree.qza \\
  --i-table table.qza \\
  --p-sampling-depth 10000 \\
  --output-dir core-metrics-results

# 分类注释
qiime feature-classifier classify-sklearn \\
  --i-classifier classifier.qza \\
  --i-reads rep-seqs.qza \\
  --o-classification taxonomy.qza""",
        "key_params": """| 命令 | 说明 |
|------|------|
| `qiime tools import` | 导入数据 |
| `qiime dada2 denoise-paired` | DADA2 去噪 |
| `qiime diversity core-metrics-phylogenetic` | 多样性分析 |
| `qiime feature-classifier classify-sklearn` | 分类注释 |
| `qiime taxa barplot` | 分类柱状图 |
| `qiime emperor plot` | PCoA 3D 可视化 |""",
    },
    "dada2-pipeline": {
        "usage": """# R 语言使用
library(dada2)

# 1. 读取文件路径
fnFs <- sort(list.files("fastq/", pattern="_R1_001.fastq.gz", full.names=TRUE))
fnRs <- sort(list.files("fastq/", pattern="_R2_001.fastq.gz", full.names=TRUE))

# 2. 质量过滤
filtered <- filterAndTrim(fnFs, filtFs, fnRs, filtRs,
                          truncLen=c(240,200),
                          maxN=0, maxEE=c(2,2),
                          truncQ=2, rm.phix=TRUE,
                          compress=TRUE, multithread=TRUE)

# 3. 学习错误模型
errF <- learnErrors(filtFs, multithread=TRUE)
errR <- learnErrors(filtRs, multithread=TRUE)

# 4. 去重
derepFs <- derepFastq(filtFs)
derepRs <- derepFastq(filtRs)

# 5. 去噪
dadaFs <- dada(derepFs, err=errF, multithread=TRUE)
dadaRs <- dada(derepRs, err=errR, multithread=TRUE)

# 6. 合并配对
mergers <- mergePairs(dadaFs, derepFs, dadaRs, derepRs)

# 7. 构建 ASV 表
seqtab <- makeSequenceTable(mergers)

# 8. 去嵌合体
seqtab.nochim <- removeBimeraDenovo(seqtab, method="consensus")

# 9. 分类注释
taxa <- assignTaxonomy(seqtab.nochim, "silva_nr99_v138.1_train_set.fa.gz")""",
        "key_params": """| 函数 | 说明 |
|------|------|
| `filterAndTrim()` | 质量过滤和修剪 |
| `learnErrors()` | 学习测序错误模型 |
| `derepFastq()` | 快速去重 |
| `dada()` | 核心去噪算法 |
| `mergePairs()` | 合并配对端 |
| `makeSequenceTable()` | 构建 ASV 表 |
| `removeBimeraDenovo()` | 去嵌合体 |
| `assignTaxonomy()` | 分类注释 |""",
    },
    "metabat2": {
        "usage": """# 1. 先生成深度文件
jgi_summarize_bam_contig_depths --outputDepth depth.txt assembly.bam

# 2. 基本分箱
metabat2 -i assembly.fa -a depth.txt -o bins/bin -t 8

# 敏感模式（适合低覆盖数据）
metabat2 -i assembly.fa -a depth.txt -o bins/bin --sensitive

# 最小 contig 长度
metabat2 -i assembly.fa -a depth.txt -o bins/bin --minContig 2500

# 与多个 BAM 合并深度
jgi_summarize_bam_contig_depths --outputDepth depth.txt sample1.bam sample2.bam sample3.bam
metabat2 -i assembly.fa -a depth.txt -o bins/bin""",
        "key_params": """| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-i` | 组装 FASTA | 必需 |
| `-a` | 深度文件 | 必需 |
| `-o` | 输出前缀 | 必需 |
| `-t` | 线程数 | 0 (全部) |
| `--minContig` | 最小 contig 长度 | 2500 |
| `--sensitive` | 敏感模式 | 关闭 |
| `--maxP` | 最大分箱数 | 自动 |
| `--seed` | 随机种子 | 不固定 |""",
    },
    "checkm2": {
        "usage": """# 预测基因组质量
checkm2 predict --threads 8 --input bins/ --output-directory checkm2_output

# 指定输出格式
checkm2 predict --threads 8 --input bins/ --output-directory checkm2_output --output-format tab

# 使用 Diamond 而非 MMseqs2（更快）
checkm2 predict --threads 8 --input bins/ --output-directory checkm2_output --database_path /path/to/CheckM2_database

# 查看结果
cat checkm2_output/quality_report.tsv""",
        "key_params": """| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | MAG 目录或文件列表 | 必需 |
| `--output-directory` | 输出目录 | 必需 |
| `--threads` | 线程数 | 1 |
| `--output_format` | 输出格式 (tab/csv) | tab |
| `--database_path` | CheckM2 数据库路径 | 内置 |
| `--extension` | 基因组文件扩展名 | fasta |""",
    },
    "anvio": {
        "usage": """# 从 FASTA 创建 Contigs DB
anvi-gen-contigs-database -f contigs.fa -o CONTIGS.db -n 'My project'

# 运行 HMMs
anvi-run-hmms -c CONTIGS.db -T 8

# 运行 NCBI COGs
anvi-run-ncbi-cogs -c CONTIGS.db -T 8

# 导入 BAM 文件
anvi-init-bam -b mapped.bam -o mapped-processed.bam
anvi-profile -i mapped-processed.bam -c CONTIGS.db -o PROFILE -T 8

# 合并多个样本
anvi-merge */PROFILE/PROFILE.db -o MERGED -c CONTIGS.db

# 交互式可视化
anvi-interactive -p MERGED/PROFILE.db -c CONTIGS.db

# 分箱和精炼
anvi-cluster-contigs -p MERGED/PROFILE.db -c CONTIGS.db -C CONCOCT --driver concoct
anvi-refine -p MERGED/PROFILE.db -c CONTIGS.db -C CONCOCT -b Bin_1""",
        "key_params": """| 命令 | 说明 |
|------|------|
| `anvi-gen-contigs-database` | 创建 Contigs 数据库 |
| `anvi-run-hmms` | 运行 HMM 搜索 |
| `anvi-profile` | 生成样本 profile |
| `anvi-merge` | 合并多个样本 |
| `anvi-interactive` | 启动交互式界面 |
| `anvi-cluster-contigs` | 自动分箱 |
| `anvi-refine` | 手动精炼分箱 |
| `anvi-export-gene-calls` | 导出基因预测 |""",
    },
}


def enrich_doc(tool_id: str, existing_md: str, enrichment: dict) -> str:
    """Enrich an existing markdown doc with usage examples."""
    usage = enrichment.get("usage", "")
    key_params = enrichment.get("key_params", "")

    # Build enrichment block
    enrichment_block = ""
    if usage:
        enrichment_block += f"""
## 使用示例

```bash
{usage}
```
"""
    if key_params:
        enrichment_block += f"""
## 关键参数

{key_params}
"""

    # Insert before the "更多使用示例" section or before the final separator
    if "更多使用示例" in existing_md:
        existing_md = existing_md.replace(
            "> 📝 更多使用示例请参考官方文档。",
            enrichment_block + "\n> 📝 更多详细参数请参考官方文档。"
        )
    elif "---\n\n*最后更新" in existing_md:
        existing_md = existing_md.replace(
            "---\n\n*最后更新",
            enrichment_block + "\n---\n\n*最后更新"
        )
    else:
        existing_md += enrichment_block

    return existing_md


def main():
    project_root = Path(__file__).parent.parent
    docs_dir = project_root / "docs" / "skills" / "tools"

    enriched_count = 0
    for tool_id, enrichment in ENRICH_TOOLS.items():
        md_file = docs_dir / f"{tool_id}.md"
        if not md_file.exists():
            print(f"  ⚠️  {tool_id}.md not found, skipping")
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        enriched = enrich_doc(tool_id, content, enrichment)

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(enriched)

        print(f"  ✅ Enriched {tool_id}.md")
        enriched_count += 1

    print(f"\n🎉 Enriched {enriched_count} tool docs with detailed usage examples")


if __name__ == "__main__":
    main()
