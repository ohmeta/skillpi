"""
Snakemake wrappers - 用于 Snakemake pipeline 的 Python 脚本
"""

import yaml
import json
from pathlib import Path
from datetime import datetime

from skillpi.models import Skill, Tool, Workflow, Concept, SkillCategory, SkillLevel
from skillpi.scrapers import GitHubScraper, PyPIScraper


def fetch_github_tools(config_file: str, output_dir: str):
    """从 GitHub 抓取工具信息"""
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    scraper = GitHubScraper()
    tools = []
    
    for repo in config.get("github_repos", []):
        print(f"抓取：{repo['url']}")
        tool = scraper.scrape_tool(repo["url"])
        if tool:
            skill = Skill(
                id=tool.name.lower().replace(" ", "-"),
                type=SkillCategory.TOOL,
                data=tool
            )
            tools.append(skill.model_dump(mode="json"))
    
    # 保存结果
    output_file = output_path / "github_tools.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 保存 {len(tools)} 个工具到 {output_file}")


def fetch_pypi_tools(config_file: str, output_dir: str):
    """从 PyPI 抓取工具信息"""
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    scraper = PyPIScraper()
    tools = []
    
    for package in config.get("pypi_packages", []):
        url = f"https://pypi.org/project/{package['name']}/"
        print(f"抓取：{url}")
        tool = scraper.scrape_tool(url)
        if tool:
            skill = Skill(
                id=tool.name.lower().replace(" ", "-"),
                type=SkillCategory.TOOL,
                data=tool
            )
            tools.append(skill.model_dump(mode="json"))
    
    # 保存结果
    output_file = output_path / "pypi_tools.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 保存 {len(tools)} 个工具到 {output_file}")


def merge_skills(input_dirs: list[str], output_file: str):
    """合并所有技能数据"""
    all_skills = []
    
    for input_dir in input_dirs:
        input_path = Path(input_dir)
        for json_file in input_path.glob("*.json"):
            with open(json_file, "r", encoding="utf-8") as f:
                skills = json.load(f)
                all_skills.extend(skills)
    
    # 去重（基于 id）
    seen = set()
    unique_skills = []
    for skill in all_skills:
        if skill["id"] not in seen:
            seen.add(skill["id"])
            unique_skills.append(skill)
    
    # 保存
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(unique_skills, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 合并 {len(unique_skills)} 个技能到 {output_file}")


def generate_docs(input_file: str, output_dir: str):
    """生成文档"""
    from skillpi.generators import MkDocsGenerator
    
    # 读取技能数据
    with open(input_file, "r", encoding="utf-8") as f:
        skills_data = json.load(f)
    
    # 临时保存到 input_dir
    input_path = Path(input_file).parent
    temp_file = input_path / "temp_skills.json"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(skills_data, f, indent=2, ensure_ascii=False)
    
    # 生成文档
    generator = MkDocsGenerator(str(input_path), output_dir)
    generator.generate()
    
    # 清理临时文件
    temp_file.unlink()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("用法：python -m skillpi.wrappers <command> [args...]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "fetch_github":
        fetch_github_tools(sys.argv[2], sys.argv[3])
    elif command == "fetch_pypi":
        fetch_pypi_tools(sys.argv[2], sys.argv[3])
    elif command == "merge":
        merge_skills(sys.argv[2].split(","), sys.argv[3])
    elif command == "generate_docs":
        generate_docs(sys.argv[2], sys.argv[3])
