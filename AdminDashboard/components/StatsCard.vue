<template>
  <div class="card hover:shadow-md transition-shadow">
    <div class="card-body">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-ink-600">{{ title }}</p>
          <p class="text-3xl font-bold text-ink-900 mt-2">{{ value }}</p>
          <p v-if="subtitle" class="text-xs text-ink-500 mt-1">{{ subtitle }}</p>
        </div>
        <div :class="iconBgClass" class="w-12 h-12 rounded-xl flex items-center justify-center">
          <component :is="icon" class="w-6 h-6" :class="iconColorClass" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Component } from 'vue'

defineProps<{
  title: string
  value: string | number
  subtitle?: string
  icon: Component
  iconBgClass?: string
  iconColorClass?: string
}>()
</script>

