<template>
  <div class="card">
    <div class="card-header">
      <h3 class="text-lg font-semibold text-ink-900">Resources Overview</h3>
      <p class="text-sm text-ink-600 mt-1">Manage learning resources and educational content</p>
    </div>
    
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead class="bg-ink-50 border-b border-ink-200">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Name</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Description</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Tags</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Platform</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-ink-600 uppercase tracking-wider">Created</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-ink-600 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-ink-200">
          <tr v-for="resource in resources" :key="resource.id" class="hover:bg-ink-50 transition-colors">
            <td class="px-6 py-4">
              <div class="text-sm font-medium text-ink-900">{{ resource.name }}</div>
              <a
                :href="resource.url"
                target="_blank"
                rel="noopener noreferrer"
                class="text-xs text-admin-600 hover:text-admin-700 hover:underline mt-1 inline-flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                View Resource
              </a>
            </td>
            <td class="px-6 py-4">
              <div class="text-sm text-ink-700 line-clamp-2 max-w-md">{{ resource.description }}</div>
            </td>
            <td class="px-6 py-4">
              <div class="flex flex-wrap gap-1">
                <span
                  v-for="tag in resource.tags.slice(0, 3)"
                  :key="tag"
                  class="inline-flex items-center px-2 py-1 bg-purple-100 text-purple-800 rounded-full text-xs"
                >
                  {{ tag }}
                </span>
                <span
                  v-if="resource.tags.length > 3"
                  class="inline-flex items-center px-2 py-1 bg-ink-100 text-ink-600 rounded-full text-xs"
                >
                  +{{ resource.tags.length - 3 }}
                </span>
              </div>
            </td>
            <td class="px-6 py-4 text-sm text-ink-700">
              {{ resource.platform || 'N/A' }}
            </td>
            <td class="px-6 py-4 text-sm text-ink-600">
              {{ formatDate(resource.created_at) }}
            </td>
            <td class="px-6 py-4 text-right">
              <div class="flex items-center justify-end gap-2">
                <button
                  @click="$emit('edit-resource', resource)"
                  class="p-2 text-ink-600 hover:text-admin-600 hover:bg-admin-50 rounded-lg transition-colors"
                  title="Edit resource"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </button>
                <button
                  @click="$emit('delete-resource', resource.id)"
                  class="p-2 text-ink-600 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                  title="Delete resource"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
            </td>
          </tr>
          <tr v-if="resources.length === 0">
            <td colspan="6" class="px-6 py-12 text-center text-ink-500">
              <div class="flex flex-col items-center justify-center">
                <svg class="w-16 h-16 text-ink-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
                <p class="text-lg font-medium text-ink-700 mb-2">No resources added yet</p>
                <p class="text-sm text-ink-500">Create your first learning resource to get started</p>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
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

defineProps<{
  resources: Resource[]
}>()

defineEmits<{
  'edit-resource': [resource: Resource]
  'delete-resource': [resourceId: string]
}>()

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  
  if (days === 0) return 'Today'
  if (days === 1) return 'Yesterday'
  if (days < 7) return `${days} days ago`
  if (days < 30) return `${Math.floor(days / 7)} weeks ago`
  if (days < 365) return `${Math.floor(days / 30)} months ago`
  return date.toLocaleDateString()
}
</script>

