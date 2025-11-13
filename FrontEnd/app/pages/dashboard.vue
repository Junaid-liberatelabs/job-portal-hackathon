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
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Jobs Applied</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ statsData.jobs_applied || 8 }}</p>
              <p class="mt-1 text-xs text-ink-400">3 responses</p>
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
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Courses Completed</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ statsData.courses_completed || 5 }}</p>
              <p class="mt-1 text-xs text-ink-400">15 hours learned</p>
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
              <p class="text-sm font-semibold text-ink-500 uppercase tracking-wide">Interviews</p>
              <p class="mt-2 text-4xl font-bold text-brand-600 transition-all duration-300 group-hover:scale-110">{{ statsData.interviews || 3 }}</p>
              <p class="mt-1 text-xs text-ink-400">2 upcoming</p>
            </div>
            <GradientIcon size="md" color="brand">
              <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </GradientIcon>
          </div>
        </div>
      </div>

      <!-- Skill Match Analysis -->
      <div class="rounded-2xl border border-white/70 bg-white p-8 shadow-sm">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h2 class="font-display text-xl font-semibold text-ink-900">Skill Match Analysis</h2>
            <p class="mt-1 text-sm text-ink-600">Your skills vs. market demand</p>
          </div>
          <NuxtLink to="/profile?tab=skills" class="text-sm font-semibold text-brand-600 hover:text-brand-700">
            Manage Skills →
          </NuxtLink>
        </div>
        <SkillChart 
          v-if="auth.user?.skills && auth.user.skills.length > 0"
          :skills="skillsForChart"
          chart-type="pie"
          :height="300"
        />
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
          <NuxtLink to="/jobs" class="text-sm font-semibold text-brand-600 hover:text-brand-700">
            View All →
          </NuxtLink>
        </div>
        <div class="grid gap-6 sm:grid-cols-2">
          <JobCard
            v-for="job in recommendedJobs"
            :key="job.id"
            :job="job as any"
            :user-skills="auth.user?.skills || []"
            @click="navigateToJob(job.id)"
          />
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
          <NuxtLink to="/resources" class="text-sm font-semibold text-brand-600 hover:text-brand-700">
            View All →
          </NuxtLink>
        </div>
        <div class="grid gap-6 sm:grid-cols-2">
          <CourseCard
            v-for="resource in recommendedResources"
            :key="resource.id"
            :resource="resource as any"
            @view="handleViewResource"
          />
        </div>
        <p v-if="!recommendedResources.length" class="rounded-2xl border border-ink-200 bg-white p-8 text-center text-sm text-ink-600">
          Add skills to discover relevant learning resources.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
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
  const total = 10
  
  if (auth.user.full_name) completed++
  if (auth.user.email) completed++
  if (auth.user.education_level) completed++
  if (auth.user.preferred_career_track) completed++
  if (auth.user.experience_level) completed++
  if (auth.user.skills && auth.user.skills.length > 0) completed++
  if (auth.user.skills && auth.user.skills.length >= 3) completed++
  if (auth.user.skills && auth.user.skills.length >= 5) completed++
  completed += 2 // Placeholder for other profile fields
  
  return Math.round((completed / total) * 100)
})

// Skills for chart
const skillsForChart = computed(() => {
  if (!auth.user?.skills) return []
  const skillCounts: Record<string, number> = {}
  auth.user.skills.forEach(skill => {
    skillCounts[skill] = (skillCounts[skill] || 0) + 1
  })
  return Object.entries(skillCounts).map(([name, value]) => ({
    name,
    value,
    category: 'skill'
  }))
})

// Stats data (placeholder - replace with real data from backend)
const statsData = computed(() => ({
  jobs_applied: 8,
  courses_completed: 5,
  interviews: 3
}))
</script>
