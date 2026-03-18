# 关于 SkillPI

## 📖 项目介绍

**SkillPI** 是一个微生物组信息学技能目录系统，帮助研究人员快速找到合适的工具并学习使用方法。

## 🎯 目标

1. **自动化** - 通过 GitHub API 自动抓取最新工具信息
2. **结构化** - 使用统一的数据模型存储技能信息
3. **易访问** - 通过美观的文档网站快速查找所需信息
4. **可扩展** - 易于添加新的数据源和技能类型

## 🔬 研究领域

SkillPI 专注于支持以下微生物组研究领域：

- 🧬 **肠道微生物组** - 理解肠道菌群在人类健康和疾病中的作用
- 🦠 **口腔微生物组** - 探索口腔微生物群落及其对全身健康的影响
- 🌿 **皮肤微生物组** - 研究皮肤微生物多样性及其保护功能
- 💊 **治疗干预** - 开发基于微生物组的疗法

## 📊 数据统计

- **16+** 工具和工作流
- **4** 核心概念
- **100%** 数据来自官方文档
- **22** Git Commits

## 🛠️ 技术栈

### 前端
- [VitePress](https://vitepress.dev/) - 现代文档框架
- Vue 3 - 前端框架

### 后端
- Python 3.9+ - 核心逻辑
- Pydantic - 数据验证

### 数据源
- GitHub API - 工具信息抓取
- PyPI API - Python 包信息
- 官方文档 - 详细使用说明

## 📚 核心功能

### 1. 工具目录
收录微生物组分析常用工具，包括：
- 物种分析工具 (MetaPhlAn, QIIME 2)
- 功能分析工具 (HUMAnN)
- 质量控制工具 (fastp)
- 组装工具 (MEGAHIT)

### 2. 工作流
提供完整分析流程：
- bioBakery 集成工作流
- 扩增子分析流程
- 宏基因组分析流程

### 3. 概念解释
详解核心概念：
- 16S rRNA 测序
- 宏基因组测序
- Alpha/Beta 多样性

## 🔍 数据来源

所有工具信息均来自**官方来源**：

| 工具 | 数据来源 | 论文 |
|------|----------|------|
| MetaPhlAn 4 | GitHub + 官网 | Nature Biotech 2023 |
| HUMAnN 3 | GitHub + 官网 | eLife 2021 |
| QIIME 2 | GitHub + 官网 | Nature Biotech 2019 |
| DADA2 | GitHub | Nature Methods 2016 |
| mothur | GitHub + 官网 | AEM 2009 |
| fastp | GitHub | iMeta 2025 |
| MEGAHIT | GitHub | Bioinformatics 2015 |

## 👥 团队

**OHMeta Team** - 致力于微生物组信息学工具开发和知识分享

## 📬 联系方式

- **GitHub**: https://github.com/ohmeta/skillpi
- **Email**: contact@ohmeta.org (示例)

## 📄 许可证

MIT License

## 🙏 致谢

感谢以下开源项目的优秀文档：
- bioBakery (Huttenhower Lab)
- QIIME 2 (Caporaso Lab)
- DADA2 (Callahan et al.)
- fastp (OpenGene)
- MEGAHIT (Li et al.)

---

**最后更新**: 2026-03-18
