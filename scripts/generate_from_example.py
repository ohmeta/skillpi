#!/usr/bin/env python3
"""
从示例 YAML 数据生成文档网站
"""

import yaml
import json
from pathlib import Path
from datetime import datetime

from skillpi.models import Skill, SkillCategory, Tool, Workflow, Concept, SkillLevel
# from skillpi.generators import MkDocsGenerator


def load_example_skills():
    """加载示例技能数据"""
    skills_file = Path("data/skills/example_skills.yaml")
    
    with open(skills_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    skills = []
    for item in data:
        skill = Skill(
            id=item["id"],
            type=SkillCategory(item["type"]),
            data=item["data"]
        )
        skills.append(skill.model_dump(mode="json"))
    
    return skills


def main():
    """主函数"""
    print("加载示例技能数据...")
    skills = load_example_skills()
    print(f"✓ 加载 {len(skills)} 个技能")
    
    # 保存到 skills 目录
    skills_dir = Path("data/skills")
    skills_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = skills_dir / "all_skills.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 保存到 {output_file}")
    
    print(f"\n✓ 技能数据生成完成！")
    print(f"\n下一步:")
    print(f"  npm install      # 安装依赖")
    print(f"  npm run dev      # 启动文档网站")
    print(f"  npm run build    # 构建静态站点")


if __name__ == "__main__":
    exit(main())
