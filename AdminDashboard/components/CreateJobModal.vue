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
        @click.self="closeModal"
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
            class="bg-white rounded-2xl shadow-2xl max-w-4xl w-full my-8 max-h-[90vh] overflow-y-auto scrollbar-thin"
          >
            <div class="sticky top-0 bg-white border-b border-ink-200 px-6 py-4 flex items-center justify-between z-10">
              <h2 class="text-2xl font-bold text-ink-900">
                {{ editMode ? 'Edit Job' : 'Create New Job' }}
              </h2>
              <button
                @click="closeModal"
                class="p-2 hover:bg-ink-100 rounded-lg transition-colors"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <form @submit.prevent="handleSubmit" class="p-6 space-y-6">
              <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
                <p class="text-sm text-red-800">{{ error }}</p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Job Title <span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="formData.title"
                    type="text"
                    required
                    class="input"
                    placeholder="e.g., Frontend Developer"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Company <span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="formData.company"
                    type="text"
                    required
                    class="input"
                    placeholder="e.g., Tech Corp"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Job Type <span class="text-red-500">*</span>
                  </label>
                  <select v-model="formData.job_type" required class="input">
                    <option value="">Select type</option>
                    <option value="FULL_TIME">Full Time</option>
                    <option value="PART_TIME">Part Time</option>
                    <option value="INTERNSHIP">Internship</option>
                    <option value="FREELANCE">Freelance</option>
                  </select>
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Job Location
                  </label>
                  <select v-model="formData.job_location" class="input">
                    <option value="">Select location</option>
                    <option value="REMOTE">Remote</option>
                    <option value="HYBRID">Hybrid</option>
                    <option value="ON_SITE">On-site</option>
                  </select>
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Experience Level <span class="text-red-500">*</span>
                  </label>
                  <select v-model="formData.recommended_experience_level" required class="input">
                    <option value="">Select level</option>
                    <option value="STUDENT">Student</option>
                    <option value="ENTRY">Entry</option>
                    <option value="JUNIOR">Junior</option>
                  </select>
                </div>

                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Description <span class="text-red-500">*</span>
                  </label>
                  <textarea
                    v-model="formData.description"
                    required
                    rows="4"
                    class="input"
                    placeholder="Describe the role, responsibilities, and requirements..."
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Minimum Salary
                  </label>
                  <input
                    v-model.number="formData.salary_range_min"
                    type="number"
                    class="input"
                    placeholder="e.g., 50000"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Maximum Salary
                  </label>
                  <input
                    v-model.number="formData.salary_range_max"
                    type="number"
                    class="input"
                    placeholder="e.g., 80000"
                  />
                </div>

                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Job URL <span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="formData.url"
                    type="url"
                    required
                    class="input"
                    placeholder="https://example.com/job-posting"
                  />
                </div>

                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Required Skills <span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="skillsInput"
                    type="text"
                    class="input mb-2"
                    placeholder="Type a skill and press Enter"
                    @keydown.enter.prevent="addSkill"
                  />
                  <div class="flex flex-wrap gap-2">
                    <span
                      v-for="(skill, index) in formData.required_skills"
                      :key="index"
                      class="inline-flex items-center gap-1 px-3 py-1 bg-admin-100 text-admin-800 rounded-full text-sm"
                    >
                      {{ skill }}
                      <button
                        type="button"
                        @click="removeSkill(index)"
                        class="hover:bg-admin-200 rounded-full p-0.5 transition-colors"
                      >
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </span>
                  </div>
                  <p v-if="formData.required_skills.length === 0" class="text-sm text-ink-500 mt-2">
                    Add at least one skill
                  </p>
                </div>
              </div>

              <div class="flex items-center justify-end gap-3 pt-4 border-t border-ink-200">
                <button
                  type="button"
                  @click="closeModal"
                  class="btn btn-secondary"
                  :disabled="loading"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  class="btn btn-primary"
                  :disabled="loading || formData.required_skills.length === 0 || !formData.url.trim()"
                >
                  <span v-if="loading">
                    {{ editMode ? 'Updating...' : 'Creating...' }}
                  </span>
                  <span v-else>
                    {{ editMode ? 'Update Job' : 'Create Job' }}
                  </span>
                </button>
              </div>
            </form>
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
  description: string
  company: string
  job_type: string
  job_location?: string
  url?: string
  required_skills: string[]
  recommended_experience_level: string
  salary_range_min?: number
  salary_range_max?: number
}

const props = defineProps<{
  isOpen: boolean
  editJob?: Job | null
}>()

const emit = defineEmits<{
  close: []
  'job-created': []
  'job-updated': []
}>()

const editMode = computed(() => !!props.editJob)

const formData = ref({
  title: '',
  description: '',
  company: '',
  job_type: '',
  job_location: '',
  url: '',
  required_skills: [] as string[],
  recommended_experience_level: '',
  salary_range_min: undefined as number | undefined,
  salary_range_max: undefined as number | undefined
})

const skillsInput = ref('')
const loading = ref(false)
const error = ref<string | null>(null)

watch(() => props.editJob, (job) => {
  if (job) {
    formData.value = {
      title: job.title,
      description: job.description,
      company: job.company,
      job_type: job.job_type,
      job_location: job.job_location || '',
      url: (job as any).url || '',
      required_skills: [...job.required_skills],
      recommended_experience_level: job.recommended_experience_level,
      salary_range_min: job.salary_range_min,
      salary_range_max: job.salary_range_max
    }
  }
}, { immediate: true })

watch(() => props.isOpen, (isOpen) => {
  if (!isOpen) {
    resetForm()
  }
})

const addSkill = () => {
  const skill = skillsInput.value.trim()
  if (skill && !formData.value.required_skills.includes(skill)) {
    formData.value.required_skills.push(skill)
    skillsInput.value = ''
  }
}

const removeSkill = (index: number) => {
  formData.value.required_skills.splice(index, 1)
}

const resetForm = () => {
  formData.value = {
    title: '',
    description: '',
    company: '',
    job_type: '',
    job_location: '',
    url: '',
    required_skills: [],
    recommended_experience_level: '',
    salary_range_min: undefined,
    salary_range_max: undefined
  }
  skillsInput.value = ''
  error.value = null
}

const closeModal = () => {
  emit('close')
}

const handleSubmit = async () => {
  error.value = null
  loading.value = true

  try {
    const { createJob, updateJob } = useJobs()
    
    // Convert enum values to lowercase as expected by backend
    const jobData = {
      title: formData.value.title.trim(),
      description: formData.value.description.trim(),
      company: formData.value.company.trim(),
      job_type: formData.value.job_type.toLowerCase(),
      job_location: formData.value.job_location && formData.value.job_location.trim() 
        ? formData.value.job_location.toLowerCase() 
        : undefined,
      url: formData.value.url.trim(),
      required_skills: formData.value.required_skills.filter(s => s.trim().length > 0),
      recommended_experience_level: formData.value.recommended_experience_level.toLowerCase(),
      salary_range_min: formData.value.salary_range_min ? Number(formData.value.salary_range_min) : undefined,
      salary_range_max: formData.value.salary_range_max ? Number(formData.value.salary_range_max) : undefined
    }

    if (editMode.value && props.editJob) {
      await updateJob(props.editJob.id, jobData)
      emit('job-updated')
    } else {
      await createJob(jobData)
      emit('job-created')
    }
    
    closeModal()
  } catch (e: any) {
    error.value = e.data?.detail || e.message || 'An error occurred'
  } finally {
    loading.value = false
  }
}
</script>

