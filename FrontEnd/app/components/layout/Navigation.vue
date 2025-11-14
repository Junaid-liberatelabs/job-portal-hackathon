<template>
  <nav class="fixed top-0 w-full z-50 bg-white shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <NuxtLink to="/dashboard" class="flex items-center gap-3 group">
          <GradientIcon size="md">
            <span class="text-white font-bold text-lg">CI</span>
          </GradientIcon>
          <div class="flex flex-col">
            <span class="text-xl font-display font-bold text-ink-900 leading-none">
              Career<span class="text-brand-600">In</span>
            </span>
            <span class="text-[10px] font-medium uppercase tracking-wider text-brand-500 leading-none mt-0.5">Career Platform</span>
          </div>
        </NuxtLink>
        
        <!-- Desktop Navigation -->
        <div v-if="isAuthenticated" class="hidden md:flex items-center space-x-2">
          <NuxtLink
            v-for="item in navigationItems"
            :key="item.path"
            :to="item.path"
            :class="[
              'relative px-4 py-2 text-sm font-medium transition-all rounded-lg flex items-center gap-2',
              isActive(item.path) 
                ? 'text-brand-600 bg-brand-50 shadow-sm' 
                : 'text-ink-600 hover:text-ink-900 hover:bg-ink-50'
            ]"
          >
            <component :is="item.icon" class="h-5 w-5" />
            {{ item.label }}
            <span 
              v-if="isActive(item.path)"
              class="absolute bottom-0 left-1/2 -translate-x-1/2 w-12 h-1 bg-brand-500 rounded-t-full"
            ></span>
          </NuxtLink>
        </div>
        
        <div v-else class="hidden md:flex items-center space-x-4">
          <NuxtLink to="/login">
            <Button variant="ghost" size="sm">Sign In</Button>
          </NuxtLink>
          <NuxtLink to="/signup">
            <Button variant="accent" size="sm">Get Started</Button>
          </NuxtLink>
        </div>
        
        <!-- User Menu -->
        <div v-if="isAuthenticated" class="flex items-center gap-3">
          <!-- Notifications Button with Material Design ripple effect -->
          <button class="relative p-2 rounded-full text-ink-600 hover:bg-ink-100 transition-all duration-200 hover:scale-110">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
            <span class="absolute top-1 right-1 h-2.5 w-2.5 rounded-full bg-red-500 border-2 border-white animate-pulse"></span>
          </button>
          
          <div class="relative" ref="profileMenuRef">
            <button
              @click="toggleProfileMenu"
              class="flex items-center gap-2 p-2 pr-3 rounded-full hover:bg-ink-50 transition-all duration-200"
            >
              <div class="h-10 w-10 rounded-full bg-gradient-to-br from-brand-400 to-brand-600 flex items-center justify-center shadow-lg ring-2 ring-white hover:scale-105 transition-transform">
                <span class="text-white font-bold text-sm">{{ userInitials }}</span>
              </div>
              <div class="hidden lg:flex flex-col items-start">
                <span class="text-sm font-semibold text-ink-900">{{ user?.full_name }}</span>
                <span class="text-xs text-ink-500">View Profile</span>
              </div>
              <svg 
                class="h-4 w-4 text-ink-400 transition-transform duration-200"
                :class="{ 'rotate-180': showProfileMenu }"
                fill="none" 
                viewBox="0 0 24 24" 
                stroke="currentColor"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            
            <!-- Dropdown Menu with Material Design elevation -->
            <Transition name="dropdown">
              <div
                v-if="showProfileMenu"
                class="absolute right-0 mt-4 w-72 rounded-2xl bg-white shadow-2xl border border-ink-100 overflow-hidden"
                style="box-shadow: 0 10px 40px rgba(0, 0, 0, 0.12), 0 2px 8px rgba(0, 0, 0, 0.08)"
              >
                <!-- User Info Header -->
                <div class="px-4 py-4 bg-gradient-to-br from-brand-50 to-white border-b border-ink-100">
                  <div class="flex items-center gap-3">
                    <div class="h-12 w-12 rounded-full bg-gradient-to-br from-brand-400 to-brand-600 flex items-center justify-center shadow-md">
                      <span class="text-white font-bold">{{ userInitials }}</span>
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="text-sm font-semibold text-ink-900 truncate">{{ user?.full_name }}</p>
                      <p class="text-xs text-ink-600 truncate">{{ user?.email }}</p>
                    </div>
                  </div>
                </div>
                
                <!-- Menu Items -->
                <div class="py-2">
                  <NuxtLink
                    to="/profile"
                    class="flex items-center gap-3 px-4 py-3 text-sm text-ink-700 hover:bg-brand-50 transition-all group"
                    @click="showProfileMenu = false"
                  >
                    <div class="h-10 w-10 rounded-lg bg-ink-100 flex items-center justify-center group-hover:bg-brand-100 group-hover:text-brand-600 transition-all">
                      <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      </svg>
                    </div>
                    <div class="flex-1">
                      <p class="font-medium">Your Profile</p>
                      <p class="text-xs text-ink-500">Manage your account</p>
                    </div>
                  </NuxtLink>
                  
                  <NuxtLink
                    to="/dashboard"
                    class="flex items-center gap-3 px-4 py-3 text-sm text-ink-700 hover:bg-brand-50 transition-all group"
                    @click="showProfileMenu = false"
                  >
                    <div class="h-10 w-10 rounded-lg bg-ink-100 flex items-center justify-center group-hover:bg-brand-100 group-hover:text-brand-600 transition-all">
                      <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                      </svg>
                    </div>
                    <div class="flex-1">
                      <p class="font-medium">Dashboard</p>
                      <p class="text-xs text-ink-500">View your overview</p>
                    </div>
                  </NuxtLink>
                </div>
                
                <!-- Logout Section -->
                <div class="border-t border-ink-100 p-2">
                  <button
                    @click="handleLogout"
                    class="w-full flex items-center gap-3 px-4 py-3 text-sm text-red-600 hover:bg-red-50 rounded-lg transition-all group"
                  >
                    <div class="h-10 w-10 rounded-lg bg-red-50 flex items-center justify-center group-hover:bg-red-100 transition-all">
                      <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                      </svg>
                    </div>
                    <div class="flex-1 text-left">
                      <p class="font-medium">Logout</p>
                      <p class="text-xs text-red-500">Sign out of your account</p>
                    </div>
                  </button>
                </div>
              </div>
            </Transition>
          </div>
          
          <!-- Mobile Menu Button -->
          <button
            @click="toggleMobileMenu"
            class="md:hidden p-2 rounded-lg text-ink-700 hover:bg-ink-50"
          >
            <svg v-if="!showMobileMenu" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Mobile Menu -->
    <Transition name="mobile-menu">
      <div v-if="showMobileMenu && isAuthenticated" class="md:hidden border-t border-ink-100 bg-white">
        <div class="px-4 py-4 space-y-1">
          <NuxtLink
            v-for="item in navigationItems"
            :key="item.path"
            :to="item.path"
            :class="[
              'block px-4 py-3 text-sm font-medium rounded-lg transition-colors',
              isActive(item.path)
                ? 'text-brand-600 bg-brand-50'
                : 'text-ink-700 hover:bg-ink-50'
            ]"
            @click="showMobileMenu = false"
          >
            {{ item.label }}
          </NuxtLink>
        </div>
      </div>
    </Transition>
  </nav>
  
  <!-- Spacer to prevent content from going under fixed navbar -->
  <div class="h-16"></div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, h } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { onClickOutside } from '@vueuse/core'
import { useAuthStore } from '~/stores/auth'
import Button from '~/components/ui/Button.vue'
import GradientIcon from '~/components/ui/GradientIcon.vue'

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()

const showProfileMenu = ref(false)
const showMobileMenu = ref(false)
const profileMenuRef = ref(null)

const isAuthenticated = computed(() => authStore.isAuthenticated)
const user = computed(() => authStore.user)

const userInitials = computed(() => {
  if (!user.value?.full_name) return '?'
  const names = user.value.full_name.split(' ')
  return names.map(n => n[0]).join('').toUpperCase().slice(0, 2)
})

// Icon components as template strings for Material Design icons
const HomeIcon = () => h('svg', { class: 'h-5 w-5', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' })
])

const BriefcaseIcon = () => h('svg', { class: 'h-5 w-5', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z' })
])

const BookIcon = () => h('svg', { class: 'h-5 w-5', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' })
])

const UserIcon = () => h('svg', { class: 'h-5 w-5', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z' })
])

const ChartIcon = () => h('svg', { class: 'h-5 w-5', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor' }, [
  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '2', d: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' })
])

const navigationItems = [
  { path: '/dashboard', label: 'Dashboard', icon: HomeIcon },
  { path: '/jobs', label: 'Jobs', icon: BriefcaseIcon },
  { path: '/resources', label: 'Resources', icon: BookIcon },
  { path: '/skill-gap-analysis', label: 'Skill Gap', icon: ChartIcon },
  { path: '/profile', label: 'Profile', icon: UserIcon }
]

const isActive = (path: string) => {
  return route.path === path || route.path.startsWith(path + '/')
}

const toggleProfileMenu = () => {
  showProfileMenu.value = !showProfileMenu.value
}

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value
}

const handleLogout = () => {
  authStore.logout()
  showProfileMenu.value = false
  router.push('/')
}

onClickOutside(profileMenuRef, () => {
  showProfileMenu.value = false
})

onMounted(() => {
  // Close mobile menu on route change
  router.afterEach(() => {
    showMobileMenu.value = false
  })
})
</script>

<style scoped>
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  max-height: 0;
}

.mobile-menu-enter-to,
.mobile-menu-leave-from {
  opacity: 1;
  max-height: 500px;
}
</style>

