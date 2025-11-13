# CareerIn Frontend

Nuxt-based experience layer for CareerIn, a youth employment and learning platform. The landing page blends immersive storytelling, Lenis-powered motion, and Three.js visuals with authenticated workspaces for dashboards, jobs, resources, and profiles.

## Tech Stack & Patterns
- Nuxt 4 (Vue 3, file-based routing, `defineNuxtConfig` runtime config)
- Tailwind CSS via `@nuxtjs/tailwindcss` with shared landing card tokens in `assets/css/tailwind.css`
- Pinia for global state management (`app/stores/auth.ts`) with persisted auth tokens
- Lenis smooth scrolling plugin (`app/plugins/lenis.client.ts`) + custom `useScrollAnimation` composable
- Three.js particle scene + video-backed hero (`app/components/hero/ThreeDHero.vue`)
- Typescript-first components, composables, and stores
- API integration through OpenAPI-driven endpoints exposed at `endpoints_info.json`

## Feature Map
- Landing experience (`app/pages/index.vue`) updated to CareerIn youth employment narrative with reusable data-driven sections
- Auth flows: `/login` and `/signup` (guest middleware) backed by Pinia store + backend tokens
- Protected workspace routes (`middleware/auth.ts`):
  - `/dashboard` – profile snapshot, recommended jobs/resources from rule-based matching
  - `/jobs` & `/jobs/[id]` – filterable listing, job detail with related learning resources
  - `/resources` – learning catalog with keyword, skill, and cost filters
  - `/profile` – profile editing and realtime skill management
- Shared API helper (`app/composables/useApi.ts`) attaches auth headers, handles 401s, and centralises fetch logic
- Navigation awareness inside `app/layouts/default.vue` swaps between marketing anchors and workspace links based on auth state

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
