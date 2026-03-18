#!/usr/bin/env python3
"""
真实世界微生物组工具抓取测试
"""

from skillpi.scrapers import GitHubScraper, PyPIScraper
from skillpi.models import Skill, SkillCategory
from skillpi.importer import SkillExporter
import json

print('='*70)
print('真实世界微生物组工具抓取测试')
print('='*70)

tools_to_test = [
    # GitHub 仓库 - 真实的微生物组工具
    ('github', 'https://github.com/benjjneb/dada2', 'DADA2'),
    ('github', 'https://github.com/biobakery/metaphlan', 'MetaPhlAn'),
    ('github', 'https://github.com/biocore/emperor', 'Emperor'),
    ('github', 'https://github.com/microbiome/microbiome', 'microbiome R package'),
    # PyPI 包 - 真实的生物信息学工具
    ('pypi', 'scikit-bio', 'scikit-bio'),
    ('pypi', 'biom-format', 'BIOM format'),
    ('pypi', 'fastp', 'fastp'),
]

results = []

for platform, identifier, name in tools_to_test:
    print(f'\n测试 {name} ({platform})...')
    
    try:
        if platform == 'github':
            scraper = GitHubScraper()
            tool = scraper.scrape_tool(identifier)
        else:
            scraper = PyPIScraper()
            url = f'https://pypi.org/project/{identifier}/'
            tool = scraper.scrape_tool(url)
        
        if tool:
            print(f'  ✓ 成功')
            print(f'     名称：{tool.name}')
            print(f'     描述：{tool.description[:60]}...')
            if tool.installation:
                print(f'     安装：{tool.installation}')
            
            # 保存为 Skill
            skill = Skill(
                id=tool.name.lower().replace(' ', '-'),
                type=SkillCategory.TOOL,
                data=tool
            )
            results.append(skill.model_dump(mode='json'))
        else:
            print(f'  ✗ 返回为空')
    except Exception as e:
        print(f'  ✗ 错误：{e}')

# 保存结果
if results:
    print(f'\n{"="*70}')
    print(f'成功抓取 {len(results)} 个工具')
    
    with open('data/skills/real_tools.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f'已保存到 data/skills/real_tools.json')
    
    # 生成文档
    print(f'\n生成文档网站...')
    from skillpi.generators import MkDocsGenerator
    generator = MkDocsGenerator('data/skills', '.')
    generator.generate()
    
    print(f'✓ 文档生成完成')
    print(f'  查看：npm run dev')
    print('='*70)
else:
    print('\n没有成功抓取到任何工具')
