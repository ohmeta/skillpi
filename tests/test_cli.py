"""
测试 CLI
"""

import pytest
from click.testing import CliRunner

from skillpi.cli import main


class TestCLI:
    """测试命令行接口"""
    
    def test_version(self):
        """测试版本显示"""
        runner = CliRunner()
        result = runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.output.lower()
    
    def test_help(self):
        """测试帮助信息"""
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "SkillPI" in result.output
    
    def test_list(self):
        """测试列出技能"""
        runner = CliRunner()
        result = runner.invoke(main, ["list"])
        assert result.exit_code == 0
    
    def test_add_tool(self):
        """测试添加工具"""
        runner = CliRunner()
        result = runner.invoke(
            main,
            ["add", "--name", "TestTool", "--type", "tool", "--category", "analysis"]
        )
        assert result.exit_code == 0
    
    def test_add_without_category(self):
        """测试添加工具时缺少分类"""
        runner = CliRunner()
        result = runner.invoke(
            main,
            ["add", "--name", "TestTool", "--type", "tool"]
        )
        assert result.exit_code == 0
        assert "错误" in result.output or "必须指定" in result.output
    
    def test_search(self):
        """测试搜索"""
        runner = CliRunner()
        result = runner.invoke(
            main,
            ["search", "--query", "test"]
        )
        assert result.exit_code == 0
