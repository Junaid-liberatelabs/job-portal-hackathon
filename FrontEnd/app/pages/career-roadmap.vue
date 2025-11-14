<template>
  <div class="relative bg-ink-50 min-h-screen py-8">
    <div class="mx-auto flex max-w-7xl flex-col gap-8 px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="rounded-3xl border border-white/70 bg-white/80 p-8 shadow-lg backdrop-blur">
        <div class="space-y-2">
          <h1 class="font-display text-3xl font-semibold text-ink-900">Career Roadmap</h1>
          <p class="text-sm text-ink-500">Generate and visualize your personalized career development path with interactive roadmap.</p>
        </div>
      </div>

      <!-- Form Section -->
      <div v-if="!roadmap" class="rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(168,85,247,0.22)] backdrop-blur">
        <form @submit.prevent="handleGenerateRoadmap" class="space-y-6">
          <div class="space-y-4">
            <div>
              <label for="timeframe" class="block text-sm font-medium text-ink-700 mb-2">
                Timeframe
              </label>
              <input
                id="timeframe"
                v-model="formData.timeframe"
                type="text"
                required
                placeholder="e.g., 6 months, 1 year, 2 years"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-ink-900 placeholder:text-ink-400 focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-500/20"
              />
            </div>
            <div>
              <label for="available_learning_time" class="block text-sm font-medium text-ink-700 mb-2">
                Available Learning Time
              </label>
              <input
                id="available_learning_time"
                v-model="formData.available_learning_time"
                type="text"
                required
                placeholder="e.g., 10 hours per week, 2 hours per day"
                class="w-full rounded-xl border border-ink-200 bg-white px-4 py-3 text-ink-900 placeholder:text-ink-400 focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-500/20"
              />
            </div>
          </div>
          <Button 
            type="submit"
            :disabled="loading"
            variant="gradient"
            class="w-full"
            size="lg"
          >
            <span v-if="loading" class="flex items-center justify-center gap-2">
              <span class="h-5 w-5 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              Generating Roadmap...
            </span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
              </svg>
              Generate Career Roadmap
            </span>
          </Button>
        </form>
      </div>

      <!-- Error Display -->
      <div v-if="error" class="rounded-xl border border-red-200 bg-red-50 p-4">
        <div class="flex items-start gap-3">
          <svg class="h-5 w-5 text-red-600 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-sm text-red-700">{{ error }}</p>
        </div>
      </div>

      <!-- Roadmap Content -->
      <div v-if="roadmap" class="space-y-6">
        <!-- Graph Visualization -->
        <div v-if="roadmap.graph_data && roadmap.graph_data.nodes.length > 0" class="rounded-[32px] border border-white/70 bg-white/80 p-6 shadow-lg backdrop-blur">
          <h2 class="font-display text-2xl font-semibold text-ink-900 mb-4">Roadmap Visualization</h2>
          <div ref="networkContainer" class="w-full h-[600px] rounded-xl border border-ink-200 bg-white"></div>
        </div>

        <!-- Report Section -->
        <div class="rounded-2xl border border-white/70 bg-white shadow-sm overflow-hidden">
          <div class="p-8">
            <h2 class="font-display text-2xl font-semibold text-ink-900 mb-6">Career Roadmap Report</h2>
            <div class="prose prose-base max-w-none prose-headings:font-display prose-headings:text-ink-900 prose-h1:text-3xl prose-h2:text-2xl prose-h3:text-xl prose-p:text-ink-700 prose-strong:text-ink-900 prose-ul:text-ink-700 prose-ol:text-ink-700 prose-li:text-ink-700 prose-code:text-brand-600 prose-code:bg-brand-50 prose-code:px-1.5 prose-code:py-1 prose-code:rounded prose-code:text-sm prose-pre:bg-ink-900 prose-pre:text-ink-50 prose-pre:rounded-lg prose-blockquote:border-l-4 prose-blockquote:border-brand-500 prose-blockquote:pl-4 prose-blockquote:text-ink-600 prose-a:text-brand-600 prose-a:no-underline hover:prose-a:underline prose-table:w-full prose-th:bg-ink-100 prose-th:text-ink-900 prose-th:font-semibold prose-td:border-t prose-td:border-ink-200" v-html="renderedMarkdown"></div>
          </div>
        </div>

        <!-- Regenerate Button -->
        <div class="flex gap-4">
          <Button 
            @click="handleRegenerate"
            variant="outline"
            class="flex-1"
            size="lg"
          >
            <svg class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Regenerate Roadmap
          </Button>
          <Button 
            @click="handleRefresh"
            :disabled="loading"
            variant="outline"
            class="flex-1"
            size="lg"
          >
            <span v-if="loading" class="flex items-center justify-center gap-2">
              <span class="h-5 w-5 animate-spin rounded-full border-2 border-brand-500 border-t-transparent"></span>
              Refreshing...
            </span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              Refresh
            </span>
          </Button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else-if="!loading && !error" class="rounded-2xl border border-ink-200 bg-ink-50 p-16 text-center">
        <svg class="mx-auto h-20 w-20 text-ink-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
        </svg>
        <h3 class="mt-6 text-lg font-semibold text-ink-900">No roadmap yet</h3>
        <p class="mt-2 text-sm text-ink-600 max-w-md mx-auto">Fill out the form above to generate your personalized career roadmap based on your profile and goals.</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { definePageMeta } from '#imports'
import { useCareerRoadmap } from '~/composables/useCareerRoadmap'
import Button from '~/components/ui/Button.vue'
import { marked } from 'marked'
import { Network } from 'vis-network'
import 'vis-network/styles/vis-network.min.css'

definePageMeta({
  middleware: 'auth'
})

const { roadmap, loading, error, generateRoadmap, fetchRoadmap } = useCareerRoadmap()

const formData = ref({
  timeframe: '',
  available_learning_time: ''
})

const networkContainer = ref<HTMLElement | null>(null)
let network: Network | null = null

const renderedMarkdown = computed(() => {
  if (!roadmap.value?.career_roadmap_report) return ''
  try {
    return marked.parse(roadmap.value.career_roadmap_report)
  } catch (err) {
    console.error('Error rendering markdown:', err)
    return roadmap.value.career_roadmap_report
  }
})

const getNodeColor = (type: string): string => {
  const colorMap: Record<string, string> = {
    milestone: '#8B5CF6',
    skill: '#10B981',
    course: '#3B82F6',
    certification: '#F59E0B',
    goal: '#EF4444',
    phase: '#6366F1'
  }
  return colorMap[type.toLowerCase()] || '#6B7280'
}

const initializeNetwork = () => {
  if (!networkContainer.value || !roadmap.value?.graph_data) return

  const graphData = roadmap.value.graph_data
  if (graphData.nodes.length === 0) return

  const nodes = graphData.nodes.map(node => ({
    id: node.id,
    label: node.label,
    title: node.description || node.label,
    color: {
      background: getNodeColor(node.type),
      border: getNodeColor(node.type),
      highlight: {
        background: getNodeColor(node.type),
        border: getNodeColor(node.type)
      }
    },
    shape: 'box',
    font: {
      color: '#FFFFFF',
      size: 14
    },
    margin: 10,
    widthConstraint: {
      minimum: 100,
      maximum: 200
    }
  }))

  const edges = graphData.edges.map(edge => ({
    from: edge.source,
    to: edge.target,
    label: edge.label || '',
    arrows: 'to',
    color: {
      color: '#9CA3AF',
      highlight: '#6366F1'
    },
    font: {
      align: 'middle',
      size: 12
    }
  }))

  const data = {
    nodes: nodes,
    edges: edges
  }

  const options = {
    nodes: {
      shape: 'box',
      font: {
        size: 14,
        color: '#FFFFFF'
      },
      borderWidth: 2,
      shadow: true
    },
    edges: {
      arrows: {
        to: {
          enabled: true,
          scaleFactor: 1.2
        }
      },
      smooth: {
        type: 'cubicBezier',
        forceDirection: 'horizontal',
        roundness: 0.4
      },
      shadow: true
    },
    layout: {
      hierarchical: {
        enabled: true,
        direction: 'LR',
        sortMethod: 'directed',
        levelSeparation: 150,
        nodeSpacing: 200,
        treeSpacing: 200,
        blockShifting: true,
        edgeMinimization: true,
        parentCentralization: true
      }
    },
    physics: {
      enabled: false
    },
    interaction: {
      dragNodes: true,
      dragView: true,
      zoomView: true
    }
  }

  network = new Network(networkContainer.value, data, options)
}

const handleGenerateRoadmap = async () => {
  try {
    await generateRoadmap(formData.value)
    await nextTick()
    initializeNetwork()
  } catch (err) {
    console.error('Error generating roadmap:', err)
  }
}

const handleRegenerate = () => {
  roadmap.value = null
  formData.value = {
    timeframe: '',
    available_learning_time: ''
  }
  if (network) {
    network.destroy()
    network = null
  }
}

const handleRefresh = async () => {
  await fetchRoadmap()
  await nextTick()
  if (network) {
    network.destroy()
    network = null
  }
  initializeNetwork()
}

watch(() => roadmap.value?.graph_data, () => {
  if (network) {
    network.destroy()
    network = null
  }
  nextTick(() => {
    initializeNetwork()
  })
}, { deep: true })

onMounted(async () => {
  await fetchRoadmap()
  await nextTick()
  initializeNetwork()
})

onBeforeUnmount(() => {
  if (network) {
    network.destroy()
    network = null
  }
})
</script>

