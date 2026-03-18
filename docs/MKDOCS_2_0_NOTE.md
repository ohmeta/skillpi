# MkDocs 2.0 兼容性说明

## ⚠️ 重要提示

MkDocs 2.0 将引入重大变更，目前**不适用于生产环境**。

## 当前配置

SkillPI 已配置使用稳定的 MkDocs 版本：

```toml
# pyproject.toml
mkdocs>=1.5.0,<2.0.0
mkdocs-material>=9.5.0,<10.0.0
```

## 已修复的问题

### 1. 主题图标路径

**问题**: Material for MkDocs 新版本更改了图标路径

**修复**:
```yaml
# mkdocs.yml
palette:
  - media: "(prefers-color-scheme)"
    toggle:
      icon: material/brightness-auto  # 使用新版图标
```

### 2. 插件系统

Material 团队警告 MkDocs 2.0 将移除插件系统。当前配置已禁用不必要的插件。

## 部署配置

GitHub Actions 已配置安装兼容版本：

```yaml
# .github/workflows/deploy.yml
- name: Install dependencies
  run: |
    pip install -e ".[pipeline]"
    pip install mkdocs-material~=9.5.0  # 固定 9.5.x 版本
```

## 本地测试

```bash
# 安装依赖
pip install -e ".[pipeline]"

# 构建测试
mkdocs build --clean

# 本地预览
mkdocs serve
```

## 参考链接

- [Material for MkDocs 官方博客](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/)
- [MkDocs 官方文档](https://www.mkdocs.org/)

## 更新计划

我们将：
1. 监控 MkDocs 2.0 进展
2. 等待稳定的迁移方案
3. 在确保兼容性后更新

**当前建议**: 使用配置的稳定版本，不要升级到 MkDocs 2.0
