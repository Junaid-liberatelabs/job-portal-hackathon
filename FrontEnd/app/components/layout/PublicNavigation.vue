<template>
  <nav class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-ink-100 shadow-sm transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center gap-3 group">
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
        <div class="hidden lg:flex items-center gap-8">
          <!-- Main Nav Items -->
          <nav class="flex items-center gap-1">
            <a
              v-for="item in navItems"
              :key="item.label"
              :href="item.href"
              class="px-4 py-2 text-sm font-medium text-ink-600 hover:text-ink-900 hover:bg-ink-50 rounded-lg transition-all"
            >
              {{ item.label }}
            </a>
          </nav>
          
          <!-- Platform Dropdown -->
          <div class="relative group">
            <button class="flex items-center gap-1 px-4 py-2 text-sm font-medium text-ink-600 hover:text-ink-900 hover:bg-ink-50 rounded-lg transition-all">
              <span>Platform</span>
              <svg class="h-4 w-4 transition-transform group-hover:rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            
            <!-- Dropdown Menu with Material Design elevation -->
            <div class="absolute top-full mt-2 right-0 w-48 bg-white rounded-xl border border-ink-100 py-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 shadow-2xl"
                 style="box-shadow: 0 10px 40px rgba(0, 0, 0, 0.12), 0 2px 8px rgba(0, 0, 0, 0.08)">
              <a
                v-for="link in companyLinks"
                :key="link.href"
                :href="link.href"
                class="block px-4 py-2.5 text-sm text-ink-700 hover:bg-brand-50 hover:text-brand-600 transition-colors"
              >
                {{ link.label }}
              </a>
            </div>
          </div>
          
          <!-- Auth Buttons -->
          <div class="flex items-center gap-3 pl-4 border-l border-ink-200">
            <NuxtLink 
              to="/login" 
              class="px-4 py-2 text-sm font-medium text-ink-700 hover:text-ink-900 hover:bg-ink-50 rounded-lg transition-all"
            >
              Sign In
            </NuxtLink>
            <NuxtLink 
              to="/signup" 
              class="group px-6 py-2.5 text-sm font-semibold text-white bg-gradient-to-r from-brand-500 to-brand-600 hover:from-brand-600 hover:to-brand-700 rounded-xl shadow-lg shadow-brand-500/30 transition-all hover:scale-105 hover:shadow-xl hover:shadow-brand-500/40"
            >
              <span>Get Started</span>
              <svg class="inline-block ml-1.5 h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </NuxtLink>
          </div>
        </div>
        
        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden p-2 rounded-lg text-ink-600 hover:bg-ink-50 transition-colors"
          aria-label="Toggle menu"
        >
          <svg v-if="!mobileMenuOpen" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>
    
    <!-- Mobile Menu -->
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-1"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-1"
    >
      <div v-if="mobileMenuOpen" class="md:hidden border-t border-ink-100 bg-white shadow-lg">
        <div class="px-4 py-4 space-y-1">
          <!-- Main Navigation -->
          <a
            v-for="item in navItems"
            :key="item.label"
            :href="item.href"
            class="block px-4 py-3 text-sm font-medium text-ink-700 hover:bg-ink-50 hover:text-ink-900 rounded-lg transition-colors"
            @click="mobileMenuOpen = false"
          >
            {{ item.label }}
          </a>
          
          <!-- Platform Section -->
          <div class="pt-2">
            <p class="px-4 py-2 text-xs font-semibold text-ink-400 uppercase tracking-wider">Platform</p>
            <a
              v-for="link in companyLinks"
              :key="link.href"
              :href="link.href"
              class="block px-4 py-3 text-sm font-medium text-ink-600 hover:bg-ink-50 hover:text-ink-900 rounded-lg transition-colors"
              @click="mobileMenuOpen = false"
            >
              {{ link.label }}
            </a>
          </div>
          
          <!-- Auth Buttons -->
          <div class="pt-4 space-y-2 border-t border-ink-100 mt-4">
            <NuxtLink 
              to="/login" 
              class="block w-full text-center px-4 py-3 text-sm font-medium text-ink-700 hover:bg-ink-50 rounded-lg transition-colors"
              @click="mobileMenuOpen = false"
            >
              Sign In
            </NuxtLink>
            <NuxtLink 
              to="/signup" 
              class="block w-full text-center px-4 py-3 text-sm font-semibold text-white bg-gradient-to-r from-brand-500 to-brand-600 rounded-lg shadow-lg transition-all"
              @click="mobileMenuOpen = false"
            >
              Get Started
            </NuxtLink>
          </div>
        </div>
      </div>
    </Transition>
  </nav>
  
  <!-- Spacer -->
  <div class="h-16"></div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import GradientIcon from '~/components/ui/GradientIcon.vue'

const mobileMenuOpen = ref(false)

const navItems = [
  { label: 'Explore', href: '/#explore' },
  { label: 'Features', href: '/#features' },
  { label: 'Foundations', href: '/#foundations' },
  { label: 'Roadmap', href: '/#roadmap' }
]

const companyLinks = [
  { label: 'Privacy', href: '/privacy' },
  { label: 'Terms', href: '/terms' },
  { label: 'Contact', href: '/#contact' }
]
</script>

