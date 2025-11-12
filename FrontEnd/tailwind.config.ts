import type { Config } from 'tailwindcss'

export default <Partial<Config>>{
  content: [
    './app/components/**/*.{vue,js,ts}',
    './app/layouts/**/*.{vue,js,ts}',
    './app/pages/**/*.{vue,js,ts}',
    './app/plugins/**/*.{js,ts}',
    './app/app.{js,ts,vue}',
    './nuxt.config.{js,ts}'
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eef7ff',
          100: '#d7ecff',
          200: '#b7ddff',
          300: '#89c6ff',
          400: '#5daaef',
          500: '#388de0',
          600: '#236fc3',
          700: '#1d55a0',
          800: '#1c467f',
          900: '#1a3a66'
        },
        ink: {
          50: '#f7f8fb',
          100: '#eef1f6',
          200: '#d9deeb',
          300: '#bbc2d5',
          400: '#919bb8',
          500: '#6f7698',
          600: '#585f7d',
          700: '#454765',
          800: '#30324c',
          900: '#1f2136'
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        display: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'ui-monospace', 'SFMono-Regular', 'monospace']
      },
      boxShadow: {
        'floating-card': '0 40px 150px -60px rgba(41, 74, 203, 0.45)'
      },
      backgroundImage: {
        'radial-spot': 'radial-gradient(circle at top, rgba(59, 130, 246, 0.22), transparent 60%)',
        'hero-gradient':
          'linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 64, 175, 0.75) 45%, rgba(14, 116, 144, 0.75))'
      }
    }
  },
  plugins: [require('@tailwindcss/typography')]
}

