# 开发指南

## 项目结构

```
skillpi/
├── src/skillpi/          # Python 源代码
│   ├── __init__.py       # 包初始化
│   ├── models.py         # 数据模型定义
│   ├── cli.py            # 命令行接口
│   ├── scrapers/         # 文档爬虫模块
│   │   ├── __init__.py
│   │   ├── base.py       # 爬虫基类
│   │   ├── github.py     # GitHub 爬虫
│   │   ├── pypi.py       # PyPI 爬虫
│   │   └── biorxiv.py    # bioRxiv 爬虫
│   ├── generators/       # 文档生成器
│   │   ├── __init__.py
│   │   └── mkdocs_gen.py # MkDocs 生成器
│   └── wrappers.py       # Snakemake wrappers
├── pipelines/            # Snakemake workflows
│   └── Snakefile
├── scripts/              # Pipeline 脚本
│   ├── fetch_github.py
│   ├── fetch_pypi.py
│   ├── merge_skills.py
│   └── generate_docs.py
├── data/
│   ├── sources.yaml      # 数据源配置
│   └── skills/           # 生成的技能数据
├── docs/                 # 文档网站
│   ├── index.md
│   └── about.md
├── tests/                # 测试文件
│   ├── test_models.py
│   ├── test_scrapers.py
│   ├── test_cli.py
│   └── conftest.py
├── pyproject.toml        # 项目配置
├── mkdocs.yml            # MkDocs 配置
└── config.yaml           # SkillPI 配置
```

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/skillpi.git
cd skillpi

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e ".[dev,pipeline]"
```

## 开发流程

### 1. 添加新工具

编辑 `data/sources.yaml` 添加新工具：

```yaml
github_repos:
  - url: "https://github.com/new/tool"
    type: tool
    category: new_category
    priority: high
```

### 2. 运行 Pipeline

```bash
cd pipelines
snakemake --cores all
```

### 3. 查看生成的文档

```bash
mkdocs serve
# 访问 http://localhost:8000
```

### 4. 运行测试

```bash
pytest -v
```

### 5. 代码格式化

```bash
black src/ tests/
ruff check src/ tests/
```

## 添加新的爬虫

1. 在 `src/skillpi/scrapers/` 创建新的爬虫文件
2. 继承 `BaseScraper` 类
3. 实现 `scrape_tool`, `scrape_workflow`, `scrape_concept` 方法
4. 在 `__init__.py` 中导出

示例：

```python
from .base import BaseScraper

class NewScraper(BaseScraper):
    def scrape_tool(self, url: str):
        # 实现抓取逻辑
        pass
```

## 添加新的文档生成器

1. 在 `src/skillpi/generators/` 创建新的生成器
2. 实现 `generate()` 方法
3. 在 CLI 中添加新的生成选项

## 发布新版本

```bash
# 更新版本号 (src/skillpi/__init__.py)
# 创建 tag
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0

# GitHub Actions 会自动发布到 PyPI
```

## 常见问题

### Q: 如何调试爬虫？

A: 使用 `logging` 模块添加调试信息：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Q: 如何处理速率限制？

A: 在 `config.yaml` 中设置 `rate_limit_wait: true`，或在爬虫中添加延迟：

```python
import time
time.sleep(1)  # 请求间延迟 1 秒
```

### Q: 如何贡献代码？

A: 
1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request
