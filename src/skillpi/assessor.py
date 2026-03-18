"""
技能难度自动评估器

根据工具/概念的复杂度、学习曲线等因素自动评估技能难度
"""

from .logger import get_logger
from .models import Concept, SkillCategory, SkillLevel, Tool, Workflow

logger = get_logger("skillpi.assessor")


class DifficultyAssessor:
    """技能难度评估器"""

    # 关键词权重
    DIFFICULT_KEYWORDS = {
        # 高级关键词
        "advanced": 3,
        "expert": 3,
        "complex": 3,
        "optimization": 3,
        "parallel": 3,
        "distributed": 3,
        # 中级关键词
        "intermediate": 2,
        "workflow": 2,
        "pipeline": 2,
        "integration": 2,
        "customization": 2,
        "statistics": 2,
        "visualization": 2,
        # 初级关键词
        "beginner": 1,
        "basic": 1,
        "introduction": 1,
        "tutorial": 1,
        "simple": 1,
        "quickstart": 1,
    }

    # 工具类型基础难度
    CATEGORY_BASE_LEVEL = {
        "analysis": SkillLevel.INTERMEDIATE,
        "denoising": SkillLevel.INTERMEDIATE,
        "assembly": SkillLevel.ADVANCED,
        "binning": SkillLevel.ADVANCED,
        "annotation": SkillLevel.INTERMEDIATE,
        "visualization": SkillLevel.BEGINNER,
        "statistics": SkillLevel.INTERMEDIATE,
        "profiling": SkillLevel.INTERMEDIATE,
        "qc": SkillLevel.BEGINNER,
        "utilities": SkillLevel.BEGINNER,
    }

    # 编程语言难度
    LANGUAGE_DIFFICULTY = {
        "python": 1,
        "r": 2,
        "command line": 1,
        "gui": 0,
        "web": 0,
        "rust": 2,
        "c++": 2,
    }

    @classmethod
    def assess_tool(cls, tool: Tool) -> SkillLevel:
        """评估工具难度"""
        logger.debug(f"评估工具难度：{tool.name}")

        score = 0

        # 1. 基于类别的基础难度
        category = tool.category.lower()
        base_level = cls.CATEGORY_BASE_LEVEL.get(category, SkillLevel.INTERMEDIATE)
        score += cls._level_to_score(base_level)

        # 2. 分析描述和文档中的关键词
        desc = tool.description
        install = tool.installation or ""
        usage = tool.usage_example or ""
        text_to_analyze = f"{desc} {install} {usage}".lower()

        for keyword, weight in cls.DIFFICULT_KEYWORDS.items():
            if keyword in text_to_analyze:
                score += weight

        # 3. 分析安装复杂度
        if tool.installation:
            install_text = tool.installation.lower()
            if "conda" in install_text or "pip" in install_text:
                score -= 1  # 包管理器安装较简单
            elif "compile" in install_text or "build" in install_text:
                score += 2  # 需要编译较复杂
            elif "docker" in install_text:
                score += 1  # Docker 需要额外知识

        # 4. 分析标签
        for tag in tool.tags:
            tag_lower = tag.lower()
            if tag_lower in cls.LANGUAGE_DIFFICULTY:
                score += cls.LANGUAGE_DIFFICULTY[tag_lower]

        # 5. 基于标签数量（标签越多通常越复杂）
        if len(tool.tags) > 10:
            score += 1

        return cls._score_to_level(score)

    @classmethod
    def assess_workflow(cls, workflow: Workflow) -> SkillLevel:
        """评估工作流难度"""
        logger.debug(f"评估工作流难度：{workflow.name}")

        score = 0

        # 1. 基于步骤数量
        num_steps = len(workflow.steps)
        if num_steps > 10:
            score += 3
        elif num_steps > 5:
            score += 2
        elif num_steps > 3:
            score += 1

        # 2. 基于使用工具数量
        num_tools = len(workflow.tools_used)
        if num_tools > 5:
            score += 2
        elif num_tools > 3:
            score += 1

        # 3. 分析描述
        text_to_analyze = f"{workflow.description}".lower()
        for keyword, weight in cls.DIFFICULT_KEYWORDS.items():
            if keyword in text_to_analyze:
                score += weight

        return cls._score_to_level(score)

    @classmethod
    def assess_concept(cls, concept: Concept) -> SkillLevel:
        """评估概念难度"""
        logger.debug(f"评估概念难度：{concept.name}")

        score = 0

        # 1. 基于定义长度（通常越长越复杂）
        definition_length = len(concept.definition)
        if definition_length > 500:
            score += 2
        elif definition_length > 200:
            score += 1

        # 2. 基于相关概念数量
        if len(concept.related_concepts) > 5:
            score += 1

        # 3. 分析关键词
        text_to_analyze = f"{concept.definition} {concept.explanation or ''}".lower()
        for keyword, weight in cls.DIFFICULT_KEYWORDS.items():
            if keyword in text_to_analyze:
                score += weight

        return cls._score_to_level(score)

    @staticmethod
    def _level_to_score(level: SkillLevel) -> int:
        """将难度级别转换为分数"""
        mapping = {
            SkillLevel.BEGINNER: 0,
            SkillLevel.INTERMEDIATE: 2,
            SkillLevel.ADVANCED: 4,
            SkillLevel.EXPERT: 6,
        }
        return mapping.get(level, 2)

    @staticmethod
    def _score_to_level(score: int) -> SkillLevel:
        """将分数转换为难度级别"""
        if score <= 1:
            return SkillLevel.BEGINNER
        elif score <= 3:
            return SkillLevel.INTERMEDIATE
        elif score <= 5:
            return SkillLevel.ADVANCED
        else:
            return SkillLevel.EXPERT


def auto_assess_skill(skill) -> SkillLevel:
    """自动评估技能难度（通用接口）"""

    if skill.type == SkillCategory.TOOL:
        return DifficultyAssessor.assess_tool(skill.data)
    elif skill.type == SkillCategory.WORKFLOW:
        return DifficultyAssessor.assess_workflow(skill.data)
    elif skill.type == SkillCategory.CONCEPT:
        return DifficultyAssessor.assess_concept(skill.data)

    return SkillLevel.INTERMEDIATE
