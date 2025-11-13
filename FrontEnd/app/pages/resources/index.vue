<template>
  <div class="relative bg-gradient-to-br from-ink-50 via-white to-emerald-50/30 min-h-screen py-8">
    <div class="mx-auto flex max-w-7xl flex-col gap-8 px-4 sm:px-6 lg:px-8">
      <!-- Header Section -->
      <header class="space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-4">
          <div class="space-y-3">
            <div class="flex items-center gap-4">
              <GradientIcon size="lg" color="brand">
                <svg class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </GradientIcon>
              <div>
                <p class="text-xs font-bold uppercase tracking-wider text-brand-600">Learning Hub</p>
                <h1 class="font-display text-4xl font-bold text-ink-900 tracking-tight">Skill Development</h1>
              </div>
            </div>
            <p class="text-base text-ink-600 max-w-3xl leading-relaxed">
              Access curated courses, tutorials, and learning materials designed to boost your skills and accelerate your career growth.
            </p>
          </div>
          
          <!-- Results Count -->
          <div class="flex items-center gap-3">
            <div class="px-4 py-2 bg-white rounded-xl border border-ink-200 shadow-sm">
              <p class="text-sm">
                <span class="font-bold text-emerald-600">{{ filteredResources.length }}</span>
                <span class="text-ink-500"> {{ filteredResources.length === 1 ? 'resource' : 'resources' }}</span>
              </p>
            </div>
          </div>
        </div>
      </header>

      <!-- Filters Section -->
      <section class="bg-white rounded-2xl border border-ink-100 shadow-lg p-6" style="box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08), 0 2px 8px rgba(0, 0, 0, 0.04)">
        <form class="space-y-6" @submit.prevent="handleFilter">
          <!-- Search Row -->
          <div class="grid gap-4 md:grid-cols-12">
            <div class="md:col-span-6 space-y-2">
              <label for="keyword" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                Search
              </label>
              <div class="relative">
                <input
                  id="keyword"
                  v-model="filters.keyword"
                  type="text"
                  class="w-full rounded-xl border border-ink-200 bg-white pl-11 pr-4 py-3 text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
                  placeholder="Course title, topic, or keyword..."
                />
                <svg class="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-ink-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
            </div>

            <div class="md:col-span-3 space-y-2">
              <label for="category" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                </svg>
                Category
              </label>
              <select
                id="category"
                v-model="filters.category"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
              >
                <option value="">All Categories</option>
                <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
              </select>
            </div>

            <div class="md:col-span-3 space-y-2">
              <label for="skill" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                </svg>
                Skill Tag
              </label>
              <input
                id="skill"
                v-model="filters.skill"
                type="text"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
                placeholder="e.g., JavaScript, Design"
              />
            </div>
          </div>

          <!-- Additional Filters Row -->
          <div class="grid gap-4 md:grid-cols-3">
            <div class="space-y-2">
              <label for="cost" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Cost
              </label>
              <select
                id="cost"
                v-model="filters.cost"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
              >
                <option value="">All</option>
                <option value="free">Free Only</option>
                <option value="paid">Paid Only</option>
              </select>
            </div>

            <div class="space-y-2">
              <label for="platform" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Platform
              </label>
              <select
                id="platform"
                v-model="filters.platform"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 transition focus:border-emerald-400 focus:outline-none focus:ring-4 focus:ring-emerald-100"
              >
                <option value="">All Platforms</option>
                <option v-for="plat in platforms" :key="plat" :value="plat">{{ plat }}</option>
              </select>
            </div>

            <div class="space-y-2">
              <label class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                </svg>
                Quick Filters
              </label>
              <div class="flex flex-wrap gap-2">
                <button
                  type="button"
                  :class="[
                    'px-3 py-1.5 text-xs font-medium rounded-lg transition-all',
                    filters.cost === 'free' 
                      ? 'bg-emerald-500 text-white shadow-md' 
                      : 'bg-ink-100 text-ink-700 hover:bg-ink-200'
                  ]"
                  @click="filters.cost = filters.cost === 'free' ? '' : 'free'"
                >
                  Free Only
                </button>
                <button
                  type="button"
                  :class="[
                    'px-3 py-1.5 text-xs font-medium rounded-lg transition-all',
                    filters.category === 'Programming' 
                      ? 'bg-emerald-500 text-white shadow-md' 
                      : 'bg-ink-100 text-ink-700 hover:bg-ink-200'
                  ]"
                  @click="filters.category = filters.category === 'Programming' ? '' : 'Programming'"
                >
                  Programming
                </button>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex flex-wrap items-center gap-3 pt-2">
            <button
              type="submit"
              :disabled="pending"
              class="inline-flex items-center gap-2 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-emerald-500/30 transition-all hover:from-emerald-600 hover:to-emerald-700 hover:scale-105 hover:shadow-xl hover:shadow-emerald-500/40 disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:scale-100"
            >
              <span v-if="pending" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <svg v-else class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
              </svg>
              <span>{{ pending ? 'Filtering...' : 'Apply Filters' }}</span>
            </button>
            <button
              type="button"
              class="inline-flex items-center gap-2 rounded-xl border-2 border-ink-200 px-6 py-3 text-sm font-semibold text-ink-700 transition-all hover:border-emerald-300 hover:text-emerald-600 hover:bg-emerald-50"
              @click="resetFilters"
            >
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              Clear All
            </button>
            <div v-if="hasActiveFilters" class="ml-auto text-sm text-ink-500">
              <span class="inline-flex items-center gap-2 px-3 py-1.5 bg-emerald-50 text-emerald-700 rounded-lg">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                </svg>
                {{ activeFiltersCount }} filter(s) active
              </span>
            </div>
          </div>
        </form>
      </section>

      <!-- Resources Grid -->
      <section class="space-y-4">
        <!-- Loading State -->
        <div v-if="pending" class="grid gap-4 lg:grid-cols-2 xl:grid-cols-3">
          <div v-for="i in 9" :key="i" class="bg-white rounded-2xl border border-ink-100 p-6 animate-pulse">
            <div class="space-y-4">
              <div class="h-40 bg-ink-200 rounded-xl"></div>
              <div class="space-y-3">
                <div class="h-5 bg-ink-200 rounded w-3/4"></div>
                <div class="h-4 bg-ink-200 rounded w-full"></div>
                <div class="h-4 bg-ink-200 rounded w-5/6"></div>
                <div class="flex gap-2 pt-2">
                  <div class="h-6 w-16 bg-ink-200 rounded-full"></div>
                  <div class="h-6 w-20 bg-ink-200 rounded-full"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Resources List -->
        <div v-else-if="filteredResources.length" class="grid gap-4 lg:grid-cols-2 xl:grid-cols-3">
          <CourseCard
            v-for="resource in filteredResources"
            :key="resource.id"
            :resource="resource as any"
            class="hover:shadow-xl transition-all duration-300"
            @view="handleViewResource"
          />
        </div>

        <!-- Empty State -->
        <div v-else class="flex flex-col items-center justify-center py-16 px-6">
          <div class="h-24 w-24 rounded-full bg-emerald-100 flex items-center justify-center mb-6">
            <svg class="h-12 w-12 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-ink-900 mb-2">No resources found</h3>
          <p class="text-sm text-ink-500 text-center max-w-md mb-6">
            We couldn't find any learning resources matching your criteria. Try adjusting your filters or exploring different topics.
          </p>
          <button
            @click="resetFilters"
            class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-500 text-white rounded-xl hover:bg-emerald-600 transition-colors"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Clear All Filters
          </button>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, onMounted } from 'vue'
import { definePageMeta, useAsyncData, useRoute } from '#imports'
import { useApi } from '~/composables/useApi'
import CourseCard from '~/components/features/CourseCard.vue'
import GradientIcon from '~/components/ui/GradientIcon.vue'

definePageMeta({
  middleware: 'auth'
})

interface ResourceResponse {
  id: string
  name: string
  description: string
  url: string
  platform?: string
  tags: string[]
}

const api = useApi()
const route = useRoute()

const filters = reactive({
  keyword: '',
  cost: '',
  skill: '',
  category: '',
  platform: ''
})

// Define categories and platforms
const categories = [
  'Programming',
  'Design',
  'Business',
  'Marketing',
  'Data Science',
  'Personal Development',
  'Communication'
]

const platforms = [
  'Coursera',
  'Udemy',
  'edX',
  'YouTube',
  'freeCodeCamp',
  'Codecademy',
  'LinkedIn Learning'
]

onMounted(() => {
  if (route.query.skill && typeof route.query.skill === 'string') {
    filters.skill = route.query.skill
  }
})

const handleViewResource = (resource: ResourceResponse) => {
  window.open(resource.url, '_blank', 'noopener,noreferrer')
}

const { data, pending, refresh } = await useAsyncData('resources-list', () =>
  api<ResourceResponse[]>('/resources/', { query: { limit: 200 } }),
  { server: false }
)

const resources = computed(() => data.value ?? [])

const filteredResources = computed(() => {
  const keyword = filters.keyword.trim().toLowerCase()
  const skill = filters.skill.trim().toLowerCase()
  const cost = filters.cost
  const category = filters.category
  const platform = filters.platform

  return resources.value.filter((resource) => {
    const matchesKeyword = keyword
      ? resource.name.toLowerCase().includes(keyword) || resource.description.toLowerCase().includes(keyword)
      : true

    const matchesSkill = skill ? resource.tags?.some((tag) => tag.toLowerCase().includes(skill)) : true

    const matchesCost = cost ? resource.tags?.some((tag) => tag.toLowerCase() === cost) : true

    const matchesCategory = category ? resource.tags?.some((tag) => tag.toLowerCase().includes(category.toLowerCase())) : true

    const matchesPlatform = platform ? resource.platform?.toLowerCase() === platform.toLowerCase() : true

    return matchesKeyword && matchesSkill && matchesCost && matchesCategory && matchesPlatform
  })
})

// Check if any filters are active
const hasActiveFilters = computed(() => {
  return !!(filters.keyword || filters.cost || filters.skill || filters.category || filters.platform)
})

// Count active filters
const activeFiltersCount = computed(() => {
  let count = 0
  if (filters.keyword) count++
  if (filters.cost) count++
  if (filters.skill) count++
  if (filters.category) count++
  if (filters.platform) count++
  return count
})

const handleFilter = async () => {
  await refresh()
}

const resetFilters = async () => {
  filters.keyword = ''
  filters.cost = ''
  filters.skill = ''
  filters.category = ''
  filters.platform = ''
  await refresh()
}

const costLabel = (resource: ResourceResponse) => {
  const tag = resource.tags?.find((item) => item.toLowerCase() === 'free' || item.toLowerCase() === 'paid')
  if (!tag) return 'Cost varies'
  return tag.toLowerCase() === 'free' ? 'Free' : 'Paid'
}
</script>
