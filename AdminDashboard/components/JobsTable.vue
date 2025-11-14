<template>
  <div class="card">
    <div class="card-header">
      <h3 class="text-lg font-semibold text-ink-900">Jobs Overview</h3>
      <p class="text-sm text-ink-600 mt-1">Manage job postings and view application statistics</p>
    </div>
    
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead class="bg-ink-50 border-b border-ink-200">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Job Title</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Company</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Type</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Experience</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Applicants</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Posted</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-ink-600 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-ink-200">
          <tr v-for="item in jobs" :key="item.job.id" class="hover:bg-ink-50 transition-colors">
            <td class="px-6 py-4">
              <div class="text-sm font-medium text-ink-900">{{ item.job.title }}</div>
              <div class="text-xs text-ink-500 mt-1 line-clamp-1">{{ item.job.description }}</div>
            </td>
            <td class="px-6 py-4 text-sm text-ink-700">{{ item.job.company }}</td>
            <td class="px-6 py-4">
              <span :class="getJobTypeBadge(item.job.job_type)">
                {{ formatJobType(item.job.job_type) }}
              </span>
            </td>
            <td class="px-6 py-4">
              <span :class="getExperienceBadge(item.job.recommended_experience_level)">
                {{ formatExperience(item.job.recommended_experience_level) }}
              </span>
            </td>
            <td class="px-6 py-4">
              <button
                @click="$emit('view-applicants', item.job)"
                class="flex items-center gap-2 text-sm font-semibold text-admin-600 hover:text-admin-700 transition-colors"
              >
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-admin-100">
                  {{ item.applicants_count }}
                </span>
                <span v-if="item.applicants_count > 0">View</span>
              </button>
            </td>
            <td class="px-6 py-4 text-sm text-ink-600">
              {{ formatDate(item.job.created_at) }}
            </td>
            <td class="px-6 py-4 text-right">
              <div class="flex items-center justify-end gap-2">
                <button
                  @click="$emit('edit-job', item.job)"
                  class="p-2 text-ink-600 hover:text-admin-600 hover:bg-admin-50 rounded-lg transition-colors"
                  title="Edit job"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </button>
                <button
                  @click="$emit('delete-job', item.job.id)"
                  class="p-2 text-ink-600 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                  title="Delete job"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </td>
          </tr>
          <tr v-if="jobs.length === 0">
            <td colspan="7" class="px-6 py-12 text-center text-ink-500">
              <div class="flex flex-col items-center justify-center">
                <svg class="w-16 h-16 text-ink-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                <p class="text-lg font-medium text-ink-700 mb-2">No jobs posted yet</p>
                <p class="text-sm text-ink-500">Create your first job posting to get started</p>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Job {
  id: string
  title: string
  description: string
  company: string
  job_type: string
  job_location?: string
  required_skills: string[]
  recommended_experience_level: string
  salary_range_min?: number
  salary_range_max?: number
  created_at: string
  updated_at: string
}

interface JobWithApplicantsCount {
  job: Job
  applicants_count: number
}

defineProps<{
  jobs: JobWithApplicantsCount[]
}>()

defineEmits<{
  'view-applicants': [job: Job]
  'edit-job': [job: Job]
  'delete-job': [jobId: string]
}>()

const formatJobType = (type: string) => {
  return type.replace('_', ' ').split(' ').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
  ).join(' ')
}

const formatExperience = (level: string) => {
  return level.charAt(0).toUpperCase() + level.slice(1).toLowerCase()
}

const getJobTypeBadge = (type: string) => {
  const badges: Record<string, string> = {
    'FULL_TIME': 'badge badge-success',
    'PART_TIME': 'badge badge-warning',
    'INTERNSHIP': 'badge badge-info',
    'FREELANCE': 'badge badge-primary'
  }
  return badges[type] || 'badge badge-primary'
}

const getExperienceBadge = (level: string) => {
  const badges: Record<string, string> = {
    'STUDENT': 'badge badge-info',
    'ENTRY': 'badge badge-success',
    'JUNIOR': 'badge badge-primary'
  }
  return badges[level] || 'badge badge-primary'
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  
  if (days === 0) return 'Today'
  if (days === 1) return 'Yesterday'
  if (days < 7) return `${days} days ago`
  if (days < 30) return `${Math.floor(days / 7)} weeks ago`
  if (days < 365) return `${Math.floor(days / 30)} months ago`
  return date.toLocaleDateString()
}
</script>

