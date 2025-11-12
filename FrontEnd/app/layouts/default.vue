<template>
  <div class="flex min-h-screen flex-col bg-ink-50 text-ink-900">
    <header class="sticky top-0 z-50 border-b border-white/10 bg-white/70 backdrop-blur-xl backdrop-saturate-150">
      <nav class="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:px-10">
        <NuxtLink to="/" class="group flex items-center gap-3">
          <div class="relative h-11 w-11 overflow-hidden rounded-2xl bg-hero-gradient shadow-lg shadow-brand-500/40 ring-2 ring-white/40 transition-transform duration-300 group-hover:-translate-y-0.5">
            <span class="absolute inset-0 flex items-center justify-center text-lg font-semibold text-white">CI</span>
          </div>
          <div class="flex flex-col leading-none">
            <span class="font-display text-lg font-semibold tracking-tight text-ink-900">CareerIn</span>
            <span class="text-xs font-medium uppercase tracking-[0.35em] text-ink-400">Youth Careers</span>
          </div>
        </NuxtLink>

        <div class="hidden items-center gap-6 text-sm font-medium text-ink-500 md:flex">
          <div
            v-for="group in navGroups"
            :key="group.label"
            class="relative"
            @mouseenter="handleMouseEnter(group.label)"
            @mouseleave="scheduleClose"
          >
            <button
              type="button"
              class="inline-flex items-center gap-2 rounded-full px-3 py-1 transition-colors hover:text-ink-900"
              @click="toggleGroup(group.label)"
            >
              {{ group.label }}
              <svg
                class="h-4 w-4 text-ink-400 transition-transform duration-200"
                :class="{ 'rotate-180 text-ink-600': openGroup === group.label }"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.25a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>
            <div
              class="absolute left-1/2 top-full z-50 mt-3 w-64 -translate-x-1/2 rounded-3xl border border-white/70 bg-white/90 p-4 shadow-[0_25px_80px_-45px_rgba(15,23,42,0.3)] backdrop-blur transition-all duration-200"
              :class="openGroup === group.label ? 'visible pointer-events-auto opacity-100' : 'invisible pointer-events-none opacity-0'"
              @mouseenter="handleMouseEnter(group.label)"
              @mouseleave="scheduleClose"
            >
              <NuxtLink
                v-for="item in group.items"
                :key="item.to"
                :to="item.to"
                class="block rounded-2xl px-3 py-2 text-sm text-ink-500 transition hover:bg-ink-50 hover:text-ink-900"
              >
                {{ item.label }}
              </NuxtLink>
            </div>
          </div>
        </div>

        <div class="hidden items-center gap-3 md:flex">
          <NuxtLink
            to="/login"
            class="inline-flex items-center justify-center rounded-full border border-ink-200/80 px-4 py-2 text-sm font-medium text-ink-500 transition hover:border-brand-200 hover:text-ink-900"
          >
            Sign In
          </NuxtLink>
          <NuxtLink
            to="/signup"
            class="inline-flex items-center justify-center rounded-full bg-ink-900 px-5 py-2 text-sm font-semibold text-white shadow-md shadow-ink-900/20 transition hover:bg-ink-800"
          >
            Create Profile
          </NuxtLink>
        </div>

        <button
          type="button"
          class="inline-flex h-10 w-10 items-center justify-center rounded-full border border-ink-200/80 text-ink-600 transition hover:border-brand-200 hover:text-ink-900 md:hidden"
          @click="mobileNavOpen = !mobileNavOpen"
        >
          <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5M12 17.25h8.25" />
          </svg>
          <span class="sr-only">Open navigation</span>
        </button>
      </nav>

      <Transition name="fade">
        <div
          v-if="mobileNavOpen"
          class="border-t border-white/10 bg-white/95 px-6 py-4 shadow-lg shadow-ink-900/5 md:hidden"
        >
          <div class="space-y-5 text-sm text-ink-600">
            <div
              v-for="group in navGroups"
              :key="`mobile-${group.label}`"
              class="space-y-2"
            >
              <p class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">
                {{ group.label }}
              </p>
              <NuxtLink
                v-for="item in group.items"
                :key="item.to"
                :to="item.to"
                class="block rounded-2xl px-3 py-2 transition hover:bg-ink-100/70 hover:text-ink-900"
                @click="mobileNavOpen = false"
              >
                {{ item.label }}
              </NuxtLink>
            </div>
          </div>
          <div class="mt-6 flex flex-col gap-3">
            <NuxtLink
              to="/login"
              class="w-full rounded-full border border-ink-200/70 px-4 py-2 text-center text-sm font-medium text-ink-700 transition hover:border-brand-200 hover:text-ink-900"
            >
              Sign In
            </NuxtLink>
            <NuxtLink
              to="/signup"
              class="w-full rounded-full bg-ink-900 px-4 py-2 text-center text-sm font-semibold text-white transition hover:bg-ink-800"
            >
              Create Profile
            </NuxtLink>
          </div>
        </div>
      </Transition>
    </header>

    <main class="flex-1">
      <slot />
    </main>

    <footer class="border-t border-white/10 bg-white/75 py-12 backdrop-blur-xl">
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
            <p class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Company</p>
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
import { ref, watch } from 'vue'
import { useRoute } from '#imports'

const navGroups = [
  {
    label: 'Platform',
    items: [
      { label: 'Features', to: '/#features' },
      { label: 'Foundations', to: '/#foundations' },
      { label: 'How It Works', to: '/#process' }
    ]
  },
  {
    label: 'Insights',
    items: [
      { label: 'Matching', to: '/#matching' },
      { label: 'Roadmap', to: '/#roadmap' },
      { label: 'Testimonials', to: '/#testimonials' }
    ]
  },
  {
    label: 'Company',
    items: [{ label: 'Contact', to: '/#contact' }]
  }
]

const mobileNavOpen = ref(false)
const openGroup = ref<string | null>(null)
const closeTimer = ref<ReturnType<typeof setTimeout> | null>(null)
const route = useRoute()

const toggleGroup = (label: string) => {
  openGroup.value = openGroup.value === label ? null : label
}

const handleMouseEnter = (label: string) => {
  if (closeTimer.value) {
    clearTimeout(closeTimer.value)
    closeTimer.value = null
  }
  openGroup.value = label
}

const scheduleClose = () => {
  if (closeTimer.value) {
    clearTimeout(closeTimer.value)
  }
  closeTimer.value = setTimeout(() => {
    openGroup.value = null
    closeTimer.value = null
  }, 180)
}

watch(
  () => route.fullPath,
  () => {
    mobileNavOpen.value = false
    openGroup.value = null
    if (closeTimer.value) {
      clearTimeout(closeTimer.value)
      closeTimer.value = null
    }
  }
)

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
