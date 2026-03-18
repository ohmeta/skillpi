# SkillPI

技能目录网站主页

## 欢迎使用 SkillPI

**SkillPI** 是一个自动化的微生物组信息学技能目录生成系统。

## 功能特点

- 🔄 **自动化更新**: Snakemake pipeline 自动执行工具文档抓取
- 📚 **综合内容**: 包含工具清单、分析流程、概念术语等
- 🎯 **结构化数据**: 使用 YAML/JSON 格式存储技能数据
- 📖 **美观文档**: 基于 MkDocs Material 的现代化文档网站
- 🔍 **易于搜索**: 支持全文搜索和分类浏览

## 快速导航

| 类型 | 描述 | 链接 |
|------|------|------|
| 🛠️ 工具 | 微生物组分析工具目录 | [查看工具](skills/tools.md) |
| 🔄 工作流 | 完整的分析工作流程 | [查看工作流](skills/workflows.md) |
| 📖 概念 | 核心概念和术语解释 | [查看概念](skills/concepts.md) |

## 使用方法

### 安装

```bash
pip install -e ".[dev,pipeline]"
```

### 运行 Pipeline

```bash
cd pipelines
snakemake --cores all
```

### 查看文档

```bash
mkdocs serve
```

## 贡献

欢迎提交 Issue 和 Pull Request！

[GitHub 仓库](https://github.com/yourusername/skillpi){ .md-button }
