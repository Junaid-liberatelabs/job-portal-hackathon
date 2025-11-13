import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { useApi } from '~/composables/useApi'

export type ExperienceLevel = 'student' | 'entry' | 'junior'
export type JobType = 'internship' | 'part_time' | 'full_time' | 'freelance'

export type UserProfile = {
  id: string
  full_name: string
  email: string
  education_level: string
  preferred_career_track: string
  skills: string[]
  experience_level?: ExperienceLevel | null
  is_active: boolean
  created_at: string
  updated_at: string
}

export type RegisterPayload = {
  full_name: string
  email: string
  password: string
  education_level: string
  preferred_career_track: string
  skills?: string[]
}

export type UpdateProfilePayload = {
  full_name?: string | null
  education_level?: string | null
  preferred_career_track?: string | null
  experience_level?: ExperienceLevel | null
  skills?: string[] | null
}

export const useAuthStore = defineStore('auth', () => {
  const isClient = typeof window !== 'undefined'
  
  const token = ref<string | null>(isClient ? localStorage.getItem('ci_token') : null)
  const tokenType = ref<string | null>(isClient ? localStorage.getItem('ci_token_type') : 'Bearer')
  const user = ref<UserProfile | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  const isAuthenticated = computed(() => Boolean(token.value))

  const persistToken = () => {
    if (!isClient) return
    if (token.value) {
      localStorage.setItem('ci_token', token.value)
      localStorage.setItem('ci_token_type', tokenType.value ?? 'Bearer')
    } else {
      localStorage.removeItem('ci_token')
      localStorage.removeItem('ci_token_type')
    }
  }

  const setToken = (accessToken: string | null, type = 'Bearer') => {
    token.value = accessToken
    tokenType.value = accessToken ? type : null
    persistToken()
  }

  const api = useApi()

  const login = async (email: string, password: string) => {
    loading.value = true
    error.value = null
    try {
      const body = new URLSearchParams()
      body.set('username', email)
      body.set('password', password)
      body.set('grant_type', 'password')

      const response = await api<{ access_token: string; token_type: string }>('/auth/login', {
        method: 'POST',
        body,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        suppressAuthError: true
      })

      setToken(response.access_token, response.token_type ?? 'Bearer')
      await fetchProfile()
      return true
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Unable to sign in. Please check your credentials.'
      setToken(null)
      return false
    } finally {
      loading.value = false
    }
  }

  const register = async (payload: RegisterPayload) => {
    loading.value = true
    error.value = null
    try {
      console.log('Registration payload:', payload)
      const response = await api<UserProfile>('/auth/register', {
        method: 'POST',
        body: payload,
        suppressAuthError: true
      })
      console.log('Registration successful:', response)
      // Automatically log in after successful registration
      await login(payload.email, payload.password)
      return true
    } catch (err: any) {
      console.error('Registration error:', err)
      console.error('Error details:', err?.data)
      console.error('Error response:', err?.response)
      
      // Try to extract the most specific error message
      let errorMessage = 'Unable to create account. Please try again.'
      
      if (err?.data?.detail) {
        errorMessage = typeof err.data.detail === 'string' 
          ? err.data.detail 
          : JSON.stringify(err.data.detail)
      } else if (err?.response?._data?.detail) {
        errorMessage = typeof err.response._data.detail === 'string'
          ? err.response._data.detail
          : JSON.stringify(err.response._data.detail)
      } else if (err?.message) {
        errorMessage = err.message
      }
      
      error.value = errorMessage
      return false
    } finally {
      loading.value = false
    }
  }

  const fetchProfile = async () => {
    if (!token.value) return null
    try {
      const profile = await api<UserProfile>('/users/me')
      user.value = profile
      return profile
    } catch (err: any) {
      if (err?.response?.status === 401) {
        logout()
      } else {
        error.value = 'Failed to load profile.'
      }
      return null
    }
  }

  const updateProfile = async (payload: UpdateProfilePayload) => {
    if (!token.value) return null
    loading.value = true
    error.value = null
    try {
      const profile = await api<UserProfile>('/users/me', {
        method: 'PUT',
        body: payload
      })
      user.value = profile
      return profile
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Unable to update profile.'
      return null
    } finally {
      loading.value = false
    }
  }

  const addSkill = async (skill: string) => {
    if (!skill || !token.value) return null
    try {
      const profile = await api<UserProfile>(`/users/me/skills`, {
        method: 'POST',
        query: { skill }
      })
      user.value = profile
      return profile
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Unable to add skill.'
      return null
    }
  }

  const removeSkill = async (skill: string) => {
    if (!skill || !token.value) return null
    try {
      const profile = await api<UserProfile>(`/users/me/skills/${encodeURIComponent(skill)}`, {
        method: 'DELETE'
      })
      user.value = profile
      return profile
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Unable to remove skill.'
      return null
    }
  }

  const logout = () => {
    user.value = null
    setToken(null)
  }

  return {
    token,
    tokenType,
    user,
    loading,
    error,
    isAuthenticated,
    login,
    register,
    fetchProfile,
    updateProfile,
    addSkill,
    removeSkill,
    logout
  }
})
