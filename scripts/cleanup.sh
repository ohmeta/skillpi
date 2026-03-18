#!/bin/bash
# SkillPI 项目清理脚本

echo "🧹 开始清理 SkillPI 项目..."

# 删除 Node.js 构建产物
echo "📦 清理 Node.js 构建产物..."
rm -rf node_modules/
rm -rf docs/.vitepress/cache/
rm -rf docs/.vitepress/dist/

# 删除 Python 构建产物
echo "🐍 清理 Python 构建产物..."
rm -rf site/
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/
rm -rf .pytest_cache/
rm -rf .mypy_cache/
rm -rf __pycache__/
rm -rf src/__pycache__/
rm -rf src/skillpi/__pycache__/
rm -rf tests/__pycache__/
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# 删除虚拟环境 (如果存在)
echo "🔧 清理虚拟环境..."
# rm -rf venv/  # 保留 venv，可能还需要用

# 删除临时文件
echo "🗑️  清理临时文件..."
rm -rf *.log
rm -rf .coverage
rm -rf coverage.xml
rm -rf htmlcov/

# 删除 MkDocs 相关文件 (已迁移到 VitePress)
echo "📚 清理 MkDocs 文件..."
rm -f mkdocs.yml

# 删除冗余文档 (保留核心文档)
echo "📄 清理冗余文档..."
rm -f DEPLOYMENT.md
rm -f DEPLOY_SUMMARY.md
rm -f UI_MODERNIZATION.md
rm -f FINAL_SUMMARY.md
rm -f REAL_DATA_UPDATE.md
rm -f VERIFICATION_REPORT.md

# 保留的核心文档:
# - README.md (主文档)
# - QUICKSTART.md (快速开始)
# - DEVELOPMENT.md (开发指南)
# - VITEPRESS_MIGRATION.md (VitePress 迁移指南)
# - docs/GITHUB_ACTIONS_UPDATE.md (CI/CD 指南)

echo "✅ 清理完成!"
echo ""
echo "📊 清理结果:"
echo "  - Node.js 构建产物 ✓"
echo "  - Python 构建产物 ✓"
echo "  - MkDocs 配置 ✓"
echo "  - 冗余文档 ✓"
echo ""
echo "💡 提示:"
echo "  运行 'npm install' 重新安装依赖"
echo "  运行 'npm run dev' 启动开发服务器"
