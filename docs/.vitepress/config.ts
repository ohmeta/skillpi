import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'SkillPI',
  description: 'Skill Catalogue for Microbiome Informatics Study',
  base: '/skillpi/',  // GitHub Pages 需要配置 base path
  lastUpdated: true,

  head: [
    ['link', { rel: 'icon', href: '/skillpi/favicon.ico' }]
  ],

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config

    // 顶部导航
    nav: [
      { text: '首页', link: '/' },
      { text: '工具', link: '/skills/tools' },
      { text: '文献', link: '/skills/publications' },
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
            { text: '工具列表 (51个)', link: '/skills/tools' },
            { text: '最新文献', link: '/skills/publications' },
            { text: '工作流', link: '/skills/workflows' },
            { text: '概念', link: '/skills/concepts' }
          ]
        },
        {
          text: '核心概念',
          collapsed: false,
          items: [
            { text: '16S rRNA 测序', link: '/skills/concepts/16s-rrna-sequencing' },
            { text: '宏基因组测序', link: '/skills/concepts/metagenomics-sequencing' },
            { text: 'Alpha 多样性', link: '/skills/concepts/alpha-diversity' },
            { text: '宏基因组组装基因组 (MAG)', link: '/skills/concepts/metagenome-assembled-genomes' },
            { text: 'GTDB 分类学框架', link: '/skills/concepts/gtdb-taxonomy' },
            { text: '组成性数据分析 (CoDA)', link: '/skills/concepts/compositional-data-analysis' },
            { text: '批次效应', link: '/skills/concepts/batch-effects' },
          ]
        },
        {
          text: '质量控制',
          collapsed: false,
          items: [
            { text: 'fastp', link: '/skills/tools/fastp' },
            { text: 'NanoPlot', link: '/skills/tools/nanoplot' },
            { text: 'Filtlong', link: '/skills/tools/filtlong' },
          ]
        },
        {
          text: '分类鉴定',
          collapsed: false,
          items: [
            { text: 'MetaPhlAn 4', link: '/skills/tools/metaphlan-4' },
            { text: 'Kraken 2', link: '/skills/tools/kraken2' },
            { text: 'Bracken', link: '/skills/tools/bracken' },
            { text: 'Centrifuge', link: '/skills/tools/centrifuge' },
            { text: 'Kaiju', link: '/skills/tools/kaiju' },
            { text: 'GTDB-Tk', link: '/skills/tools/gtdb_tk' },
          ]
        },
        {
          text: '组装',
          collapsed: false,
          items: [
            { text: 'MEGAHIT', link: '/skills/tools/megahit' },
            { text: 'metaSPAdes', link: '/skills/tools/metaspades' },
            { text: 'Flye', link: '/skills/tools/flye' },
            { text: 'Canu', link: '/skills/tools/canu' },
            { text: 'Unicycler', link: '/skills/tools/unicycler' },
          ]
        },
        {
          text: '分箱',
          collapsed: false,
          items: [
            { text: 'MetaBAT 2', link: '/skills/tools/metabat2' },
            { text: 'MaxBin 2', link: '/skills/tools/maxbin2' },
            { text: 'CONCOCT', link: '/skills/tools/concoct' },
            { text: 'DAS Tool', link: '/skills/tools/das_tool' },
            { text: 'CheckM2', link: '/skills/tools/checkm2' },
          ]
        },
        {
          text: '菌株分析',
          collapsed: false,
          items: [
            { text: 'StrainPhlAn', link: '/skills/tools/strainphlan' },
            { text: 'inStrain', link: '/skills/tools/instrain' },
          ]
        },
        {
          text: '功能注释',
          collapsed: false,
          items: [
            { text: 'HUMAnN 3', link: '/skills/tools/humann-3' },
            { text: 'eggNOG-mapper', link: '/skills/tools/eggnog_mapper' },
            { text: 'Prokka', link: '/skills/tools/prokka' },
            { text: 'Bakta', link: '/skills/tools/bakta' },
            { text: 'antiSMASH', link: '/skills/tools/antismash' },
            { text: 'DRAM', link: '/skills/tools/dram' },
          ]
        },
        {
          text: '序列比对',
          collapsed: false,
          items: [
            { text: 'Bowtie 2', link: '/skills/tools/bowtie2' },
            { text: 'minimap2', link: '/skills/tools/minimap2' },
            { text: 'BWA-MEM2', link: '/skills/tools/bwa_mem2' },
          ]
        },
        {
          text: '变异检测 & 定量',
          collapsed: false,
          items: [
            { text: 'Clair3', link: '/skills/tools/clair3' },
            { text: 'Salmon', link: '/skills/tools/salmon' },
            { text: 'featureCounts', link: '/skills/tools/featurecounts' },
          ]
        },
        {
          text: '扩增子 & 去噪',
          collapsed: false,
          items: [
            { text: 'QIIME 2', link: '/skills/tools/qiime2-amplicon' },
            { text: 'DADA2', link: '/skills/tools/dada2-pipeline' },
            { text: 'mothur', link: '/skills/tools/mothur' },
          ]
        },
        {
          text: '病毒分析',
          collapsed: false,
          items: [
            { text: 'VirSorter 2', link: '/skills/tools/virsorter2' },
            { text: 'Pharokka', link: '/skills/tools/pharokka' },
          ]
        },
        {
          text: '下游分析',
          collapsed: false,
          items: [
            { text: 'phyloseq', link: '/skills/tools/phyloseq' },
            { text: 'DESeq2', link: '/skills/tools/deseq2' },
            { text: 'LEfSe', link: '/skills/tools/lefse' },
            { text: 'ANCOM-BC', link: '/skills/tools/ancom_bc' },
            { text: 'microeco', link: '/skills/tools/microeco' },
          ]
        },
        {
          text: '可视化',
          collapsed: false,
          items: [
            { text: "anvi'o", link: '/skills/tools/anvio' },
            { text: 'Pavian', link: '/skills/tools/pavian' },
            { text: 'Krona', link: '/skills/tools/krona' },
          ]
        },
        {
          text: '流程框架',
          collapsed: false,
          items: [
            { text: 'Nextflow', link: '/skills/tools/nextflow' },
            { text: 'nf-core/mag', link: '/skills/tools/nf_core_mag' },
          ]
        },
      ]
    },

    // 社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ohmeta/skillpi' }
    ],

    // 页脚
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-2026 OHMeta Team'
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
