#!/usr/bin/env python3
"""
从 GitHub 抓取工具信息
"""

import yaml
import json
from pathlib import Path
from datetime import datetime

from skillpi.models import Skill, Tool, SkillCategory, SkillLevel
from skillpi.scrapers import GitHubScraper

# 读取 Snakemake 参数
config_file = snakemake.params.config
output_file = snakemake.output[0]

# 加载配置
with open(config_file, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# 创建输出目录
output_path = Path(output_file)
output_path.parent.mkdir(parents=True, exist_ok=True)

# 抓取工具
scraper = GitHubScraper()
tools = []

for repo in config.get("github_repos", []):
    print(f"抓取：{repo['url']}")
    try:
        tool = scraper.scrape_tool(repo["url"])
        if tool:
            skill = Skill(
                id=tool.name.lower().replace(" ", "-").replace("/", "-"),
                type=SkillCategory.TOOL,
                data=tool
            )
            tools.append(skill.model_dump(mode="json"))
            print(f"  ✓ {tool.name}")
    except Exception as e:
        print(f"  ✗ 失败：{e}")

# 保存结果
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(tools, f, indent=2, ensure_ascii=False)

print(f"✓ 保存 {len(tools)} 个工具到 {output_file}")
