<template>
  <div class="relative bg-ink-50 min-h-screen py-8">
    <div class="mx-auto flex max-w-5xl flex-col gap-8 px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="rounded-3xl border border-white/70 bg-white/80 p-8 shadow-lg backdrop-blur">
        <div class="space-y-2">
          <h1 class="font-display text-3xl font-semibold text-ink-900">Skill Gap Analysis</h1>
          <p class="text-sm text-ink-500">Analyze your skills against job requirements to identify gaps and opportunities for growth.</p>
        </div>
      </div>

      <!-- Main Content -->
      <div class="space-y-6">
        <div class="mx-auto max-w-md rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(168,85,247,0.22)] backdrop-blur">
          <div class="flex flex-col gap-4">
            <Button 
              @click="handleRunSkillGapAnalysis" 
              :disabled="skillGapAnalysisLoading"
              variant="gradient"
              class="w-full"
              size="lg"
            >
              <span v-if="skillGapAnalysisLoading" class="flex items-center justify-center gap-2">
                <span class="h-5 w-5 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
                Analyzing...
              </span>
              <span v-else class="flex items-center justify-center gap-2">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
                </svg>
                Run Skill Gap Analysis
              </span>
            </Button>
            <Button 
              v-if="skillGapReport" 
              @click="handleRefreshReport" 
              :disabled="skillGapReportLoading"
              variant="outline"
              class="w-full"
              size="lg"
            >
              <span v-if="skillGapReportLoading" class="flex items-center justify-center gap-2">
                <span class="h-5 w-5 animate-spin rounded-full border-2 border-brand-500 border-t-transparent"></span>
                Refreshing...
              </span>
              <span v-else class="flex items-center justify-center gap-2">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                Refresh Report
              </span>
            </Button>
          </div>
        </div>

        <div v-if="skillGapError" class="rounded-xl border border-red-200 bg-red-50 p-4">
          <div class="flex items-start gap-3">
            <svg class="h-5 w-5 text-red-600 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p class="text-sm text-red-700">{{ skillGapError }}</p>
          </div>
        </div>

        <div v-if="skillGapReport" class="rounded-2xl border border-white/70 bg-white shadow-sm overflow-hidden">
          <div class="p-8">
            <div class="prose prose-base max-w-none prose-headings:font-display prose-headings:text-ink-900 prose-h1:text-3xl prose-h2:text-2xl prose-h3:text-xl prose-p:text-ink-700 prose-strong:text-ink-900 prose-ul:text-ink-700 prose-ol:text-ink-700 prose-li:text-ink-700 prose-code:text-brand-600 prose-code:bg-brand-50 prose-code:px-1.5 prose-code:py-1 prose-code:rounded prose-code:text-sm prose-pre:bg-ink-900 prose-pre:text-ink-50 prose-pre:rounded-lg prose-blockquote:border-l-4 prose-blockquote:border-brand-500 prose-blockquote:pl-4 prose-blockquote:text-ink-600 prose-a:text-brand-600 prose-a:no-underline hover:prose-a:underline prose-table:w-full prose-th:bg-ink-100 prose-th:text-ink-900 prose-th:font-semibold prose-td:border-t prose-td:border-ink-200" v-html="renderedMarkdown"></div>
          </div>
        </div>

        <div v-else-if="!skillGapAnalysisLoading && !skillGapReportLoading" class="rounded-2xl border border-ink-200 bg-ink-50 p-16 text-center">
          <svg class="mx-auto h-20 w-20 text-ink-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 class="mt-6 text-lg font-semibold text-ink-900">No analysis report yet</h3>
          <p class="mt-2 text-sm text-ink-600 max-w-md mx-auto">Click "Run Skill Gap Analysis" to generate your personalized skill gap report based on your profile and job applications.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { definePageMeta } from '#imports'
import { useApi } from '~/composables/useApi'
import Button from '~/components/ui/Button.vue'
import { marked } from 'marked'

definePageMeta({
  middleware: 'auth'
})

const api = useApi()

// Skill Gap Analysis
const skillGapReport = ref<string | null>(null)
const skillGapAnalysisLoading = ref(false)
const skillGapReportLoading = ref(false)
const skillGapError = ref<string | null>(null)

const renderedMarkdown = computed(() => {
  if (!skillGapReport.value) return ''
  try {
    return marked.parse(skillGapReport.value)
  } catch (error) {
    console.error('Error rendering markdown:', error)
    return skillGapReport.value
  }
})

const handleRunSkillGapAnalysis = async () => {
  skillGapAnalysisLoading.value = true
  skillGapError.value = null
  
  try {
    const response = await api<{ gap_analysis_report: string }>('/skill-gap-analysis/skill-gap-analysis', {
      method: 'POST'
    })
    
    skillGapReport.value = response.gap_analysis_report
    skillGapError.value = null
  } catch (error: any) {
    console.error('Error running skill gap analysis:', error)
    skillGapError.value = error?.response?._data?.detail || 'Failed to run skill gap analysis. Please try again.'
    skillGapReport.value = null
  } finally {
    skillGapAnalysisLoading.value = false
  }
}

const handleRefreshReport = async () => {
  skillGapReportLoading.value = true
  skillGapError.value = null
  
  try {
    const response = await api<{ gap_analysis_report: string }>('/skill-gap-analysis/skill-gap-analysis/')
    skillGapReport.value = response.gap_analysis_report
    skillGapError.value = null
  } catch (error: any) {
    console.error('Error fetching skill gap report:', error)
    if (error?.response?.status === 404) {
      skillGapError.value = null
      skillGapReport.value = null
    } else {
      skillGapError.value = error?.response?._data?.detail || 'Failed to fetch skill gap report. Please try again.'
    }
  } finally {
    skillGapReportLoading.value = false
  }
}

// Load existing report on mount
onMounted(async () => {
  await handleRefreshReport()
})
</script>

