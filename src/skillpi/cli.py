"""
命令行接口
"""

import click
from rich.console import Console
from rich.table import Table

from . import __version__
from .assessor import auto_assess_skill
from .importer import SkillExporter, SkillImporter

# 移除 MkDocs 导入
# from .generators import MkDocsGenerator

console = Console()


@click.group()
@click.version_option(version=__version__)
def main():
    """SkillPI - 微生物组信息学技能目录管理工具"""
    pass


@main.command()
@click.option("--name", required=True, help="技能名称")
@click.option(
    "--type",
    "skill_type",
    type=click.Choice(["tool", "workflow", "concept"]),
    required=True,
    help="技能类型",
)
@click.option("--category", help="分类（仅 tool 类型需要）")
@click.option("--output", "-o", default="data/skills", help="输出目录")
def add(name: str, skill_type: str, category: str | None, output: str):
    """添加新技能"""
    console.print(f"[green]添加新技能:[/green] {name} (类型：{skill_type})")

    if skill_type == "tool" and not category:
        console.print("[red]错误:[/red] tool 类型必须指定 --category")
        return

    # TODO: 实现交互式技能信息录入
    console.print("[yellow]提示:[/yellow] 交互式录入功能开发中...")


@main.command()
@click.option("--input", "-i", "input_file", required=True, help="输入文件路径")
@click.option(
    "--format",
    "file_format",
    type=click.Choice(["json", "yaml", "csv"]),
    default="json",
    help="输入文件格式",
)
@click.option("--output", "-o", default="data/skills", help="输出目录")
def import_skills(input_file: str, file_format: str, output: str):
    """导入技能数据"""
    console.print("[green]导入技能数据...[/green]")
    console.print(f"输入文件：{input_file}")
    console.print(f"格式：{file_format}")

    try:
        if file_format == "json":
            skills = SkillImporter.from_json(input_file)
        elif file_format == "yaml":
            skills = SkillImporter.from_yaml(input_file)
        elif file_format == "csv":
            skills = SkillImporter.from_csv(input_file)
        else:
            console.print(f"[red]不支持的格式：{file_format}[/red]")
            return

        console.print(f"[green]✓ 成功导入 {len(skills)} 个技能[/green]")

        # 保存到输出目录
        import json
        from pathlib import Path

        output_path = Path(output)
        output_path.mkdir(parents=True, exist_ok=True)

        output_file = output_path / "imported_skills.json"
        data = [skill.model_dump(mode="json") for skill in skills]
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        console.print(f"[green]✓ 保存到：{output_file}[/green]")
    except Exception as e:
        console.print(f"[red]导入失败：{e}[/red]")


@main.command()
@click.option("--input", "-i", "input_file", required=True, help="输入技能 JSON 文件")
@click.option("--output", "-o", required=True, help="输出文件路径")
@click.option(
    "--format",
    "file_format",
    type=click.Choice(["json", "yaml", "csv", "markdown"]),
    default="json",
    help="输出文件格式",
)
def export_skills(input_file: str, output: str, file_format: str):
    """导出技能数据"""
    console.print("[green]导出技能数据...[/green]")
    console.print(f"输入文件：{input_file}")
    console.print(f"输出文件：{output}")
    console.print(f"格式：{file_format}")

    try:
        skills = SkillImporter.from_json(input_file)
        exporter = SkillExporter(skills)

        if file_format == "json":
            exporter.to_json(output)
        elif file_format == "yaml":
            exporter.to_yaml(output)
        elif file_format == "csv":
            exporter.to_csv(output)
        elif file_format == "markdown":
            exporter.to_markdown(output)

        console.print(f"[green]✓ 成功导出 {len(skills)} 个技能[/green]")
    except Exception as e:
        console.print(f"[red]导出失败：{e}[/red]")


@main.command()
@click.option("--input", "-i", "input_file", required=True, help="技能 JSON 文件")
@click.option("--auto-apply", is_flag=True, help="自动应用评估结果")
@click.option("--output", "-o", help="输出文件（仅当 --auto-apply 时需要）")
def assess(input_file: str, auto_apply: bool, output: str):
    """评估技能难度"""
    console.print("[green]评估技能难度...[/green]")

    try:
        skills = SkillImporter.from_json(input_file)

        for skill in skills:
            old_level = skill.data.skill_level
            new_level = auto_assess_skill(skill)

            status = "✓" if old_level == new_level else "→"
            color = "green" if old_level == new_level else "yellow"

            msg = f"{skill.data.name}: {old_level.value} → {new_level.value}"
            console.print(f"  [{color}]{status}[/] {msg}")

            if auto_apply:
                skill.data.skill_level = new_level

        if auto_apply and output:
            exporter = SkillExporter(skills)
            exporter.to_json(output)
            console.print(f"[green]✓ 评估结果已保存到：{output}[/green]")

    except Exception as e:
        console.print(f"[red]评估失败：{e}[/red]")


@main.command()
@click.option("--input", "-i", "input_file", required=True, help="技能 JSON 文件")
@click.option("--output", "-o", default="docs", help="文档输出目录")
def generate(input_file: str, output: str):
    """生成文档网站 (VitePress)"""
    console.print("[green]生成 VitePress 文档...[/green]")
    console.print(f"输入文件：{input_file}")
    console.print(f"输出目录：{output}")

    # TODO: 实现 VitePress 文档生成逻辑
    console.print("[yellow]提示:[/yellow] 请使用 npm run build 构建文档")


@main.command()
def list():  # noqa: A001
    """列出所有技能"""
    console.print("[green]技能列表:[/green]")

    # TODO: 从文件读取技能列表
    table = Table(title="已注册的技能")
    table.add_column("名称", style="cyan")
    table.add_column("类型", style="magenta")
    table.add_column("分类", style="green")
    table.add_column("难度", style="yellow")

    # 示例数据
    table.add_row("QIIME2", "tool", "analysis", "intermediate")
    table.add_row("DADA2", "tool", "denoising", "intermediate")
    table.add_row("16S rRNA", "concept", "sequencing", "beginner")

    console.print(table)


@main.command()
@click.option("--query", "-q", required=True, help="搜索关键词")
@click.option(
    "--type",
    "skill_type",
    type=click.Choice(["tool", "workflow", "concept"]),
    help="技能类型过滤",
)
def search(query: str, skill_type: str | None):
    """搜索技能"""
    console.print(f"[green]搜索:[/green] {query}")

    # TODO: 实现搜索功能
    console.print("[yellow]提示:[/yellow] 搜索功能开发中...")


@main.command()
def init():
    """初始化项目结构"""
    console.print("[green]初始化 SkillPI 项目结构...[/green]")

    # TODO: 实现初始化逻辑
    console.print("[yellow]提示:[/yellow] 初始化功能开发中...")


if __name__ == "__main__":
    main()
