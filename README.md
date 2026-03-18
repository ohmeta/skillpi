# SkillPI

**Skill Catalogue for Microbiome Informatics Study**

SkillPI 是一个自动化的微生物组信息学技能目录生成系统，通过 Snakemake pipeline 自动抓取最新工具的文档和使用技巧，并通过美观的文档网站展现。

## 功能特点

- 🔄 **自动化更新**: Snakemake pipeline 自动执行工具文档抓取
- 📚 **综合内容**: 包含工具清单、分析流程、概念术语等
- 🎯 **结构化数据**: 使用 YAML/JSON 格式存储技能数据
- 📖 **美观文档**: 基于 MkDocs Material 的现代化文档网站
- 🔍 **易于搜索**: 支持全文搜索和分类浏览

## 快速开始

### 1. 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/skillpi.git
cd skillpi

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -e ".[dev,pipeline]"
```

### 2. 使用示例数据（快速体验）

```bash
# 生成文档网站
python scripts/generate_from_example.py

# 本地预览
mkdocs serve
# 访问 http://localhost:8000
```

### 3. 使用 Snakemake Pipeline（自动抓取）

```bash
# 编辑 data/sources.yaml 配置数据源
# 然后运行：
cd pipelines
snakemake --cores all
```

### 4. 使用 CLI 工具

```bash
skillpi --help
skillpi list
skillpi search --query "16S"
```

## 项目结构

```
skillpi/
├── src/skillpi/          # Python 源代码
│   ├── models.py         # 数据模型 (Tool, Workflow, Concept)
│   ├── cli.py            # 命令行接口
│   ├── scrapers/         # 文档爬虫 (GitHub, PyPI)
│   └── generators/       # 文档生成器 (MkDocs)
├── pipelines/            # Snakemake workflows
├── scripts/              # 辅助脚本
├── data/
│   ├── sources.yaml      # 数据源配置
│   └── skills/           # 技能数据
├── docs/                 # 生成的文档网站
├── tests/                # 测试文件
├── mkdocs.yml            # MkDocs 配置
└── pyproject.toml        # 项目配置
```

## 文档

- 📖 [快速开始](QUICKSTART.md) - 5 分钟上手
- 🔧 [开发指南](DEVELOPMENT.md) - 贡献代码必读

## 开发

```bash
# 运行测试
pytest

# 代码格式化
black src/ tests/
ruff check src/ tests/

# 类型检查
mypy src/
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
