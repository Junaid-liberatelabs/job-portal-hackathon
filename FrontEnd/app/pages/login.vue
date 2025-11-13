<template>
  <div class="relative min-h-screen bg-gradient-to-br from-ink-50 via-white to-brand-50/30 overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiMzYjgyZjYiIGZpbGwtb3BhY2l0eT0iMC4wMyI+PHBhdGggZD0iTTM2IDM0djItaDJ2LTJoLTJ6bTAtNGgtMnYyaDJ2LTJ6bTAgNGgydjItMnYtMnoiLz48L2c+PC9nPjwvc3ZnPg==')] opacity-50"></div>
    
    <div class="relative flex min-h-screen">
      <!-- Left Side - Branding & Features -->
      <div class="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-brand-600 via-brand-700 to-ink-900 p-12 flex-col justify-between relative overflow-hidden">
        <!-- Background Animation -->
        <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PHBhdGggZD0iTTM2IDM0djItaDJ2LTJoLTJ6bTAtNGgtMnYyaDJ2LTJ6bTAgNGgydjItMnYtMnoiLz48L2c+PC9nPjwvc3ZnPg==')] opacity-30"></div>
        
        <div class="relative z-10">
          <!-- Logo -->
          <NuxtLink to="/" class="flex items-center gap-3 group">
            <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-white/20 backdrop-blur-sm text-white shadow-lg shadow-black/20 ring-2 ring-white/30 transition group-hover:scale-105">
              <span class="font-bold text-xl">CI</span>
            </div>
            <div class="flex flex-col">
              <span class="text-2xl font-display font-bold text-white leading-none">
                Career<span class="text-blue-200">In</span>
              </span>
              <span class="text-[10px] font-medium uppercase tracking-wider text-blue-200 leading-none mt-1">Career Platform</span>
            </div>
          </NuxtLink>
        </div>
        
        <div class="relative z-10 space-y-8">
          <div>
            <h2 class="font-display text-4xl font-bold text-white mb-4 leading-tight">
              Welcome back to your<br/>career journey
            </h2>
            <p class="text-lg text-blue-100 leading-relaxed">
              Access your personalized dashboard, discover new opportunities, and continue building your future.
            </p>
          </div>
          
          <!-- Features List -->
          <div class="space-y-4">
            <div v-for="feature in features" :key="feature.title" class="flex items-start gap-4 p-4 rounded-2xl bg-white/10 backdrop-blur-sm border border-white/20 hover:bg-white/15 transition group">
              <div class="flex-shrink-0 h-12 w-12 rounded-xl bg-white/20 flex items-center justify-center text-white shadow-lg">
                <component :is="feature.icon" class="h-6 w-6" />
              </div>
              <div>
                <h3 class="font-semibold text-white mb-1">{{ feature.title }}</h3>
                <p class="text-sm text-blue-100">{{ feature.description }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="relative z-10 text-sm text-blue-200">
          © {{ currentYear }} CareerIn. All rights reserved.
        </div>
      </div>
      
      <!-- Right Side - Sign In Form -->
      <div class="w-full lg:w-1/2 flex items-center justify-center p-6 lg:p-12">
        <div class="w-full max-w-md space-y-8 animate-fade-in">
          <!-- Mobile Logo -->
          <div class="lg:hidden flex justify-center mb-8">
            <NuxtLink to="/" class="flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-brand-500 to-brand-600 text-white shadow-lg">
                <span class="font-bold text-lg">CI</span>
              </div>
              <div class="flex flex-col">
                <span class="text-xl font-display font-bold text-ink-900 leading-none">
                  Career<span class="text-brand-600">In</span>
                </span>
              </div>
            </NuxtLink>
          </div>
          
          <!-- Header -->
          <div class="text-center lg:text-left space-y-3">
            <div class="inline-flex items-center gap-2 rounded-full border border-brand-200 bg-brand-50 px-4 py-2 text-xs font-bold uppercase tracking-wider text-brand-700">
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
              </svg>
              Welcome Back
            </div>
            <h1 class="font-display text-4xl font-bold text-ink-900 tracking-tight">
              Sign in to <span class="text-brand-600">CareerIn</span>
            </h1>
            <p class="text-base text-ink-600">
              Continue your journey to career success
            </p>
          </div>
          
          <!-- Sign In Form -->
          <form class="space-y-6" @submit.prevent="handleSubmit">
            <!-- Email Field -->
            <div class="space-y-2">
              <label for="email" class="block text-sm font-semibold text-ink-700">
                Email address
              </label>
              <div class="relative">
                <div class="absolute left-4 top-1/2 -translate-y-1/2 text-ink-400">
                  <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                  </svg>
                </div>
                <input
                  id="email"
                  v-model="form.email"
                  type="email"
                  required
                  autocomplete="email"
                  class="w-full pl-12 pr-4 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
                  placeholder="you@example.com"
                />
              </div>
            </div>
            
            <!-- Password Field -->
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <label for="password" class="block text-sm font-semibold text-ink-700">
                  Password
                </label>
                <button type="button" class="text-sm font-medium text-brand-600 hover:text-brand-700 transition">
                  Forgot?
                </button>
              </div>
              <div class="relative">
                <div class="absolute left-4 top-1/2 -translate-y-1/2 text-ink-400">
                  <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <input
                  id="password"
                  v-model="form.password"
                  :type="showPassword ? 'text' : 'password'"
                  minlength="8"
                  required
                  autocomplete="current-password"
                  class="w-full pl-12 pr-12 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
                  placeholder="Enter your password"
                />
                <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-ink-400 hover:text-ink-600 transition"
                >
                  <svg v-if="!showPassword" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  <svg v-else class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                  </svg>
                </button>
              </div>
            </div>
            
            <!-- Remember Me -->
            <div class="flex items-center">
              <input
                id="remember"
                v-model="rememberMe"
                type="checkbox"
                class="h-4 w-4 rounded border-ink-300 text-brand-600 focus:ring-brand-500 focus:ring-offset-0"
              />
              <label for="remember" class="ml-2 text-sm text-ink-600">
                Keep me signed in
              </label>
            </div>
            
            <!-- Error Message -->
            <div v-if="auth.error" class="rounded-xl border-2 border-red-200 bg-red-50 p-4 flex items-start gap-3">
              <svg class="h-5 w-5 text-red-600 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div class="flex-1">
                <p class="text-sm font-semibold text-red-900">Sign in failed</p>
                <p class="text-sm text-red-700">{{ auth.error }}</p>
              </div>
            </div>
            
            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="auth.loading"
              class="w-full inline-flex items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 px-6 py-4 text-base font-semibold text-white shadow-lg shadow-brand-500/30 transition-all hover:from-brand-600 hover:to-brand-700 hover:scale-[1.02] hover:shadow-xl hover:shadow-brand-500/40 disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:scale-100"
            >
              <span v-if="auth.loading" class="h-5 w-5 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <svg v-else class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
              </svg>
              <span>{{ auth.loading ? 'Signing in...' : 'Sign in to Dashboard' }}</span>
            </button>
          </form>
          
          <!-- Divider -->
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-ink-200"></div>
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-4 bg-white text-ink-500 font-medium">New to CareerIn?</span>
            </div>
          </div>
          
          <!-- Sign Up Link -->
          <NuxtLink
            to="/signup"
            class="w-full inline-flex items-center justify-center gap-2 rounded-xl border-2 border-brand-300 px-6 py-4 text-base font-semibold text-brand-700 transition-all hover:bg-brand-50 hover:border-brand-400 hover:scale-[1.02]"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
            </svg>
            <span>Create your free account</span>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, h } from 'vue'
import { useRouter, useRoute, definePageMeta } from '#imports'
import { useAuthStore } from '~/stores/auth'

definePageMeta({
  middleware: 'guest',
  layout: 'public'
})

const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const form = reactive({
  email: '',
  password: ''
})

const showPassword = ref(false)
const rememberMe = ref(false)
const currentYear = new Date().getFullYear()

// Feature icons
const DashboardIcon = () => h('svg', { class: 'h-6 w-6', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' })
])

const BriefcaseIcon = () => h('svg', { class: 'h-6 w-6', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z' })
])

const BookIcon = () => h('svg', { class: 'h-6 w-6', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' })
])

const features = [
  {
    title: 'Personalized Dashboard',
    description: 'Track your progress, skills, and career goals in one place',
    icon: DashboardIcon
  },
  {
    title: 'AI-Powered Job Matching',
    description: 'Discover opportunities that match your skills and aspirations',
    icon: BriefcaseIcon
  },
  {
    title: 'Curated Learning Resources',
    description: 'Access courses and materials tailored to your career path',
    icon: BookIcon
  }
]

const handleSubmit = async () => {
  const success = await auth.login(form.email, form.password)
  if (success) {
    const redirect = typeof route.query.redirect === 'string' ? route.query.redirect : '/dashboard'
    await router.push(redirect)
  }
}
</script>
