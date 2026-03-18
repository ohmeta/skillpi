"""
GitHub 仓库爬虫

从 GitHub 抓取工具信息
"""

import re
from typing import Optional
from datetime import datetime

from .base import BaseScraper
from ..models import Tool, Workflow, Concept, SkillLevel
from ..logger import get_logger

logger = get_logger("skillpi.scraper.github")


class GitHubScraper(BaseScraper):
    """GitHub 爬虫"""
    
    API_BASE = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None, **kwargs):
        """
        初始化 GitHub 爬虫
        
        Args:
            token: GitHub API token（可选，用于提高速率限制）
        """
        super().__init__(**kwargs)
        if token:
            self.session.headers.update({"Authorization": f"token {token}"})
        logger.info("GitHubScraper 初始化完成")
    
    def _parse_repo_url(self, url: str) -> Optional[tuple[str, str]]:
        """解析 GitHub 仓库 URL"""
        match = re.search(r"github\.com/([^/]+)/([^/]+)", url)
        if match:
            return match.group(1), match.group(2)
        logger.warning(f"无法解析 GitHub URL: {url}")
        return None
    
    def scrape_tool(self, url: str) -> Optional[Tool]:
        """从 GitHub 仓库抓取工具信息"""
        logger.info(f"抓取 GitHub 仓库：{url}")
        
        # 尝试使用 API
        repo_info = self._parse_repo_url(url)
        if not repo_info:
            return None
        
        owner, repo = repo_info
        api_url = f"{self.API_BASE}/repos/{owner}/{repo}"
        
        try:
            response = self.session.get(api_url, timeout=self.timeout)
            if response.status_code == 403:
                logger.warning("GitHub API 速率限制，使用网页抓取")
                return self._scrape_from_html(url)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            logger.error(f"API 请求失败：{e}")
            return self._scrape_from_html(url)
        
        return self._parse_api_response(data, url)
    
    def _parse_api_response(self, data: dict, url: str) -> Tool:
        """解析 API 响应"""
        logger.debug(f"解析 API 响应：{data.get('full_name')}")
        
        # 获取 README
        readme_url = f"{self.API_BASE}/repos/{data['full_name']}/readme"
        readme_content = None
        try:
            resp = self.session.get(readme_url, timeout=10)
            if resp.status_code == 200:
                import base64
                readme_data = resp.json()
                readme_content = base64.b64decode(readme_data['content']).decode('utf-8')[:1000]
        except Exception as e:
            logger.debug(f"无法获取 README: {e}")
        
        # 获取 topics
        topics = []
        try:
            topics_url = f"{self.API_BASE}/repos/{data['full_name']}/topics"
            resp = self.session.get(topics_url, timeout=10, headers={"Accept": "application/vnd.github.mercy-preview+json"})
            if resp.status_code == 200:
                topics = resp.json().get('names', [])[:10]
        except Exception as e:
            logger.debug(f"无法获取 topics: {e}")
        
        return Tool(
            name=data['name'],
            description=data.get('description', '') or '',
            category="tool",
            url=data.get('html_url', url),
            repo_url=data.get('html_url'),
            homepage=data.get('homepage'),
            installation=self._generate_install_command(data),
            usage_example=readme_content,
            tags=topics,
            skill_level=SkillLevel.INTERMEDIATE,
            last_updated=datetime.now()
        )
    
    def _generate_install_command(self, data: dict) -> Optional[str]:
        """生成安装命令"""
        name = data['name']
        # 检查是否有 Python 标识
        language = data.get('language', '')
        
        if language == 'Python':
            return f"pip install {name}"
        elif language == 'R':
            return f"# 在 R 中安装\n# install.packages('{name}')"
        elif language == 'Rust':
            return f"cargo install {name}"
        elif language == 'Go':
            return f"go get github.com/{data['full_name']}"
        
        return None
    
    def _scrape_from_html(self, url: str) -> Optional[Tool]:
        """从网页抓取（备用方案）"""
        html = self.fetch(url)
        if not html:
            return None
        
        soup = self.parse_html(html)
        repo_info = self._parse_repo_url(url)
        if not repo_info:
            return None
        
        description_elem = soup.find("meta", attrs={"name": "description"})
        description = description_elem["content"].strip() if description_elem else ""
        
        tags = []
        topic_elems = soup.select(".topic-tag .Link--primary")
        for topic in topic_elems[:10]:
            tags.append(topic.text.strip())
        
        return Tool(
            name=repo_info[1],
            description=description,
            category="tool",
            url=url,
            repo_url=url,
            tags=tags,
            skill_level=SkillLevel.INTERMEDIATE,
            last_updated=datetime.now()
        )
    
    def scrape_workflow(self, url: str) -> Optional[Workflow]:
        """抓取工作流信息（从 GitHub Actions）"""
        logger.info(f"抓取 GitHub Actions 工作流：{url}")
        # TODO: 实现工作流抓取
        return None
    
    def scrape_concept(self, url: str) -> Optional[Concept]:
        """GitHub 不直接包含概念信息"""
        return None
