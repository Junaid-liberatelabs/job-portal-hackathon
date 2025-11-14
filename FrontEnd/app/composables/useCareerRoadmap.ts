import { ref } from 'vue'
import { useApi } from './useApi'

export interface CareerRoadmapRequest {
  timeframe: string
  available_learning_time: string
}

export interface GraphNode {
  id: string
  label: string
  type: string
  description?: string | null
  metadata?: Record<string, any> | null
}

export interface GraphEdge {
  source: string
  target: string
  label?: string | null
  type?: string | null
}

export interface CareerRoadmapGraphData {
  nodes: GraphNode[]
  edges: GraphEdge[]
}

export interface CareerRoadmapResponse {
  career_roadmap_report: string
  graph_data?: CareerRoadmapGraphData | null
}

export const useCareerRoadmap = () => {
  const api = useApi()
  const roadmap = ref<CareerRoadmapResponse | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  const generateRoadmap = async (request: CareerRoadmapRequest) => {
    loading.value = true
    error.value = null
    
    try {
      const data = await api<CareerRoadmapResponse>('/career-roadmap/career-roadmap', {
        method: 'POST',
        body: request
      })
      roadmap.value = data
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to generate career roadmap'
      throw err
    } finally {
      loading.value = false
    }
  }

  const fetchRoadmap = async () => {
    loading.value = true
    error.value = null
    
    try {
      const data = await api<CareerRoadmapResponse>('/career-roadmap/career-roadmap')
      roadmap.value = data
      return data
    } catch (err: any) {
      if (err?.response?.status === 404) {
        roadmap.value = null
        error.value = null
      } else {
        error.value = err?.response?._data?.detail ?? 'Failed to fetch career roadmap'
      }
      return null
    } finally {
      loading.value = false
    }
  }

  return {
    roadmap,
    loading,
    error,
    generateRoadmap,
    fetchRoadmap
  }
}

