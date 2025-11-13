<template>
  <div class="min-h-screen bg-gradient-to-br from-ink-50 via-admin-50/20 to-ink-50">
    <header class="bg-white border-b border-ink-200 sticky top-0 z-40 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-gradient-to-br from-admin-500 to-admin-600 rounded-xl flex items-center justify-center">
              <span class="material-symbols-outlined text-white text-2xl">admin_panel_settings</span>
            </div>
            <div>
              <h1 class="text-xl font-bold text-ink-900">CareerIn Admin</h1>
              <p class="text-xs text-ink-600">Dashboard & Management</p>
            </div>
          </div>
          
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-2 px-3 py-2 bg-ink-100 rounded-lg">
              <div class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span class="text-sm font-medium text-ink-700">Live</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="mb-8">
        <h2 class="text-3xl font-bold text-ink-900 mb-2">Dashboard Overview</h2>
        <p class="text-ink-600">Manage job postings and track applications</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <StatsCard
          title="Total Jobs"
          :value="stats.totalJobs"
          subtitle="Active job postings"
          :icon="BriefcaseIcon"
          icon-bg-class="bg-admin-100"
          icon-color-class="text-admin-600"
        />
        <StatsCard
          title="Total Applications"
          :value="stats.totalApplications"
          subtitle="All time applications"
          :icon="UsersIcon"
          icon-bg-class="bg-green-100"
          icon-color-class="text-green-600"
        />
        <StatsCard
          title="Avg. Applicants/Job"
          :value="stats.avgApplicants"
          subtitle="Per job posting"
          :icon="ChartBarIcon"
          icon-bg-class="bg-purple-100"
          icon-color-class="text-purple-600"
        />
        <StatsCard
          title="Most Popular"
          :value="stats.mostPopularType"
          subtitle="Job type"
          :icon="FireIcon"
          icon-bg-class="bg-orange-100"
          icon-color-class="text-orange-600"
        />
      </div>

      <div v-if="error" class="mb-6 bg-red-50 border border-red-200 rounded-lg p-4">
        <div class="flex items-center gap-2">
          <svg class="w-5 h-5 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-sm text-red-800 font-medium">{{ error }}</p>
        </div>
      </div>

      <div class="flex items-center justify-between mb-6">
        <div>
          <h3 class="text-2xl font-bold text-ink-900">Job Listings</h3>
          <p class="text-sm text-ink-600 mt-1">Manage and monitor all job postings</p>
        </div>
        <button
          @click="openCreateModal"
          class="btn btn-primary flex items-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Create New Job
        </button>
      </div>

      <div v-if="loading" class="flex items-center justify-center py-20">
        <div class="text-center">
          <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-admin-600 mx-auto mb-4"></div>
          <p class="text-ink-600">Loading jobs...</p>
        </div>
      </div>

      <JobsTable
        v-else
        :jobs="jobsWithApplicants"
        @view-applicants="openApplicantsModal"
        @edit-job="openEditModal"
        @delete-job="handleDeleteJob"
      />
    </main>

    <CreateJobModal
      :is-open="isCreateModalOpen"
      :edit-job="editingJob"
      @close="closeCreateModal"
      @job-created="handleJobCreated"
      @job-updated="handleJobUpdated"
    />

    <ApplicantsModal
      :is-open="isApplicantsModalOpen"
      :job="selectedJob"
      @close="closeApplicantsModal"
    />

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
          v-if="showDeleteConfirm"
          class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4"
          @click.self="showDeleteConfirm = false"
        >
          <div class="bg-white rounded-xl shadow-2xl max-w-md w-full p-6">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 rounded-full bg-red-100 flex items-center justify-center">
                <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </div>
              <div>
                <h3 class="text-lg font-bold text-ink-900">Delete Job</h3>
                <p class="text-sm text-ink-600">This action cannot be undone</p>
              </div>
            </div>
            <p class="text-ink-700 mb-6">
              Are you sure you want to delete this job? All associated applications will be affected.
            </p>
            <div class="flex items-center justify-end gap-3">
              <button
                @click="showDeleteConfirm = false"
                class="btn btn-secondary"
              >
                Cancel
              </button>
              <button
                @click="confirmDelete"
                class="btn btn-danger"
              >
                Delete Job
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import {
  BriefcaseIcon,
  UsersIcon,
  ChartBarIcon,
  FireIcon
} from '@heroicons/vue/24/outline'

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

useHead({
  title: 'Dashboard'
})

const { jobsWithApplicants, loading, error, fetchJobsWithApplicants, deleteJob } = useJobs()

const isCreateModalOpen = ref(false)
const isApplicantsModalOpen = ref(false)
const editingJob = ref<Job | null>(null)
const selectedJob = ref<Job | null>(null)
const showDeleteConfirm = ref(false)
const deleteJobId = ref<string | null>(null)

const stats = computed(() => {
  const totalJobs = jobsWithApplicants.value.length
  const totalApplications = jobsWithApplicants.value.reduce((sum, item) => sum + item.applicants_count, 0)
  const avgApplicants = totalJobs > 0 ? Math.round(totalApplications / totalJobs * 10) / 10 : 0
  
  const typeCount: Record<string, number> = {}
  jobsWithApplicants.value.forEach(item => {
    const type = item.job.job_type
    typeCount[type] = (typeCount[type] || 0) + 1
  })
  
  const mostPopularType = Object.entries(typeCount).sort((a, b) => b[1] - a[1])[0]?.[0] || 'N/A'
  const formattedType = mostPopularType !== 'N/A' 
    ? mostPopularType.replace('_', ' ').split(' ').map(w => w.charAt(0) + w.slice(1).toLowerCase()).join(' ')
    : 'N/A'
  
  return {
    totalJobs,
    totalApplications,
    avgApplicants,
    mostPopularType: formattedType
  }
})

onMounted(() => {
  fetchJobsWithApplicants()
})

const openCreateModal = () => {
  editingJob.value = null
  isCreateModalOpen.value = true
}

const openEditModal = (job: Job) => {
  editingJob.value = job
  isCreateModalOpen.value = true
}

const closeCreateModal = () => {
  isCreateModalOpen.value = false
  editingJob.value = null
}

const openApplicantsModal = (job: Job) => {
  selectedJob.value = job
  isApplicantsModalOpen.value = true
}

const closeApplicantsModal = () => {
  isApplicantsModalOpen.value = false
  selectedJob.value = null
}

const handleJobCreated = () => {
  fetchJobsWithApplicants()
}

const handleJobUpdated = () => {
  fetchJobsWithApplicants()
}

const handleDeleteJob = (jobId: string) => {
  deleteJobId.value = jobId
  showDeleteConfirm.value = true
}

const confirmDelete = async () => {
  if (deleteJobId.value) {
    try {
      await deleteJob(deleteJobId.value)
      showDeleteConfirm.value = false
      deleteJobId.value = null
    } catch (e) {
      console.error('Failed to delete job:', e)
    }
  }
}
</script>

