<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition-opacity duration-200"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="isOpen"
        class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4 overflow-y-auto"
        @click.self="closeModal"
      >
        <Transition
          enter-active-class="transition-all duration-200"
          enter-from-class="opacity-0 scale-95"
          enter-to-class="opacity-100 scale-100"
          leave-active-class="transition-all duration-200"
          leave-from-class="opacity-100 scale-100"
          leave-to-class="opacity-0 scale-95"
        >
          <div
            v-if="isOpen"
            class="bg-white rounded-2xl shadow-2xl max-w-4xl w-full my-8 max-h-[90vh] overflow-y-auto scrollbar-thin"
          >
            <div class="sticky top-0 bg-white border-b border-ink-200 px-6 py-4 flex items-center justify-between z-10">
              <h2 class="text-2xl font-bold text-ink-900">
                {{ editMode ? 'Edit Resource' : 'Create New Resource' }}
              </h2>
              <button
                @click="closeModal"
                class="p-2 hover:bg-ink-100 rounded-lg transition-colors"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <form @submit.prevent="handleSubmit" class="p-6 space-y-6">
              <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
                <p class="text-sm text-red-800">{{ error }}</p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Resource Name <span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="formData.name"
                    type="text"
                    required
                    class="input"
                    placeholder="e.g., Python for Beginners"
                  />
                </div>

                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Description <span class="text-red-500">*</span>
                  </label>
                  <textarea
                    v-model="formData.description"
                    required
                    rows="4"
                    class="input"
                    placeholder="Describe the resource, what learners will gain, and key features..."
                  />
                </div>

                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    URL <span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="formData.url"
                    type="url"
                    required
                    class="input"
                    placeholder="https://example.com/resource"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Platform
                  </label>
                  <input
                    v-model="formData.platform"
                    type="text"
                    class="input"
                    placeholder="e.g., Coursera, Udemy"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Pricing
                  </label>
                  <input
                    v-model="formData.pricing"
                    type="text"
                    class="input"
                    placeholder="e.g., Free, $49.99"
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Duration
                  </label>
                  <input
                    v-model="formData.duration"
                    type="text"
                    class="input"
                    placeholder="e.g., 10 hours, 4 weeks"
                  />
                </div>

                <div class="md:col-span-2">
                  <label class="block text-sm font-medium text-ink-700 mb-2">
                    Tags
                  </label>
                  <input
                    v-model="tagsInput"
                    type="text"
                    class="input mb-2"
                    placeholder="Type a tag and press Enter"
                    @keydown.enter.prevent="addTag"
                  />
                  <div class="flex flex-wrap gap-2">
                    <span
                      v-for="(tag, index) in formData.tags"
                      :key="index"
                      class="inline-flex items-center gap-1 px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm"
                    >
                      {{ tag }}
                      <button
                        type="button"
                        @click="removeTag(index)"
                        class="hover:bg-purple-200 rounded-full p-0.5 transition-colors"
                      >
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </span>
                  </div>
                </div>
              </div>

              <div class="flex items-center justify-end gap-3 pt-4 border-t border-ink-200">
                <button
                  type="button"
                  @click="closeModal"
                  class="btn btn-secondary"
                  :disabled="loading"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  class="btn btn-primary"
                  :disabled="loading"
                >
                  <span v-if="loading">
                    {{ editMode ? 'Updating...' : 'Creating...' }}
                  </span>
                  <span v-else>
                    {{ editMode ? 'Update Resource' : 'Create Resource' }}
                  </span>
                </button>
              </div>
            </form>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
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

const props = defineProps<{
  isOpen: boolean
  editResource?: Resource | null
}>()

const emit = defineEmits<{
  close: []
  'resource-created': []
  'resource-updated': []
}>()

const editMode = computed(() => !!props.editResource)

const formData = ref({
  name: '',
  description: '',
  url: '',
  tags: [] as string[],
  pricing: '',
  platform: '',
  duration: ''
})

const tagsInput = ref('')
const loading = ref(false)
const error = ref<string | null>(null)

watch(() => props.editResource, (resource) => {
  if (resource) {
    formData.value = {
      name: resource.name,
      description: resource.description,
      url: resource.url,
      tags: [...resource.tags],
      pricing: resource.pricing || '',
      platform: resource.platform || '',
      duration: resource.duration || ''
    }
  }
}, { immediate: true })

watch(() => props.isOpen, (isOpen) => {
  if (!isOpen) {
    resetForm()
  }
})

const addTag = () => {
  const tag = tagsInput.value.trim()
  if (tag && !formData.value.tags.includes(tag)) {
    formData.value.tags.push(tag)
    tagsInput.value = ''
  }
}

const removeTag = (index: number) => {
  formData.value.tags.splice(index, 1)
}

const resetForm = () => {
  formData.value = {
    name: '',
    description: '',
    url: '',
    tags: [],
    pricing: '',
    platform: '',
    duration: ''
  }
  tagsInput.value = ''
  error.value = null
}

const closeModal = () => {
  emit('close')
}

const handleSubmit = async () => {
  error.value = null
  loading.value = true

  try {
    const { createResource, updateResource } = useResources()
    
    const resourceData = {
      name: formData.value.name.trim(),
      description: formData.value.description.trim(),
      url: formData.value.url.trim(),
      tags: formData.value.tags.filter(t => t.trim().length > 0),
      pricing: formData.value.pricing.trim() || undefined,
      platform: formData.value.platform.trim() || undefined,
      duration: formData.value.duration.trim() || undefined
    }

    if (editMode.value && props.editResource) {
      await updateResource(props.editResource.id, resourceData)
      emit('resource-updated')
    } else {
      await createResource(resourceData)
      emit('resource-created')
    }
    
    closeModal()
  } catch (e: any) {
    error.value = e.data?.detail || e.message || 'An error occurred'
  } finally {
    loading.value = false
  }
}
</script>

