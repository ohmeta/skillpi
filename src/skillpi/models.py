"""
数据模型定义

定义微生物组信息学技能的数据结构
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class SkillLevel(str, Enum):
    """技能难度级别"""

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class SkillCategory(str, Enum):
    """技能分类"""

    TOOL = "tool"
    WORKFLOW = "workflow"
    CONCEPT = "concept"
    DATASET = "dataset"
    METHOD = "method"


class Tool(BaseModel):
    """微生物组分析工具模型"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "QIIME2",
                "description": "强大的微生物组分析平台",
                "category": "analysis",
                "tags": ["16S", "metagenomics", "python"],
                "skill_level": "intermediate",
            }
        }
    )

    name: str = Field(..., description="工具名称")
    version: Optional[str] = Field(None, description="版本号")
    description: str = Field(..., description="工具描述")
    category: str = Field(..., description="工具类别，如 QC, assembly, binning 等")
    url: Optional[HttpUrl] = Field(None, description="官方网站 URL")
    repo_url: Optional[HttpUrl] = Field(None, description="代码仓库 URL")
    homepage: Optional[str] = Field(None, description="项目主页")
    paper_url: Optional[HttpUrl] = Field(None, description="相关论文 URL")
    installation: Optional[str] = Field(None, description="安装说明")
    usage_example: Optional[str] = Field(None, description="使用示例")
    tags: list[str] = Field(default_factory=list, description="标签列表")
    skill_level: SkillLevel = Field(
        default=SkillLevel.INTERMEDIATE, description="技能难度"
    )
    last_updated: datetime = Field(
        default_factory=datetime.now, description="最后更新时间"
    )


class Workflow(BaseModel):
    """分析工作流程模型"""

    name: str = Field(..., description="工作流名称")
    description: str = Field(..., description="工作流描述")
    steps: list[str] = Field(default_factory=list, description="分析步骤")
    tools_used: list[str] = Field(default_factory=list, description="使用的工具")
    input_format: str = Field(..., description="输入数据格式")
    output_format: str = Field(..., description="输出数据格式")
    documentation_url: Optional[HttpUrl] = Field(None, description="文档 URL")
    tags: list[str] = Field(default_factory=list, description="标签列表")
    skill_level: SkillLevel = Field(
        default=SkillLevel.INTERMEDIATE, description="技能难度"
    )
    last_updated: datetime = Field(
        default_factory=datetime.now, description="最后更新时间"
    )


class Concept(BaseModel):
    """概念/术语模型"""

    name: str = Field(..., description="概念名称")
    definition: str = Field(..., description="定义")
    explanation: Optional[str] = Field(None, description="详细解释")
    related_concepts: list[str] = Field(default_factory=list, description="相关概念")
    examples: list[str] = Field(default_factory=list, description="示例")
    references: list[HttpUrl] = Field(default_factory=list, description="参考资料")
    tags: list[str] = Field(default_factory=list, description="标签列表")
    skill_level: SkillLevel = Field(default=SkillLevel.BEGINNER, description="技能难度")
    last_updated: datetime = Field(
        default_factory=datetime.now, description="最后更新时间"
    )


class Skill(BaseModel):
    """通用技能模型（联合类型）"""

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "qiime2-basics",
                "type": "tool",
                "data": {
                    "name": "QIIME2",
                    "description": "强大的微生物组分析平台",
                    "category": "analysis",
                },
            }
        }
    )

    id: str = Field(..., description="技能唯一标识")
    type: SkillCategory = Field(..., description="技能类型")
    data: Tool | Workflow | Concept = Field(..., description="技能数据")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")


class SkillCollection(BaseModel):
    """技能集合模型"""

    name: str = Field(..., description="集合名称")
    description: str = Field(..., description="集合描述")
    skills: list[Skill] = Field(default_factory=list, description="技能列表")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    updated_at: datetime = Field(default_factory=datetime.now, description="更新时间")
