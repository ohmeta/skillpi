"""
MkDocs 文档生成器
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional

from ..models import Skill, Tool, Workflow, Concept, SkillCategory


class MkDocsGenerator:
    """生成 MkDocs 文档"""
    
    def __init__(self, input_dir: str, output_dir: str):
        """
        初始化生成器
        
        Args:
            input_dir: 技能数据输入目录
            output_dir: MkDocs 文档输出目录
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.docs_dir = self.output_dir / "docs"
        self.skills_dir = self.docs_dir / "skills"
    
    def generate(self) -> bool:
        """
        生成完整文档
        
        Returns:
            是否成功
        """
        try:
            # 创建目录结构
            self.docs_dir.mkdir(parents=True, exist_ok=True)
            self.skills_dir.mkdir(parents=True, exist_ok=True)
            
            # 生成技能文档
            self._generate_skill_docs()
            
            # 生成导航配置
            self._update_nav()
            
            print(f"✓ 文档生成完成：{self.output_dir}")
            return True
        except Exception as e:
            print(f"✗ 文档生成失败：{e}")
            return False
    
    def _generate_skill_docs(self):
        """生成各个技能的文档页面"""
        # 读取所有技能数据
        skills = self._load_skills()
        
        # 按类型分组
        tools = [s for s in skills if s.type == SkillCategory.TOOL]
        workflows = [s for s in skills if s.type == SkillCategory.WORKFLOW]
        concepts = [s for s in skills if s.type == SkillCategory.CONCEPT]
        
        # 创建子目录
        (self.skills_dir / "tools").mkdir(parents=True, exist_ok=True)
        (self.skills_dir / "workflows").mkdir(parents=True, exist_ok=True)
        (self.skills_dir / "concepts").mkdir(parents=True, exist_ok=True)
        
        # 生成工具文档
        self._write_category_index("tools", tools)
        for skill in tools:
            self._write_tool_page(skill)
        
        # 生成工作流文档
        self._write_category_index("workflows", workflows)
        for skill in workflows:
            self._write_workflow_page(skill)
        
        # 生成概念文档
        self._write_category_index("concepts", concepts)
        for skill in concepts:
            self._write_concept_page(skill)
    
    def _load_skills(self) -> list[Skill]:
        """加载技能数据"""
        skills = []
        
        # 从 JSON 文件加载
        for json_file in self.input_dir.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            skills.append(Skill(**item))
                    else:
                        skills.append(Skill(**data))
            except Exception as e:
                print(f"警告：读取 {json_file} 失败：{e}")
        
        # 从 YAML 文件加载
        for yaml_file in self.input_dir.glob("*.yaml"):
            try:
                with open(yaml_file, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, list):
                        for item in data:
                            skills.append(Skill(**item))
                    else:
                        skills.append(Skill(**item))
            except Exception as e:
                print(f"警告：读取 {yaml_file} 失败：{e}")
        
        return skills
    
    def _write_category_index(self, category: str, skills: list[Skill]):
        """生成分类索引页面"""
        content = f"""# {category.title()}

本页面包含所有{category}类型的技能。

## 列表

| 名称 | 难度 | 标签 | 更新时间 |
|------|------|------|----------|
"""
        for skill in skills:
            data = skill.data
            tags = ", ".join(getattr(data, "tags", [])[:3])
            content += f"| [{data.name}]({category}/{skill.id}.md) | {data.skill_level.value} | {tags} | {skill.updated_at.strftime('%Y-%m-%d')} |\n"
        
        with open(self.skills_dir / f"{category}.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_tool_page(self, skill: Skill):
        """生成工具页面"""
        tool: Tool = skill.data  # type: ignore
        
        content = f"""# {tool.name}

{tool.description}

## 基本信息

- **类别**: {tool.category}
- **版本**: {tool.version or "N/A"}
- **难度**: {tool.skill_level.value}
- **最后更新**: {tool.last_updated.strftime('%Y-%m-%d')}

## 链接

"""
        if tool.url:
            content += f"- [官方网站]({tool.url})\n"
        if tool.repo_url:
            content += f"- [代码仓库]({tool.repo_url})\n"
        if tool.paper_url:
            content += f"- [相关论文]({tool.paper_url})\n"
        
        if tool.installation:
            content += f"\n## 安装\n\n```bash\n{tool.installation}\n```\n"
        
        if tool.usage_example:
            content += f"\n## 使用示例\n\n{tool.usage_example}\n"
        
        if tool.tags:
            content += f"\n## 标签\n\n{' '.join(['`' + t + '`' for t in tool.tags])}\n"
        
        with open(self.skills_dir / "tools" / f"{skill.id}.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_workflow_page(self, skill: Skill):
        """生成工作流页面"""
        workflow: Workflow = skill.data  # type: ignore
        
        content = f"""# {workflow.name}

{workflow.description}

## 基本信息

- **输入格式**: {workflow.input_format}
- **输出格式**: {workflow.output_format}
- **难度**: {workflow.skill_level.value}

## 使用工具

"""
        for tool in workflow.tools_used:
            content += f"- {tool}\n"
        
        content += "\n## 步骤\n\n"
        for i, step in enumerate(workflow.steps, 1):
            content += f"{i}. {step}\n"
        
        if workflow.documentation_url:
            content += f"\n## 文档\n\n[{workflow.documentation_url}]({workflow.documentation_url})\n"
        
        with open(self.skills_dir / "workflows" / f"{skill.id}.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _write_concept_page(self, skill: Skill):
        """生成概念页面"""
        concept: Concept = skill.data  # type: ignore
        
        content = f"""# {concept.name}

## 定义

{concept.definition}

"""
        if concept.explanation:
            content += f"## 解释\n\n{concept.explanation}\n\n"
        
        if concept.examples:
            content += "## 示例\n\n"
            for example in concept.examples:
                content += f"- {example}\n"
            content += "\n"
        
        if concept.related_concepts:
            content += "## 相关概念\n\n"
            for related in concept.related_concepts:
                content += f"- {related}\n"
            content += "\n"
        
        if concept.references:
            content += "## 参考资料\n\n"
            for ref in concept.references:
                content += f"- [{ref}]({ref})\n"
        
        with open(self.skills_dir / "concepts" / f"{skill.id}.md", "w", encoding="utf-8") as f:
            f.write(content)
    
    def _update_nav(self):
        """更新 mkdocs.yml 导航"""
        mkdocs_file = self.output_dir / "mkdocs.yml"
        
        if not mkdocs_file.exists():
            print(f"警告：{mkdocs_file} 不存在，跳过导航更新")
            return
        
        with open(mkdocs_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        # 更新导航
        config["nav"] = [
            {"首页": "index.md"},
            {"技能": [
                {"工具": "skills/tools.md"},
                {"工作流": "skills/workflows.md"},
                {"概念": "skills/concepts.md"}
            ]}
        ]
        
        with open(mkdocs_file, "w", encoding="utf-8") as f:
            yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
