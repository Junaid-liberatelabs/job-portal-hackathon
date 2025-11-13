<template>
  <div class="relative bg-ink-50 py-16">
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
              <Button size="lg" @click="handleApply">
                Apply for this role
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
import { computed, ref } from 'vue'
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
  job_location?: string | null
  required_skills: string[]
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

const { data: job, pending } = await useAsyncData(
  `job-${jobId.value}`,
  () => api<JobResponse>(`/jobs/${jobId.value}`),
  { server: false }
)

const { data: allJobs } = await useAsyncData(
  'similar-jobs',
  () => api<JobResponse[]>('/jobs/', { query: { limit: 50 } }),
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
  if (!job.value || !allJobs.value) return []
  
  return allJobs.value
    .filter(j => j.id !== job.value!.id)
    .map(j => {
      const overlap = j.required_skills.filter(skill => 
        job.value!.required_skills.some(js => js.toLowerCase() === skill.toLowerCase())
      )
      return { job: j, overlap: overlap.length }
    })
    .filter(({ overlap }) => overlap > 0)
    .sort((a, b) => b.overlap - a.overlap)
    .slice(0, 4)
    .map(({ job }) => job)
})

const navigateToJob = (id: string) => {
  router.push(`/jobs/${id}`)
}

const handleApply = () => {
  if (job.value) {
    alert(`Application feature coming soon! You're applying for: ${job.value.title}`)
  }
}

const handleSave = () => {
  isSaved.value = !isSaved.value
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
