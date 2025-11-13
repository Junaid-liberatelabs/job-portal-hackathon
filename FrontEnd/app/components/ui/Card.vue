<template>
  <div :class="cardClasses">
    <div v-if="$slots.header || title" class="card-header">
      <slot name="header">
        <h3 v-if="title" class="text-lg font-semibold text-ink-900">{{ title }}</h3>
      </slot>
    </div>
    
    <div :class="bodyClasses">
      <slot />
    </div>
    
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  title?: string
  variant?: 'default' | 'bordered' | 'elevated' | 'glass'
  padding?: 'none' | 'sm' | 'md' | 'lg'
  hover?: boolean
  clickable?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'default',
  padding: 'md',
  hover: false,
  clickable: false
})

const cardClasses = computed(() => {
  const base = 'card rounded-xl overflow-hidden'
  
  const variants = {
    default: 'bg-white shadow-sm',
    bordered: 'bg-white border border-ink-200',
    elevated: 'bg-white shadow-lg',
    glass: 'glass shadow-md'
  }
  
  const interactive = props.hover || props.clickable ? 'card-hover cursor-pointer' : ''
  
  return `${base} ${variants[props.variant]} ${interactive}`
})

const bodyClasses = computed(() => {
  const paddings = {
    none: '',
    sm: 'p-4',
    md: 'p-6',
    lg: 'p-8'
  }
  
  return paddings[props.padding]
})
</script>

<style scoped>
.card-header {
  border-bottom: 1px solid rgb(var(--color-ink-100) / 1);
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.card-footer {
  border-top: 1px solid rgb(var(--color-ink-100) / 1);
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-top: 1rem;
  padding-bottom: 1rem;
}
</style>

