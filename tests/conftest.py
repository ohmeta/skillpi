"""
SkillPI 测试配置
"""

import pytest


@pytest.fixture
def sample_tool():
    """示例工具数据"""
    from skillpi.models import Tool

    return Tool(
        name="TestTool",
        description="A test tool for microbiome analysis",
        category="analysis",
    )


@pytest.fixture
def sample_workflow():
    """示例工作流数据"""
    from skillpi.models import Workflow

    return Workflow(
        name="Test Workflow",
        description="A test workflow",
        input_format="FASTQ",
        output_format="BAM",
    )


@pytest.fixture
def sample_concept():
    """示例概念数据"""
    from skillpi.models import Concept

    return Concept(name="Test Concept", definition="A test concept definition")


@pytest.fixture
def sample_skill(sample_tool):
    """示例技能数据"""
    from skillpi.models import Skill, SkillCategory

    return Skill(id="test-skill", type=SkillCategory.TOOL, data=sample_tool)
