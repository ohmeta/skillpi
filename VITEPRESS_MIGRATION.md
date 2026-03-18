# VitePress 迁移指南

## 🎉 为什么迁移到 VitePress？

### MkDocs 的问题
- ❌ 定制能力弱，难以实现现代化仪表板
- ❌ 主题风格受限，违和感重
- ❌ Python 生态，前端能力有限

### VitePress 的优势
- ✅ 现代设计，默认主题就很美观
- ✅ Vue 3 驱动，支持自定义组件
- ✅ 极速加载 (Vite 构建)
- ✅ 中文文档完善
- ✅ 更好的响应式设计

---

## 📦 安装步骤

### 1. 安装 Node.js (如果还没有)

```bash
# 使用 nvm (推荐)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18

# 或使用系统包管理器
# Ubuntu/Debian
sudo apt install nodejs npm

# macOS
brew install node
```

### 2. 安装依赖

```bash
cd skillpi
npm install
```

### 3. 本地开发

```bash
# 启动开发服务器
npm run dev

# 访问 http://localhost:5173
```

### 4. 构建生产版本

```bash
# 构建静态站点
npm run build

# 预览构建结果
npm run preview
```

---

## 📁 目录结构

```
skillpi/
├── docs/                    # 文档目录
│   ├── .vitepress/         # VitePress 配置
│   │   └── config.ts       # 配置文件
│   ├── public/             # 静态资源
│   │   └── hero.svg        # Logo
│   ├── guide/              # 指南
│   ├── skills/             # 技能文档
│   ├── index.md            # 主页
│   └── about.md            # 关于
├── package.json            # Node.js 配置
├── src/skillpi/            # Python 代码 (保留)
└── scripts/                # Python 脚本 (保留)
```

---

## 🔧 配置说明

### VitePress 配置 (docs/.vitepress/config.ts)

```typescript
export default defineConfig({
  title: 'SkillPI',
  description: 'Skill Catalogue for Microbiome Informatics Study',
  
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '工具', link: '/skills/tools' },
      // ...
    ],
    
    sidebar: {
      '/skills/': [
        // 侧边栏配置
      ]
    }
  }
})
```

### 主页配置 (docs/index.md)

使用 VitePress 的 frontmatter 配置：

```yaml
---
layout: home
title: SkillPI
hero:
  name: SkillPI
  text: 微生物组信息学技能目录
  tagline: Exploring the Human Microbiome
  actions:
    - theme: brand
      text: 开始使用
      link: /skills/tools
---
```

---

## 🎨 自定义样式

### 使用默认主题变量

VitePress 提供 CSS 变量：

```css
/* 颜色 */
--vp-c-brand          /* 主色调 */
--vp-c-bg             /* 背景色 */
--vp-c-text-1         /* 主文字 */
--vp-c-text-2         /* 次要文字 */

/* 阴影 */
--vp-shadow-2
--vp-shadow-4
```

### 添加自定义 CSS

在 Markdown 中使用 `<style>` 标签：

```markdown
<style>
.dashboard-section {
  padding: 4rem 2rem;
  background: var(--vp-c-bg-soft);
}
</style>
```

---

## 📊 对比

| 特性 | MkDocs | VitePress |
|------|--------|-----------|
| 加载速度 | 慢 | 极快 ⚡ |
| 定制能力 | 弱 | 强 ✅ |
| 设计现代感 | 一般 | 优秀 ✨ |
| 学习曲线 | 低 | 中等 |
| 生态 | Python | Node.js/Vue |

---

## 🚀 部署到 GitHub Pages

### 1. 添加部署脚本

```json
{
  "scripts": {
    "docs:build": "vitepress build docs",
    "docs:deploy": "npm run docs:build && npx gh-pages -d docs/.vitepress/dist"
  }
}
```

### 2. 安装 gh-pages

```bash
npm install --save-dev gh-pages
```

### 3. 部署

```bash
npm run docs:deploy
```

### 或使用 GitHub Actions

创建 `.github/workflows/deploy.yml`:

```yaml
name: Deploy Docs

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
      
      - name: Install dependencies
        run: npm install
      
      - name: Build
        run: npm run build
      
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/.vitepress/dist
```

---

## 🔍 常用命令

```bash
# 开发
npm run dev              # 启动开发服务器

# 构建
npm run build            # 构建生产版本
npm run preview          # 预览构建结果

# 部署
npm run docs:deploy      # 部署到 GitHub Pages
```

---

## ⚠️ 注意事项

### 1. Python 代码保留

SkillPI 的 Python 代码（爬虫、CLI 等）仍然保留：
- `src/skillpi/` - Python 包
- `scripts/` - Python 脚本
- `data/` - 数据文件

### 2. 文档迁移

原有 MkDocs 文档需要转换为 VitePress 格式：
- Frontmatter 语法略有不同
- 导航配置在 config.ts 中
- 支持 Markdown + Vue 组件

### 3. 依赖管理

- Node.js 依赖：`package.json`
- Python 依赖：`pyproject.toml` (保留)

---

## 📚 学习资源

- [VitePress 官方文档](https://vitepress.dev/)
- [VitePress 中文文档](https://vitepress.docschina.org/)
- [Vue 3 文档](https://vuejs.org/)
- [Markdown 指南](https://commonmark.org/help/)

---

## 🎯 下一步

1. ✅ 安装依赖 - `npm install`
2. ✅ 本地测试 - `npm run dev`
3. ✅ 自定义主题 - 修改 config.ts
4. ✅ 添加内容 - 编写 Markdown
5. ✅ 部署上线 - `npm run build`

---

**迁移完成时间**: 2026-03-18  
**状态**: ✅ 已完成  
**Git Commit**: 46e16ce
