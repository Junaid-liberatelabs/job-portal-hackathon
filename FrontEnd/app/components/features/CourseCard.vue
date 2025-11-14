<template>
  <div 
    class="group relative overflow-hidden rounded-[24px] border border-ink-100 bg-white p-6 shadow-[0_2px_8px_rgba(0,0,0,0.04)] transition-all duration-500 hover:shadow-[0_20px_60px_rgba(16,185,129,0.15)] hover:-translate-y-2 cursor-pointer"
    @click="$emit('click', resource)"
  >
    <!-- Gradient accent line -->
    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-accent via-emerald-400 to-green-500 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
    
    <!-- Floating background gradient -->
    <div class="absolute -bottom-20 -left-20 w-40 h-40 bg-gradient-to-tr from-accent/5 to-emerald-500/5 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
    
    <div class="relative space-y-4">
      <!-- Header Section with Bookmark -->
      <div class="flex items-start justify-between gap-3">
        <div class="flex-1 min-w-0">
          <h3 class="text-lg font-bold text-ink-900 mb-2 line-clamp-2 group-hover:text-accent transition-colors duration-300">
            {{ resource.name }}
          </h3>
          <p class="text-sm text-ink-600 leading-relaxed line-clamp-3">
            {{ resource.description }}
          </p>
        </div>
        
        <!-- Match Badge and Bookmark -->
        <div class="flex flex-col items-end gap-2 shrink-0">
          <div v-if="matchPercentage !== null && matchPercentage > 0" :class="matchBadgeClasses">
            <span class="text-sm font-bold">{{ matchPercentage }}%</span>
            <span class="text-[10px] font-semibold opacity-90">MATCH</span>
          </div>
          <button
            @click.stop="$emit('bookmark', resource)"
            class="text-ink-400 hover:text-accent transition-all duration-300 p-2 rounded-xl hover:bg-accent/5 group/bookmark"
            :aria-label="isBookmarked ? 'Remove bookmark' : 'Bookmark resource'"
          >
            <BookmarkIcon v-if="!isBookmarked" class="h-5 w-5 group-hover/bookmark:scale-110 transition-transform" />
            <BookmarkSolidIcon v-else class="h-5 w-5 text-accent group-hover/bookmark:scale-110 transition-transform" />
          </button>
        </div>
      </div>
      
      <!-- Tags Section -->
      <div class="flex flex-wrap gap-2">
        <span
          v-for="tag in resource.tags.slice(0, 4)"
          :key="tag"
          class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-gradient-to-r from-accent/10 to-emerald-500/10 text-accent border border-accent/20 hover:border-accent/40 hover:shadow-md transition-all duration-300"
        >
          {{ tag }}
        </span>
        <span v-if="resource.tags.length > 4" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-ink-100 text-ink-600">
          +{{ resource.tags.length - 4 }}
        </span>
      </div>
      
      <!-- Footer Actions -->
      <div class="flex items-center justify-between pt-3 border-t border-ink-100/50">
        <div class="flex items-center gap-2 text-xs text-ink-500">
          <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-ink-50 group-hover:bg-accent/5 transition-colors duration-300">
            <LinkIcon class="h-3.5 w-3.5" />
            <span class="truncate max-w-[150px] font-medium">{{ extractDomain(resource.url) }}</span>
          </div>
        </div>
        
        <button
          @click.stop="handleViewResource"
          class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-accent to-emerald-600 hover:from-emerald-600 hover:to-accent text-white text-xs font-semibold rounded-xl shadow-md hover:shadow-xl transition-all duration-300 hover:scale-105"
        >
          <span>View Resource</span>
          <svg class="h-3.5 w-3.5 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { BookmarkIcon, LinkIcon } from '@heroicons/vue/24/outline'
import { BookmarkIcon as BookmarkSolidIcon } from '@heroicons/vue/24/solid'
import type { Resource } from '~/composables/useResources'

interface Props {
  resource: Resource
  isBookmarked?: boolean
  similarityScore?: number | null // Backend similarity score (0-1)
}

const props = withDefaults(defineProps<Props>(), {
  isBookmarked: false,
  similarityScore: null
})

const emit = defineEmits<{
  click: [resource: Resource]
  bookmark: [resource: Resource]
  view: [resource: Resource]
}>()

const matchPercentage = computed(() => {
  // Use backend similarity score if available
  if (props.similarityScore !== null && props.similarityScore !== undefined) {
    return Math.round(props.similarityScore * 100)
  }
  return null
})

const matchBadgeClasses = computed(() => {
  const base = 'flex flex-col items-center justify-center px-4 py-2 rounded-xl text-white shadow-lg transition-all duration-300 group-hover:scale-110'
  
  if (matchPercentage.value === null) return `${base} bg-gradient-to-br from-ink-400 to-ink-500`
  
  if (matchPercentage.value >= 70) return `${base} bg-gradient-to-br from-green-500 to-emerald-600 shadow-green-500/30`
  if (matchPercentage.value >= 40) return `${base} bg-gradient-to-br from-emerald-500 to-green-600 shadow-emerald-500/30`
  return `${base} bg-gradient-to-br from-amber-500 to-orange-600 shadow-amber-500/30`
})

const extractDomain = (url: string): string => {
  try {
    const urlObj = new URL(url)
    return urlObj.hostname.replace('www.', '')
  } catch {
    return url
  }
}

const handleViewResource = () => {
  emit('view', props.resource)
  // Open in new tab
  window.open(props.resource.url, '_blank', 'noopener,noreferrer')
}
</script>

