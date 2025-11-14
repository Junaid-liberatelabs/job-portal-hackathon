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

interface JobFilters {
  skip?: number
  limit?: number
  job_type?: string
  experience_level?: string
  skills?: string
}

export const useJobs = () => {
  const apiFetch = useAdminApi()
  
  const jobsWithApplicants = ref<JobWithApplicantsCount[]>([])
  const jobs = ref<Job[]>([])
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

  const fetchJobs = async (filters?: JobFilters) => {
    loading.value = true
    error.value = null
    
    try {
      const params = new URLSearchParams()
      if (filters?.skip !== undefined) params.append('skip', filters.skip.toString())
      if (filters?.limit !== undefined) params.append('limit', filters.limit.toString())
      if (filters?.job_type) params.append('job_type', filters.job_type)
      if (filters?.experience_level) params.append('experience_level', filters.experience_level)
      if (filters?.skills) params.append('skills', filters.skills)
      
      const queryString = params.toString()
      const url = queryString ? `/jobs/?${queryString}` : '/jobs/'
      
      const data = await apiFetch<Job[]>(url, {
        method: 'GET'
      })
      jobs.value = data
      return data
    } catch (e: any) {
      error.value = e.message || 'Failed to fetch jobs'
      throw e
    } finally {
      loading.value = false
    }
  }

  const getJobById = async (jobId: string) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<Job>(`/jobs/${jobId}`, {
        method: 'GET'
      })
      return data
    } catch (e: any) {
      error.value = e.message || 'Failed to fetch job'
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
    jobs,
    loading,
    error,
    fetchJobsWithApplicants,
    fetchJobs,
    getJobById,
    createJob,
    updateJob,
    deleteJob
  }
}

