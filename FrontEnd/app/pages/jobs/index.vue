<template>
  <div class="relative bg-gradient-to-br from-ink-50 via-white to-brand-50/30 min-h-screen py-8">
    <!-- Notification Popup -->
    <Transition name="popup">
      <div
        v-if="showNotification"
        class="fixed top-4 right-4 z-50 max-w-md rounded-lg shadow-lg p-4"
        :class="notificationType === 'success' ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'"
      >
        <div class="flex items-start gap-3">
          <div v-if="notificationType === 'success'" class="flex-shrink-0">
            <svg class="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div v-else class="flex-shrink-0">
            <svg class="h-5 w-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div class="flex-1">
            <p
              class="text-sm font-medium"
              :class="notificationType === 'success' ? 'text-green-800' : 'text-red-800'"
            >
              {{ notificationMessage }}
            </p>
          </div>
          <button
            @click="showNotification = false"
            class="flex-shrink-0 text-ink-400 hover:text-ink-600 transition-colors"
          >
            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </Transition>
    <div class="mx-auto flex max-w-7xl flex-col gap-8 px-4 sm:px-6 lg:px-8">
      <!-- Header Section -->
      <header class="space-y-4">
        <div class="flex items-center justify-between flex-wrap gap-4">
          <div class="space-y-3">
            <div class="flex items-center gap-4">
              <GradientIcon size="lg" color="brand">
                <svg class="h-7 w-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </GradientIcon>
              <div>
                <p class="text-xs font-bold uppercase tracking-wider text-brand-600">Opportunity Catalog</p>
                <h1 class="font-display text-4xl font-bold text-ink-900 tracking-tight">Find Your Perfect Job</h1>
              </div>
            </div>
            <p class="text-base text-ink-600 max-w-3xl leading-relaxed">
              Discover internships, entry-level positions, and freelance opportunities perfectly matched to your skills and career aspirations.
            </p>
          </div>
          
          <!-- Results Count & Sort -->
          <div class="flex items-center gap-3">
            <div class="px-4 py-2 bg-white rounded-xl border border-ink-200 shadow-sm">
              <p class="text-sm">
                <span class="font-bold text-brand-600">{{ jobs.length }}</span>
                <span class="text-ink-500"> {{ jobs.length === 1 ? 'job' : 'jobs' }} found</span>
              </p>
            </div>
          </div>
        </div>
      </header>

      <!-- Filters & Sorting Section -->
      <section class="bg-white rounded-2xl border border-ink-100 shadow-lg p-6" style="box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08), 0 2px 8px rgba(0, 0, 0, 0.04)">
        <form class="space-y-6" @submit.prevent="handleSearch">
          <!-- Search & Sort Row -->
          <div class="grid gap-4 md:grid-cols-12">
            <div class="md:col-span-6 space-y-2">
              <label for="search" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                Search
              </label>
              <div class="relative">
                <input
                  id="search"
                  v-model="filters.search"
                  type="text"
                  class="w-full rounded-xl border border-ink-200 bg-white pl-11 pr-4 py-3 text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
                  placeholder="Job title, company, or keyword..."
                />
                <svg class="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-ink-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
            </div>

            <div class="md:col-span-3 space-y-2">
              <label for="sort" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4h13M3 8h9m-9 4h6m4 0l4-4m0 0l4 4m-4-4v12" />
                </svg>
                Sort by
              </label>
              <select
                id="sort"
                v-model="sortBy"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
              >
                <option value="relevance">Best Match</option>
                <option value="recent">Most Recent</option>
                <option value="title">Title (A-Z)</option>
                <option value="company">Company (A-Z)</option>
              </select>
            </div>

            <div class="md:col-span-3 space-y-2">
              <label for="skills" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                </svg>
                Skills
              </label>
              <input
                id="skills"
                v-model="filters.skills"
                type="text"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 placeholder:text-ink-400 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
                placeholder="e.g., JavaScript, Design"
              />
            </div>
          </div>

          <!-- Filters Row -->
          <div class="grid gap-4 md:grid-cols-3">
            <div class="space-y-2">
              <label for="job_type" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Job Type
              </label>
              <select
                id="job_type"
                v-model="filters.job_type"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
              >
                <option value="">All Types</option>
                <option v-for="type in jobTypes" :key="type" :value="type">{{ capitalize(type) }}</option>
              </select>
            </div>

            <div class="space-y-2">
              <label for="experience_level" class="text-xs font-semibold uppercase tracking-wider text-ink-500 flex items-center gap-2">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
                Experience Level
              </label>
              <select
                id="experience_level"
                v-model="filters.experience_level"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-4 focus:ring-brand-100"
              >
                <option value="">All Levels</option>
                <option v-for="level in experienceLevels" :key="level" :value="level">{{ experienceLabel(level) }}</option>
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
                    filters.skills.includes('Remote') 
                      ? 'bg-brand-500 text-white shadow-md' 
                      : 'bg-ink-100 text-ink-700 hover:bg-ink-200'
                  ]"
                  @click="toggleQuickFilter('Remote')"
                >
                  Remote
                </button>
                <button
                  type="button"
                  :class="[
                    'px-3 py-1.5 text-xs font-medium rounded-lg transition-all',
                    filters.job_type === 'internship'
                      ? 'bg-brand-500 text-white shadow-md' 
                      : 'bg-ink-100 text-ink-700 hover:bg-ink-200'
                  ]"
                  @click="filters.job_type = filters.job_type === 'internship' ? '' : 'internship'"
                >
                  Internships Only
                </button>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex flex-wrap items-center gap-3 pt-2">
            <button
              type="submit"
              :disabled="pending"
              class="inline-flex items-center gap-2 rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-brand-500/30 transition-all hover:from-brand-600 hover:to-brand-700 hover:scale-105 hover:shadow-xl hover:shadow-brand-500/40 disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:scale-100"
            >
              <span v-if="pending" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <svg v-else class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <span>{{ pending ? 'Searching...' : 'Apply Filters' }}</span>
            </button>
            <button
              type="button"
              class="inline-flex items-center gap-2 rounded-xl border-2 border-ink-200 px-6 py-3 text-sm font-semibold text-ink-700 transition-all hover:border-brand-300 hover:text-brand-600 hover:bg-brand-50"
              @click="resetFilters"
            >
              <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              Clear All
            </button>
            <div v-if="hasActiveFilters" class="ml-auto text-sm text-ink-500">
              <span class="inline-flex items-center gap-2 px-3 py-1.5 bg-brand-50 text-brand-700 rounded-lg">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                </svg>
                {{ activeFiltersCount }} filter(s) active
              </span>
            </div>
          </div>
        </form>
      </section>

      <!-- Jobs Grid -->
      <section class="space-y-4">
        <!-- Error State -->
        <div v-if="fetchError" class="flex flex-col items-center justify-center py-16 px-6">
          <div class="h-24 w-24 rounded-full bg-red-100 flex items-center justify-center mb-6">
            <svg class="h-12 w-12 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-ink-900 mb-2">Failed to load jobs</h3>
          <p class="text-sm text-ink-500 text-center max-w-md mb-6">
            There was an error loading job listings. Please check your connection and try again.
          </p>
          <button
            @click="refresh()"
            class="inline-flex items-center gap-2 px-6 py-3 bg-brand-500 text-white rounded-xl hover:bg-brand-600 transition-colors"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Try Again
          </button>
        </div>
        
        <!-- Loading State -->
        <div v-else-if="pending" class="grid gap-4 lg:grid-cols-2">
          <div v-for="i in 6" :key="i" class="bg-white rounded-2xl border border-ink-100 p-6 animate-pulse">
            <div class="flex items-start gap-4">
              <div class="h-14 w-14 bg-ink-200 rounded-xl"></div>
              <div class="flex-1 space-y-3">
                <div class="h-5 bg-ink-200 rounded w-3/4"></div>
                <div class="h-4 bg-ink-200 rounded w-1/2"></div>
                <div class="flex gap-2">
                  <div class="h-6 w-16 bg-ink-200 rounded"></div>
                  <div class="h-6 w-20 bg-ink-200 rounded"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Jobs List -->
        <div v-else-if="sortedJobs.length" class="grid gap-4 lg:grid-cols-2">
          <JobCard
            v-for="job in sortedJobs"
            :key="job.id"
            :job="job as any"
            :user-skills="auth.user?.skills || []"
            class="cursor-pointer hover:shadow-xl transition-all duration-300"
            @click="navigateToJob(job.id)"
            @applied="handleApplied"
            @apply-error="handleApplyError"
          />
        </div>

        <!-- Empty State -->
        <div v-else class="flex flex-col items-center justify-center py-16 px-6">
          <div class="h-24 w-24 rounded-full bg-ink-100 flex items-center justify-center mb-6">
            <svg class="h-12 w-12 text-ink-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-ink-900 mb-2">No jobs found</h3>
          <p class="text-sm text-ink-500 text-center max-w-md mb-6">
            We couldn't find any jobs matching your criteria. Try adjusting your filters or broadening your search.
          </p>
          <button
            @click="resetFilters"
            class="inline-flex items-center gap-2 px-6 py-3 bg-brand-500 text-white rounded-xl hover:bg-brand-600 transition-colors"
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
import { reactive, computed, ref, watch } from 'vue'
import { definePageMeta, useAsyncData, useRouter } from '#imports'
import { useAuthStore, type ExperienceLevel, type JobType } from '~/stores/auth'
import { useApi } from '~/composables/useApi'
import JobCard from '~/components/features/JobCard.vue'
import GradientIcon from '~/components/ui/GradientIcon.vue'

definePageMeta({
  middleware: 'auth'
})

interface JobResponse {
  id: string
  title: string
  description: string
  company: string
  job_type: JobType
  job_location?: 'remote' | 'hybrid' | 'on_site' | null
  required_skills: string[]
  url?: string | null
  recommended_experience_level: ExperienceLevel
  salary_range_min?: number | null
  salary_range_max?: number | null
  created_at?: string
  updated_at?: string
}

const jobTypes: JobType[] = ['internship', 'part_time', 'full_time', 'freelance']
const experienceLevels: ExperienceLevel[] = ['student', 'entry', 'junior']

const auth = useAuthStore()
const api = useApi()
const router = useRouter()

await auth.fetchProfile()

const navigateToJob = (jobId: string) => {
  router.push(`/jobs/${jobId}`)
}

// Notification popup
const showNotification = ref(false)
const notificationMessage = ref('')
const notificationType = ref<'success' | 'error'>('success')

const showNotificationPopup = (message: string, type: 'success' | 'error') => {
  notificationMessage.value = message
  notificationType.value = type
  showNotification.value = true
  setTimeout(() => {
    showNotification.value = false
  }, 5000)
}

const handleApplied = (job: JobResponse) => {
  showNotificationPopup(`Application submitted successfully for ${job.title}!`, 'success')
}

const handleApplyError = (job: JobResponse, error: string) => {
  showNotificationPopup(error, 'error')
}

const filters = reactive({
  search: '',
  job_type: '',
  experience_level: '',
  skills: ''
})

const sortBy = ref<'relevance' | 'recent' | 'title' | 'company'>('relevance')

const fetchJobs = async () => {
  try {
    const query: Record<string, any> = { 
      skip: 0,
      limit: 100 
    }
    
    // Add job_type filter if provided
    if (filters.job_type) {
      query.job_type = filters.job_type
    }
    
    // Add experience_level filter if provided
    if (filters.experience_level) {
      query.experience_level = filters.experience_level
    }

    // Add skills filter if provided (comma-separated string)
    const skillsInput = filters.skills.trim()
    if (skillsInput) {
      query.skills = skillsInput
    }

    console.log('Fetching jobs with query:', query)
    const response = await api<JobResponse[]>('/jobs/', { query })
    console.log('Jobs fetched:', response?.length || 0)
    return response || []
  } catch (error) {
    console.error('Error fetching jobs:', error)
    return []
  }
}

const { data, pending, refresh, error: fetchError } = await useAsyncData('jobs-listing', fetchJobs, {
  server: false,
  default: () => []
})

interface JobRecommendation {
  job: JobResponse
  similarity_score: number
}

const { data: recommendationsData, refresh: refreshRecommendations } = await useAsyncData(
  'job-recommendations',
  () => api<JobRecommendation[]>('/recommendations/jobs', { query: { limit: 100 } }),
  { server: false, default: () => [] }
)

const jobs = computed(() => {
  const list = data.value ?? []
  if (!filters.search.trim()) {
    return list
  }
  const keyword = filters.search.trim().toLowerCase()
  return list.filter((job) =>
    job.title.toLowerCase().includes(keyword) || job.company.toLowerCase().includes(keyword)
  )
})

// Sorted jobs based on selected sort option
const sortedJobs = computed(() => {
  // If relevance sort is selected, use recommendations from backend
  if (sortBy.value === 'relevance' && recommendationsData.value?.length) {
    const recommendedJobs = recommendationsData.value
      .map(rec => rec.job)
      .filter(job => {
        // Apply search filter if active
        if (filters.search.trim()) {
          const keyword = filters.search.trim().toLowerCase()
          if (!job.title.toLowerCase().includes(keyword) && 
              !job.company.toLowerCase().includes(keyword)) {
            return false
          }
        }
        return true
      })
    
    const recommendedJobIds = new Set(recommendedJobs.map(j => j.id))
    
    // Merge recommended jobs with other filtered jobs, prioritizing recommendations
    const otherJobs = jobs.value.filter(j => !recommendedJobIds.has(j.id))
    return [...recommendedJobs, ...otherJobs]
  }
  
  // For other sorts, use regular jobs list
  const jobsList = [...jobs.value]
  
  switch (sortBy.value) {
    case 'recent':
      return jobsList
    case 'title':
      return jobsList.sort((a, b) => a.title.localeCompare(b.title))
    case 'company':
      return jobsList.sort((a, b) => a.company.localeCompare(b.company))
    default:
      return jobsList
  }
})

// Watch sortBy to refresh recommendations when switching to relevance
watch(sortBy, async (newValue) => {
  if (newValue === 'relevance') {
    await refreshRecommendations()
  }
})

// Check if any filters are active
const hasActiveFilters = computed(() => {
  return !!(filters.search || filters.job_type || filters.experience_level || filters.skills)
})

// Count active filters
const activeFiltersCount = computed(() => {
  let count = 0
  if (filters.search) count++
  if (filters.job_type) count++
  if (filters.experience_level) count++
  if (filters.skills) count++
  return count
})

const handleSearch = async () => {
  await refresh()
}

const resetFilters = async () => {
  filters.search = ''
  filters.job_type = ''
  filters.experience_level = ''
  filters.skills = ''
  sortBy.value = 'relevance'
  await refresh()
}

const toggleQuickFilter = (filterValue: string) => {
  const currentSkills = filters.skills.split(',').map(s => s.trim()).filter(Boolean)
  const index = currentSkills.indexOf(filterValue)
  
  if (index > -1) {
    currentSkills.splice(index, 1)
  } else {
    currentSkills.push(filterValue)
  }
  
  filters.skills = currentSkills.join(', ')
}

const experienceLabel = (value: ExperienceLevel | '') => {
  const mapping: Record<string, string> = {
    student: 'Student',
    entry: 'Entry-level',
    junior: 'Junior'
  }
  return mapping[value] || 'Any'
}

const capitalize = (value: string | null | undefined) => {
  if (!value) return 'Unknown'
  return value.charAt(0).toUpperCase() + value.slice(1)
}

</script>

<style scoped>
.popup-enter-active,
.popup-leave-active {
  transition: all 0.3s ease;
}

.popup-enter-from {
  opacity: 0;
  transform: translateX(100%);
}

.popup-leave-to {
  opacity: 0;
  transform: translateX(100%);
}
</style>
