<template>
  <div id="app">
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
useHead({
  titleTemplate: (title) => title ? `${title} - CareerIn Admin` : 'CareerIn Admin Dashboard',
})
</script>

