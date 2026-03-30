---
title: 基因组解析的宏基因组学
description: Genome-resolved Metagenomics — 从复杂群落中解析单个基因组
---

# 基因组解析的宏基因组学

> **Genome-resolved metagenomics** 将宏基因组分析从"群落整体统计"推进到"单个基因组水平"，使我们能够直接研究未培养微生物的基因组生物学。

## 与传统宏基因组的区别

| 维度 | 传统宏基因组 | 基因组解析宏基因组 |
|------|------------|-----------------|
| **分析单位** | reads / contigs | 完整基因组 (MAGs) |
| **输出** | 物种丰度表、通路丰度表 | 个体基因组 + 群落统计 |
| **深度** | 群落水平 | 单菌水平 |
| **可比性** | 跨样本丰度变化 | 基因组结构变异、SNV |
| **工具链** | MetaPhlAn + HUMAnN | MEGAHIT + MetaBAT2 + CheckM2 + GTDB-Tk |

## 完整工作流程

```
原始数据 → QC → 组装 → 分箱 → 质量评估 → 分类 → 功能注释 → 比较基因组学
   ↓       ↓     ↓      ↓       ↓         ↓       ↓           ↓
 fastp  MEGAHIT MetaBAT2 CheckM2  GTDB-Tk  Prokka   anvi'o
        metaSPAdes MaxBin2                Bakta    PanPhlAn
          Flye   CONCOCT                  DRAM
                    ↓
               DAS Tool (整合)
```

## 核心步骤详解

### 1. 组装

```bash
# 短读长
megahit -1 R1.fq.gz -2 R2.fq.gz -o assembly --min-contig-len 1000

# 长读长 (PacBio HiFi)
flye --pacbio-hifi reads.fq.gz --out-dir assembly --meta

# 混合
# 先分别组装，再用 metaSPAdes hybrid 模式
```

### 2. 分箱

```bash
# 计算丰度
bowtie2-build assembly/final.contigs.fa assembly_bt2
bowtie2 -x assembly_bt2 -1 R1.fq.gz -2 R2.fq.gz | samtools sort > mapped.bam
jgi_summarize_bam_contig_depths --outputDepth depth.txt mapped.bam

# 多工具分箱
metabat2 -i assembly.fa -a depth.txt -o metabat2_bins/bin
maxbin2 -i assembly.fa -abund depth.txt -out maxbin2_bins
concoct --composition_file assembly.fa --coverage_file depth.txt -b concoct_bins

# 整合
DAStool -i metabat2.tsv,maxbin2.tsv,concoct.tsv -c assembly.fa -o dastool_out
```

### 3. 质量评估

```bash
# CheckM2
checkm2 predict --input bins/ --output-directory checkm2 --threads 8

# 过滤: 完整性 ≥50%, 污染 ≤10%
```

### 4. 分类注释

```bash
gtdbtk classify_wf --genome_dir bins/ --out_dir gtdbtk_out --cpus 16
```

### 5. 功能注释

```bash
# Prokka (快速注释)
prokka --outdir prokka_out --prefix bin1 bins/bin1.fa

# Bakta (标准化注释)
bakta --output bakta_out --db /path/to/db bins/bin1.fa

# DRAM (代谢注释)
DRAM.py annotate -i bins/ -o dram_out

# antiSMASH (BGC 检测)
antismash --output-dir antismash_out bins/bin1.fa
```

### 6. 比较基因组学

```bash
# anvi'o
anvi-gen-contigs-database -f contigs.fa -o CONTIGS.db
anvi-run-hmms -c CONTIGS.db
anvi-import-collection bins.txt -c CONTIGS.db -p PROFILE.db -C BINS
anvi-compute-genome-sanityity -c CONTIGS.db -p PROFILE.db -C BINS

# Pan-genome
anvi-gen-genomes-storage -e external-genomes.txt -o GENOMES.db
anvi-pan-genome -g GENOMES.db -o PAN --num-threads 16
```

## 质量标准总结

| 等级 | 完整性 | 污染 | 附加要求 |
|------|--------|------|---------|
| **高质量 (HQ)** | ≥90% | ≤5% | 23S+16S+5S rRNA, ≥18 tRNA |
| **中质量 (MQ)** | ≥50% | ≤10% | — |
| **低质量 (LQ)** | <50% | ≤10% | — |

## 参考文献

1. Parks et al. (2017) Recovery of nearly 8,000 metagenome-assembled genomes substantially expands the tree of life. *Nature Microbiology*. DOI: 10.1038/s41564-017-0012-7
2. Bowers et al. (2017) Minimum information about a single amplified genome (MISAG) and a metagenome-assembled genome (MIMAG). *Nature Biotechnology*. DOI: 10.1038/nbt.3893
3. Chen et al. (2025) MAGs: Advances, Challenges, and Opportunities. *Microorganisms*. DOI: 10.3390/microorganisms13050985

---

*最后更新: 2026-03-30*
