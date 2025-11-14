// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt'
  ],
  
  css: [],
  
  tailwindcss: {
    config: {
      theme: {
        extend: {
          colors: {
            primary: '#1a2332',
            secondary: '#ff6b6b',
            accent: '#4ecdc4',
            neutral: '#f8f9fa',
            'ink': {
              50: '#f9fafb',
              100: '#f3f4f6',
              200: '#e5e7eb',
              300: '#d1d5db',
              400: '#9ca3af',
              500: '#6b7280',
              600: '#4b5563',
              700: '#374151',
              800: '#1f2937',
              900: '#111827',
            },
            'brand': {
              50: '#f0fdfa',
              100: '#ccfbf1',
              200: '#99f6e4',
              300: '#5eead4',
              400: '#2dd4bf',
              500: '#4ecdc4',
              600: '#3cb8ae',
              700: '#0f766e',
              800: '#115e59',
              900: '#134e4a',
            }
          },
          fontFamily: {
            display: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
            body: ['Inter', 'sans-serif'],
            mono: ['IBM Plex Mono', 'monospace']
          }
        }
      }
    }
  },
  
  runtimeConfig: {
    public: {
      // API base URL - defaults to localhost:8000 for development
      // Can be overridden with NUXT_PUBLIC_API_BASE environment variable
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000'
    }
  },
  
  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
        class: 'scroll-smooth'
      },
      title: 'CareerIn - AI-Powered Youth Employment Platform',
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous' },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap'
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200'
        },
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ],
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'theme-color', content: '#1a2332' },
        {
          name: 'description',
          content: 'CareerIn is an AI-powered talent intelligence platform aligning employers and candidates with precision AI and human insight.'
        },
        { name: 'keywords', content: 'career, jobs, skills, learning, employment, AI, talent, youth employment' }
      ]
    }
  },
  
  build: {
    transpile: ['echarts']
  },
  
  vite: {
    optimizeDeps: {
      include: ['animejs', 'echarts', 'typed.js']
    }
  }
})