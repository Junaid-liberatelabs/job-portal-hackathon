import { navigateTo, defineNuxtRouteMiddleware } from '#imports'
import { useAuthStore } from '~/stores/auth'

export default defineNuxtRouteMiddleware(async () => {
  const auth = useAuthStore()
  if (auth.token) {
    if (!auth.user) {
      await auth.fetchProfile()
    }
    if (auth.token) {
      return navigateTo('/dashboard')
    }
  }
})
