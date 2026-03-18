"""
文档爬虫模块

用于从各种来源自动抓取微生物组工具的文档和使用技巧
"""

from .base import BaseScraper
from .github import GitHubScraper
from .pypi import PyPIScraper
from .biorxiv import BioRxivScraper

__all__ = ["BaseScraper", "GitHubScraper", "PyPIScraper", "BioRxivScraper"]
