import { navigateTo, defineNuxtRouteMiddleware } from '#imports'
import { useAuthStore } from '~/stores/auth'

export default defineNuxtRouteMiddleware(async (to) => {
  const auth = useAuthStore()

  if (!auth.token) {
    return navigateTo({ path: '/login', query: { redirect: to.fullPath } })
  }

  if (!auth.user) {
    await auth.fetchProfile()
  }

  if (!auth.token) {
    return navigateTo({ path: '/login', query: { redirect: to.fullPath } })
  }
})
