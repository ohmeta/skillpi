"""
爬虫基类
"""

from abc import ABC, abstractmethod
from typing import Optional

import requests
from bs4 import BeautifulSoup

from ..models import Concept, Tool, Workflow


class BaseScraper(ABC):
    """爬虫基类"""

    def __init__(self, timeout: int = 30):
        """
        初始化爬虫

        Args:
            timeout: 请求超时时间（秒）
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (compatible; SkillPI Bot/1.0; +https://github.com/yourusername/skillpi)"
            }
        )

    def fetch(self, url: str) -> Optional[str]:
        """
        获取网页内容

        Args:
            url: 目标 URL

        Returns:
            网页 HTML 内容，失败时返回 None
        """
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"请求失败 {url}: {e}")
            return None

    def parse_html(self, html: str) -> BeautifulSoup:
        """
        解析 HTML

        Args:
            html: HTML 内容

        Returns:
            BeautifulSoup 对象
        """
        return BeautifulSoup(html, "html.parser")

    @abstractmethod
    def scrape_tool(self, url: str) -> Optional[Tool]:
        """
        抓取工具信息

        Args:
            url: 工具页面 URL

        Returns:
            Tool 对象，失败时返回 None
        """
        pass

    @abstractmethod
    def scrape_workflow(self, url: str) -> Optional[Workflow]:
        """
        抓取工作流信息

        Args:
            url: 工作流页面 URL

        Returns:
            Workflow 对象，失败时返回 None
        """
        pass

    @abstractmethod
    def scrape_concept(self, url: str) -> Optional[Concept]:
        """
        抓取概念信息

        Args:
            url: 概念页面 URL

        Returns:
            Concept 对象，失败时返回 None
        """
        pass
