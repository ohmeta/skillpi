# 工作流

本页面包含所有微生物组分析工作流。

## 🔬 核心工作流

| 工作流 | 用途 | 难度 |
|--------|------|------|
| [bioBakery](workflows/biobakery-workflow) | 集成分析流程 | ⭐⭐ 中级 |

## 📊 bioBakery 工作流

**完整分析流程**:

```
1. 质量控制（fastp）
   ↓
2. 物种分类谱分析（MetaPhlAn）
   ↓
3. 功能谱分析（HUMAnN）
   ↓
4. 下游统计分析
```

**特点**:
- ✅ 集成多个 bioBakery 工具
- ✅ 支持宏基因组和宏转录组
- ✅ 完整的文档和教程
- ✅ Docker/Vagrant支持

**安装**:
```bash
# 使用 Docker
docker pull biobakery/biobakery

# 或单独安装工具
conda install -c bioconda metaphlan
pip install humann
```
