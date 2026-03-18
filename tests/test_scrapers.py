"""
测试爬虫模块
"""

import pytest
from unittest.mock import Mock, patch

from skillpi.scrapers import GitHubScraper, PyPIScraper
from skillpi.models import Tool


class TestGitHubScraper:
    """测试 GitHub 爬虫"""
    
    def test_init(self):
        """测试初始化"""
        scraper = GitHubScraper()
        assert scraper.timeout == 30
        assert "User-Agent" in scraper.session.headers
    
    def test_init_with_token(self):
        """测试带 token 初始化"""
        scraper = GitHubScraper(token="test_token")
        assert "Authorization" in scraper.session.headers
    
    @patch.object(GitHubScraper, 'fetch')
    def test_scrape_tool(self, mock_fetch):
        """测试抓取工具"""
        # 模拟 HTML 响应
        mock_html = """
        <html>
        <head>
            <meta name="description" content="Test repository description">
        </head>
        <body>
            <a href="/test/repo">test/repo</a>
        </body>
        </html>
        """
        mock_fetch.return_value = mock_html
        
        scraper = GitHubScraper()
        tool = scraper.scrape_tool("https://github.com/test/repo")
        
        assert tool is not None
        assert tool.description == "Test repository description"


class TestPyPIScraper:
    """测试 PyPI 爬虫"""
    
    def test_init(self):
        """测试初始化"""
        scraper = PyPIScraper()
        assert scraper.api_base == "https://pypi.org/pypi"
    
    @patch('skillpi.scrapers.pypi.requests.Session.get')
    def test_scrape_tool(self, mock_get):
        """测试抓取工具"""
        # 模拟 API 响应
        mock_response = Mock()
        mock_response.json.return_value = {
            "info": {
                "name": "test-package",
                "version": "1.0.0",
                "summary": "Test package summary",
                "classifiers": [
                    "Topic :: Scientific/Engineering :: Bio-Informatics"
                ],
                "project_urls": {
                    "Homepage": "https://example.com"
                }
            }
        }
        mock_get.return_value = mock_response
        
        scraper = PyPIScraper()
        tool = scraper.scrape_tool("https://pypi.org/project/test-package/")
        
        assert tool is not None
        assert tool.name == "test-package"
        assert tool.version == "1.0.0"
        assert tool.description == "Test package summary"
