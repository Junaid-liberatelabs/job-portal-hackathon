<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto flex max-w-7xl flex-col gap-10 px-6 lg:px-10">
      <header class="space-y-4">
        <p class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/70 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-600">
          Opportunity catalog
        </p>
        <div class="flex flex-col gap-3 md:flex-row md:items-end md:justify-between">
          <div class="space-y-3">
            <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Find roles aligned with your skills</h1>
            <p class="text-sm text-ink-500">
              Filter internships, entry roles, and freelance projects tailored to youth starting their careers.
            </p>
          </div>
        </div>
      </header>

      <section class="grid gap-6 rounded-[28px] border border-white/70 bg-white/80 p-8 shadow-[0_45px_140px_-80px_rgba(59,130,246,0.25)]">
        <form class="grid gap-5 md:grid-cols-4" @submit.prevent="handleSearch">
          <div class="space-y-2 md:col-span-1">
            <label for="search" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Keyword</label>
            <input
              id="search"
              v-model="filters.search"
              type="text"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
              placeholder="Search job title or company"
            />
          </div>

          <div class="space-y-2">
            <label for="job_type" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Job type</label>
            <select
              id="job_type"
              v-model="filters.job_type"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            >
              <option value="">Any</option>
              <option v-for="type in jobTypes" :key="type" :value="type">{{ capitalize(type) }}</option>
            </select>
          </div>

          <div class="space-y-2">
            <label for="experience_level" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Experience</label>
            <select
              id="experience_level"
              v-model="filters.experience_level"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            >
              <option value="">Any</option>
              <option v-for="level in experienceLevels" :key="level" :value="level">{{ experienceLabel(level) }}</option>
            </select>
          </div>

          <div class="space-y-2 md:col-span-1">
            <label for="skills" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Skills (comma separated)</label>
            <input
              id="skills"
              v-model="filters.skills"
              type="text"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
              placeholder="JavaScript, Communication"
            />
          </div>

          <div class="md:col-span-4 flex flex-wrap items-center gap-3">
            <button
              type="submit"
              :disabled="pending"
              class="inline-flex items-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <span v-if="pending" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <span>{{ pending ? 'Searching...' : 'Apply filters' }}</span>
            </button>
            <button
              type="button"
              class="inline-flex items-center gap-2 rounded-full border border-ink-200/70 px-5 py-3 text-sm font-semibold text-ink-600 transition hover:border-brand-200 hover:text-ink-900"
              @click="resetFilters"
            >
              Clear filters
            </button>
          </div>
        </form>
      </section>

      <section class="grid gap-6 lg:grid-cols-2">
        <article
          v-for="job in jobs"
          :key="job.id"
          class="landing-card landing-card--glass border border-white/60 p-6"
        >
          <div class="flex flex-wrap items-start justify-between gap-3">
            <div>
              <h2 class="font-display text-xl font-semibold text-ink-900">{{ job.title }}</h2>
              <p class="text-sm text-ink-500">{{ job.company }}</p>
            </div>
            <span class="rounded-full bg-brand-100 px-3 py-1 text-xs font-semibold text-brand-700">{{ capitalize(job.job_type) }}</span>
          </div>
          <p class="mt-3 text-sm text-ink-500 line-clamp-3">{{ job.description }}</p>
          <div class="mt-4 flex flex-wrap gap-2 text-xs text-ink-500">
            <span v-for="skill in job.required_skills" :key="`${job.id}-${skill}`" class="rounded-full bg-white px-3 py-1 font-semibold">
              {{ skill }}
            </span>
          </div>
          <div class="mt-5 flex flex-wrap items-center justify-between gap-3 text-xs text-ink-500">
            <span>Experience: {{ experienceLabel(job.recommended_experience_level) }}</span>
            <span v-if="overlap(job).length">Matches: {{ overlap(job).join(', ') }}</span>
          </div>
          <NuxtLink :to="`/jobs/${job.id}`" class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-brand-600 transition hover:text-brand-500">
            View details
            <span aria-hidden="true">→</span>
          </NuxtLink>
        </article>

        <div v-if="!pending && !jobs.length" class="rounded-[28px] border border-ink-100/70 bg-white/80 p-10 text-sm text-ink-500">
          No roles found. Try expanding your filters or broadening the skill list.
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed } from 'vue'
import { definePageMeta, useAsyncData } from '#imports'
import { useAuthStore, type ExperienceLevel, type JobType } from '~/stores/auth'
import { useApi } from '~/composables/useApi'

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
}

const jobTypes: JobType[] = ['internship', 'part_time', 'full_time', 'freelance']
const experienceLevels: ExperienceLevel[] = ['student', 'entry', 'junior']

const auth = useAuthStore()
const api = useApi()

await auth.fetchProfile()

const filters = reactive({
  search: '',
  job_type: '',
  experience_level: '',
  skills: ''
})

const fetchJobs = () => {
  const query: Record<string, any> = { limit: 50 }
  if (filters.job_type) query.job_type = filters.job_type
  if (filters.experience_level) query.experience_level = filters.experience_level

  const skillsInput = filters.skills.trim()
  if (skillsInput) {
    query.skills = skillsInput
  } else if (auth.user?.skills?.length) {
    query.skills = auth.user.skills.join(',')
  }

  return api<JobResponse[]>('/jobs/', { query })
}

const { data, pending, refresh } = await useAsyncData('jobs-listing', () => fetchJobs(), {
  server: false
})

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

const handleSearch = async () => {
  await refresh()
}

const resetFilters = async () => {
  filters.search = ''
  filters.job_type = ''
  filters.experience_level = ''
  filters.skills = ''
  await refresh()
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

const lowerSkills = computed(() => new Set((auth.user?.skills ?? []).map((skill) => skill.toLowerCase())))

const overlap = (job: JobResponse) => {
  return job.required_skills.filter((skill) => lowerSkills.value.has(skill.toLowerCase()))
}
</script>
