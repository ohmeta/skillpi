---
title: BWA-MEM2
description: BWA-MEM 的加速版本，利用 SIMD 指令提升比对速度 2-3 倍
---

# BWA-MEM2

> BWA-MEM 的加速版本，利用 SIMD 指令提升比对速度 2-3 倍

## 基本信息

| 属性 | 值 |
|------|-----|
| **类别** | alignment |
| **难度** | ⭐ 初级 |
| **语言** | C++ |
| **GitHub Stars** | 825 |
| **标签** | alignment, short-read, SIMD, accelerated, bioinformatics, genomics, sequence-alignment |

## 链接

- 📦 **代码仓库**: [https://github.com/bwa-mem2/bwa-mem2](https://github.com/bwa-mem2/bwa-mem2)
- 📄 **论文**: [https://doi.org/10.1109/IPDPS.2019.00041](https://doi.org/10.1109/IPDPS.2019.00041)

## 安装

```bash
conda install -c bioconda bwa-mem2
```

## 简介

BWA-MEM 的加速版本，利用 SIMD 指令提升比对速度 2-3 倍

## 使用示例

> 📝 更多使用示例请参考官方文档。

## 参考资源

- 📖 **官方文档**: [https://github.com/bwa-mem2/bwa-mem2](https://github.com/bwa-mem2/bwa-mem2)
- 🎓 **教程**: [https://github.com/bwa-mem2/bwa-mem2#usage](https://github.com/bwa-mem2/bwa-mem2#usage)
- 📄 **论文**: Vasimuddin et al. (2019) Efficient Architecture-Aware Acceleration of BWA-MEM for Multicore Systems. *IEEE IPDPS*. DOI: [10.1109/IPDPS.2019.00041](https://doi.org/10.1109/IPDPS.2019.00041)

### 相关工具

- [Bowtie 2](./bowtie2)
- [minimap2](./minimap2)

### 相关概念

- [Quality Control](../concepts/quality-control)

---

*最后更新: 2026-03-30*
