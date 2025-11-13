import { onNuxtReady, useNuxtApp } from 'nuxt/app'
import Lenis from 'lenis'

type ScrollTarget = Parameters<Lenis['scrollTo']>[0]
type ScrollOptions = Parameters<Lenis['scrollTo']>[1]

const DEFAULT_SCROLL_OPTIONS: ScrollOptions = {
  duration: 1.1,
  easing: (t: number) => 1 - Math.pow(1 - t, 1.9)
}

export default defineNuxtPlugin(() => {
  if (import.meta.server) {
    return
  }

  let lenis: Lenis | null = null
  let frameId: number | null = null

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)')

  const stopRaf = () => {
    if (frameId !== null) {
      cancelAnimationFrame(frameId)
      frameId = null
    }
    lenis?.stop()
  }

  const tick = (time: number) => {
    lenis?.raf(time)
    frameId = requestAnimationFrame(tick)
  }

  const startRaf = () => {
    if (!lenis || prefersReducedMotion.matches) {
      return
    }
    if (frameId === null) {
      lenis.start()
      frameId = requestAnimationFrame(tick)
    }
  }

  const initLenis = () => {
    if (lenis) {
      stopRaf()
      lenis.destroy()
    }

    lenis = new Lenis({
      autoRaf: false,
      duration: 1.2,
      easing: (t) => 1 - Math.pow(1 - t, 1.9),
      smoothWheel: true,
      syncTouch: true,
      syncTouchLerp: 0.12,
      touchInertiaExponent: 28,
      lerp: 0.07,
      wheelMultiplier: 0.85,
      touchMultiplier: 1.05,
      anchors: true
    })

    if (!prefersReducedMotion.matches) {
      startRaf()
    }
  }

  const resetScrollToTop = () => {
    if (!lenis || window.location.hash) return

    window.scrollTo({ top: 0, left: 0, behavior: 'auto' })
    requestAnimationFrame(() => {
      lenis?.scrollTo(0, { immediate: true, duration: 0 })
    })
  }

  const handleVisibilityChange = () => {
    if (document.hidden) {
      stopRaf()
    } else {
      startRaf()
    }
  }

  const handleReducedMotionChange = (event: MediaQueryListEvent) => {
    if (event.matches) {
      stopRaf()
    } else {
      startRaf()
    }
  }

  const handleResize = () => {
    lenis?.resize()
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

    document.addEventListener('visibilitychange', handleVisibilityChange)
    window.addEventListener('focus', startRaf)
    window.addEventListener('blur', stopRaf)
    window.addEventListener('resize', handleResize)

    if (typeof prefersReducedMotion.addEventListener === 'function') {
      prefersReducedMotion.addEventListener('change', handleReducedMotionChange)
    } else if (typeof prefersReducedMotion.addListener === 'function') {
      prefersReducedMotion.addListener(handleReducedMotionChange)
    }
  })

  const nuxtApp = useNuxtApp()

  nuxtApp.hook('page:start', () => {
    stopRaf()
  })

  nuxtApp.hook('page:finish', () => {
    if (!lenis) return

    if (!window.location.hash) {
      resetScrollToTop()
    }
    startRaf()
  })

  const scrollTo = (target: ScrollTarget, options?: ScrollOptions) => {
    if (!lenis) {
      if (typeof target === 'number') {
        window.scrollTo({ top: target, behavior: options?.immediate ? 'auto' : 'smooth' })
      } else if (typeof target === 'string') {
        const element = document.querySelector(target)
        element?.scrollIntoView({ behavior: 'smooth' })
      } else if (target instanceof HTMLElement) {
        target.scrollIntoView({ behavior: 'smooth' })
      }
      return
    }

    const mergedOptions = { ...DEFAULT_SCROLL_OPTIONS, ...options }
    lenis.scrollTo(target, mergedOptions)
  }

  const cleanup = () => {
    document.removeEventListener('visibilitychange', handleVisibilityChange)
    window.removeEventListener('focus', startRaf)
    window.removeEventListener('blur', stopRaf)
    window.removeEventListener('resize', handleResize)

    if (typeof prefersReducedMotion.removeEventListener === 'function') {
      prefersReducedMotion.removeEventListener('change', handleReducedMotionChange)
    } else if (typeof prefersReducedMotion.removeListener === 'function') {
      prefersReducedMotion.removeListener(handleReducedMotionChange)
    }

    stopRaf()
    lenis?.destroy()
    lenis = null
  }

  nuxtApp.hook('app:error', () => stopRaf())
  nuxtApp.hook('app:beforeMount', () => startRaf())

  if (import.meta.hot) {
    import.meta.hot.accept(() => {})
    import.meta.hot.dispose(() => {
      cleanup()
    })
  }

  return {
    provide: {
      lenis: () => lenis,
      scrollTo
    }
  }
})
