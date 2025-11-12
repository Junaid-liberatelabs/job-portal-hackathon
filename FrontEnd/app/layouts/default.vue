<template>
  <div class="h-screen flex flex-col">
    <!-- Minimal Header -->
    <div class="bg-white border-b border-gray-200 px-4 py-3 flex-shrink-0">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <NuxtLink to="/" class="flex items-center space-x-2">
          <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-lg">H+</span>
          </div>
          <span class="text-lg font-bold text-gray-900">HealthAlly</span>
        </NuxtLink>

        <NuxtLink 
          to="/"
          class="text-gray-600 hover:text-gray-900 transition-colors text-sm"
        >
          Back to Home
        </NuxtLink>
      </div>
    </div>

    <!-- Page Content -->
    <main class="flex-1 overflow-hidden">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
// Minimal layout for chat and focused pages
</script>
