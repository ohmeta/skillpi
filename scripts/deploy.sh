#!/bin/bash
# SkillPI 一键部署脚本

set -e

echo "================================"
echo "  SkillPI 部署到 GitHub Pages  "
echo "================================"
echo ""

# 检查依赖
check_dependencies() {
    echo "🔍 检查依赖..."
    
    if ! command -v python3 &> /dev/null; then
        echo "❌ 需要 Python3"
        exit 1
    fi
    
    if ! command -v git &> /dev/null; then
        echo "❌ 需要 Git"
        exit 1
    fi
    
    echo "✅ 依赖检查通过"
}

# 安装 Python 依赖
install_deps() {
    echo ""
    echo "📦 安装 Python 依赖..."
    
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    pip install -q --upgrade pip
    pip install -q -e ".[pipeline]"
    pip install -q mkdocs-material
    
    echo "✅ 依赖安装完成"
}

# 生成文档
generate_docs() {
    echo ""
    echo "📝 生成文档..."
    
    python scripts/generate_from_example.py
    
    echo "✅ 文档生成完成"
}

# 构建网站
build_site() {
    echo ""
    echo "🔨 构建网站..."
    
    mkdocs build --clean
    
    if [ ! -d "site" ]; then
        echo "❌ 构建失败"
        exit 1
    fi
    
    echo "✅ 网站构建完成"
}

# 部署到 gh-pages 分支
deploy() {
    echo ""
    echo "🚀 部署到 GitHub Pages..."
    
    # 检查是否在 git 仓库
    if [ ! -d ".git" ]; then
        echo "❌ 不在 Git 仓库中"
        exit 1
    fi
    
    # 保存当前分支
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    
    # 创建或切换到 gh-pages 分支
    if git show-ref --verify --quiet refs/heads/gh-pages; then
        echo "  切换到 gh-pages 分支..."
        git checkout gh-pages
    else
        echo "  创建 gh-pages 分支..."
        git checkout --orphan gh-pages
    fi
    
    # 清理旧文件
    echo "  清理旧文件..."
    rm -rf *
    rm -rf .[^.]*
    
    # 复制新文件
    echo "  复制新文件..."
    cp -r ../site/* .
    
    # 添加 CNAME 文件（如果有自定义域名）
    if [ -f "../docs/CNAME" ]; then
        cp ../docs/CNAME .
    fi
    
    # 提交
    echo "  提交更改..."
    git add .
    git commit -m "docs: 自动部署 $(date '+%Y-%m-%d %H:%M:%S')" || echo "  ⚠️  没有更改"
    
    # 推送
    echo "  推送到 GitHub..."
    git push -f origin gh-pages
    
    # 返回原分支
    echo "  返回原分支..."
    git checkout $CURRENT_BRANCH
    
    echo "✅ 部署完成"
}

# 显示访问地址
show_url() {
    echo ""
    echo "================================"
    echo "  ✨ 部署成功！"
    echo "================================"
    echo ""
    
    # 获取仓库信息
    REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
    
    if [[ $REMOTE == *"github.com"* ]]; then
        REPO_NAME=$(basename -s .git $REMOTE)
        USER_NAME=$(dirname $REMOTE | awk -F'/' '{print $(NF-1)}' | sed 's/.*://')
        
        echo "📍 访问地址:"
        echo "   https://${USER_NAME}.github.io/${REPO_NAME}"
        echo ""
        echo "⏱️  部署可能需要 5-10 分钟生效"
    else
        echo "📍 请手动检查 GitHub Pages 设置"
    fi
    
    echo ""
}

# 主函数
main() {
    check_dependencies
    install_deps
    generate_docs
    build_site
    deploy
    show_url
}

# 运行
main
