import type { Ref } from 'vue'
import type { ExperienceLevel, JobType } from '~/stores/auth'

export type JobLocation = 'remote' | 'hybrid' | 'on_site'

export interface Job {
  id: string
  title: string
  description: string
  company: string
  job_type: JobType
  job_location: JobLocation | null
  required_skills: string[]
  url: string | null
  recommended_experience_level: ExperienceLevel
  salary_range_min: number | null
  salary_range_max: number | null
  created_at: string
  updated_at: string
}

export interface JobFilters {
  skip?: number
  limit?: number
  job_type?: JobType
  experience_level?: ExperienceLevel
  skills?: string | string[] // Can be comma-separated string or array (will be converted to string)
}

export const useJobs = () => {
  const api = useApi()
  const jobs = ref<Job[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const fetchJobs = async (filters?: JobFilters) => {
    loading.value = true
    error.value = null
    
    try {
      const query: Record<string, any> = {}
      
      if (filters?.skip !== undefined) query.skip = filters.skip
      if (filters?.limit !== undefined) query.limit = filters.limit
      if (filters?.job_type) query.job_type = filters.job_type
      if (filters?.experience_level) query.experience_level = filters.experience_level
      
      // Convert skills array to comma-separated string if needed
      if (filters?.skills) {
        if (Array.isArray(filters.skills)) {
          query.skills = filters.skills.join(',')
        } else {
          query.skills = filters.skills
        }
      }
      
      const data = await api<Job[]>('/jobs/', { query })
      jobs.value = data || []
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch jobs'
      return []
    } finally {
      loading.value = false
    }
  }

  const fetchJobById = async (id: string) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await api<Job>(`/jobs/${id}`)
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch job details'
      return null
    } finally {
      loading.value = false
    }
  }

  const getSimilarJobs = async (jobId: string, limit: number = 5) => {
    loading.value = true
    error.value = null
    
    try {
      const query: Record<string, any> = { limit }
      const data = await api<Array<{ job: Job; similarity_score: number }>>(`/jobs/${jobId}/similar`, { query })
      return data || []
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch similar jobs'
      return []
    } finally {
      loading.value = false
    }
  }

  const getJobRecommendations = async (limit: number = 10) => {
    loading.value = true
    error.value = null
    
    try {
      const query: Record<string, any> = { limit }
      const data = await api<Array<{ job: Job; similarity_score: number }>>('/recommendations/jobs', { query })
      return data || []
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch job recommendations'
      return []
    } finally {
      loading.value = false
    }
  }

  const calculateSkillMatch = (job: Job, userSkills: string[]): number => {
    if (!userSkills || userSkills.length === 0) return 0
    if (!job.required_skills || job.required_skills.length === 0) return 0

    const normalizedUserSkills = userSkills.map(s => s.toLowerCase().trim())
    const normalizedJobSkills = job.required_skills.map(s => s.toLowerCase().trim())

    const matchingSkills = normalizedJobSkills.filter(skill =>
      normalizedUserSkills.some(userSkill => 
        userSkill.includes(skill) || skill.includes(userSkill)
      )
    )

    return Math.round((matchingSkills.length / normalizedJobSkills.length) * 100)
  }

  const formatJobType = (type: JobType): string => {
    const typeMap: Record<JobType, string> = {
      internship: 'Internship',
      part_time: 'Part-time',
      full_time: 'Full-time',
      freelance: 'Freelance'
    }
    return typeMap[type] || type
  }

  const formatLocation = (location: JobLocation | null): string => {
    if (!location) return 'Not specified'
    
    const locationMap: Record<JobLocation, string> = {
      remote: 'Remote',
      hybrid: 'Hybrid',
      on_site: 'On-site'
    }
    return locationMap[location] || location
  }

  const formatSalaryRange = (min: number | null, max: number | null): string => {
    if (!min && !max) return 'Not disclosed'
    if (!max) return `$${min?.toLocaleString()}+`
    if (!min) return `Up to $${max?.toLocaleString()}`
    return `$${min.toLocaleString()} - $${max.toLocaleString()}`
  }

  return {
    jobs,
    loading,
    error,
    fetchJobs,
    fetchJobById,
    getSimilarJobs,
    getJobRecommendations,
    calculateSkillMatch,
    formatJobType,
    formatLocation,
    formatSalaryRange
  }
}

