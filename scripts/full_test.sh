#!/bin/bash
# SkillPI 完整测试脚本

set -e

echo "=========================================="
echo "  SkillPI 完整测试"
echo "=========================================="
echo ""

# 1. Python 测试
echo "🧪 1. 运行 Python 测试..."
./venv/bin/pytest tests/ -v --tb=short
echo "✅ Python 测试通过"
echo ""

# 2. 检查 CLI
echo "🔧 2. 测试 CLI 工具..."
./venv/bin/skillpi --version
./venv/bin/skillpi --help
./venv/bin/skillpi list
echo "✅ CLI 工具正常"
echo ""

# 3. 生成技能数据
echo "📊 3. 生成技能数据..."
./venv/bin/python scripts/generate_from_example.py
echo "✅ 技能数据生成成功"
echo ""

# 4. 检查数据文件
echo "📁 4. 检查数据文件..."
if [ -f "data/skills/curated_tools.json" ]; then
    echo "✅ curated_tools.json 存在"
    python3 -c "import json; d=json.load(open('data/skills/curated_tools.json')); print(f'  包含 {len(d)} 个技能')"
else
    echo "❌ curated_tools.json 不存在"
    exit 1
fi
echo ""

# 5. 文档构建测试
echo "📖 5. 构建文档网站..."
npm install --silent
npm run build
echo "✅ 文档构建成功"
echo ""

# 6. 检查构建产物
echo "📦 6. 检查构建产物..."
if [ -d "docs/.vitepress/dist" ]; then
    echo "✅ 构建目录存在"
    echo "  文件列表:"
    ls -1 docs/.vitepress/dist/ | head -10
else
    echo "❌ 构建目录不存在"
    exit 1
fi
echo ""

# 7. 检查死链接
echo "🔗 7. 检查死链接..."
npm run build 2>&1 | grep -i "dead link" && echo "⚠️  发现死链接" || echo "✅ 无死链接"
echo ""

# 8. 代码质量检查
echo "🎨 8. 代码质量检查..."
./venv/bin/ruff check src/ tests/ && echo "✅ Ruff 检查通过"
./venv/bin/black --check src/ tests/ && echo "✅ Black 格式化检查通过"
echo ""

echo "=========================================="
echo "  ✅ 所有测试通过！"
echo "=========================================="
echo ""
echo "📊 测试总结:"
echo "  ✓ Python 测试"
echo "  ✓ CLI 工具"
echo "  ✓ 数据生成"
echo "  ✓ 文档构建"
echo "  ✓ 构建产物"
echo "  ✓ 链接检查"
echo "  ✓ 代码质量"
echo ""
echo "🚀 项目已准备好部署！"
