"""
PyPI 爬虫

从 Python Package Index 抓取工具信息
"""

from datetime import datetime
from typing import Optional

import requests

from ..models import Concept, SkillLevel, Tool, Workflow
from .base import BaseScraper


class PyPIScraper(BaseScraper):
    """PyPI 爬虫"""

    def __init__(self, **kwargs):
        """初始化 PyPI 爬虫"""
        super().__init__(**kwargs)
        self.api_base = "https://pypi.org/pypi"

    def scrape_tool(self, url: str) -> Optional[Tool]:
        """从 PyPI 页面抓取工具信息"""
        # 从 URL 提取包名
        package_name = url.rstrip("/").split("/")[-1]

        # 使用 PyPI API
        api_url = f"{self.api_base}/{package_name}/json"
        try:
            response = self.session.get(api_url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException:
            return None

        info = data.get("info", {})

        # 提取项目 URL
        project_urls = info.get("project_urls", {})
        repo = project_urls.get("Source") or project_urls.get("Repository")
        paper = project_urls.get("Paper") or project_urls.get("Publication")

        # 提取标签（从 classifiers）
        tags = []
        for classifier in info.get("classifiers", []):
            if classifier.startswith("Topic ::"):
                tags.append(classifier.split("::")[-1].strip())

        return Tool(
            name=info.get("name", package_name),
            version=info.get("version"),
            description=info.get("summary", ""),
            category="tool",
            url=url,
            repo_url=repo,
            paper_url=paper,
            installation=f"pip install {package_name}",
            tags=tags,
            skill_level=SkillLevel.INTERMEDIATE,
            last_updated=datetime.now(),
        )

    def scrape_workflow(self, url: str) -> Optional[Workflow]:
        """PyPI 不直接包含工作流信息"""
        return None

    def scrape_concept(self, url: str) -> Optional[Concept]:
        """PyPI 不包含概念信息"""
        return None
