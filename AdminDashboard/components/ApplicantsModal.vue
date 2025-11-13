<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition-opacity duration-200"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="isOpen"
        class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4 overflow-y-auto"
        @click.self="$emit('close')"
      >
        <Transition
          enter-active-class="transition-all duration-200"
          enter-from-class="opacity-0 scale-95"
          enter-to-class="opacity-100 scale-100"
          leave-active-class="transition-all duration-200"
          leave-from-class="opacity-100 scale-100"
          leave-to-class="opacity-0 scale-95"
        >
          <div
            v-if="isOpen"
            class="bg-white rounded-2xl shadow-2xl max-w-5xl w-full my-8 max-h-[90vh] flex flex-col"
          >
            <div class="sticky top-0 bg-white border-b border-ink-200 px-6 py-4 flex items-center justify-between">
              <div>
                <h2 class="text-2xl font-bold text-ink-900">Applicants</h2>
                <p v-if="job" class="text-sm text-ink-600 mt-1">{{ job.title }} at {{ job.company }}</p>
              </div>
              <button
                @click="$emit('close')"
                class="p-2 hover:bg-ink-100 rounded-lg transition-colors"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <div class="flex-1 overflow-y-auto scrollbar-thin p-6">
              <div v-if="loading" class="flex items-center justify-center py-12">
                <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-admin-600"></div>
              </div>

              <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
                <p class="text-sm text-red-800">{{ error }}</p>
              </div>

              <div v-else-if="applicants.length === 0" class="text-center py-12">
                <svg class="w-16 h-16 text-ink-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                <p class="text-lg font-medium text-ink-700 mb-2">No applicants yet</p>
                <p class="text-sm text-ink-500">This job hasn't received any applications</p>
              </div>

              <div v-else class="space-y-4">
                <div
                  v-for="applicant in applicants"
                  :key="applicant.application_id"
                  class="card hover:shadow-md transition-shadow"
                >
                  <div class="card-body">
                    <div class="flex items-start justify-between">
                      <div class="flex items-start gap-4 flex-1">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-admin-500 to-admin-600 flex items-center justify-center text-white font-bold text-lg">
                          {{ getInitials(applicant.user.full_name || applicant.user.email) }}
                        </div>
                        
                        <div class="flex-1">
                          <h3 class="text-lg font-semibold text-ink-900">
                            {{ applicant.user.full_name || 'Unnamed User' }}
                          </h3>
                          <p class="text-sm text-ink-600">{{ applicant.user.email }}</p>
                          
                          <div v-if="applicant.user.career_goals" class="mt-2">
                            <p class="text-sm text-ink-700">
                              <span class="font-medium">Career Goals:</span> 
                              {{ applicant.user.career_goals }}
                            </p>
                          </div>
                          
                          <div v-if="applicant.user.skills && applicant.user.skills.length > 0" class="mt-3">
                            <p class="text-xs font-medium text-ink-600 mb-2">Skills:</p>
                            <div class="flex flex-wrap gap-2">
                              <span
                                v-for="skill in applicant.user.skills"
                                :key="skill"
                                class="px-2 py-1 bg-ink-100 text-ink-700 rounded text-xs font-medium"
                              >
                                {{ skill }}
                              </span>
                            </div>
                          </div>
                          
                          <div class="mt-3 flex items-center gap-2 text-xs text-ink-500">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                            </svg>
                            <span>Applied {{ formatDate(applicant.applied_at) }}</span>
                          </div>
                        </div>
                      </div>
                      
                      <div class="flex flex-col gap-2">
                        <a
                          :href="`mailto:${applicant.user.email}`"
                          class="btn btn-primary text-sm"
                          target="_blank"
                        >
                          <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                          </svg>
                          Contact
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="border-t border-ink-200 px-6 py-4 bg-ink-50">
              <div class="flex items-center justify-between">
                <p class="text-sm text-ink-600">
                  Total Applicants: <span class="font-semibold text-ink-900">{{ applicants.length }}</span>
                </p>
                <button @click="$emit('close')" class="btn btn-secondary">
                  Close
                </button>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
interface Job {
  id: string
  title: string
  company: string
}

interface UserResponse {
  id: string
  email: string
  full_name?: string
  skills?: string[]
  career_goals?: string
  created_at: string
}

interface ApplicantInfo {
  application_id: string
  user_id: string
  applied_at: string
  user: UserResponse
}

const props = defineProps<{
  isOpen: boolean
  job: Job | null
}>()

defineEmits<{
  close: []
}>()

const { applicants, loading, error, fetchApplicantsByJob } = useApplicants()

watch(() => props.isOpen, async (isOpen) => {
  if (isOpen && props.job) {
    await fetchApplicantsByJob(props.job.id)
  }
}, { immediate: true })

const getInitials = (name: string) => {
  if (!name) return '??'
  
  const parts = name.split(/[\s@]+/).filter(p => p.length > 0)
  if (parts.length >= 2) {
    const first = parts[0]?.[0]
    const second = parts[1]?.[0]
    if (first && second) {
      return (first + second).toUpperCase()
    }
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  
  if (days === 0) return 'today'
  if (days === 1) return 'yesterday'
  if (days < 7) return `${days} days ago`
  if (days < 30) return `${Math.floor(days / 7)} weeks ago`
  if (days < 365) return `${Math.floor(days / 30)} months ago`
  return date.toLocaleDateString()
}
</script>

