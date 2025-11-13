<template>
  <div class="form-group">
    <label v-if="label" :for="inputId" class="form-label">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    
    <div class="relative">
      <slot name="icon-left">
        <div v-if="iconLeft" class="absolute left-3 top-1/2 -translate-y-1/2 text-ink-400">
          <component :is="iconLeft" class="h-5 w-5" />
        </div>
      </slot>
      
      <input
        v-if="type !== 'textarea'"
        :id="inputId"
        :type="type"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        :required="required"
        :min="min"
        :max="max"
        :minlength="minlength"
        :maxlength="maxlength"
        :autocomplete="autocomplete"
        :class="inputClasses"
        @input="handleInput"
        @blur="handleBlur"
        @focus="handleFocus"
      />
      
      <textarea
        v-else
        :id="inputId"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        :required="required"
        :rows="rows"
        :minlength="minlength"
        :maxlength="maxlength"
        :class="inputClasses"
        @input="handleInput"
        @blur="handleBlur"
        @focus="handleFocus"
      />
      
      <slot name="icon-right">
        <div v-if="iconRight" class="absolute right-3 top-1/2 -translate-y-1/2 text-ink-400">
          <component :is="iconRight" class="h-5 w-5" />
        </div>
      </slot>
    </div>
    
    <p v-if="error" class="mt-1 text-sm text-red-600">{{ error }}</p>
    <p v-else-if="hint" class="mt-1 text-sm text-ink-500">{{ hint }}</p>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

interface Props {
  modelValue: string | number
  label?: string
  type?: 'text' | 'email' | 'password' | 'number' | 'tel' | 'url' | 'search' | 'textarea'
  placeholder?: string
  error?: string
  hint?: string
  disabled?: boolean
  required?: boolean
  iconLeft?: any
  iconRight?: any
  rows?: number
  min?: number
  max?: number
  minlength?: number
  maxlength?: number
  autocomplete?: string
}

const props = withDefaults(defineProps<Props>(), {
  type: 'text',
  rows: 4
})

const emit = defineEmits<{
  'update:modelValue': [value: string | number]
  blur: [event: FocusEvent]
  focus: [event: FocusEvent]
}>()

const inputId = ref(`input-${Math.random().toString(36).substr(2, 9)}`)
const isFocused = ref(false)

const inputClasses = computed(() => {
  const base = 'form-input w-full transition-all duration-200'
  const error = props.error ? 'form-input-error' : 'border-ink-300 focus:border-accent'
  const icon = props.iconLeft ? 'pl-10' : props.iconRight ? 'pr-10' : ''
  const disabled = props.disabled ? 'bg-ink-50 cursor-not-allowed' : 'bg-white'
  
  return `${base} ${error} ${icon} ${disabled}`
})

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement | HTMLTextAreaElement
  const value = props.type === 'number' ? Number(target.value) : target.value
  emit('update:modelValue', value)
}

const handleBlur = (event: FocusEvent) => {
  isFocused.value = false
  emit('blur', event)
}

const handleFocus = (event: FocusEvent) => {
  isFocused.value = true
  emit('focus', event)
}
</script>

