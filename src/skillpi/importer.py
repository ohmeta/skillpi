"""
技能导入/导出工具

支持多种格式的导入导出：JSON, YAML, CSV
"""

import json
import csv
import yaml
from pathlib import Path
from typing import Optional

from .models import Skill, SkillCollection, SkillCategory
from .logger import get_logger

logger = get_logger("skillpi.importer")


class SkillImporter:
    """技能导入器"""
    
    @staticmethod
    def from_json(file_path: str) -> list[Skill]:
        """从 JSON 文件导入"""
        path = Path(file_path)
        logger.info(f"从 JSON 导入：{path}")
        
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        skills = []
        items = data if isinstance(data, list) else [data]
        
        for item in items:
            try:
                skill = Skill(**item)
                skills.append(skill)
            except Exception as e:
                logger.warning(f"跳过无效技能数据：{e}")
        
        logger.info(f"成功导入 {len(skills)} 个技能")
        return skills
    
    @staticmethod
    def from_yaml(file_path: str) -> list[Skill]:
        """从 YAML 文件导入"""
        path = Path(file_path)
        logger.info(f"从 YAML 导入：{path}")
        
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        skills = []
        items = data if isinstance(data, list) else [data]
        
        for item in items:
            try:
                skill = Skill(**item)
                skills.append(skill)
            except Exception as e:
                logger.warning(f"跳过无效技能数据：{e}")
        
        logger.info(f"成功导入 {len(skills)} 个技能")
        return skills
    
    @staticmethod
    def from_csv(file_path: str) -> list[Skill]:
        """从 CSV 文件导入"""
        path = Path(file_path)
        logger.info(f"从 CSV 导入：{path}")
        
        skills = []
        
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # 转换 CSV 数据为 Skill 格式
                    skill_data = {
                        "id": row.get("id", row.get("name", "").lower().replace(" ", "-")),
                        "type": row.get("type", "tool"),
                        "data": {
                            "name": row.get("name", ""),
                            "description": row.get("description", ""),
                            "category": row.get("category", "tool"),
                            "tags": row.get("tags", "").split(";") if row.get("tags") else [],
                            "skill_level": row.get("skill_level", "intermediate")
                        }
                    }
                    skill = Skill(**skill_data)
                    skills.append(skill)
                except Exception as e:
                    logger.warning(f"跳过无效行：{e}")
        
        logger.info(f"成功导入 {len(skills)} 个技能")
        return skills
    
    @staticmethod
    def from_directory(dir_path: str) -> list[Skill]:
        """从目录导入所有技能文件"""
        path = Path(dir_path)
        logger.info(f"从目录导入：{path}")
        
        all_skills = []
        
        for json_file in path.glob("*.json"):
            skills = SkillImporter.from_json(str(json_file))
            all_skills.extend(skills)
        
        for yaml_file in path.glob("*.yaml"):
            skills = SkillImporter.from_yaml(str(yaml_file))
            all_skills.extend(skills)
        
        logger.info(f"从目录导入总计 {len(all_skills)} 个技能")
        return all_skills


class SkillExporter:
    """技能导出器"""
    
    def __init__(self, skills: list[Skill]):
        self.skills = skills
    
    def to_json(self, file_path: str, indent: int = 2) -> None:
        """导出为 JSON"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        data = [skill.model_dump(mode="json") for skill in self.skills]
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        
        logger.info(f"导出 {len(self.skills)} 个技能到 JSON: {path}")
    
    def to_yaml(self, file_path: str) -> None:
        """导出为 YAML"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        data = [skill.model_dump(mode="json") for skill in self.skills]
        
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
        
        logger.info(f"导出 {len(self.skills)} 个技能到 YAML: {path}")
    
    def to_csv(self, file_path: str) -> None:
        """导出为 CSV"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        fieldnames = ["id", "name", "type", "category", "description", "skill_level", "tags", "url"]
        
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for skill in self.skills:
                data = skill.model_dump(mode="json")
                row = {
                    "id": data["id"],
                    "name": data["data"]["name"],
                    "type": data["type"],
                    "category": data["data"].get("category", ""),
                    "description": data["data"].get("description", "")[:200],
                    "skill_level": data["data"].get("skill_level", ""),
                    "tags": ";".join(data["data"].get("tags", [])),
                    "url": data["data"].get("url", "")
                }
                writer.writerow(row)
        
        logger.info(f"导出 {len(self.skills)} 个技能到 CSV: {path}")
    
    def to_markdown(self, output_dir: str) -> None:
        """导出为 Markdown 文件（按类型分组）"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 按类型分组
        by_type = {}
        for skill in self.skills:
            skill_type = skill.type.value
            if skill_type not in by_type:
                by_type[skill_type] = []
            by_type[skill_type].append(skill)
        
        # 为每个类型创建文件
        for skill_type, skills in by_type.items():
            md_file = output_path / f"{skill_type}.md"
            
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(f"# {skill_type.title()}s\n\n")
                
                for skill in skills:
                    data = skill.data
                    f.write(f"## {data.name}\n\n")
                    f.write(f"{data.description}\n\n")
                    
                    if hasattr(data, "category") and data.category:
                        f.write(f"- **类别**: {data.category}\n")
                    if hasattr(data, "skill_level"):
                        f.write(f"- **难度**: {data.skill_level}\n")
                    if hasattr(data, "tags") and data.tags:
                        f.write(f"- **标签**: {', '.join(data.tags)}\n")
                    
                    f.write("\n---\n\n")
            
            logger.info(f"导出 {len(skills)} 个 {skill_type} 到 Markdown: {md_file}")
