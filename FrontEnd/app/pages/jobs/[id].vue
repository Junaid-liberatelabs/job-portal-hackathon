<template>
  <div class="relative bg-ink-50 py-16">
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
    <div class="mx-auto flex max-w-5xl flex-col gap-10 px-6 lg:px-10">
      <div class="flex items-center gap-3">
        <Button variant="outline" size="sm" @click="router.back()">
          <ArrowLeftIcon class="h-4 w-4" />
          Back
        </Button>
      </div>

      <div v-if="pending" class="flex items-center justify-center py-20">
        <div class="h-8 w-8 animate-spin rounded-full border-4 border-brand-200 border-t-brand-600"></div>
      </div>

      <div v-else-if="job" class="space-y-8">
        <Card variant="glass" class="p-8">
          <div class="space-y-6">
            <div class="flex flex-wrap items-start justify-between gap-4">
              <div class="space-y-2">
                <h1 class="font-display text-3xl font-semibold text-ink-900">{{ job.title }}</h1>
                <p class="text-lg text-ink-600">{{ job.company }}</p>
              </div>
              <div class="flex flex-wrap gap-2">
                <span class="rounded-full bg-brand-100 px-4 py-2 text-sm font-semibold text-brand-700">
                  {{ capitalize(job.job_type) }}
                </span>
                <span class="rounded-full bg-emerald-100 px-4 py-2 text-sm font-semibold text-emerald-700">
                  {{ experienceLabel(job.recommended_experience_level) }}
                </span>
              </div>
            </div>

            <div v-if="job.job_location" class="flex items-center gap-2 text-sm text-ink-500">
              <MapPinIcon class="h-5 w-5" />
              {{ job.job_location }}
            </div>

            <div class="space-y-3">
              <h2 class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Description</h2>
              <p class="text-ink-600 leading-relaxed">{{ job.description }}</p>
            </div>

            <div class="space-y-3">
              <h2 class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Required skills</h2>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="skill in job.required_skills"
                  :key="skill"
                  :class="[
                    'rounded-full px-4 py-2 text-sm font-semibold',
                    userHasSkill(skill)
                      ? 'bg-emerald-100 text-emerald-700 ring-2 ring-emerald-200'
                      : 'bg-white text-ink-600 ring-1 ring-ink-200'
                  ]"
                >
                  {{ skill }}
                  <span v-if="userHasSkill(skill)" class="ml-1">✓</span>
                </span>
              </div>
              <p class="text-sm text-ink-500">
                You match {{ matchedSkillsCount }} of {{ job.required_skills.length }} required skills
                <span v-if="matchPercentage >= 70" class="ml-2 font-semibold text-emerald-600">
                  (Strong match!)
                </span>
              </p>
            </div>

            <div v-if="missingSkills.length" class="space-y-3">
              <h2 class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Skills to develop</h2>
              <div class="flex flex-wrap gap-2">
                <NuxtLink
                  v-for="skill in missingSkills"
                  :key="skill"
                  :to="`/resources?skill=${encodeURIComponent(skill)}`"
                  class="rounded-full bg-amber-50 px-4 py-2 text-sm font-semibold text-amber-700 ring-1 ring-amber-200 transition hover:bg-amber-100"
                >
                  {{ skill }}
                  <span class="ml-1">→</span>
                </NuxtLink>
              </div>
              <p class="text-sm text-ink-500">
                Click a skill to find learning resources
              </p>
            </div>

            <div class="flex flex-wrap gap-3 pt-4">
              <Button size="lg" @click="handleApply" :disabled="applying || hasApplied">
                <span v-if="applying" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent mr-2"></span>
                {{ applying ? 'Applying...' : hasApplied ? 'Applied' : 'Apply for this role' }}
              </Button>
              <Button variant="outline" size="lg" @click="handleSave">
                <BookmarkIcon :class="['h-5 w-5', isSaved && 'fill-current']" />
                {{ isSaved ? 'Saved' : 'Save for later' }}
              </Button>
            </div>
          </div>
        </Card>

        <Card variant="glass" class="p-8">
          <div class="space-y-4">
            <h2 class="font-display text-xl font-semibold text-ink-900">Similar opportunities</h2>
            <p class="text-sm text-ink-500">
              Other roles that align with your skills
            </p>
            <div class="grid gap-4 md:grid-cols-2">
              <JobCard
                v-for="similar in similarJobs"
                :key="similar.id"
                :job="similar as any"
                :user-skills="auth.user?.skills || []"
                @click="navigateToJob(similar.id)"
                @applied="handleSimilarApplied"
                @apply-error="handleSimilarApplyError"
              />
            </div>
          </div>
        </Card>
      </div>

      <Card v-else variant="glass" class="p-8 text-center">
        <p class="text-ink-500">Job not found</p>
        <Button variant="outline" size="sm" class="mt-4" @click="router.push('/jobs')">
          Browse all jobs
        </Button>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { definePageMeta, useRoute, useRouter, useAsyncData } from '#imports'
import { useAuthStore, type ExperienceLevel, type JobType } from '~/stores/auth'
import { useApi } from '~/composables/useApi'
import Button from '~/components/ui/Button.vue'
import Card from '~/components/ui/Card.vue'
import JobCard from '~/components/features/JobCard.vue'
import { ArrowLeftIcon, MapPinIcon, BookmarkIcon } from '@heroicons/vue/24/outline'

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

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()
const api = useApi()

await auth.fetchProfile()

const jobId = computed(() => route.params.id as string)
const isSaved = ref(false)
const applying = ref(false)
const hasApplied = ref(false)

// Check if user has already applied
const checkApplicationStatus = async () => {
  if (!jobId.value) return
  try {
    const response = await api<{ has_applied: boolean; application: any }>(`/applications/job/${jobId.value}/check`)
    hasApplied.value = response?.has_applied || false
  } catch (error) {
    console.error('Error checking application status:', error)
  }
}

const { data: job, pending } = await useAsyncData(
  `job-${jobId.value}`,
  () => api<JobResponse>(`/jobs/${jobId.value}`),
  { server: false }
)

// Check application status when job is loaded
watch(() => job.value, async (newJob) => {
  if (newJob) {
    await checkApplicationStatus()
  }
}, { immediate: true })

interface JobRecommendation {
  job: JobResponse
  similarity_score: number
}

const { data: similarJobsData } = await useAsyncData(
  `similar-jobs-${jobId.value}`,
  () => api<JobRecommendation[]>(`/jobs/${jobId.value}/similar`, { query: { limit: 4 } }),
  { server: false }
)

const userSkillsSet = computed(() => new Set((auth.user?.skills ?? []).map(s => s.toLowerCase())))

const userHasSkill = (skill: string) => {
  return userSkillsSet.value.has(skill.toLowerCase())
}

const matchedSkillsCount = computed(() => {
  if (!job.value) return 0
  return job.value.required_skills.filter(skill => userHasSkill(skill)).length
})

const matchPercentage = computed(() => {
  if (!job.value || !job.value.required_skills.length) return 0
  return Math.round((matchedSkillsCount.value / job.value.required_skills.length) * 100)
})

const missingSkills = computed(() => {
  if (!job.value) return []
  return job.value.required_skills.filter(skill => !userHasSkill(skill))
})

const similarJobs = computed(() => {
  if (!similarJobsData.value) return []
  return similarJobsData.value.map(item => item.job)
})

const navigateToJob = (id: string) => {
  router.push(`/jobs/${id}`)
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

const handleApply = async () => {
  if (!job.value || applying.value || hasApplied.value) return

  applying.value = true
  try {
    await api('/applications/', {
      method: 'POST',
      body: {
        job_id: job.value.id
      }
    })
    
    hasApplied.value = true
    showNotificationPopup('Application submitted successfully!', 'success')
  } catch (error: any) {
    const errorMessage = error?.response?._data?.detail || 'Failed to submit application. Please try again.'
    showNotificationPopup(errorMessage, 'error')
  } finally {
    applying.value = false
  }
}

const handleSave = () => {
  isSaved.value = !isSaved.value
}

const handleSimilarApplied = (job: JobResponse) => {
  showNotificationPopup(`Application submitted successfully for ${job.title}!`, 'success')
}

const handleSimilarApplyError = (job: JobResponse, error: string) => {
  showNotificationPopup(error, 'error')
}

const experienceLabel = (value: ExperienceLevel) => {
  const mapping: Record<string, string> = {
    student: 'Student',
    entry: 'Entry-level',
    junior: 'Junior'
  }
  return mapping[value] || 'Unknown'
}

const capitalize = (value: string | null | undefined) => {
  if (!value) return 'Unknown'
  return value.replace(/_/g, ' ').replace(/\b\w/g, char => char.toUpperCase())
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
