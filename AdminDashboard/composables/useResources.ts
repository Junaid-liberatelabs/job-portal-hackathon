interface Resource {
  id: string
  name: string
  description: string
  url: string
  tags: string[]
  pricing?: string
  platform?: string
  duration?: string
  created_at: string
  updated_at: string
}

interface ResourceFormData {
  name: string
  description: string
  url: string
  tags: string[]
  pricing?: string
  platform?: string
  duration?: string
}

interface ResourceFilters {
  skip?: number
  limit?: number
  tags?: string
}

export const useResources = () => {
  const apiFetch = useAdminApi()
  
  const resources = ref<Resource[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const fetchResources = async (filters?: ResourceFilters) => {
    loading.value = true
    error.value = null
    
    try {
      const params = new URLSearchParams()
      if (filters?.skip !== undefined) params.append('skip', filters.skip.toString())
      if (filters?.limit !== undefined) params.append('limit', filters.limit.toString())
      if (filters?.tags) params.append('tags', filters.tags)
      
      const queryString = params.toString()
      const url = queryString ? `/resources/?${queryString}` : '/resources/'
      
      const data = await apiFetch<Resource[]>(url, {
        method: 'GET'
      })
      resources.value = data
      return data
    } catch (e: any) {
      error.value = e.message || 'Failed to fetch resources'
      throw e
    } finally {
      loading.value = false
    }
  }

  const getResourceById = async (resourceId: string) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<Resource>(`/resources/${resourceId}`, {
        method: 'GET'
      })
      return data
    } catch (e: any) {
      error.value = e.message || 'Failed to fetch resource'
      throw e
    } finally {
      loading.value = false
    }
  }

  const createResource = async (resourceData: ResourceFormData) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<Resource>('/resources/', {
        method: 'POST',
        body: resourceData
      })
      await fetchResources()
      return data
    } catch (e: any) {
      error.value = e.data?.detail || e.message || 'Failed to create resource'
      throw e
    } finally {
      loading.value = false
    }
  }

  const updateResource = async (resourceId: string, resourceData: Partial<ResourceFormData>) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await apiFetch<Resource>(`/resources/${resourceId}`, {
        method: 'PUT',
        body: resourceData
      })
      await fetchResources()
      return data
    } catch (e: any) {
      error.value = e.data?.detail || e.message || 'Failed to update resource'
      throw e
    } finally {
      loading.value = false
    }
  }

  const deleteResource = async (resourceId: string) => {
    loading.value = true
    error.value = null
    
    try {
      await apiFetch(`/resources/${resourceId}`, {
        method: 'DELETE'
      })
      await fetchResources()
    } catch (e: any) {
      error.value = e.data?.detail || e.message || 'Failed to delete resource'
      throw e
    } finally {
      loading.value = false
    }
  }

  return {
    resources,
    loading,
    error,
    fetchResources,
    getResourceById,
    createResource,
    updateResource,
    deleteResource
  }
}

