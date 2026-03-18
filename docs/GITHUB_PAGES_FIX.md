# GitHub Pages 部署修复

## 🐛 问题诊断

### 症状
- ✅ 本地 `npm run dev` 工作正常
- ❌ GitHub Pages 上页面无主题
- ❌ CSS/JS 文件加载失败

### 根本原因
**缺少 VitePress `base` 配置**

GitHub Pages 部署在子路径：
```
https://ohmeta.github.io/skillpi/
                      ^^^^^^^^^
                      子路径
```

如果没有配置 `base`，VitePress 会生成绝对路径：
```html
<!-- 错误的路径 -->
<link rel="stylesheet" href="/assets/style.css">
<script src="/assets/app.js"></script>

<!-- 浏览器会请求 -->
https://ohmeta.github.io/assets/style.css  ❌ 404
```

## ✅ 修复方案

### 1. 配置 base path

```typescript
// docs/.vitepress/config.ts
export default defineConfig({
  base: '/skillpi/',  // ← 添加这个
  // ...
})
```

### 2. 更新资源路径

```typescript
head: [
  ['link', { rel: 'icon', href: '/skillpi/favicon.ico' }]
]
```

### 3. 重新构建

```bash
npm run build
```

### 4. 部署

```bash
git push origin main
# GitHub Actions 会自动部署
```

## 🔍 验证方法

### 检查生成的 HTML

```bash
npm run build
grep -E "(href|src)" docs/.vitepress/dist/index.html
```

**正确输出**:
```html
<link rel="stylesheet" href="/skillpi/assets/style.css">
<script src="/skillpi/assets/app.js"></script>
```

### 访问 GitHub Pages

打开 https://ohmeta.github.io/skillpi/

检查浏览器开发者工具：
- Network 标签应该显示所有资源加载成功
- Console 标签应该没有 404 错误

## 📚 VitePress 部署文档

- [GitHub Pages 部署指南](https://vitepress.dev/guide/deploy)
- [Base URL 配置](https://vitepress.dev/reference/site-config#base)

## ⚠️ 常见错误

### 错误 1: 忘记配置 base

```typescript
// ❌ 错误
export default defineConfig({
  title: 'SkillPI',
  // 缺少 base 配置
})
```

**症状**: 页面无主题，资源 404

### 错误 2: base 路径不匹配

```typescript
// ❌ 错误 - 仓库名是 skillpi，但配置成其他值
export default defineConfig({
  base: '/my-docs/',  // 应该是 /skillpi/
})
```

**症状**: 资源路径错误

### 错误 3: 忘记更新 favicon 路径

```typescript
// ❌ 错误
head: [
  ['link', { rel: 'icon', href: '/favicon.ico' }]
  // 应该是 /skillpi/favicon.ico
]
```

**症状**: favicon 404

## 🎯 完整配置示例

```typescript
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'SkillPI',
  description: 'Skill Catalogue for Microbiome Informatics Study',
  base: '/skillpi/',  // ← GitHub Pages 必需
  
  head: [
    ['link', { rel: 'icon', href: '/skillpi/favicon.ico' }]
  ],
  
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '工具', link: '/skills/tools' }
    ],
    // ...
  }
})
```

## 🚀 部署检查清单

- [x] 配置 `base: '/skillpi/'`
- [x] 更新 favicon 路径
- [x] 本地构建成功
- [x] 检查 HTML 资源路径
- [x] 推送到 GitHub
- [x] GitHub Actions 部署成功
- [x] 访问 GitHub Pages 验证

---

**修复时间**: 2026-03-18  
**状态**: ✅ 已修复  
**Commit**: 0c292a0
