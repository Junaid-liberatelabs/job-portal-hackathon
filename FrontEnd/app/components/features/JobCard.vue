<template>
  <div 
    class="group relative overflow-hidden rounded-[24px] border border-ink-100 bg-white p-6 shadow-[0_2px_8px_rgba(0,0,0,0.04)] transition-all duration-500 hover:shadow-[0_20px_60px_rgba(59,130,246,0.15)] hover:-translate-y-2 cursor-pointer card-hover-effect"
    @click="$emit('click', job)"
  >
    <!-- Gradient accent line -->
    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-brand-500 via-brand-400 to-brand-600 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
    
    <!-- Floating background gradient -->
    <div class="absolute -top-20 -right-20 w-40 h-40 bg-gradient-to-br from-brand-500/5 to-accent/5 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
    
    <div class="relative space-y-4">
      <!-- Header Section -->
      <div class="flex items-start justify-between gap-4">
        <div class="flex-1 min-w-0">
          <h3 class="text-xl font-bold text-ink-900 mb-1 truncate group-hover:text-brand-600 transition-colors duration-300">
            {{ job.title }}
          </h3>
          <p class="text-ink-600 font-semibold mb-3">{{ job.company }}</p>
          
          <div class="flex flex-wrap items-center gap-3 text-xs text-ink-500">
            <span class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-ink-50 group-hover:bg-brand-50 transition-colors duration-300">
              <MapPinIcon class="h-3.5 w-3.5" />
              <span class="font-medium">{{ formatLocation(job.job_location) }}</span>
            </span>
            <span class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-ink-50 group-hover:bg-brand-50 transition-colors duration-300">
              <BriefcaseIcon class="h-3.5 w-3.5" />
              <span class="font-medium">{{ formatJobType(job.job_type) }}</span>
            </span>
            <span class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-ink-50 group-hover:bg-brand-50 transition-colors duration-300">
              <CurrencyDollarIcon class="h-3.5 w-3.5" />
              <span class="font-medium">{{ formatSalaryRange(job.salary_range_min, job.salary_range_max) }}</span>
            </span>
          </div>
        </div>
        
        <!-- Match Badge -->
        <div class="flex flex-col items-end gap-2 shrink-0">
          <div v-if="matchPercentage !== null && matchPercentage > 0" :class="matchBadgeClasses">
            <span class="text-sm font-bold">{{ matchPercentage }}%</span>
            <span class="text-[10px] font-semibold opacity-90">MATCH</span>
          </div>
          <span class="px-2.5 py-1 rounded-lg bg-gradient-to-r from-ink-100 to-ink-50 text-[11px] font-bold text-ink-600 uppercase tracking-wider">
            {{ formatExperienceLevel(job.recommended_experience_level) }}
          </span>
        </div>
      </div>
      
      <!-- Description -->
      <p class="text-ink-600 text-sm leading-relaxed line-clamp-2">{{ job.description }}</p>
      
      <!-- Skills -->
      <div class="flex flex-wrap gap-2">
        <span
          v-for="skill in job.required_skills.slice(0, 5)"
          :key="skill"
          :class="getSkillBadgeClass(skill)"
          class="px-3 py-1.5 rounded-lg text-xs font-semibold transition-all duration-300"
        >
          {{ skill }}
        </span>
        <span v-if="job.required_skills.length > 5" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-ink-100 text-ink-600">
          +{{ job.required_skills.length - 5 }}
        </span>
      </div>
      
      <!-- Actions -->
      <div class="flex items-center justify-between pt-3 border-t border-ink-100/50">
        <button
          @click.stop="$emit('save', job)"
          class="flex items-center gap-2 text-ink-400 hover:text-brand-600 transition-all duration-300 p-2 rounded-xl hover:bg-brand-50 group/bookmark"
          :aria-label="isSaved ? 'Remove bookmark' : 'Bookmark job'"
        >
          <BookmarkIcon v-if="!isSaved" class="h-5 w-5 group-hover/bookmark:scale-110 transition-transform" />
          <BookmarkSolidIcon v-else class="h-5 w-5 text-brand-600 group-hover/bookmark:scale-110 transition-transform" />
        </button>
        
        <button
          @click.stop="handleApply"
          :disabled="applying || hasApplied"
          class="inline-flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-brand-500 to-brand-600 hover:from-brand-600 hover:to-brand-700 text-white text-sm font-semibold rounded-xl shadow-md hover:shadow-xl transition-all duration-300 hover:scale-105 disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:scale-100"
        >
          <span v-if="applying" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
          <span v-else-if="hasApplied" class="h-4 w-4">
            <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
            </svg>
          </span>
          <svg v-else class="h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
          </svg>
          <span>{{ applying ? 'Applying...' : hasApplied ? 'Applied' : 'Apply Now' }}</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, watch } from 'vue'
import { MapPinIcon, BriefcaseIcon, CurrencyDollarIcon, BookmarkIcon } from '@heroicons/vue/24/outline'
import { BookmarkIcon as BookmarkSolidIcon } from '@heroicons/vue/24/solid'
import type { Job } from '~/composables/useJobs'
import { useApi } from '~/composables/useApi'

interface Props {
  job: Job
  userSkills?: string[]
  isSaved?: boolean
  similarityScore?: number | null // Backend similarity score (0-1)
}

const props = withDefaults(defineProps<Props>(), {
  userSkills: () => [],
  isSaved: false,
  similarityScore: null
})

const emit = defineEmits<{
  click: [job: Job]
  save: [job: Job]
  apply: [job: Job]
  applied: [job: Job]
  'apply-error': [job: Job, error: string]
}>()

const api = useApi()
const applying = ref(false)
const hasApplied = ref(false)

// Check if user has already applied
const checkApplicationStatus = async () => {
  if (!props.job?.id) return
  try {
    const response = await api<{ has_applied: boolean; application: any }>(`/applications/job/${props.job.id}/check`)
    hasApplied.value = response?.has_applied || false
  } catch (error) {
    console.error('Error checking application status:', error)
  }
}

// Check application status on mount and when job changes
onMounted(() => {
  checkApplicationStatus()
})

watch(() => props.job?.id, () => {
  checkApplicationStatus()
})

const handleApply = async () => {
  if (!props.job || applying.value || hasApplied.value) return

  applying.value = true
  try {
    await api('/applications/', {
      method: 'POST',
      body: {
        job_id: props.job.id
      }
    })
    
    hasApplied.value = true
    emit('apply', props.job)
    emit('applied', props.job)
  } catch (error: any) {
    const errorMessage = error?.response?._data?.detail || 'Failed to submit application. Please try again.'
    emit('apply', props.job)
    emit('apply-error', props.job, errorMessage)
  } finally {
    applying.value = false
  }
}

const { formatJobType, formatLocation, formatSalaryRange, calculateSkillMatch } = useJobs()

const matchPercentage = computed(() => {
  // Prioritize backend similarity score if available
  if (props.similarityScore !== null && props.similarityScore !== undefined) {
    return Math.round(props.similarityScore * 100)
  }
  // Fallback to frontend calculation if no backend score
  if (!props.userSkills || props.userSkills.length === 0) return null
  return calculateSkillMatch(props.job, props.userSkills)
})

const matchBadgeClasses = computed(() => {
  const base = 'flex flex-col items-center justify-center px-4 py-2 rounded-xl text-white shadow-lg transition-all duration-300 group-hover:scale-110'
  
  if (matchPercentage.value === null) return `${base} bg-gradient-to-br from-ink-400 to-ink-500`
  
  if (matchPercentage.value >= 70) return `${base} bg-gradient-to-br from-green-500 to-emerald-600 shadow-green-500/30`
  if (matchPercentage.value >= 40) return `${base} bg-gradient-to-br from-blue-500 to-brand-600 shadow-brand-500/30`
  return `${base} bg-gradient-to-br from-amber-500 to-orange-600 shadow-amber-500/30`
})

const formatExperienceLevel = (level: string): string => {
  const levelMap: Record<string, string> = {
    student: 'Student',
    entry: 'Entry Level',
    junior: 'Junior Level'
  }
  return levelMap[level] || level
}

const getSkillBadgeClass = (skill: string): string => {
  const isMatched = props.userSkills?.some(userSkill => 
    userSkill.toLowerCase() === skill.toLowerCase()
  )
  
  return isMatched 
    ? 'bg-gradient-to-r from-emerald-50 to-green-50 text-emerald-700 border border-emerald-200 hover:border-emerald-300 hover:shadow-md'
    : 'bg-gradient-to-r from-brand-50 to-blue-50 text-brand-700 border border-brand-200 hover:border-brand-300 hover:shadow-md'
}
</script>

