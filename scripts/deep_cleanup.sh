#!/bin/bash
# SkillPI 深度清理脚本 - 移除 MkDocs 相关代码和冗余数据

echo "🧹 开始深度清理 SkillPI 项目..."

# 1. 删除 MkDocs 相关依赖
echo "📦 更新 pyproject.toml，移除 MkDocs 依赖..."
sed -i '/mkdocs>=/d' pyproject.toml
sed -i '/mkdocs-material>=/d' pyproject.toml

# 2. 删除 MkDocs 生成器代码
echo "🗑️  删除 MkDocs 生成器..."
rm -f src/skillpi/generators/mkdocs_gen.py
rm -f src/skillpi/generators/__init__.py

# 3. 删除 CLI 中的 mkdocs 选项
echo "📝 更新 CLI..."
# 这个需要手动编辑，暂时跳过

# 4. 删除冗余的 JSON 数据文件
echo "🗑️  删除冗余 JSON 数据..."
rm -f data/skills/all_skills.json
rm -f data/skills/imported_skills.json
rm -f data/skills/real_tools.json
# 只保留 curated_tools.json

# 5. 删除使用 MkDocs 的脚本
echo "🗑️  删除依赖 MkDocs 的脚本..."
rm -f scripts/generate_docs.py
# generate_from_example.py 保留但需要更新

# 6. 清理 Python 缓存
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

echo "✅ 深度清理完成!"
echo ""
echo "⚠️  需要手动处理:"
echo "  1. 更新 src/skillpi/cli.py - 移除 mkdocs 选项"
echo "  2. 更新 scripts/generate_from_example.py - 移除 mkdocs 引用"
echo "  3. 更新 scripts/test_real_scrape.py - 移除 mkdocs 引用"
echo "  4. 更新 scripts/update_with_real_docs.py - 移除 mkdocs 引用"
echo "  5. 更新 src/skillpi/generators/__init__.py 或删除导入"
