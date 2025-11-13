<template>
  <div 
    :class="[
      'rounded-2xl bg-gradient-to-br from-brand-500 to-brand-600 flex items-center justify-center shadow-lg transition-all duration-300',
      sizeClasses,
      shadowColor
    ]"
    class="hover:scale-105 hover:shadow-xl"
  >
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  size?: 'sm' | 'md' | 'lg' | 'xl'
  color?: 'brand' | 'emerald' | 'purple' | 'amber'
}

const props = withDefaults(defineProps<Props>(), {
  size: 'md',
  color: 'brand'
})

const sizeClasses = computed(() => {
  const sizes = {
    sm: 'h-10 w-10',
    md: 'h-12 w-12',
    lg: 'h-14 w-14',
    xl: 'h-16 w-16'
  }
  return sizes[props.size]
})

const shadowColor = computed(() => {
  const shadows = {
    brand: 'shadow-brand-500/30 hover:shadow-brand-500/40',
    emerald: 'shadow-emerald-500/30 hover:shadow-emerald-500/40 from-emerald-500 to-emerald-600',
    purple: 'shadow-purple-500/30 hover:shadow-purple-500/40 from-purple-500 to-purple-600',
    amber: 'shadow-amber-500/30 hover:shadow-amber-500/40 from-amber-500 to-amber-600'
  }
  return shadows[props.color]
})
</script>

