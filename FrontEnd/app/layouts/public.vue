<template>
  <div class="flex min-h-screen flex-col bg-ink-50">
    <PublicNavigation />
    
    <main class="flex-1">
      <slot />
    </main>
    
    <Footer />
  </div>
</template>

<script setup lang="ts">
import PublicNavigation from '~/components/layout/PublicNavigation.vue'
import Footer from '~/components/layout/Footer.vue'
</script>

