---
layout: home
title: SkillPI
titleTemplate: Skill Catalogue for Microbiome Informatics Study

hero:
  name: SkillPI
  text: 微生物组信息学技能目录
  tagline: Exploring the Human Microbiome - Seeking Healthy Microbiome
  image:
    src: /hero.svg
    alt: SkillPI Logo
  actions:
    - theme: brand
      text: 开始使用
      link: /skills/tools
    - theme: alt
      text: 查看工具
      link: /skills/tools
    - theme: alt
      text: GitHub
      link: https://github.com/ohmeta/skillpi

features:
  - icon: 🛠️
    title: 核心工具
    details: 7 个精选微生物组分析工具，包括 MetaPhlAn 4、HUMAnN 3、QIIME 2 等
    link: /skills/tools
  - icon: 🔄
    title: 完整工作流
    details: 从原始数据到统计分析的完整分析流程
    link: /skills/workflows
  - icon: 📖
    title: 核心概念
    details: 16S 测序、宏基因组等关键概念详解
    link: /skills/concepts
  - icon: ✅
    title: 真实验证
    details: 所有工具信息均来自官方文档和论文
    link: /about
  - icon: 🚀
    title: 快速上手
    details: 清晰的学习路径和工具选择建议
    link: /guide/quick-start
  - icon: 📊
    title: 持续更新
    details: 通过 GitHub API 自动抓取最新工具信息
    link: /guide/auto-update
---

<div class="dashboard-section">
  <h2 style="text-align: center; margin-bottom: 2rem;">📊 技能概览</h2>
  
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-number">16+</div>
      <div class="stat-label">工具与工作流</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">4</div>
      <div class="stat-label">核心概念</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">100%</div>
      <div class="stat-label">官方验证</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">22</div>
      <div class="stat-label">Git Commits</div>
    </div>
  </div>
</div>

<div class="pipeline-section">
  <h2 style="text-align: center; margin-bottom: 2rem;">🔬 分析流程</h2>
  
  <div class="pipeline-steps">
    <div class="step">
      <div class="step-icon">📥</div>
      <h4>原始数据</h4>
      <p>FASTQ 文件</p>
    </div>
    <div class="step-arrow">→</div>
    <div class="step">
      <div class="step-icon">✨</div>
      <h4>质量控制</h4>
      <p>fastp</p>
    </div>
    <div class="step-arrow">→</div>
    <div class="step">
      <div class="step-icon">🔍</div>
      <h4>物种分析</h4>
      <p>MetaPhlAn</p>
    </div>
    <div class="step-arrow">→</div>
    <div class="step">
      <div class="step-icon">📈</div>
      <h4>功能分析</h4>
      <p>HUMAnN</p>
    </div>
  </div>
</div>

<div class="research-section">
  <h2 style="text-align: center; margin-bottom: 2rem;">🧬 研究领域</h2>
  
  <div class="research-grid">
    <div class="research-card">
      <h3>🧬 肠道微生物组</h3>
      <p>理解肠道菌群在人类健康和疾病中的作用</p>
    </div>
    <div class="research-card">
      <h3>🦠 口腔微生物组</h3>
      <p>探索口腔微生物群落及其对全身健康的影响</p>
    </div>
    <div class="research-card">
      <h3>🌿 皮肤微生物组</h3>
      <p>研究皮肤微生物多样性及其保护功能</p>
    </div>
    <div class="research-card">
      <h3>💊 治疗干预</h3>
      <p>开发基于微生物组的疗法以改善健康结果</p>
    </div>
  </div>
</div>

<style>
/* 统计卡片 */
.dashboard-section {
  padding: 4rem 2rem;
  background: var(--vp-c-bg-soft);
  border-radius: 16px;
  margin: 2rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}

.stat-card {
  background: var(--vp-c-bg);
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: var(--vp-shadow-2);
  transition: transform 0.3s, box-shadow 0.3s;
}

.stat-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--vp-shadow-4);
}

.stat-number {
  font-size: 3rem;
  font-weight: bold;
  color: var(--vp-c-brand);
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 1rem;
  color: var(--vp-c-text-2);
}

/* 流程步骤 */
.pipeline-section {
  padding: 4rem 2rem;
  margin: 2rem 0;
}

.pipeline-steps {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

.step {
  flex: 1;
  min-width: 150px;
  background: var(--vp-c-bg);
  padding: 2rem 1rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: var(--vp-shadow-2);
  transition: all 0.3s;
}

.step:hover {
  transform: scale(1.05);
  box-shadow: var(--vp-shadow-4);
}

.step-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.step h4 {
  margin: 0.5rem 0;
  color: var(--vp-c-text-1);
}

.step p {
  margin: 0;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}

.step-arrow {
  font-size: 1.5rem;
  color: var(--vp-c-brand);
  font-weight: bold;
}

/* 研究领域 */
.research-section {
  padding: 4rem 2rem;
  background: linear-gradient(135deg, var(--vp-c-bg-soft) 0%, var(--vp-c-bg) 100%);
  border-radius: 16px;
  margin: 2rem 0;
}

.research-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.research-card {
  background: var(--vp-c-bg);
  padding: 2rem;
  border-radius: 12px;
  border-left: 4px solid var(--vp-c-brand);
  box-shadow: var(--vp-shadow-2);
  transition: all 0.3s;
}

.research-card:hover {
  box-shadow: var(--vp-shadow-4);
  border-left-width: 6px;
}

.research-card h3 {
  margin: 0 0 1rem 0;
  color: var(--vp-c-text-1);
}

.research-card p {
  margin: 0;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .pipeline-steps {
    flex-direction: column;
  }
  
  .step-arrow {
    transform: rotate(90deg);
  }
  
  .research-grid {
    grid-template-columns: 1fr;
  }
}
</style>
