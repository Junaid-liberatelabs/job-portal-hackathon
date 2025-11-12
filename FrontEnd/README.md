# CareerIn Frontend

Nuxt-based experience layer for the CareerIn talent platform. The landing page pairs conversational copy with interactive 3D visuals and smooth scrolling inspired by [Careerly](https://www.careerlyny.com/).

## Tech Stack
- Nuxt 4 (Vue 3, server-aware meta via `defineNuxtConfig`)
- Tailwind CSS through `@nuxtjs/tailwindcss`
- Pinia for global state (planned for authenticated experiences)
- Lenis for smooth scrolling and anchor handling
- TypeScript across components and plugins
- Google Fonts: Inter (body), Plus Jakarta Sans (display), IBM Plex Mono (code)
- Three.js-powered hero scene for interactive motion

## Frontend Patterns
- Layout-driven navigation in `app/layouts/default.vue` with responsive mobile menu
- Reusable interactive hero module at `app/components/HeroOrbit.vue` using CSS 3D transforms and brand palette
- 3D background renderer in `app/components/HeroScene.vue` driven by Three.js shaders
- Section anchors (`#features`, `#process`, etc.) wired to Lenis for soft scroll
- Tailwind utility-first styling with theme extensions defined in `tailwind.config.ts` and global tokens in `assets/css/tailwind.css`

## Commands

Install dependencies:

```bash
npm install
```

Run the development server on `http://localhost:3000`:

```bash
npm run dev
```

Build for production:

```bash
npm run build
```

Preview the production build locally:

```bash
npm run preview
```

Refer to the [Nuxt deployment docs](https://nuxt.com/docs/getting-started/deployment) for hosting guidance.
