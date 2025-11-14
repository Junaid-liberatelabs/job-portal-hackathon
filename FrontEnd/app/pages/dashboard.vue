<template>
  <div class="relative bg-ink-50 min-h-screen py-8">
    <div class="mx-auto flex max-w-7xl flex-col gap-8 px-4 sm:px-6 lg:px-8">
      <!-- Welcome Header -->
      <div class="space-y-2">
        <h1 class="font-display text-3xl font-bold text-ink-900">
          Welcome back!
        </h1>
        <p class="text-ink-600">Here's your personalized career dashboard</p>
      </div>

      <!-- Profile Completion Banner -->
      <div v-if="profileCompletion < 100" class="rounded-2xl border border-amber-200 bg-amber-50 p-6">
        <div class="flex items-start gap-4">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div class="flex-1">
            <h3 class="font-semibold text-amber-900">Complete your profile</h3>
            <p class="mt-1 text-sm text-amber-800">Your profile is {{ profileCompletion }}% complete. Add more information to get better job matches.</p>
            <div class="mt-3 flex items-center gap-4">
              <div class="flex-1 h-2 bg-amber-200 rounded-full overflow-hidden">
                <div class="h-full bg-amber-500 transition-all duration-500" :style="{ width: `${profileCompletion}%` }"></div>
              </div>
              <NuxtLink to="/profile" class="text-sm font-semibold text-amber-700 hover:text-amber-800">
                Complete Profile →
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>

      <!-- Stats Cards with Smooth Animations -->
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div class="group rounded-2xl border border-ink-100 bg-white p-6 shadow-md hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Skills Added</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ auth.user?.skills?.length || 0 }}</p>
              <p class="mt-1 text-xs text-ink-400">+2 this week</p>
            </div>
            <GradientIcon size="md" color="brand">
              <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
              </svg>
            </GradientIcon>
          </div>
        </div>

        <div class="group rounded-2xl border border-ink-100 bg-white p-6 shadow-md hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Jobs Matched</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ statsData.jobs_matched }}</p>
              <p class="mt-1 text-xs text-ink-400">Based on your skills</p>
            </div>
            <GradientIcon size="md" color="brand">
              <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </GradientIcon>
          </div>
        </div>

        <div class="group rounded-2xl border border-ink-100 bg-white p-6 shadow-md hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Resources Found</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ statsData.resources_found }}</p>
              <p class="mt-1 text-xs text-ink-400">Tailored for you</p>
            </div>
            <GradientIcon size="md" color="brand">
              <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </GradientIcon>
          </div>
        </div>

        <div class="group rounded-2xl border border-ink-100 bg-white p-6 shadow-md hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Bookmarked</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ statsData.bookmarked_count }}</p>
              <p class="mt-1 text-xs text-ink-400">Saved resources</p>
            </div>
            <GradientIcon size="md" color="brand">
              <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
              </svg>
            </GradientIcon>
          </div>
        </div>
      </div>

      <!-- Skill Match Analysis -->
      <div class="rounded-2xl border border-white/70 bg-white p-8 shadow-sm">
        <div class="flex items-center justify-between mb-8">
          <div>
            <h2 class="font-display text-xl font-semibold text-ink-900">Skill Visualization</h2>
            <p class="mt-1 text-sm text-ink-600">Your skills overview</p>
          </div>
          <NuxtLink to="/profile?tab=skills" class="text-sm font-semibold text-brand-600 hover:text-brand-700 transition-colors">
            Manage Skills →
          </NuxtLink>
        </div>

        <div v-if="auth.user?.skills && auth.user.skills.length > 0">
          <!-- Chart Container -->
          <div class="w-full" style="height: 550px;">
            <SkillChart
              :skills="skillsForChart"
              chart-type="pie"
              :height="550"
            />
          </div>
        </div>

        <div v-else class="py-12 text-center">
          <svg class="mx-auto h-12 w-12 text-ink-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <p class="mt-4 text-sm text-ink-600">No skills added yet</p>
          <NuxtLink to="/profile?tab=skills" class="mt-2 inline-flex items-center text-sm font-semibold text-brand-600 hover:text-brand-700">
            Add your first skill →
          </NuxtLink>
        </div>
      </div>

      <!-- Recommended Jobs -->
      <div class="space-y-6">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="font-display text-2xl font-semibold text-ink-900">Recommended Jobs</h2>
            <p class="mt-1 text-sm text-ink-600">{{ scoredJobs.length }} jobs matched to your skills</p>
          </div>
          <NuxtLink to="/jobs" class="text-sm font-semibold text-brand-600 hover:text-brand-700 transition-colors">
            View All →
          </NuxtLink>
        </div>
        <div class="grid gap-6 sm:grid-cols-2">
          <div
            v-for="(job, index) in recommendedJobs"
            :key="job.id"
            :ref="el => jobCardRefs[index] = el as HTMLElement"
            class="opacity-0 translate-y-8 transition-all duration-700"
            :style="{ transitionDelay: `${index * 100}ms` }"
          >
            <JobCard
              :job="job as any"
              :user-skills="auth.user?.skills || []"
              @click="navigateToJob(job.id)"
            />
          </div>
        </div>
        <p v-if="!recommendedJobs.length" class="rounded-2xl border border-ink-200 bg-white p-8 text-center text-sm text-ink-600">
          Add more skills to your profile to see personalized job recommendations.
        </p>
      </div>

      <!-- Recommended Learning -->
      <div class="space-y-6">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="font-display text-2xl font-semibold text-ink-900">Recommended Learning</h2>
            <p class="mt-1 text-sm text-ink-600">Courses tailored to boost your career</p>
          </div>
          <NuxtLink to="/resources" class="text-sm font-semibold text-brand-600 hover:text-brand-700 transition-colors">
            View All →
          </NuxtLink>
        </div>
        <div class="grid gap-6 sm:grid-cols-2">
          <div
            v-for="(resource, index) in recommendedResources"
            :key="resource.id"
            :ref="el => resourceCardRefs[index] = el as HTMLElement"
            class="opacity-0 translate-y-8 transition-all duration-700"
            :style="{ transitionDelay: `${index * 100}ms` }"
          >
            <CourseCard
              :resource="resource as any"
              :is-bookmarked="isBookmarked(resource.id)"
              @bookmark="toggleBookmark(resource.id)"
              @view="handleViewResource"
            />
          </div>
        </div>
        <p v-if="!recommendedResources.length" class="rounded-2xl border border-ink-200 bg-white p-8 text-center text-sm text-ink-600">
          Add skills to discover relevant learning resources.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'
import { definePageMeta, useAsyncData, useRouter } from '#imports'
import { useAuthStore, type ExperienceLevel } from '~/stores/auth'
import { useApi } from '~/composables/useApi'
import JobCard from '~/components/features/JobCard.vue'
import CourseCard from '~/components/features/CourseCard.vue'
import SkillChart from '~/components/features/SkillChart.vue'
import GradientIcon from '~/components/ui/GradientIcon.vue'

interface JobResponse {
  id: string
  title: string
  description: string
  company: string
  job_type: string
  job_location?: string | null
  required_skills: string[]
  recommended_experience_level: ExperienceLevel
  salary_range_min?: number | null
  salary_range_max?: number | null
  created_at?: string
  updated_at?: string
}

interface ResourceResponse {
  id: string
  name: string
  description: string
  url: string
  platform?: string
  tags: string[]
  created_at?: string
  updated_at?: string
}

definePageMeta({
  middleware: 'auth'
})

const auth = useAuthStore()
const api = useApi()
const router = useRouter()

await auth.fetchProfile()

const navigateToJob = (jobId: string) => {
  router.push(`/jobs/${jobId}`)
}

const handleViewResource = (resource: ResourceResponse) => {
  window.open(resource.url, '_blank', 'noopener,noreferrer')
}

// Refs for scroll animations
const jobCardRefs = ref<HTMLElement[]>([])
const resourceCardRefs = ref<HTMLElement[]>([])
let observer: IntersectionObserver | null = null

// Chart type for dashboard (only pie chart now)
// const dashboardChartType = ref<'pie' | 'radar' | 'bar'>('pie')

const { data: jobsData } = await useAsyncData('dashboard-jobs', () =>
  api<JobResponse[]>('/jobs/', {
    query: { limit: 50 }
  })
)

const { data: resourcesData } = await useAsyncData('dashboard-resources', () =>
  api<ResourceResponse[]>('/resources/', {
    query: { limit: 50 }
  })
)

const userSkills = computed(() => new Set((auth.user?.skills ?? []).map((skill) => skill.toLowerCase())))

const scoredJobs = computed(() => {
  const jobs = jobsData.value ?? []
  if (!auth.user) return []
  return jobs
    .map((job) => {
      const overlap = job.required_skills.filter((skill) => userSkills.value.has(skill.toLowerCase()))
      return { job, overlap }
    })
    .filter(({ overlap }) => overlap.length > 0)
    .sort((a, b) => b.overlap.length - a.overlap.length)
})

const recommendedJobs = computed(() => scoredJobs.value.slice(0, 4).map((item) => item.job))
const topJob = computed(() => recommendedJobs.value[0])

const scoredResources = computed(() => {
  const resources = resourcesData.value ?? []
  if (!auth.user) return []
  return resources
    .map((resource) => {
      const tags = resource.tags?.map((tag) => tag.toLowerCase()) ?? []
      const overlap = tags.filter((tag) => userSkills.value.has(tag))
      return { resource, overlap }
    })
    .filter(({ overlap }) => overlap.length > 0)
    .sort((a, b) => b.overlap.length - a.overlap.length)
})

const recommendedResources = computed(() => scoredResources.value.slice(0, 4).map((item) => item.resource))
const topResource = computed(() => recommendedResources.value[0])

const experienceLabel = computed(() => {
  const mapping: Record<string, string> = {
    student: 'Student',
    entry: 'Entry-level',
    junior: 'Junior'
  }
  return mapping[auth.user?.experience_level ?? ''] || 'Not provided'
})

const overlapMessage = (job: JobResponse) => {
  const overlap = job.required_skills.filter((skill) => userSkills.value.has(skill.toLowerCase()))
  if (!overlap.length) return 'Review job requirements to plan your next sprint.'
  return `Matches: ${overlap.slice(0, 3).join(', ')}${overlap.length > 3 ? ' +' : ''}`
}

const resourceMessage = (resource: ResourceResponse) => {
  const tags = resource.tags ?? []
  const overlap = tags.filter((tag) => userSkills.value.has(tag.toLowerCase()))
  return overlap.length ? `Supports: ${overlap.join(', ')}` : 'Strengthens adjacent capabilities.'
}

const resourceCost = (resource: ResourceResponse) => {
  const tags = resource.tags ?? []
  const costTag = tags.find((tag) => ['free', 'paid'].includes(tag.toLowerCase()))
  if (!costTag) return 'Varies'
  return costTag.toLowerCase() === 'free' ? 'Free' : 'Paid'
}

const capitalize = (value: string | null | undefined) => {
  if (!value) return 'Unknown'
  return value.charAt(0).toUpperCase() + value.slice(1).toLowerCase()
}

// Profile completion calculation
const profileCompletion = computed(() => {
  if (!auth.user) return 0
  
  let completed = 0
  const total = 7 // Total profile fields to complete
  
  // Core fields (always present after registration)
  if (auth.user.full_name && auth.user.full_name.trim().length > 0) completed++
  if (auth.user.email && auth.user.email.trim().length > 0) completed++
  
  // Profile fields
  if (auth.user.education_level && auth.user.education_level.trim().length > 0) completed++
  if (auth.user.preferred_career_track && auth.user.preferred_career_track.trim().length > 0) completed++
  if (auth.user.experience_level) completed++
  
  // Skills-based completion
  if (auth.user.skills && auth.user.skills.length >= 1) completed++
  if (auth.user.skills && auth.user.skills.length >= 5) completed++ // Bonus for having 5+ skills
  
  return Math.round((completed / total) * 100)
})

// Skills for chart with weighted values
const skillsForChart = computed(() => {
  if (!auth.user?.skills || auth.user.skills.length === 0) return []
  
  // Categorize skills (simplified - you can enhance this with actual categorization logic)
  const getCategoryWeight = (skill: string): number => {
    const skillLower = skill.toLowerCase()
    if (skillLower.includes('javascript') || skillLower.includes('python') || skillLower.includes('java') || skillLower.includes('react') || skillLower.includes('node')) {
      return 85 // Programming
    } else if (skillLower.includes('design') || skillLower.includes('ui') || skillLower.includes('ux') || skillLower.includes('figma')) {
      return 75 // Design
    } else if (skillLower.includes('data') || skillLower.includes('sql') || skillLower.includes('analytics')) {
      return 80 // Data
    } else if (skillLower.includes('marketing') || skillLower.includes('seo') || skillLower.includes('content')) {
      return 70 // Marketing
    }
    return 60 // Other
  }
  
  return auth.user.skills.map((skill, index) => {
    const baseValue = getCategoryWeight(skill)
    const variation = (index % 3) * 10 // Adds 0, 10, or 20 for visual variety
    
    return {
      name: skill,
      value: Math.min(100, baseValue + variation),
      category: 'skill'
    }
  })
})

// Bookmarked resources (client-side storage)
const bookmarkedResources = ref<Set<string>>(new Set())

// Save bookmarks to localStorage
const saveBookmarks = () => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('ci_bookmarked_resources', JSON.stringify(Array.from(bookmarkedResources.value)))
  }
}

// Toggle bookmark
const toggleBookmark = (resourceId: string) => {
  if (bookmarkedResources.value.has(resourceId)) {
    bookmarkedResources.value.delete(resourceId)
  } else {
    bookmarkedResources.value.add(resourceId)
  }
  saveBookmarks()
}

// Check if resource is bookmarked
const isBookmarked = (resourceId: string) => {
  return bookmarkedResources.value.has(resourceId)
}

// Real stats data from actual data
const statsData = computed(() => {
  const skillsCount = auth.user?.skills?.length || 0
  const jobsCount = scoredJobs.value.length
  const resourcesCount = recommendedResources.value.length
  
  return {
    skills_added: skillsCount,
    jobs_matched: jobsCount,
    resources_found: resourcesCount,
    bookmarked_count: bookmarkedResources.value.size
  }
})

// Intersection Observer for scroll animations and load bookmarks
onMounted(() => {
  if (typeof window === 'undefined') return

  // Load bookmarks from localStorage
  const saved = localStorage.getItem('ci_bookmarked_resources')
  if (saved) {
    try {
      const parsed = JSON.parse(saved)
      bookmarkedResources.value = new Set(parsed)
    } catch (e) {
      console.error('Error loading bookmarks:', e)
    }
  }

  // Setup intersection observer for card animations
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('opacity-100', 'translate-y-0')
          entry.target.classList.remove('opacity-0', 'translate-y-8')
          observer?.unobserve(entry.target)
        }
      })
    },
    {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    }
  )

  // Observe all card elements
  ;[...jobCardRefs.value, ...resourceCardRefs.value].forEach((el) => {
    if (el) observer?.observe(el)
  })
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
    observer = null
  }
})
</script>
