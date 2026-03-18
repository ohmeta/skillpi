# 关于 SkillPI

## 项目背景

微生物组学研究正在快速发展，新的分析工具和方法不断涌现。研究人员需要花费大量时间来：

- 发现和评估合适的分析工具
- 学习不同工具的使用方法
- 理解复杂的分析流程
- 掌握相关概念和术语

SkillPI 旨在解决这个问题，通过自动化的方式收集、整理和展示微生物组信息学相关的技能信息。

## 项目目标

1. **自动化**: 通过 Snakemake pipeline 自动抓取最新工具的文档
2. **结构化**: 使用统一的数据模型存储技能信息
3. **易访问**: 通过美观的文档网站快速查找所需信息
4. **可扩展**: 易于添加新的数据源和技能类型

## 技术架构

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   数据源        │────▶│   Snakemake      │────▶│   技能数据      │
│   - GitHub      │     │   Pipeline       │     │   (JSON/YAML)   │
│   - PyPI        │     │                  │     │                 │
│   - bioRxiv     │     │                  │     │                 │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   MkDocs        │◀────│   文档生成器     │◀────│   技能数据      │
│   文档网站      │     │   (Python)       │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

## 核心组件

### Python 模块

- `models.py`: 数据模型定义（Tool, Workflow, Concept, Skill）
- `scrapers/`: 文档爬虫模块（GitHub, PyPI, bioRxiv）
- `generators/`: 文档生成器（MkDocs）
- `cli.py`: 命令行接口

### Snakemake Pipeline

- `fetch_github`: 从 GitHub 抓取工具信息
- `fetch_pypi`: 从 PyPI 抓取工具信息
- `merge_skills`: 合并所有技能数据
- `generate_docs`: 生成文档网站

### 数据源配置

`data/sources.yaml` 定义要抓取的数据源：

```yaml
github_repos:
  - url: "https://github.com/biocore/qiime2"
    type: tool
    category: analysis

pypi_packages:
  - name: "qiime2"
    type: tool
    category: analysis
```

## 开发计划

- [ ] 实现完整的爬虫功能
- [ ] 添加更多数据源（如 Nature Methods, Genome Biology 等）
- [ ] 实现技能难度评估
- [ ] 添加用户贡献功能
- [ ] 实现技能学习路径推荐

## 许可证

MIT License

## 联系方式

- Email: your.email@example.com
- GitHub: https://github.com/yourusername/skillpi
