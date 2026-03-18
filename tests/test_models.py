"""
测试数据模型
"""

import pytest
from datetime import datetime

from skillpi.models import (
    Tool, Workflow, Concept, Skill, SkillCategory, SkillLevel,
    SkillCollection
)


class TestTool:
    """测试 Tool 模型"""
    
    def test_create_tool(self):
        """测试创建工具"""
        tool = Tool(
            name="TestTool",
            description="A test tool",
            category="analysis"
        )
        assert tool.name == "TestTool"
        assert tool.description == "A test tool"
        assert tool.category == "analysis"
        assert tool.skill_level == SkillLevel.INTERMEDIATE
    
    def test_tool_with_all_fields(self):
        """测试完整字段的工具"""
        tool = Tool(
            name="CompleteTool",
            version="1.0.0",
            description="Complete tool description",
            category="denoising",
            url="https://example.com",
            repo_url="https://github.com/user/repo",
            paper_url="https://doi.org/10.1000/test",
            installation="pip install test",
            usage_example="test --help",
            tags=["tag1", "tag2"],
            skill_level=SkillLevel.ADVANCED
        )
        assert tool.version == "1.0.0"
        assert len(tool.tags) == 2
        assert tool.skill_level == SkillLevel.ADVANCED
    
    def test_tool_validation(self):
        """测试工具验证"""
        # 缺少必填字段
        with pytest.raises(Exception):
            Tool(description="Missing name")


class TestWorkflow:
    """测试 Workflow 模型"""
    
    def test_create_workflow(self):
        """测试创建工作流"""
        workflow = Workflow(
            name="Test Workflow",
            description="A test workflow",
            input_format="FASTQ",
            output_format="BAM"
        )
        assert workflow.name == "Test Workflow"
        assert workflow.input_format == "FASTQ"
        assert workflow.output_format == "BAM"
    
    def test_workflow_with_steps(self):
        """测试带步骤的工作流"""
        workflow = Workflow(
            name="Assembly Workflow",
            description="Genome assembly",
            steps=["QC", "Assembly", "Annotation"],
            tools_used=["FastQC", "SPAdes"],
            input_format="FASTQ",
            output_format="FASTA"
        )
        assert len(workflow.steps) == 3
        assert len(workflow.tools_used) == 2


class TestConcept:
    """测试 Concept 模型"""
    
    def test_create_concept(self):
        """测试创建概念"""
        concept = Concept(
            name="Test Concept",
            definition="A test concept"
        )
        assert concept.name == "Test Concept"
        assert concept.definition == "A test concept"
        assert concept.skill_level == SkillLevel.BEGINNER
    
    def test_concept_with_examples(self):
        """测试带示例的概念"""
        concept = Concept(
            name="Alpha Diversity",
            definition="Within-sample diversity",
            examples=["Shannon index", "Simpson index"],
            related_concepts=["Beta Diversity"]
        )
        assert len(concept.examples) == 2
        assert "Beta Diversity" in concept.related_concepts


class TestSkill:
    """测试 Skill 模型"""
    
    def test_create_skill_tool(self):
        """测试创建工具技能"""
        tool = Tool(
            name="TestTool",
            description="Test",
            category="analysis"
        )
        skill = Skill(
            id="test-tool",
            type=SkillCategory.TOOL,
            data=tool
        )
        assert skill.id == "test-tool"
        assert skill.type == SkillCategory.TOOL
        assert isinstance(skill.data, Tool)
    
    def test_create_skill_concept(self):
        """测试创建概念技能"""
        concept = Concept(
            name="Test Concept",
            definition="Test"
        )
        skill = Skill(
            id="test-concept",
            type=SkillCategory.CONCEPT,
            data=concept
        )
        assert skill.type == SkillCategory.CONCEPT
        assert isinstance(skill.data, Concept)
    
    def test_skill_serialization(self):
        """测试技能序列化"""
        tool = Tool(
            name="TestTool",
            description="Test",
            category="analysis"
        )
        skill = Skill(
            id="test-tool",
            type=SkillCategory.TOOL,
            data=tool
        )
        
        # 序列化为 JSON
        data = skill.model_dump(mode="json")
        assert data["id"] == "test-tool"
        assert data["type"] == "tool"
        
        # 从 JSON 反序列化
        skill2 = Skill(**data)
        assert skill2.id == skill.id


class TestSkillCollection:
    """测试 SkillCollection 模型"""
    
    def test_create_collection(self):
        """测试创建技能集合"""
        collection = SkillCollection(
            name="Test Collection",
            description="A test collection"
        )
        assert collection.name == "Test Collection"
        assert len(collection.skills) == 0
    
    def test_collection_with_skills(self):
        """测试带技能的技能集合"""
        tool = Tool(
            name="TestTool",
            description="Test",
            category="analysis"
        )
        skill = Skill(
            id="test-tool",
            type=SkillCategory.TOOL,
            data=tool
        )
        collection = SkillCollection(
            name="Tools",
            description="Tool collection",
            skills=[skill]
        )
        assert len(collection.skills) == 1
