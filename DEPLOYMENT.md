# SkillPI 部署指南

本文档介绍如何将 SkillPI 文档网站部署到 GitHub Pages。

## 部署方式对比

| 方式 | 适用场景 | 难度 |
|------|---------|------|
| GitHub Actions 自动部署 | 推荐，每次推送自动更新 | ⭐ |
| 本地手动部署 | 测试或调试 | ⭐⭐ |
| 自定义域名 | 需要独立域名 | ⭐⭐ |

---

## 方案一：GitHub Actions 自动部署（推荐）

### 1. 启用 GitHub Pages

1. 进入仓库 **Settings** → **Pages**
2. **Source** 选择 **GitHub Actions**
3. 保存配置

### 2. 配置 Workflow

已配置 `deploy.yml`，触发条件：
- 推送到 `main` 分支
- 修改了 `docs/`, `mkdocs.yml`, `data/skills/` 等文件
- 手动触发（Workflow Dispatch）

### 3. 推送代码

```bash
git add .
git commit -m "docs: 更新技能数据"
git push origin main
```

### 4. 查看部署状态

1. 进入仓库 **Actions** 标签
2. 查看 **Deploy Docs** 工作流
3. 等待构建完成（约 2-5 分钟）
4. 访问生成的 URL

### 5. 访问网站

部署成功后，访问：
```
https://ohmeta.github.io/skillpi
```

---

## 方案二：本地手动部署

### 1. 安装依赖

```bash
pip install -e ".[pipeline]"
pip install mkdocs-material
```

### 2. 生成文档

```bash
python scripts/generate_from_example.py
```

### 3. 构建静态文件

```bash
mkdocs build --clean
```

生成的文件在 `site/` 目录。

### 4. 部署到 GitHub Pages

```bash
# 使用 ghpip 工具
pip install ghp-import
ghp-import -n -p -f site -b gh-pages

# 或使用 git 手动推送
cd site
git init
git add .
git commit -m "Deploy docs"
git remote add origin git@github.com:ohmeta/skillpi.git
git push -f origin HEAD:gh-pages
```

---

## 方案三：自定义域名

### 1. 准备域名

假设你有域名 `skillpi.example.com`

### 2. 配置 DNS

添加 CNAME 记录：
```
skillpi.example.com.  CNAME  ohmeta.github.io.
```

### 3. 配置 MkDocs

编辑 `mkdocs.yml`：
```yaml
custom_domain: skillpi.example.com
```

### 4. 创建 CNAME 文件

在 `docs/` 目录创建 `CNAME` 文件：
```
skillpi.example.com
```

### 5. 部署

推送后 GitHub Actions 会自动配置 SSL 证书。

---

## 故障排查

### 部署失败

查看 **Actions** 日志，常见问题：

1. **依赖安装失败**
   ```bash
   pip install --upgrade pip
   ```

2. **MkDocs 构建错误**
   ```bash
   mkdocs build --verbose
   ```

3. **权限错误**
   检查 `deploy.yml` 中的 permissions 配置

### 网站 404

1. 确认 `gh-pages` 分支存在
2. 检查 **Settings** → **Pages** 配置
3. 等待 5-10 分钟 CDN 刷新

### 样式丢失

清除浏览器缓存或检查：
```yaml
# mkdocs.yml
theme:
  name: material  # 确保主题正确
```

---

## 自动化建议

### 定时更新

添加定时任务自动更新技能数据：

```yaml
# .github/workflows/update-skills.yml
name: Update Skills

on:
  schedule:
    - cron: '0 0 * * 1'  # 每周一运行
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Update skills
        run: |
          cd pipelines
          snakemake --cores all
      
      - name: Commit changes
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add data/skills/
          git commit -m "chore: auto-update skills" || echo "No changes"
          git push
```

---

## 部署检查清单

- [ ] 已启用 GitHub Pages
- [ ] 已配置 deploy.yml
- [ ] 已推送代码到 main 分支
- [ ] Actions 中显示部署成功
- [ ] 访问 URL 正常显示
- [ ] 搜索功能正常
- [ ] 所有链接有效

---

## 其他部署平台

### Vercel

1. 在 Vercel 导入仓库
2. 设置构建命令：`mkdocs build`
3. 设置输出目录：`site`
4. 自动部署

### Netlify

1. 连接 GitHub 仓库
2. 构建命令：`mkdocs build`
3. 发布目录：`site`
4. 配置环境变量

### Cloudflare Pages

1. 连接 GitHub
2. 选择直接上传 `site` 目录
3. 享受免费 CDN

---

## 总结

**推荐流程**：
1. 使用 GitHub Actions 自动部署
2. 配置定时任务每周更新技能数据
3. 使用 GitHub Pages 免费托管
4. 可选：配置自定义域名

有任何问题欢迎提 Issue！
