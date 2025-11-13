<template>
  <div class="flex min-h-screen flex-col bg-ink-50 text-ink-900">
    <!-- Use PublicNavigation for landing page, Navigation for authenticated pages -->
    <PublicNavigation v-if="!isAuthenticated" />
    <Navigation v-else />

    <main class="flex-1">
      <slot />
    </main>

    <footer v-if="!isAuthenticated" class="border-t border-white/10 bg-white/75 py-12 backdrop-blur-xl">
      <div class="mx-auto flex max-w-7xl flex-col gap-10 px-6 text-sm text-ink-500 lg:flex-row lg:items-start lg:justify-between lg:px-10">
        <div class="flex items-start gap-4">
          <div class="flex h-11 w-11 items-center justify-center rounded-2xl bg-hero-gradient text-white shadow-lg shadow-brand-500/30 ring-2 ring-white/40">
            <span class="font-semibold">CI</span>
          </div>
          <div class="space-y-2">
            <p class="font-display text-base font-semibold text-ink-800">CareerIn</p>
            <p class="max-w-xs text-sm text-ink-500">
              We help students and emerging talent translate their skills into sustainable careers with transparent matches and guided learning paths.
            </p>
            <p class="text-xs text-ink-400">© {{ currentYear }} CareerIn. All rights reserved.</p>
          </div>
        </div>

        <div class="grid gap-6 text-sm text-ink-500 sm:grid-cols-2 lg:grid-cols-3">
          <div class="space-y-2">
            <p class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Explore</p>
            <NuxtLink to="/#features" class="block transition hover:text-ink-700">Features</NuxtLink>
            <NuxtLink to="/#foundations" class="block transition hover:text-ink-700">Foundations</NuxtLink>
            <NuxtLink to="/#roadmap" class="block transition hover:text-ink-700">Roadmap</NuxtLink>
          </div>
          <div class="space-y-2">
            <p class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Platform</p>
            <NuxtLink to="/privacy" class="block transition hover:text-ink-700">Privacy</NuxtLink>
            <NuxtLink to="/terms" class="block transition hover:text-ink-700">Terms</NuxtLink>
            <NuxtLink to="/#contact" class="block transition hover:text-ink-700">Contact</NuxtLink>
          </div>
          <div class="space-y-3">
            <p class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Connect</p>
            <div class="flex gap-3 text-ink-500">
              <a href="https://linkedin.com" target="_blank" rel="noopener" class="flex h-9 w-9 items-center justify-center rounded-full border border-ink-200/80 transition hover:border-brand-300 hover:text-brand-600">
                <span class="sr-only">LinkedIn</span>
                <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M4.98 3.5a2.5 2.5 0 11-.002 5.002A2.5 2.5 0 014.98 3.5zM3 9h4v12H3zM9 9h3.8v1.71h.05c.53-.96 1.84-1.97 3.79-1.97 4.05 0 4.8 2.67 4.8 6.13V21H18v-5.33c0-1.27-.02-2.9-1.77-2.9-1.77 0-2.04 1.38-2.04 2.8V21H10V9z" />
                </svg>
              </a>
              <a href="https://twitter.com" target="_blank" rel="noopener" class="flex h-9 w-9 items-center justify-center rounded-full border border-ink-200/80 transition hover:border-brand-300 hover:text-brand-600">
                <span class="sr-only">Twitter</span>
                <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M19.633 7.997c.013.18.013.36.013.54 0 5.5-4.185 11.84-11.84 11.84-2.355 0-4.553-.69-6.402-1.884.325.04.637.053.975.053a8.38 8.38 0 0 0 5.195-1.787 4.18 4.18 0 0 1-3.897-2.89c.26.04.52.066.794.066.38 0 .76-.053 1.114-.14a4.17 4.17 0 0 1-3.35-4.09v-.053c.56.31 1.205.5 1.89.52a4.16 4.16 0 0 1-1.86-3.47c0-.78.21-1.49.58-2.11a11.84 11.84 0 0 0 8.6 4.36c-.066-.31-.1-.62-.1-.94a4.17 4.17 0 0 1 4.17-4.17c1.2 0 2.29.5 3.05 1.31a8.23 8.23 0 0 0 2.64-1.01 4.16 4.16 0 0 1-1.83 2.3 8.35 8.35 0 0 0 2.4-.65 8.56 8.56 0 0 1-2.09 2.16z" />
                </svg>
              </a>
              <a href="https://youtube.com" target="_blank" rel="noopener" class="flex h-9 w-9 items-center justify-center rounded-full border border-ink-200/80 transition hover:border-brand-300 hover:text-brand-600">
                <span class="sr-only">YouTube</span>
                <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M21.8 8.001a2.751 2.751 0 0 0-1.94-1.947C18.05 5.5 12 5.5 12 5.5s-6.05 0-7.86.554A2.751 2.751 0 0 0 2.2 8.001C1.65 9.82 1.65 12 1.65 12s0 2.18.55 3.999a2.75 2.75 0 0 0 1.94 1.947C5.95 18.5 12 18.5 12 18.5s6.05 0 7.86-.554a2.75 2.75 0 0 0 1.94-1.947C22.35 14.18 22.35 12 22.35 12s0-2.18-.55-3.999zM10.5 14.65v-5.3L15 12l-4.5 2.65z" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useAuthStore } from '~/stores/auth'
import Navigation from '~/components/layout/Navigation.vue'
import PublicNavigation from '~/components/layout/PublicNavigation.vue'

const authStore = useAuthStore()
const isAuthenticated = computed(() => authStore.isAuthenticated)
const currentYear = new Date().getFullYear()
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
