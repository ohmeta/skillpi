# SkillPI 部署总结

## ✅ 已完成的配置

### 1. GitHub Actions Workflow

**文件**: `.github/workflows/deploy.yml`

功能：
- 自动部署到 GitHub Pages
- 支持手动触发（workflow_dispatch）
- 自动取消正在运行的旧任务
- 使用最新的 Pages API

触发条件：
- 推送到 main 分支
- 修改 docs/, mkdocs.yml, data/skills/ 等路径
- 手动触发

### 2. MkDocs 配置

**文件**: `mkdocs.yml`

更新内容：
- site_url: https://ohmeta.github.io/skillpi
- repo_url: https://github.com/ohmeta/skillpi
- 中文语言支持
- Material 主题配置

### 3. 部署脚本

**文件**: `scripts/deploy.sh`

功能：
- 一键部署到 gh-pages 分支
- 自动检查依赖
- 生成文档并构建
- 显示访问地址

使用方式：
```bash
./scripts/deploy.sh
```

### 4. 文档

| 文件 | 说明 |
|------|------|
| DEPLOYMENT.md | 完整部署指南 |
| docs/DEPLOY.md | 快速参考 |
| README.md | 更新了部署说明 |

---

## 🚀 部署步骤

### 首次部署

1. **启用 GitHub Pages**
   ```
   Settings → Pages → Source → GitHub Actions
   ```

2. **配置 Workflow 权限**
   ```
   Settings → Actions → General → Workflow permissions
   选择 "Read and write permissions"
   ```

3. **推送代码**
   ```bash
   git push origin main
   ```

4. **等待部署**
   - 查看：https://github.com/ohmeta/skillpi/actions
   - 时间：2-5 分钟

5. **访问网站**
   ```
   https://ohmeta.github.io/skillpi
   ```

### 后续更新

```bash
# 推送代码后自动部署
git add .
git commit -m "docs: 更新内容"
git push origin main
```

---

## 📊 部署架构

```
┌─────────────────┐
│   推送代码      │
│   (git push)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Actions  │
│  - 安装依赖     │
│  - 生成文档     │
│  - 构建网站     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Pages    │
│  (gh-pages 分支) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   CDN 分发      │
│  全球访问加速   │
└─────────────────┘
```

---

## 🔧 配置说明

### deploy.yml 关键配置

```yaml
# 触发条件
on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'mkdocs.yml'
      - 'data/skills/**'

# 权限配置
permissions:
  contents: read
  pages: write
  id-token: write

# 部署环境
environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
```

### mkdocs.yml 关键配置

```yaml
site_url: https://ohmeta.github.io/skillpi
repo_url: https://github.com/ohmeta/skillpi

theme:
  name: material
  language: zh
```

---

## ⚠️ 注意事项

### 1. 域名配置

如果使用自定义域名：

1. 添加 CNAME 记录
2. 在 docs/ 目录创建 CNAME 文件
3. 更新 mkdocs.yml

```yaml
# mkdocs.yml
custom_domain: skillpi.example.com
```

### 2. 部署失败处理

查看日志：
```
Actions → Deploy Docs → 查看失败步骤
```

常见问题：
- 依赖安装失败 → 检查 pyproject.toml
- MkDocs 构建错误 → 运行 `mkdocs build --verbose`
- 权限错误 → 检查 Workflow permissions

### 3. CDN 缓存

部署后可能需要 5-10 分钟生效，因为 CDN 缓存刷新。

强制刷新：
```
https://ohmeta.github.io/skillpi/?v=时间戳
```

---

## 📈 优化建议

### 1. 减少构建时间

- 使用 pip cache
- 减少不必要的依赖
- 使用并发构建

### 2. 自动化更新

添加定时任务：

```yaml
# .github/workflows/update.yml
on:
  schedule:
    - cron: '0 0 * * 1'  # 每周一
```

### 3. 预览功能

使用 Netlify 或 Vercel 可以获得 PR 预览功能。

---

## 🎯 下一步

1. **推送代码到 GitHub**
   ```bash
   git push origin main
   ```

2. **配置 GitHub Pages**
   - Settings → Pages
   - 选择 GitHub Actions

3. **验证部署**
   - 访问 https://ohmeta.github.io/skillpi
   - 测试搜索功能
   - 检查所有链接

4. **配置自定义域名**（可选）
   - 添加 DNS 记录
   - 创建 CNAME 文件

---

## 📚 相关资源

- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [MkDocs 文档](https://www.mkdocs.org/)
- [Material 主题](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

祝部署顺利！🎉
