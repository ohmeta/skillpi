# GitHub Actions 部署指南

## 📦 更新内容

由于迁移到 VitePress，GitHub Actions workflow 已更新。

### 主要变更

| 项目 | 之前 (MkDocs) | 现在 (VitePress) |
|------|--------------|-----------------|
| **运行环境** | Python 3.11 | Node.js 18 + Python 3.11 |
| **依赖安装** | `pip install mkdocs-material` | `npm ci` |
| **构建命令** | `mkdocs build` | `npm run build` |
| **输出目录** | `./site` | `./docs/.vitepress/dist` |
| **缓存** | pip cache | npm cache |

---

## 🔧 Workflow 配置

### deploy.yml (文档部署)

**触发条件**:
- 推送到 main 分支
- 修改了 `docs/`, `package.json`, `package-lock.json`
- 手动触发 (workflow_dispatch)

**构建流程**:
```yaml
1. Checkout 代码
2. 设置 Node.js 18
3. 设置 Python 3.11
4. 安装 Python 依赖 (生成技能文档)
5. 运行 Python 脚本生成技能文档
6. 安装 Node 依赖
7. 构建 VitePress 站点
8. 上传到 GitHub Pages
9. 部署
```

**输出目录**:
```
./docs/.vitepress/dist/
├── index.html
├── assets/
├── skills/
└── ...
```

### ci.yml (持续集成)

**无需更改** - 仍然用于测试 Python 代码

**测试流程**:
```yaml
1. 设置 Python (3.9, 3.10, 3.11)
2. 安装依赖
3. 运行 linting (ruff, black, mypy)
4. 运行测试 (pytest)
5. 上传覆盖率
```

---

## 🚀 部署步骤

### 首次部署配置

1. **启用 GitHub Pages**
   ```
   Settings → Pages → Build and deployment
   Source: GitHub Actions
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

4. **查看部署状态**
   ```
   Actions → Deploy Docs
   ```

### 手动触发部署

在 GitHub 上：
```
Actions → Deploy Docs → Run workflow → Run workflow
```

---

## 📊 部署时间

| 步骤 | 预计时间 |
|------|---------|
| Checkout | 10 秒 |
| Setup Node + Python | 20 秒 |
| Install dependencies | 30 秒 |
| Generate docs | 10 秒 |
| Build VitePress | 30 秒 |
| Deploy | 20 秒 |
| **总计** | **~2 分钟** |

---

## 🔍 故障排查

### 构建失败

**检查点**:
1. Node.js 版本是否正确 (18+)
2. `package.json` 是否存在
3. `npm ci` 是否成功
4. `npm run build` 是否有错误

**查看日志**:
```
Actions → Deploy Docs → 查看失败步骤
```

### 常见错误

#### 1. Node 版本错误
```
Error: Unable to find Node.js version
```
**解决**: 确保使用 Node 18+

#### 2. 依赖安装失败
```
npm ERR! code ENOENT
```
**解决**: 检查 `package.json` 是否存在

#### 3. 构建错误
```
[vitepress] Error during build
```
**解决**: 本地运行 `npm run build` 测试

#### 4. 权限错误
```
Error: Permission denied
```
**解决**: 检查 Workflow permissions

---

## 📁 文件结构

```
.github/workflows/
├── deploy.yml      # 文档部署 (VitePress)
└── ci.yml          # 持续集成 (Python 测试)
```

---

## 🎯 本地测试部署

### 1. 本地构建
```bash
npm install
npm run build
```

### 2. 预览构建结果
```bash
npm run preview
```

### 3. 检查输出
```bash
ls -la docs/.vitepress/dist/
```

---

## 📈 优化建议

### 1. 缓存优化
```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    cache: 'npm'  # 启用 npm 缓存
```

### 2. 并行构建
如果有多个独立任务，可以使用 matrix 策略并行运行。

### 3. 减少触发路径
```yaml
paths:
  - 'docs/**'
  - 'package.json'
  # 只在这些文件变化时触发
```

---

## 🔗 相关资源

- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [VitePress 部署指南](https://vitepress.dev/guide/deploy)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

**更新时间**: 2026-03-18  
**状态**: ✅ 已更新  
**Workflow**: deploy.yml
