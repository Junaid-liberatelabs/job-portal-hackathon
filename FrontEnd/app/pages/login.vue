<template>
  <div class="mx-auto flex min-h-[calc(100vh-160px)] max-w-4xl flex-col justify-center px-6 py-16 lg:px-10">
    <div class="space-y-6 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_40px_120px_-60px_rgba(15,23,42,0.25)] backdrop-blur">
      <div class="space-y-3">
        <p class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/60 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-700">
          Welcome back
        </p>
        <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Sign in to continue your journey</h1>
        <p class="text-sm text-ink-500">
          Access your dashboard, up-to-date matches, and curated learning plan in seconds.
        </p>
      </div>

      <form class="space-y-5" @submit.prevent="handleSubmit">
        <div class="space-y-2">
          <label for="email" class="text-sm font-medium text-ink-600">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            required
            autocomplete="email"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="you@example.com"
          />
        </div>
        <div class="space-y-2">
          <label for="password" class="text-sm font-medium text-ink-600">Password</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            minlength="8"
            required
            autocomplete="current-password"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="Enter your password"
          />
        </div>

        <p v-if="auth.error" class="rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-600">
          {{ auth.error }}
        </p>

        <button
          type="submit"
          :disabled="auth.loading"
          class="inline-flex w-full items-center justify-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800 disabled:cursor-not-allowed disabled:opacity-60"
        >
          <span v-if="auth.loading" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
          <span>{{ auth.loading ? 'Signing in...' : 'Sign in' }}</span>
        </button>
      </form>

      <p class="text-sm text-ink-500">
        Don’t have an account?
        <NuxtLink to="/signup" class="font-semibold text-brand-600 transition hover:text-brand-500">Create one in minutes</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter, useRoute, definePageMeta } from '#imports'
import { useAuthStore } from '~/stores/auth'

definePageMeta({
  middleware: 'guest'
})

const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const form = reactive({
  email: '',
  password: ''
})

const handleSubmit = async () => {
  const success = await auth.login(form.email, form.password)
  if (success) {
    const redirect = typeof route.query.redirect === 'string' ? route.query.redirect : '/dashboard'
    await router.push(redirect)
  }
}
</script>
