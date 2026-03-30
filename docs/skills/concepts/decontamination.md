---
title: 样本污染与去污染
description: 识别和去除微生物组样本中的环境/试剂污染
---

# 样本污染与去污染

> 低生物量样本（如血液、组织、CSF）极易受试剂和环境污染。不处理污染会导致严重的假阳性结果。

## 污染来源

| 来源 | 常见污染物 | 影响 |
|------|-----------|------|
| **DNA 提取试剂盒** | *Bacillus*, *Bradyrhizobium*, *Aquabacterium* | 主要来源 |
| **PCR 试剂** | *Pseudomonas*, *Acinetobacter* | 引入假阳性 |
| **环境空气** | 皮肤菌群 (*Staphylococcus*, *Corynebacterium*) | 操作污染 |
| **样本采集** | 口腔菌群、皮肤菌群 | 操作污染 |

## 检测方法

### 阴性对照法

```bash
# 1. 对阴性对照进行分类
kraken2 --db /db --output neg_control.kreport --report neg_control.report neg_control.fastq

# 2. 比较样本与阴性对照的 OTU 表
# 污染物在阴性对照中丰度高，在样本中丰度低
```

### 统计方法

| 工具 | 方法 | 输入 |
|------|------|------|
| **decontam** (R) | 频率法 + 频率/丰度组合 | OTU 表 + DNA 浓度 |
| **SourceTracker2** | 贝叶斯源追踪 | OTU 表 + 源标签 |
| **microDecon** | 去卷积 | OTU 表 + 阴性对照 |

### decontam 使用

```r
library(decontam)

# 1. 准备数据
ps <- phyloseq(otu_table, sample_data)

# 2. 标记阴性对照
sample_data(ps)$is_neg <- sample_data(ps)$SampleType == "Control"

# 3. 频率法（需要 DNA 浓度）
contam_df <- isContaminant(ps, method="frequency", conc="DNA_conc")

# 4. 丰度法（不需要浓度）
contam_df <- isContaminant(ps, method="prevalence", neg="is_neg", threshold=0.1)

# 5. 过滤
ps_clean <- prune_taxa(!contam_df$contaminant, ps)
```

## 最佳实践

1. **必做阴性对照**: 每批提取至少 2-3 个阴性对照
2. **记录批次**: 样本与阴性对照来自同一批次
3. **低生物量专项**: 血液/CSF 等低生物量样本需额外防护
4. **去除已知污染物**: 维护常见污染物列表并定期过滤

## 常见污染物列表

```python
# 常见试剂盒污染物 (Salter et al., 2014)
COMMON_CONTAMINANTS = [
    "Bradyrhizobium",
    "Aquabacterium",
    "Bacillus",
    "Pseudomonas",
    "Acinetobacter",
    "Staphylococcus",
    "Corynebacterium",
]
```

## 参考文献

1. Salter et al. (2014) Reagent and laboratory contamination can critically impact sequence-based microbiome analyses. *BMC Biology*. DOI: 10.1186/s12915-014-0087-z
2. Davis et al. (2018) Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data. *Microbiome*. DOI: 10.1186/s40168-018-0605-2
3. Knights et al. (2011) Bayesian community-wide culture-independent microbial source tracking. *Nature Methods*. DOI: 10.1038/nmeth.1650

---

*最后更新: 2026-03-30*
