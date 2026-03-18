# SkillPI 部署快速参考

## 🚀 快速部署（3 步）

### 方式 1: GitHub Actions（推荐）

```bash
# 1. 推送代码
git push origin main

# 2. 等待自动部署（2-5 分钟）
# 查看：https://github.com/ohmeta/skillpi/actions

# 3. 访问网站
# https://ohmeta.github.io/skillpi
```

### 方式 2: 一键脚本

```bash
# 运行部署脚本
./scripts/deploy.sh
```

### 方式 3: 手动部署

```bash
# 1. 生成文档
python scripts/generate_from_example.py

# 2. 构建网站
mkdocs build --clean

# 3. 部署
ghp-import -n -p -f site -b gh-pages
```

---

## 📋 首次配置

### 1. 启用 GitHub Pages

```
Settings → Pages → Source → GitHub Actions
```

### 2. 检查 Workflow 权限

```
Settings → Actions → General → Workflow permissions
选择 "Read and write permissions"
```

### 3. 验证部署

```bash
# 本地测试
mkdocs serve
# 访问 http://localhost:8000
```

---

## 🔧 常用命令

```bash
# 生成文档
python scripts/generate_from_example.py

# 本地预览
mkdocs serve

# 构建静态文件
mkdocs build

# 部署到 gh-pages
ghp-import -n -p -f site

# 查看 git 历史
git log --oneline
```

---

## ⚠️ 常见问题

| 问题 | 解决方案 |
|------|---------|
| 部署后 404 | 等待 10 分钟，检查 gh-pages 分支 |
| 样式丢失 | 清除浏览器缓存 |
| Workflow 失败 | 查看 Actions 日志 |
| 权限错误 | 检查 Workflow permissions |

---

## 📊 部署流程

```
推送代码 → GitHub Actions → 安装依赖 → 生成文档 → 构建网站 → 部署到 gh-pages → CDN 分发
```

---

## 🔗 相关链接

- **部署指南**: DEPLOYMENT.md
- **开发指南**: DEVELOPMENT.md
- **仓库**: https://github.com/ohmeta/skillpi
- **文档**: https://ohmeta.github.io/skillpi
