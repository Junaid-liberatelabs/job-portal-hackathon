<template>
  <nav class="fixed top-0 w-full z-50 glass border-b border-white/20 no-print">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center gap-2">
          <div class="h-8 w-8 rounded-lg bg-gradient-accent flex items-center justify-center">
            <span class="text-white font-bold text-xl">C</span>
          </div>
          <span class="text-xl font-display font-bold text-ink-900">Career<span class="text-accent">In</span></span>
        </NuxtLink>
        
        <!-- Desktop Navigation -->
        <div v-if="isAuthenticated" class="hidden md:block">
          <div class="ml-10 flex items-baseline space-x-6">
            <NuxtLink
              v-for="item in navigationItems"
              :key="item.path"
              :to="item.path"
              class="px-3 py-2 text-sm font-medium transition-colors rounded-lg"
              :class="isActive(item.path) 
                ? 'text-accent bg-accent/10' 
                : 'text-ink-700 hover:text-ink-900 hover:bg-ink-50'"
            >
              <component :is="item.icon" class="h-5 w-5 inline mr-1.5" />
              {{ item.label }}
            </NuxtLink>
          </div>
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
        <div v-if="isAuthenticated" class="flex items-center space-x-4">
          <div class="relative" ref="profileMenuRef">
            <button
              @click="toggleProfileMenu"
              class="flex items-center space-x-3 p-2 rounded-lg hover:bg-ink-50 transition-colors"
            >
              <div class="hidden sm:block text-right">
                <p class="text-sm font-medium text-ink-900">{{ user?.full_name }}</p>
                <p class="text-xs text-ink-500">{{ user?.email }}</p>
              </div>
              <div class="h-10 w-10 rounded-full bg-gradient-accent flex items-center justify-center">
                <span class="text-white font-semibold">{{ userInitials }}</span>
              </div>
              <ChevronDownIcon class="h-4 w-4 text-ink-500" />
            </button>
            
            <!-- Dropdown Menu -->
            <Transition name="dropdown">
              <div
                v-if="showProfileMenu"
                class="absolute right-0 mt-2 w-56 rounded-xl shadow-xl bg-white border border-ink-100 py-2"
              >
                <NuxtLink
                  to="/profile"
                  class="flex items-center gap-3 px-4 py-2.5 text-sm text-ink-700 hover:bg-ink-50 transition-colors"
                  @click="showProfileMenu = false"
                >
                  <UserIcon class="h-5 w-5" />
                  Your Profile
                </NuxtLink>
                <NuxtLink
                  to="/dashboard"
                  class="flex items-center gap-3 px-4 py-2.5 text-sm text-ink-700 hover:bg-ink-50 transition-colors"
                  @click="showProfileMenu = false"
                >
                  <ChartBarIcon class="h-5 w-5" />
                  Dashboard
                </NuxtLink>
                <hr class="my-2 border-ink-100" />
                <button
                  @click="handleLogout"
                  class="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-red-600 hover:bg-red-50 transition-colors"
                >
                  <ArrowRightOnRectangleIcon class="h-5 w-5" />
                  Sign Out
                </button>
              </div>
            </Transition>
          </div>
          
          <!-- Mobile Menu Button -->
          <button
            @click="toggleMobileMenu"
            class="md:hidden p-2 rounded-lg text-ink-700 hover:bg-ink-50"
          >
            <Bars3Icon v-if="!showMobileMenu" class="h-6 w-6" />
            <XMarkIcon v-else class="h-6 w-6" />
          </button>
        </div>
      </div>
    </div>
    
    <!-- Mobile Menu -->
    <Transition name="mobile-menu">
      <div v-if="showMobileMenu && isAuthenticated" class="md:hidden border-t border-ink-100 bg-white">
        <div class="px-4 py-4 space-y-2">
          <NuxtLink
            v-for="item in navigationItems"
            :key="item.path"
            :to="item.path"
            class="flex items-center gap-3 px-4 py-3 text-sm font-medium rounded-lg transition-colors"
            :class="isActive(item.path)
              ? 'text-accent bg-accent/10'
              : 'text-ink-700 hover:bg-ink-50'"
            @click="showMobileMenu = false"
          >
            <component :is="item.icon" class="h-5 w-5" />
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
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { onClickOutside } from '@vueuse/core'
import {
  HomeIcon,
  BriefcaseIcon,
  BookOpenIcon,
  UserIcon,
  ChartBarIcon,
  ArrowRightOnRectangleIcon,
  ChevronDownIcon,
  Bars3Icon,
  XMarkIcon
} from '@heroicons/vue/24/outline'

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

const navigationItems = [
  { path: '/dashboard', label: 'Dashboard', icon: HomeIcon },
  { path: '/jobs', label: 'Jobs', icon: BriefcaseIcon },
  { path: '/resources', label: 'Resources', icon: BookOpenIcon },
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

