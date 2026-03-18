# SkillPI 快速开始指南

## 1. 环境设置

### 创建虚拟环境（如果还没有）

```bash
cd skillpi
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

### 安装依赖

```bash
pip install -e ".[dev,pipeline]"
```

## 2. 使用示例数据生成文档

最简单的方式是使用内置的示例数据：

```bash
# 生成文档网站
python scripts/generate_from_example.py

# 启动本地服务器
mkdocs serve

# 访问 http://localhost:8000
```

## 3. 使用 Snakemake Pipeline 自动抓取

### 配置数据源

编辑 `data/sources.yaml` 添加要抓取的工具：

```yaml
github_repos:
  - url: "https://github.com/biocore/qiime2"
    type: tool
    category: analysis
    priority: high

pypi_packages:
  - name: "qiime2"
    type: tool
    category: analysis
```

### 运行 Pipeline

```bash
cd pipelines
snakemake --cores all
```

### 查看生成的文档

```bash
cd ..
mkdocs serve
```

## 4. 使用 CLI 工具

```bash
# 查看所有命令
skillpi --help

# 列出技能
skillpi list

# 搜索技能
skillpi search --query "16S"

# 添加新技能
skillpi add --name "MyTool" --type tool --category analysis
```

## 5. 自定义配置

编辑 `config.yaml` 自定义：

- 数据源设置
- 爬虫参数
- 文档生成选项

## 6. 开发

```bash
# 运行测试
pytest

# 代码格式化
black src/ tests/
ruff check src/ tests/

# 类型检查
mypy src/
```

## 常见问题

### Q: 如何添加新的数据源？

A: 在 `src/skillpi/scrapers/` 创建新的爬虫类，继承 `BaseScraper`，然后在 `data/sources.yaml` 中配置。

### Q: Snakemake 运行失败？

A: 确保：
1. 已安装 snakemake: `pip install snakemake`
2. 在 `pipelines/` 目录运行
3. 检查 `data/sources.yaml` 格式正确

### Q: 文档网站不显示？

A: 运行 `mkdocs serve` 后访问 `http://localhost:8000`，确保端口未被占用。

## 下一步

- 查看 `DEVELOPMENT.md` 了解开发指南
- 查看 `data/skills/example_skills.yaml` 了解数据格式
- 贡献代码：Fork 仓库 → 创建分支 → 提交 PR
