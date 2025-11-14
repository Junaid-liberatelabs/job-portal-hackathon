<template>
  <div class="relative min-h-screen bg-gradient-to-br from-ink-50 via-white to-emerald-50/20 overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiMxMGI5ODEiIGZpbGwtb3BhY2l0eT0iMC4wMyI+PHBhdGggZD0iTTM2IDM0djItaDJ2LTJoLTJ6bTAtNGgtMnYyaDJ2LTJ6bTAgNGgydjItMnYtMnoiLz48L2c+PC9nPjwvc3ZnPg==')] opacity-50"></div>
    
    <div class="relative flex min-h-screen">
      <!-- Left Side - Branding & Benefits -->
      <div class="hidden lg:flex lg:w-2/5 bg-gradient-to-br from-emerald-600 via-emerald-700 to-ink-900 p-12 flex-col justify-between relative overflow-hidden">
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
                Career<span class="text-emerald-200">In</span>
              </span>
              <span class="text-[10px] font-medium uppercase tracking-wider text-emerald-200 leading-none mt-1">Career Platform</span>
            </div>
          </NuxtLink>
        </div>
        
        <div class="relative z-10 space-y-8">
          <div>
            <h2 class="font-display text-4xl font-bold text-white mb-4 leading-tight">
              Start your career<br/>journey today
            </h2>
            <p class="text-lg text-emerald-100 leading-relaxed">
              Join thousands of students and professionals discovering their perfect career path.
            </p>
          </div>
          
          <!-- Benefits -->
          <div class="space-y-4">
            <div v-for="(benefit, index) in benefits" :key="index" class="flex items-center gap-3 text-white">
              <div class="flex-shrink-0 h-8 w-8 rounded-lg bg-white/20 flex items-center justify-center">
                <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span class="font-medium">{{ benefit }}</span>
            </div>
          </div>
          
          <!-- Stats -->
          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-white/20">
            <div v-for="stat in stats" :key="stat.label" class="text-center">
              <div class="text-3xl font-bold text-white mb-1">{{ stat.value }}</div>
              <div class="text-xs text-emerald-200">{{ stat.label }}</div>
            </div>
          </div>
        </div>
        
        <div class="relative z-10 text-sm text-emerald-200">
          © {{ currentYear }} CareerIn. All rights reserved.
        </div>
      </div>
      
      <!-- Right Side - Sign Up Form -->
      <div class="w-full lg:w-3/5 flex items-center justify-center p-6 lg:p-12">
        <div class="w-full max-w-2xl space-y-8 animate-fade-in">
          <!-- Mobile Logo -->
          <div class="lg:hidden flex justify-center mb-8">
            <NuxtLink to="/" class="flex items-center gap-3">
              <div class="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-emerald-500 to-emerald-600 text-white shadow-lg">
                <span class="font-bold text-lg">CI</span>
              </div>
              <div class="flex flex-col">
                <span class="text-xl font-display font-bold text-ink-900 leading-none">
                  Career<span class="text-emerald-600">In</span>
                </span>
              </div>
            </NuxtLink>
          </div>
          
          <!-- Header -->
          <div class="text-center lg:text-left space-y-3">
            <div class="inline-flex items-center gap-2 rounded-full border border-emerald-200 bg-emerald-50 px-4 py-2 text-xs font-bold uppercase tracking-wider text-emerald-700">
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              Free Forever
            </div>
            <h1 class="font-display text-4xl font-bold text-ink-900 tracking-tight">
              Create your <span class="text-emerald-600">CareerIn</span> account
            </h1>
            <p class="text-base text-ink-600">
              Build your profile in minutes and unlock personalized opportunities
            </p>
          </div>
          
          <!-- Progress Steps -->
          <div class="flex items-center justify-center gap-2">
            <div v-for="step in 3" :key="step" :class="[
              'h-2 rounded-full transition-all',
              step === 1 ? 'w-8 bg-emerald-500' : 'w-2 bg-ink-200'
            ]"></div>
          </div>
          
          <!-- Sign Up Form -->
          <form class="space-y-5" @submit.prevent="handleSubmit">
            <!-- Full Name -->
            <div class="space-y-2">
              <label for="full_name" class="block text-sm font-semibold text-ink-700">
                Full Name <span class="text-red-500">*</span>
              </label>
              <div class="relative">
                <div class="absolute left-4 top-1/2 -translate-y-1/2 text-ink-400">
                  <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <input
                  id="full_name"
                  v-model="form.full_name"
                  type="text"
                  required
                  autocomplete="name"
                  class="w-full pl-12 pr-4 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
                  placeholder="Alex Doe"
                />
              </div>
            </div>

            <!-- Email & Password Row -->
            <div class="grid md:grid-cols-2 gap-5">
              <div class="space-y-2">
                <label for="email" class="block text-sm font-semibold text-ink-700">
                  Email Address <span class="text-red-500">*</span>
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
                    class="w-full pl-12 pr-4 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
                    placeholder="you@example.com"
                  />
                </div>
              </div>

              <div class="space-y-2">
                <label for="password" class="block text-sm font-semibold text-ink-700">
                  Password <span class="text-red-500">*</span>
                </label>
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
                    autocomplete="new-password"
                    class="w-full pl-12 pr-12 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
                    placeholder="Min. 8 characters"
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
            </div>

            <!-- Education & Experience Row -->
            <div class="grid md:grid-cols-2 gap-5">
              <div class="space-y-2">
                <label for="education_level" class="block text-sm font-semibold text-ink-700">
                  Education Level <span class="text-red-500">*</span>
                </label>
                <div class="relative">
                  <div class="absolute left-4 top-1/2 -translate-y-1/2 text-ink-400">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path d="M12 14l9-5-9-5-9 5 9 5z" />
                      <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
                    </svg>
                  </div>
                  <input
                    id="education_level"
                    v-model="form.education_level"
                    type="text"
                    required
                    class="w-full pl-12 pr-4 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
                    placeholder="e.g., BSc Computer Science"
                  />
                </div>
              </div>

              <div class="space-y-2">
                <label for="experience_level" class="block text-sm font-semibold text-ink-700">
                  Experience Level <span class="text-red-500">*</span>
                </label>
                <div class="relative" ref="experienceDropdownRef">
                  <div class="absolute left-4 top-1/2 -translate-y-1/2 text-ink-400 pointer-events-none z-10">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  </div>
                  <button
                    type="button"
                    @click="showExperienceDropdown = !showExperienceDropdown"
                    class="w-full pl-12 pr-10 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100 text-left flex items-center gap-3"
                  >
                    <component v-if="selectedExperience" :is="MaterialIcon(selectedExperience.icon, 5)" class="text-ink-400 flex-shrink-0" />
                    <span v-if="selectedExperience">{{ selectedExperience.label }}</span>
                  </button>
                  <div class="absolute right-4 top-1/2 -translate-y-1/2 text-ink-400 pointer-events-none">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>
                  <div
                    v-if="showExperienceDropdown"
                    class="absolute z-20 w-full mt-1 bg-white border-2 border-ink-200 rounded-xl shadow-lg overflow-hidden"
                  >
                    <button
                      v-for="option in experienceOptions"
                      :key="option.value"
                      type="button"
                      @click="form.experience_level = option.value as ExperienceLevel; showExperienceDropdown = false"
                      :class="[
                        'w-full px-4 py-3 text-left text-sm flex items-center gap-3 transition',
                        form.experience_level === option.value ? 'bg-emerald-50 text-emerald-700' : 'text-ink-900 hover:bg-ink-50'
                      ]"
                    >
                      <component :is="MaterialIcon(option.icon, 5)" class="text-ink-400 flex-shrink-0" />
                      <span>{{ option.label }}</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Career Track -->
            <div class="space-y-2">
              <label for="track" class="block text-sm font-semibold text-ink-700">
                Preferred Career Track <span class="text-red-500">*</span>
              </label>
              <div class="relative">
                <div class="absolute left-4 top-1/2 -translate-y-1/2 text-ink-400 pointer-events-none">
                  <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <select
                  id="track"
                  v-model="form.preferred_career_track"
                  required
                  class="w-full pl-12 pr-10 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100 appearance-none cursor-pointer"
                >
                  <option disabled value="">Select your track...</option>
                  <option v-for="track in tracks" :key="track" :value="track">{{ track }}</option>
                </select>
                <div class="absolute right-4 top-1/2 -translate-y-1/2 text-ink-400 pointer-events-none">
                  <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                  </svg>
                </div>
              </div>
            </div>

            <!-- Skills -->
            <div class="space-y-2">
              <label for="skills" class="block text-sm font-semibold text-ink-700">
                Key Skills <span class="text-ink-400 text-xs font-normal">(Optional)</span>
              </label>
              <div class="relative">
                <div class="absolute left-4 top-4 text-ink-400">
                  <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                  </svg>
                </div>
                <textarea
                  id="skills"
                  v-model="skillsInput"
                  rows="2"
                  class="w-full pl-12 pr-4 py-3.5 rounded-xl border-2 border-ink-200 bg-white text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100 resize-none"
                  placeholder="JavaScript, Python, Communication, Problem Solving..."
                ></textarea>
              </div>
              <p class="text-xs text-ink-500">Separate skills with commas</p>
            </div>

            <!-- Error Message -->
            <div v-if="auth.error" class="rounded-xl border-2 border-red-200 bg-red-50 p-4 flex items-start gap-3">
              <svg class="h-5 w-5 text-red-600 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <div class="flex-1">
                <p class="text-sm font-semibold text-red-900">Registration failed</p>
                <p class="text-sm text-red-700">{{ auth.error }}</p>
              </div>
            </div>

            <!-- Terms Checkbox -->
            <div class="flex items-start gap-3">
              <input
                id="terms"
                v-model="acceptedTerms"
                type="checkbox"
                required
                class="mt-1 h-4 w-4 rounded border-ink-300 text-emerald-600 focus:ring-emerald-500 focus:ring-offset-0"
              />
              <label for="terms" class="text-sm text-ink-600">
                I agree to the <a href="/terms" class="text-emerald-600 hover:text-emerald-700 font-medium">Terms of Service</a> and <a href="/privacy" class="text-emerald-600 hover:text-emerald-700 font-medium">Privacy Policy</a>
              </label>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="auth.loading || !acceptedTerms"
              class="w-full inline-flex items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 px-6 py-4 text-base font-semibold text-white shadow-lg shadow-emerald-500/30 transition-all hover:from-emerald-600 hover:to-emerald-700 hover:scale-[1.02] hover:shadow-xl hover:shadow-emerald-500/40 disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:scale-100"
            >
              <span v-if="auth.loading" class="h-5 w-5 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <svg v-else class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              <span>{{ auth.loading ? 'Creating your account...' : 'Create My Account' }}</span>
            </button>
          </form>

          <!-- Divider -->
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-ink-200"></div>
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-4 bg-white text-ink-500 font-medium">Already have an account?</span>
            </div>
          </div>

          <!-- Sign In Link -->
          <NuxtLink
            to="/login"
            class="w-full inline-flex items-center justify-center gap-2 rounded-xl border-2 border-emerald-300 px-6 py-4 text-base font-semibold text-emerald-700 transition-all hover:bg-emerald-50 hover:border-emerald-400 hover:scale-[1.02]"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
            </svg>
            <span>Sign in instead</span>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, h, computed } from 'vue'
import { useRouter, useRoute, definePageMeta } from '#imports'
import { useAuthStore, type ExperienceLevel, type RegisterPayload } from '~/stores/auth'
import { mdiSchool, mdiRocketLaunch, mdiBriefcase } from '@mdi/js'
import { onClickOutside } from '@vueuse/core'

definePageMeta({
  middleware: 'guest',
  layout: 'public'
})

const tracks = ['Web Development', 'Data & Analytics', 'Design', 'Marketing', 'Product', 'Cybersecurity']
const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const form = reactive({
  full_name: '',
  email: '',
  password: '',
  education_level: '',
  preferred_career_track: '',
  experience_level: 'student' as ExperienceLevel
})

const skillsInput = ref('')
const showPassword = ref(false)
const acceptedTerms = ref(false)
const currentYear = new Date().getFullYear()
const showExperienceDropdown = ref(false)
const experienceDropdownRef = ref<HTMLElement | null>(null)

onClickOutside(experienceDropdownRef, () => {
  showExperienceDropdown.value = false
})

const experienceOptions = [
  { value: 'student', label: 'Student', icon: mdiSchool },
  { value: 'entry', label: 'Entry Level', icon: mdiRocketLaunch },
  { value: 'junior', label: 'Junior (1-3 years)', icon: mdiBriefcase }
]

const selectedExperience = computed(() => {
  const found = experienceOptions.find(opt => opt.value === form.experience_level)
  if (found) return found
  return experienceOptions[0]
})

const MaterialIcon = (path: string, size = 5) => {
  return h('svg', {
    class: `h-${size} w-${size}`,
    viewBox: '0 0 24 24',
    fill: 'currentColor'
  }, [
    h('path', { d: path })
  ])
}

const benefits = [
  'Free forever - no hidden costs',
  'AI-powered job matching',
  'Personalized learning paths',
  'Expert career guidance',
  'Connect with mentors'
]

const stats = [
  { value: '2.5k+', label: 'Users' },
  { value: '1.8k+', label: 'Jobs' },
  { value: '94%', label: 'Success' }
]

const handleSubmit = async () => {
  if (!acceptedTerms.value) {
    return
  }

  const skills = skillsInput.value
    .split(',')
    .map((skill) => skill.trim())
    .filter((skill) => Boolean(skill))

  const payload: RegisterPayload = {
    full_name: form.full_name,
    email: form.email,
    password: form.password,
    education_level: form.education_level,
    preferred_career_track: form.preferred_career_track,
    skills: skills.length ? skills : undefined
  }

  const success = await auth.register(payload)
  if (success) {
    if (form.experience_level) {
      await auth.updateProfile({ experience_level: form.experience_level })
    }
    const redirect = typeof route.query.redirect === 'string' ? route.query.redirect : '/dashboard'
    await router.push(redirect)
  }
}
</script>
