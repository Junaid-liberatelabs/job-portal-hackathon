<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    :class="buttonClasses"
    @click="handleClick"
  >
    <span v-if="loading" class="h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent"></span>
    <slot v-if="!loading" name="icon-left" />
    <span v-if="!loading || loadingText"><slot /></span>
    <slot v-if="!loading" name="icon-right" />
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  variant?: 'primary' | 'secondary' | 'accent' | 'outline' | 'ghost' | 'danger' | 'gradient'
  size?: 'sm' | 'md' | 'lg'
  type?: 'button' | 'submit' | 'reset'
  disabled?: boolean
  loading?: boolean
  loadingText?: string
  fullWidth?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  type: 'button',
  disabled: false,
  loading: false,
  fullWidth: false
})

const emit = defineEmits<{
  click: [event: MouseEvent]
}>()

const buttonClasses = computed(() => {
  const base = 'inline-flex items-center justify-center gap-2 font-semibold transition-all duration-300 rounded-xl focus:outline-none focus:ring-4 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100'
  
  const variants = {
    primary: 'bg-primary text-white hover:bg-primary-light focus:ring-primary/30 hover:scale-105 shadow-lg hover:shadow-xl',
    secondary: 'bg-secondary text-white hover:bg-secondary-dark focus:ring-secondary/30 hover:scale-105 shadow-lg hover:shadow-xl',
    accent: 'bg-accent text-white hover:bg-accent-dark focus:ring-accent/30 hover:scale-105 shadow-lg hover:shadow-xl',
    gradient: 'bg-gradient-to-r from-brand-500 to-brand-600 hover:from-brand-600 hover:to-brand-700 text-white shadow-lg shadow-brand-500/30 hover:shadow-xl hover:shadow-brand-500/40 focus:ring-brand-400 hover:scale-105',
    outline: 'border-2 border-brand-500 text-brand-600 hover:bg-brand-50 focus:ring-brand-400 hover:border-brand-600',
    ghost: 'text-brand-600 hover:bg-brand-50 focus:ring-brand-300',
    danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500/30 hover:scale-105 shadow-lg hover:shadow-xl'
  }
  
  const sizes = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-5 py-2.5 text-sm',
    lg: 'px-6 py-3.5 text-base'
  }
  
  const width = props.fullWidth ? 'w-full' : ''
  
  return `${base} ${variants[props.variant]} ${sizes[props.size]} ${width}`
})

const handleClick = (event: MouseEvent) => {
  if (!props.disabled && !props.loading) {
    emit('click', event)
  }
}
</script>

