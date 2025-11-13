<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto flex max-w-7xl flex-col gap-10 px-6 lg:px-10">
      <header class="space-y-4">
        <p class="inline-flex items-center gap-2 rounded-full border border-emerald-200/80 bg-emerald-50/70 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-emerald-600">
          Learning hub
        </p>
        <div class="flex flex-col gap-3 md:flex-row md:items-end md:justify-between">
          <div class="space-y-3">
            <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Close skill gaps with curated resources</h1>
            <p class="text-sm text-ink-500">
              Courses, tutorials, and community-led content mapped to the skills employers expect.
            </p>
          </div>
        </div>
      </header>

      <section class="grid gap-6 rounded-[28px] border border-white/70 bg-white/80 p-8 shadow-[0_45px_140px_-80px_rgba(16,185,129,0.25)]">
        <form class="grid gap-5 md:grid-cols-4" @submit.prevent="handleFilter">
          <div class="space-y-2 md:col-span-2">
            <label for="keyword" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Keyword</label>
            <input
              id="keyword"
              v-model="filters.keyword"
              type="text"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
              placeholder="Search title or description"
            />
          </div>

          <div class="space-y-2">
            <label for="cost" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Cost</label>
            <select
              id="cost"
              v-model="filters.cost"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            >
              <option value="">Any</option>
              <option value="free">Free</option>
              <option value="paid">Paid</option>
            </select>
          </div>

          <div class="space-y-2">
            <label for="skill" class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Skill tag</label>
            <input
              id="skill"
              v-model="filters.skill"
              type="text"
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
              placeholder="e.g., React"
            />
          </div>

          <div class="md:col-span-4 flex flex-wrap items-center gap-3">
            <button
              type="submit"
              :disabled="pending"
              class="inline-flex items-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <span v-if="pending" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <span>{{ pending ? 'Filtering...' : 'Apply filters' }}</span>
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
        <CourseCard
          v-for="resource in filteredResources"
          :key="resource.id"
          :resource="resource as any"
          @view="handleViewResource"
        />

        <div v-if="!pending && !filteredResources.length" class="rounded-[28px] border border-ink-100/70 bg-white/80 p-10 text-sm text-ink-500">
          No resources found. Try a different skill keyword or reset your filters.
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
  skill: ''
})

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

  return resources.value.filter((resource) => {
    const matchesKeyword = keyword
      ? resource.name.toLowerCase().includes(keyword) || resource.description.toLowerCase().includes(keyword)
      : true

    const matchesSkill = skill ? resource.tags?.some((tag) => tag.toLowerCase().includes(skill)) : true

    const matchesCost = cost ? resource.tags?.some((tag) => tag.toLowerCase() === cost) : true

    return matchesKeyword && matchesSkill && matchesCost
  })
})

const handleFilter = async () => {
  await refresh()
}

const resetFilters = async () => {
  filters.keyword = ''
  filters.cost = ''
  filters.skill = ''
  await refresh()
}

const costLabel = (resource: ResourceResponse) => {
  const tag = resource.tags?.find((item) => item.toLowerCase() === 'free' || item.toLowerCase() === 'paid')
  if (!tag) return 'Cost varies'
  return tag.toLowerCase() === 'free' ? 'Free' : 'Paid'
}
</script>
