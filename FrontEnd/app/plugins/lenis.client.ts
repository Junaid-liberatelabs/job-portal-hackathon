import { onNuxtReady, useNuxtApp } from 'nuxt/app'
import Lenis from 'lenis'

export default defineNuxtPlugin(() => {
  if (import.meta.server) {
    return
  }

  let lenis: Lenis | null = null

  const initLenis = () => {
    if (lenis) {
      lenis.destroy()
    }

    lenis = new Lenis({
      autoRaf: true,
      duration: 1.15,
      anchors: true,
      touchMultiplier: 1.2
    })
  }

  const resetScrollToTop = () => {
    if (!lenis || window.location.hash) return

    window.scrollTo({ top: 0, left: 0, behavior: 'auto' })
    requestAnimationFrame(() => {
      lenis?.scrollTo(0, { immediate: true, duration: 0 })
    })
  }

  onNuxtReady(() => {
    if ('scrollRestoration' in window.history) {
      window.history.scrollRestoration = 'manual'
    }

    initLenis()

    const navigation = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming | undefined
    if (navigation?.type === 'reload') {
      resetScrollToTop()
    } else if (!window.location.hash) {
      resetScrollToTop()
    }
  })

  const nuxtApp = useNuxtApp()

  nuxtApp.hook('page:finish', () => {
    if (!lenis) return

    lenis.stop()
    if (!window.location.hash) {
      resetScrollToTop()
    }
    lenis.start()
  })

  return {
    provide: {
      lenis: () => lenis
    }
  }
})

