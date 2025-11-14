import {
  mdiCodeBraces,
  mdiChartBox,
  mdiPalette,
  mdiCellphone,
  mdiBriefcase,
  mdiHandshake,
  mdiTag,
  mdiCurrencyUsd,
  mdiVideo,
  mdiFileDocument,
  mdiBookOpen,
  mdiSchool,
  mdiTagOutline
} from '@mdi/js'

export interface Resource {
  id: string
  name: string
  description: string
  url: string
  tags: string[]
  created_at: string
  updated_at: string
}

export interface ResourceFilters {
  tags?: string[]
  search?: string
}

export const useResources = () => {
  const api = useApi()
  const resources = ref<Resource[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const allTags = computed(() => {
    const tagsSet = new Set<string>()
    resources.value.forEach(resource => {
      resource.tags.forEach(tag => tagsSet.add(tag))
    })
    return Array.from(tagsSet).sort()
  })

  const fetchResources = async (filters?: ResourceFilters) => {
    loading.value = true
    error.value = null
    
    try {
      const params = new URLSearchParams()
      
      if (filters?.search) params.append('search', filters.search)
      if (filters?.tags && filters.tags.length > 0) {
        filters.tags.forEach(tag => params.append('tags', tag))
      }
      
      const queryString = params.toString()
      const url = queryString ? `/resources?${queryString}` : '/resources'
      
      const data = await api<Resource[]>(url)
      resources.value = data || []
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch resources'
      return []
    } finally {
      loading.value = false
    }
  }

  const fetchResourceById = async (id: string) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await api<Resource>(`/resources/${id}`)
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch resource details'
      return null
    } finally {
      loading.value = false
    }
  }

  const getRecommendedResources = async () => {
    loading.value = true
    error.value = null
    
    try {
      const data = await api<Resource[]>('/resources/recommended')
      return data || []
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch recommended resources'
      return []
    } finally {
      loading.value = false
    }
  }

  const filterByCategory = (category: string) => {
    return resources.value.filter(resource =>
      resource.tags.some(tag => tag.toLowerCase() === category.toLowerCase())
    )
  }

  const searchResources = (query: string) => {
    if (!query) return resources.value
    
    const lowerQuery = query.toLowerCase()
    return resources.value.filter(resource =>
      resource.name.toLowerCase().includes(lowerQuery) ||
      resource.description.toLowerCase().includes(lowerQuery) ||
      resource.tags.some(tag => tag.toLowerCase().includes(lowerQuery))
    )
  }

  const getCategoryIcon = (category: string): string => {
    const iconMap: Record<string, string> = {
      'programming': mdiCodeBraces,
      'data-science': mdiChartBox,
      'design': mdiPalette,
      'marketing': mdiCellphone,
      'business': mdiBriefcase,
      'soft-skills': mdiHandshake,
      'free': mdiTag,
      'paid': mdiCurrencyUsd,
      'video': mdiVideo,
      'article': mdiFileDocument,
      'course': mdiBookOpen,
      'tutorial': mdiSchool
    }
    return iconMap[category.toLowerCase()] || mdiTagOutline
  }

  return {
    resources,
    loading,
    error,
    allTags,
    fetchResources,
    fetchResourceById,
    getRecommendedResources,
    filterByCategory,
    searchResources,
    getCategoryIcon
  }
}

