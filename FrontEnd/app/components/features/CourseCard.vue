<template>
  <Card :hover="true" :clickable="true" @click="$emit('click', resource)">
    <div class="space-y-4">
      <div class="flex items-start justify-between gap-3">
        <div class="flex-1 min-w-0">
          <h3 class="text-lg font-semibold text-ink-900 mb-2 line-clamp-2">
            {{ resource.name }}
          </h3>
          <p class="text-sm text-ink-600 line-clamp-3">
            {{ resource.description }}
          </p>
        </div>
        
        <button
          @click.stop="$emit('bookmark', resource)"
          class="text-ink-400 hover:text-accent transition-colors p-2 rounded-lg hover:bg-ink-50 shrink-0"
          :aria-label="isBookmarked ? 'Remove bookmark' : 'Bookmark resource'"
        >
          <BookmarkIcon v-if="!isBookmarked" class="h-5 w-5" />
          <BookmarkSolidIcon v-else class="h-5 w-5 text-accent" />
        </button>
      </div>
      
      <div class="flex flex-wrap gap-2">
        <span
          v-for="tag in resource.tags.slice(0, 4)"
          :key="tag"
          class="badge badge-primary text-xs"
        >
          {{ getCategoryIcon(tag) }} {{ tag }}
        </span>
        <span v-if="resource.tags.length > 4" class="badge badge-primary text-xs">
          +{{ resource.tags.length - 4 }}
        </span>
      </div>
      
      <div class="flex items-center justify-between pt-2 border-t border-ink-100">
        <div class="flex items-center gap-2 text-xs text-ink-500">
          <LinkIcon class="h-4 w-4" />
          <span class="truncate max-w-[200px]">{{ extractDomain(resource.url) }}</span>
        </div>
        
        <Button
          variant="outline"
          size="sm"
          @click.stop="handleViewResource"
        >
          View Resource
        </Button>
      </div>
    </div>
  </Card>
</template>

<script setup lang="ts">
import { BookmarkIcon, LinkIcon } from '@heroicons/vue/24/outline'
import { BookmarkIcon as BookmarkSolidIcon } from '@heroicons/vue/24/solid'
import type { Resource } from '~/composables/useResources'

interface Props {
  resource: Resource
  isBookmarked?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  isBookmarked: false
})

const emit = defineEmits<{
  click: [resource: Resource]
  bookmark: [resource: Resource]
  view: [resource: Resource]
}>()

const { getCategoryIcon } = useResources()

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

