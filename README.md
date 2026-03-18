# SkillPI

**Skill Catalogue for Microbiome Informatics Study**

微生物组信息学技能目录 - 帮助研究人员快速找到合适的工具并学习使用方法。

---

## 🚀 快速开始

### 安装依赖

```bash
# Node.js 依赖 (文档)
npm install

# Python 依赖 (工具)
pip install -e ".[dev,pipeline]"
```

### 本地开发

```bash
# 启动文档网站
npm run dev
# 访问 http://localhost:5173

# 生成技能文档
python scripts/generate_from_example.py
```

### 部署

```bash
# 构建静态站点
npm run build

# 部署到 GitHub Pages
git push origin main
# GitHub Actions 会自动部署
```

---

## 📚 核心内容

### 🛠️ 分析工具 (7 个核心工具)

| 工具 | 用途 | 难度 |
|------|------|------|
| [MetaPhlAn 4](docs/skills/tools/metaphlan-4.md) | 物种级分类分析 | ⭐ |
| [HUMAnN 3](docs/skills/tools/humann-3.md) | 功能谱分析 | ⭐⭐ |
| [QIIME 2](docs/skills/tools/qiime2-amplicon.md) | 扩增子分析平台 | ⭐⭐ |
| [DADA2](docs/skills/tools/dada2-pipeline.md) | ASV 去噪 | ⭐⭐ |
| [mothur](docs/skills/tools/mothur.md) | 16S 分析 | ⭐⭐ |
| [fastp](docs/skills/tools/fastp.md) | 质量控制 | ⭐ |
| [MEGAHIT](docs/skills/tools/megahit.md) | 宏基因组组装 | ⭐⭐⭐ |

### 🔄 工作流

- [bioBakery](docs/skills/workflows/biobakery-workflow.md) - 集成分析流程

### 📖 核心概念

- [16S rRNA 测序](docs/skills/concepts/16s-rrna-sequencing.md)
- [宏基因组测序](docs/skills/concepts/metagenomics-sequencing.md)

---

## 📊 项目统计

- **16+** 工具和工作流
- **4** 核心概念
- **100%** 数据来自官方文档
- **26** Git Commits

---

## 🎯 学习路径

### 初学者：16S 分析
```
16S 概念 → fastp 质控 → QIIME 2/DADA2 → 多样性分析
```

### 进阶：宏基因组
```
宏基因组概念 → MEGAHIT 组装 → MetaPhlAn → HUMAnN
```

---

## 🛠️ 技术栈

### 文档网站
- **VitePress** - 现代文档框架
- **Vue 3** - 前端框架

### Python 工具
- **Pydantic** - 数据验证
- **BeautifulSoup** - 网页爬虫
- **Snakemake** - 工作流管理

### 数据源
- **GitHub API** - 工具信息
- **PyPI API** - Python 包
- **官方文档** - 详细说明

---

## 📁 项目结构

```
skillpi/
├── docs/                    # 文档网站
│   ├── .vitepress/         # VitePress 配置
│   ├── skills/             # 技能文档
│   ├── guide/              # 使用指南
│   └── index.md            # 主页
├── src/skillpi/            # Python 包
│   ├── models.py           # 数据模型
│   ├── scrapers/           # 爬虫模块
│   └── generators/         # 文档生成器
├── scripts/                # 辅助脚本
├── data/                   # 数据文件
├── tests/                  # 测试
├── package.json            # Node.js 配置
└── pyproject.toml          # Python 配置
```

---

## 📖 文档

- **[快速开始](QUICKSTART.md)** - 5 分钟上手
- **[开发指南](DEVELOPMENT.md)** - 贡献代码必读
- **[VitePress 迁移](VITEPRESS_MIGRATION.md)** - 框架迁移说明
- **[CI/CD 指南](docs/GITHUB_ACTIONS_UPDATE.md)** - 部署配置

---

## 🧪 测试

```bash
# 运行测试
pytest

# 代码格式化
black src/ tests/
ruff check src/ tests/

# 类型检查
mypy src/
```

---

## 🤝 贡献

1. Fork 仓库
2. 创建分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📄 许可证

MIT License

---

## 🙏 致谢

感谢以下开源项目：
- [bioBakery](https://github.com/biobakery)
- [QIIME 2](https://qiime2.org)
- [DADA2](https://benjjneb.github.io/dada2/)
- [fastp](https://github.com/OpenGene/fastp)
- [MEGAHIT](https://github.com/voutcn/megahit)

---

## 📬 联系方式

- **GitHub**: https://github.com/ohmeta/skillpi
- **文档**: https://ohmeta.github.io/skillpi

---

**最后更新**: 2026-03-18
