import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'SkillPI',
  description: 'Skill Catalogue for Microbiome Informatics Study',
  lastUpdated: true,
  
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }]
  ],

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    
    // 顶部导航
    nav: [
      { text: '首页', link: '/' },
      { text: '工具', link: '/skills/tools' },
      { text: '工作流', link: '/skills/workflows' },
      { text: '概念', link: '/skills/concepts' },
      { text: '关于', link: '/about' }
    ],

    // 侧边栏
    sidebar: {
      '/skills/': [
        {
          text: '技能目录',
          items: [
            { text: '工具列表', link: '/skills/tools' },
            { text: '工作流', link: '/skills/workflows' },
            { text: '概念', link: '/skills/concepts' }
          ]
        },
        {
          text: '分析工具',
          items: [
            { text: 'MetaPhlAn 4', link: '/skills/tools/metaphlan-4' },
            { text: 'HUMAnN 3', link: '/skills/tools/humann-3' },
            { text: 'QIIME 2', link: '/skills/tools/qiime2-amplicon' },
            { text: 'DADA2', link: '/skills/tools/dada2-pipeline' },
            { text: 'mothur', link: '/skills/tools/mothur' },
            { text: 'fastp', link: '/skills/tools/fastp' },
            { text: 'MEGAHIT', link: '/skills/tools/megahit' }
          ]
        }
      ]
    },

    // 社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ohmeta/skillpi' }
    ],

    // 页脚
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024 OHMeta Team'
    },

    // 搜索
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '搜索',
                buttonAriaLabel: '搜索文档'
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换'
                }
              }
            }
          }
        }
      }
    }
  },

  // Markdown 配置
  markdown: {
    lineNumbers: true
  },

  // Vite 配置
  vite: {
    resolve: {
      alias: {
        '@': './.vitepress'
      }
    }
  }
})
