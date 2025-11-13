<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto flex max-w-7xl flex-col gap-12 px-6 lg:px-10">
      <section class="grid gap-8 rounded-[32px] border border-white/70 bg-white/90 p-10 shadow-[0_50px_140px_-70px_rgba(15,23,42,0.3)] backdrop-blur lg:grid-cols-[minmax(0,1.1fr)_minmax(0,0.9fr)]">
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/70 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-600">
            Welcome back, {{ auth.user?.full_name?.split(' ')[0] || 'Explorer' }}
          </p>
          <div class="space-y-3">
            <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Your career launchpad</h1>
            <p class="text-sm text-ink-500">
              Track your strengths, review transparent matches, and commit to a learning sprint—all from a single command centre.
            </p>
          </div>

          <div class="grid gap-4 rounded-3xl border border-ink-100/80 bg-ink-50/60 p-6 text-sm text-ink-600 shadow-inner">
            <div class="flex flex-wrap items-center gap-3">
              <span class="inline-flex rounded-full border border-ink-200/70 bg-white px-3 py-1 text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">
                Profile snapshot
              </span>
              <span class="rounded-full bg-emerald-100 px-3 py-1 text-xs font-semibold text-emerald-700">
                {{ auth.user?.preferred_career_track || 'Track pending' }}
              </span>
            </div>
            <div class="grid gap-2 sm:grid-cols-2">
              <p><strong class="text-ink-800">Education:</strong> {{ auth.user?.education_level || 'Not provided' }}</p>
              <p><strong class="text-ink-800">Experience level:</strong> {{ experienceLabel }}</p>
            </div>
            <div class="flex flex-wrap gap-2" v-if="auth.user?.skills?.length">
              <span v-for="skill in auth.user?.skills" :key="skill" class="rounded-full bg-white px-3 py-1 text-xs font-semibold text-ink-500 shadow">
                {{ skill }}
              </span>
            </div>
            <NuxtLink
              to="/profile"
              class="inline-flex w-max items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500"
            >
              Update profile
              <span aria-hidden="true">→</span>
            </NuxtLink>
          </div>
        </div>

        <div class="space-y-5">
          <div class="rounded-[28px] border border-white/70 bg-white/80 p-6 shadow-[0_35px_100px_-60px_rgba(59,130,246,0.25)]">
            <h2 class="font-display text-lg font-semibold text-ink-900">Weekly focus</h2>
            <p class="mt-2 text-sm text-ink-500">
              Stay consistent by tackling one opportunity and one learning sprint at a time.
            </p>
            <dl class="mt-4 grid gap-4 text-sm text-ink-600">
              <div class="rounded-2xl border border-brand-100/70 bg-brand-50/60 p-4">
                <dt class="text-xs font-semibold uppercase tracking-[0.3em] text-brand-500">Next application</dt>
                <dd class="mt-1 font-semibold text-ink-900">{{ topJob?.title || 'Review recommended roles below' }}</dd>
                <p v-if="topJob" class="mt-1 text-xs text-ink-500">{{ overlapMessage(topJob) }}</p>
              </div>
              <div class="rounded-2xl border border-emerald-100/70 bg-emerald-50/60 p-4">
                <dt class="text-xs font-semibold uppercase tracking-[0.3em] text-emerald-600">Learning sprint</dt>
                <dd class="mt-1 font-semibold text-ink-900">{{ topResource?.name || 'Pick a resource to level up this week' }}</dd>
                <p v-if="topResource" class="mt-1 text-xs text-ink-500">{{ resourceMessage(topResource) }}</p>
              </div>
            </dl>
          </div>
        </div>
      </section>

      <section class="space-y-6">
        <div class="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <span class="inline-flex items-center gap-2 rounded-full border border-brand-200/60 bg-brand-50/60 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-600">
              Recommended jobs
            </span>
            <h2 class="mt-3 font-display text-2xl font-semibold text-ink-900">Opportunities aligned to your profile</h2>
          </div>
          <NuxtLink to="/jobs" class="inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
            View all roles
            <span aria-hidden="true">→</span>
          </NuxtLink>
        </div>
        <div class="grid gap-6 lg:grid-cols-2">
          <article
            v-for="job in recommendedJobs"
            :key="job.id"
            class="landing-card landing-card--glass border border-white/60 p-6"
          >
            <div class="flex items-center justify-between">
              <h3 class="font-display text-xl font-semibold text-ink-900">{{ job.title }}</h3>
              <span class="rounded-full bg-emerald-100 px-3 py-1 text-xs font-semibold text-emerald-700">{{ job.company }}</span>
            </div>
            <p class="mt-3 text-sm text-ink-500 line-clamp-3">{{ job.description }}</p>
            <div class="mt-4 flex flex-wrap gap-2 text-xs text-ink-500">
              <span v-for="skill in job.required_skills" :key="`${job.id}-${skill}`" class="rounded-full bg-white px-3 py-1 font-semibold">{{ skill }}</span>
            </div>
            <div class="mt-5 flex flex-wrap items-center justify-between gap-3 text-xs text-ink-500">
              <span>Experience: {{ capitalize(job.recommended_experience_level) }}</span>
              <span>{{ overlapMessage(job) }}</span>
            </div>
            <NuxtLink :to="`/jobs/${job.id}`" class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
              View details
              <span aria-hidden="true">→</span>
            </NuxtLink>
          </article>
          <p v-if="!recommendedJobs.length" class="rounded-3xl border border-ink-100/70 bg-white/80 p-6 text-sm text-ink-500">
            Add more skills or adjust your track to see tailored matches.
          </p>
        </div>
      </section>

      <section class="space-y-6">
        <div class="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <span class="inline-flex items-center gap-2 rounded-full border border-emerald-200/70 bg-emerald-50/60 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-emerald-600">
              Recommended learning
            </span>
            <h2 class="mt-3 font-display text-2xl font-semibold text-ink-900">Strengthen skills with purposeful resources</h2>
          </div>
          <NuxtLink to="/resources" class="inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
            Explore all resources
            <span aria-hidden="true">→</span>
          </NuxtLink>
        </div>
        <div class="grid gap-6 lg:grid-cols-2">
          <article
            v-for="resource in recommendedResources"
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
            <div class="mt-5 flex items-center justify-between text-xs text-ink-500">
              <span>Cost: {{ resourceCost(resource) }}</span>
              <a :href="resource.url" target="_blank" rel="noopener" class="inline-flex items-center gap-1 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
                Open resource
                <span aria-hidden="true">↗</span>
              </a>
            </div>
          </article>
          <p v-if="!recommendedResources.length" class="rounded-3xl border border-ink-100/70 bg-white/80 p-6 text-sm text-ink-500">
            Tell us more about the skills you want to strengthen to unlock personalised learning plans.
          </p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { definePageMeta, useAsyncData } from '#imports'
import { useAuthStore, type ExperienceLevel } from '~/stores/auth'
import { useApi } from '~/composables/useApi'

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

definePageMeta({
  middleware: 'auth'
})

const auth = useAuthStore()
const api = useApi()

await auth.fetchProfile()

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
</script>
