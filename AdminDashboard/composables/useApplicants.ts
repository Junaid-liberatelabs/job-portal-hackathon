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

export const useApplicants = () => {
  const apiFetch = useAdminApi()
  
  const applicants = ref<ApplicantInfo[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const fetchApplicantsByJob = async (jobId: string) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<ApplicantInfo[]>(`/applications/job/${jobId}/applicants`, {
        method: 'GET'
      })
      applicants.value = data
      return data
    } catch (e: any) {
      error.value = e.message || 'Failed to fetch applicants'
      throw e
    } finally {
      loading.value = false
    }
  }

  return {
    applicants,
    loading,
    error,
    fetchApplicantsByJob
  }
}

