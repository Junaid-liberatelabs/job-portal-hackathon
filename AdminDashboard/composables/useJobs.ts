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

interface JobFormData {
  title: string
  description: string
  company: string
  job_type: string
  job_location?: string
  required_skills: string[]
  recommended_experience_level: string
  salary_range_min?: number
  salary_range_max?: number
}

export const useJobs = () => {
  const apiFetch = useAdminApi()
  
  const jobsWithApplicants = ref<JobWithApplicantsCount[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const fetchJobsWithApplicants = async () => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<JobWithApplicantsCount[]>('/applications/dashboard', {
        method: 'GET'
      })
      jobsWithApplicants.value = data
      return data
    } catch (e: any) {
      error.value = e.message || 'Failed to fetch jobs'
      throw e
    } finally {
      loading.value = false
    }
  }

  const createJob = async (jobData: JobFormData) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<Job>('/jobs/', {
        method: 'POST',
        body: jobData
      })
      await fetchJobsWithApplicants()
      return data
    } catch (e: any) {
      error.value = e.data?.detail || e.message || 'Failed to create job'
      throw e
    } finally {
      loading.value = false
    }
  }

  const updateJob = async (jobId: string, jobData: Partial<JobFormData>) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<Job>(`/jobs/${jobId}`, {
        method: 'PUT',
        body: jobData
      })
      await fetchJobsWithApplicants()
      return data
    } catch (e: any) {
      error.value = e.data?.detail || e.message || 'Failed to update job'
      throw e
    } finally {
      loading.value = false
    }
  }

  const deleteJob = async (jobId: string) => {
    loading.value = true
    error.value = null
    
    try {
      await apiFetch(`/jobs/${jobId}`, {
        method: 'DELETE'
      })
      await fetchJobsWithApplicants()
    } catch (e: any) {
      error.value = e.data?.detail || e.message || 'Failed to delete job'
      throw e
    } finally {
      loading.value = false
    }
  }

  return {
    jobsWithApplicants,
    loading,
    error,
    fetchJobsWithApplicants,
    createJob,
    updateJob,
    deleteJob
  }
}

