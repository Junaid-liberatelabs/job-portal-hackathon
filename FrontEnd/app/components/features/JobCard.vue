<template>
  <Card 
    :hover="true" 
    :clickable="true" 
    variant="default"
    @click="$emit('click', job)"
  >
    <div class="space-y-4">
      <div class="flex items-start justify-between gap-4">
        <div class="flex-1 min-w-0">
          <h3 class="text-xl font-semibold text-ink-900 mb-1 truncate">{{ job.title }}</h3>
          <p class="text-ink-600 font-medium mb-2">{{ job.company }}</p>
          
          <div class="flex flex-wrap items-center gap-3 text-sm text-ink-500">
            <span class="flex items-center gap-1">
              <MapPinIcon class="h-4 w-4" />
              {{ formatLocation(job.job_location) }}
            </span>
            <span class="flex items-center gap-1">
              <BriefcaseIcon class="h-4 w-4" />
              {{ formatJobType(job.job_type) }}
            </span>
            <span class="flex items-center gap-1">
              <CurrencyDollarIcon class="h-4 w-4" />
              {{ formatSalaryRange(job.salary_range_min, job.salary_range_max) }}
            </span>
          </div>
        </div>
        
        <div class="text-right shrink-0">
          <div v-if="matchPercentage !== null" :class="matchBadgeClasses">
            {{ matchPercentage }}% Match
          </div>
          <p class="text-xs text-ink-500 mt-2">
            {{ formatExperienceLevel(job.recommended_experience_level) }}
          </p>
        </div>
      </div>
      
      <p class="text-ink-700 text-sm line-clamp-2">{{ job.description }}</p>
      
      <div class="flex flex-wrap gap-2">
        <span
          v-for="skill in job.required_skills.slice(0, 5)"
          :key="skill"
          :class="getSkillBadgeClass(skill)"
        >
          {{ skill }}
        </span>
        <span v-if="job.required_skills.length > 5" class="badge badge-primary">
          +{{ job.required_skills.length - 5 }} more
        </span>
      </div>
      
      <div class="flex items-center justify-between pt-2">
        <button
          @click.stop="$emit('save', job)"
          class="text-ink-500 hover:text-accent transition-colors p-2 rounded-lg hover:bg-ink-50"
          :aria-label="isSaved ? 'Remove bookmark' : 'Bookmark job'"
        >
          <BookmarkIcon v-if="!isSaved" class="h-5 w-5" />
          <BookmarkSolidIcon v-else class="h-5 w-5 text-accent" />
        </button>
        
        <Button
          variant="accent"
          size="sm"
          @click.stop="$emit('apply', job)"
        >
          Apply Now
        </Button>
      </div>
    </div>
  </Card>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { MapPinIcon, BriefcaseIcon, CurrencyDollarIcon, BookmarkIcon } from '@heroicons/vue/24/outline'
import { BookmarkIcon as BookmarkSolidIcon } from '@heroicons/vue/24/solid'
import type { Job } from '~/composables/useJobs'

interface Props {
  job: Job
  userSkills?: string[]
  isSaved?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  userSkills: () => [],
  isSaved: false
})

const emit = defineEmits<{
  click: [job: Job]
  save: [job: Job]
  apply: [job: Job]
}>()

const { formatJobType, formatLocation, formatSalaryRange, calculateSkillMatch } = useJobs()

const matchPercentage = computed(() => {
  if (!props.userSkills || props.userSkills.length === 0) return null
  return calculateSkillMatch(props.job, props.userSkills)
})

const matchBadgeClasses = computed(() => {
  const base = 'px-3 py-1 rounded-full text-xs font-semibold text-white'
  
  if (matchPercentage.value === null) return `${base} bg-ink-400`
  
  if (matchPercentage.value >= 70) return `${base} skill-match-high`
  if (matchPercentage.value >= 40) return `${base} skill-match-medium`
  return `${base} skill-match-low`
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
    ? 'badge bg-accent/10 text-accent border border-accent/20'
    : 'badge badge-primary'
}
</script>

