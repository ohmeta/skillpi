#!/usr/bin/env python3
"""
生成文档网站
"""

import json
from pathlib import Path

from skillpi.generators import MkDocsGenerator

# 读取 Snakemake 输入和输出
input_file = snakemake.input[0]
output_dir = snakemake.params.output_dir

# 读取技能数据
with open(input_file, "r", encoding="utf-8") as f:
    skills_data = json.load(f)

print(f"✓ 加载 {len(skills_data)} 个技能")

# 临时保存到输入目录
input_path = Path(input_file).parent
temp_file = input_path / "temp_skills.json"
with open(temp_file, "w", encoding="utf-8") as f:
    json.dump(skills_data, f, indent=2, ensure_ascii=False)

# 生成文档
generator = MkDocsGenerator(str(input_path), output_dir)
success = generator.generate()

# 清理临时文件
if temp_file.exists():
    temp_file.unlink()

if not success:
    raise Exception("文档生成失败")

print(f"✓ 文档生成完成：{output_dir}")
