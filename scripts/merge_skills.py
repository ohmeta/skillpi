#!/usr/bin/env python3
"""
合并所有技能数据
"""

import json
from pathlib import Path

# 读取 Snakemake 输入和输出
github_file = snakemake.input.github
pypi_file = snakemake.input.pypi
output_file = snakemake.output[0]

# 合并技能
all_skills = []

# 读取 GitHub 工具
with open(github_file, "r", encoding="utf-8") as f:
    github_tools = json.load(f)
    all_skills.extend(github_tools)
    print(f"✓ 加载 {len(github_tools)} 个 GitHub 工具")

# 读取 PyPI 工具
with open(pypi_file, "r", encoding="utf-8") as f:
    pypi_tools = json.load(f)
    all_skills.extend(pypi_tools)
    print(f"✓ 加载 {len(pypi_tools)} 个 PyPI 工具")

# 去重（基于 id）
seen = set()
unique_skills = []
for skill in all_skills:
    if skill["id"] not in seen:
        seen.add(skill["id"])
        unique_skills.append(skill)

print(f"✓ 去重后剩余 {len(unique_skills)} 个技能")

# 保存
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(unique_skills, f, indent=2, ensure_ascii=False)

print(f"✓ 保存到 {output_file}")
