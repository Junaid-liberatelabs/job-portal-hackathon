<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto flex max-w-5xl flex-col gap-10 px-6 lg:px-10">
      <NuxtLink to="/jobs" class="inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
        ← Back to jobs
      </NuxtLink>

      <section class="space-y-6 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(15,23,42,0.3)] backdrop-blur">
        <div class="flex flex-wrap items-start justify-between gap-4">
          <div>
            <span class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/70 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-600">
              {{ capitalize(job?.job_type) }} role
            </span>
            <h1 class="mt-3 font-display text-3xl font-semibold text-ink-900">{{ job?.title }}</h1>
            <p class="text-sm text-ink-500">{{ job?.company }} • {{ jobLocation }}</p>
          </div>
          <div class="rounded-full bg-emerald-100 px-4 py-2 text-xs font-semibold text-emerald-700">
            Experience: {{ experienceLabel(job?.recommended_experience_level) }}
          </div>
        </div>

        <p class="text-sm text-ink-600 whitespace-pre-line">{{ job?.description }}</p>

        <div class="grid gap-6 md:grid-cols-2">
          <div class="rounded-3xl border border-ink-100/80 bg-ink-50/70 p-6">
            <h2 class="text-sm font-semibold uppercase tracking-[0.3em] text-ink-400">Required skills</h2>
            <div class="mt-4 flex flex-wrap gap-2 text-xs text-ink-500">
              <span v-for="skill in job?.required_skills" :key="skill" class="rounded-full bg-white px-3 py-1 font-semibold">
                {{ skill }}
              </span>
            </div>
          </div>
          <div class="rounded-3xl border border-ink-100/80 bg-white p-6 text-sm text-ink-500">
            <h2 class="text-sm font-semibold uppercase tracking-[0.3em] text-ink-400">Why this matches you</h2>
            <p v-if="overlap.length" class="mt-3">
              Strong overlap with your skills: <strong class="text-ink-800">{{ overlap.join(', ') }}</strong>.
            </p>
            <p v-else class="mt-3">Add more skills to your profile to see tailored guidance for this role.</p>
            <p v-if="job?.recommended_experience_level" class="mt-4">
              Target experience level: <strong class="text-ink-800">{{ experienceLabel(job?.recommended_experience_level) }}</strong>.
            </p>
          </div>
        </div>
      </section>

      <section v-if="relatedResources.length" class="space-y-4">
        <div class="flex items-center justify-between">
          <h2 class="font-display text-xl font-semibold text-ink-900">Learning resources to boost your fit</h2>
          <NuxtLink to="/resources" class="text-sm font-semibold text-brand-600 transition hover:text-brand-500">
            Explore all resources →
          </NuxtLink>
        </div>
        <div class="grid gap-6 md:grid-cols-2">
          <article
            v-for="resource in relatedResources"
            :key="resource.id"
            class="landing-card landing-card--glass border border-white/60 p-6"
          >
            <div class="flex items-center justify-between">
              <h3 class="font-display text-lg font-semibold text-ink-900">{{ resource.name }}</h3>
              <span class="rounded-full bg-ink-900/10 px-3 py-1 text-xs font-semibold uppercase tracking-[0.3em] text-ink-600">{{ resource.platform }}</span>
            </div>
            <p class="mt-3 text-sm text-ink-500 line-clamp-3">{{ resource.description }}</p>
            <div class="mt-4 flex flex-wrap gap-2 text-xs text-ink-500">
              <span v-for="tag in resource.tags" :key="`${resource.id}-${tag}`" class="rounded-full bg-white px-3 py-1 font-semibold">{{ tag }}</span>
            </div>
            <a :href="resource.url" target="_blank" rel="noopener" class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
              Open resource
              <span aria-hidden="true">↗</span>
            </a>
          </article>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { definePageMeta, useRoute, useAsyncData } from '#imports'
import { useAuthStore, type ExperienceLevel } from '~/stores/auth'
import { useApi } from '~/composables/useApi'

definePageMeta({
  middleware: 'auth'
})

interface JobResponse {
  id: string
  title: string
  description: string
  company: string
  job_type: string
  job_location?: string | null
  required_skills: string[]
  recommended_experience_level: ExperienceLevel
}

interface ResourceResponse {
  id: string
  name: string
  description: string
  url: string
  platform?: string
  tags: string[]
}

const route = useRoute()
const api = useApi()
const auth = useAuthStore()

await auth.fetchProfile()

const jobId = route.params.id as string

const { data: jobData } = await useAsyncData(`job-${jobId}`, () => api<JobResponse>(`/jobs/${jobId}`))
const { data: resourcesData } = await useAsyncData(`job-resources-${jobId}`, () =>
  api<ResourceResponse[]>('/resources/', { query: { limit: 50 } })
)

const job = computed(() => jobData.value ?? null)
const userSkills = computed(() => new Set((auth.user?.skills ?? []).map((skill) => skill.toLowerCase())))
const overlap = computed(() => {
  if (!job.value) return []
  return job.value.required_skills.filter((skill) => userSkills.value.has(skill.toLowerCase()))
})

const jobLocation = computed(() => {
  if (!job.value?.job_location) return 'Location flexible'
  return job.value.job_location.replace(/_/g, ' ').replace(/\b\w/g, (char) => char.toUpperCase())
})

const experienceLabel = (value?: ExperienceLevel | null) => {
  const mapping: Record<string, string> = {
    student: 'Student',
    entry: 'Entry-level',
    junior: 'Junior'
  }
  if (!value) return 'Not specified'
  return mapping[value] ?? 'Not specified'
}

const capitalize = (value?: string | null) => {
  if (!value) return 'Unknown'
  return value.charAt(0).toUpperCase() + value.slice(1)
}

const relatedResources = computed(() => {
  const resources = resourcesData.value ?? []
  if (!job.value) return []
  const jobSkillSet = new Set(job.value.required_skills.map((skill) => skill.toLowerCase()))
  return resources
    .filter((resource) => resource.tags?.some((tag) => jobSkillSet.has(tag.toLowerCase())))
    .slice(0, 4)
})
</script>
