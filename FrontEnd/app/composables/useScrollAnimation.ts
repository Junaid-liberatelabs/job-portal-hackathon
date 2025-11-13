import { isRef, onBeforeUnmount, onMounted, ref, unref, watch, type Ref } from 'vue'

type MaybeElement = HTMLElement | null
type MaybeElementRef<T extends HTMLElement = HTMLElement> = Ref<T | null> | T | null

type ObserveOptions = {
  once?: boolean
  threshold?: number | number[]
  rootMargin?: string
  onEnter?: (entry: IntersectionObserverEntry) => void
  onLeave?: (entry: IntersectionObserverEntry) => void
}

type TiltOptions = {
  maxAngle?: number
  perspective?: number
  axis?: 'x' | 'y' | 'both'
  damping?: number
}

type ParallaxOptions = {
  intensity?: number
  axis?: 'x' | 'y'
  clamp?: boolean
}

const getElement = <T extends HTMLElement>(target: MaybeElementRef<T>): T | null => {
  return (isRef(target) ? target.value : target) ?? null
}

const prefersReducedMotion = import.meta.client ? window.matchMedia('(prefers-reduced-motion: reduce)') : null

export function useScrollAnimation() {
  const reduceMotion = prefersReducedMotion?.matches ?? false

  const observeElement = <T extends HTMLElement>(
    target: MaybeElementRef<T>,
    options: ObserveOptions = {}
  ) => {
    if (!import.meta.client) {
      return { stop: () => {} }
    }

    let element: T | null = null
    let observer: IntersectionObserver | null = null

    const { once = true, threshold = 0.2, rootMargin = '0px', onEnter, onLeave } = options

    const cleanup = () => {
      if (observer && element) {
        observer.unobserve(element)
      }
      observer?.disconnect()
      observer = null
      element = null
    }

    const setup = () => {
      element = getElement(target)
      if (!element) return

      observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              onEnter?.(entry)
              if (once) {
                cleanup()
              }
            } else {
              onLeave?.(entry)
            }
          })
        },
        { threshold, rootMargin }
      )

      observer.observe(element)
    }

    onMounted(() => {
      setup()
    })

    onBeforeUnmount(() => {
      cleanup()
    })

    if (isRef(target)) {
      watch(
        target,
        () => {
          cleanup()
          setup()
        },
        { flush: 'post' }
      )
    }

    return {
      stop: cleanup
    }
  }

  const createTiltEffect = <T extends HTMLElement>(target: MaybeElementRef<T>, options: TiltOptions = {}) => {
    if (!import.meta.client || reduceMotion) {
      return { destroy: () => {} }
    }

    const { maxAngle = 7, perspective = 900, axis = 'both', damping = 0.18 } = options
    let frame = 0
    let currentX = 0
    let currentY = 0
    let targetX = 0
    let targetY = 0
    let element: T | null = null

    const applyTilt = () => {
      if (!element) return
      currentX += (targetX - currentX) * damping
      currentY += (targetY - currentY) * damping
      element.style.setProperty('--tilt-rotate-x', `${currentX.toFixed(3)}deg`)
      element.style.setProperty('--tilt-rotate-y', `${currentY.toFixed(3)}deg`)
      element.style.setProperty(
        '--tilt-transform',
        `perspective(${perspective}px) rotateX(${currentX.toFixed(3)}deg) rotateY(${currentY.toFixed(3)}deg)`
      )
      frame = requestAnimationFrame(applyTilt)
    }

    const resetTilt = () => {
      targetX = 0
      targetY = 0
    }

    const handlePointerMove = (event: PointerEvent) => {
      if (!element) return
      const rect = element.getBoundingClientRect()
      const offsetX = event.clientX - rect.left
      const offsetY = event.clientY - rect.top
      const centerX = rect.width / 2
      const centerY = rect.height / 2

      if (axis !== 'y') {
        targetX = ((centerY - offsetY) / centerY) * maxAngle
      }
      if (axis !== 'x') {
        targetY = ((offsetX - centerX) / centerX) * maxAngle
      }
    }

    const mount = () => {
      element = getElement(target)
      if (!element) return

      element.style.setProperty('--tilt-rotate-x', '0deg')
      element.style.setProperty('--tilt-rotate-y', '0deg')
      element.style.setProperty('--tilt-transform', `perspective(${perspective}px) rotateX(0deg) rotateY(0deg)`)

      frame = requestAnimationFrame(applyTilt)
      element.addEventListener('pointermove', handlePointerMove)
      element.addEventListener('pointerleave', resetTilt)
    }

    const destroy = () => {
      if (!element) return
      element.removeEventListener('pointermove', handlePointerMove)
      element.removeEventListener('pointerleave', resetTilt)
      cancelAnimationFrame(frame)
      element.style.removeProperty('--tilt-rotate-x')
      element.style.removeProperty('--tilt-rotate-y')
      element.style.removeProperty('--tilt-transform')
      element = null
    }

    onMounted(mount)
    onBeforeUnmount(destroy)

    if (isRef(target)) {
      watch(
        target,
        () => {
          destroy()
          mount()
        },
        { flush: 'post' }
      )
    }

    return { destroy }
  }

  const createParallaxEffect = <T extends HTMLElement>(target: MaybeElementRef<T>, options: ParallaxOptions = {}) => {
    if (!import.meta.client || reduceMotion) {
      return { destroy: () => {} }
    }

    const { intensity = 0.2, axis = 'y', clamp = true } = options
    let element: T | null = null

    const applyOffset = () => {
      if (!element) return
      const rect = element.getBoundingClientRect()
      const viewportHeight = window.innerHeight || 1
      const progress = (rect.top + rect.height / 2) / viewportHeight - 0.5
      let offset = progress * intensity * 100

      if (clamp) {
        offset = Math.max(Math.min(offset, intensity * 100), -intensity * 100)
      }

      if (axis === 'y') {
        element.style.setProperty('--parallax-offset-y', `${offset}px`)
      } else {
        element.style.setProperty('--parallax-offset-x', `${offset}px`)
      }
    }

    const onScroll = () => {
      requestAnimationFrame(applyOffset)
    }

    const mount = () => {
      element = getElement(target)
      if (!element) return
      applyOffset()
      window.addEventListener('scroll', onScroll, { passive: true })
      window.addEventListener('resize', applyOffset)
    }

    const destroy = () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', applyOffset)
      if (element) {
        element.style.removeProperty('--parallax-offset-y')
        element.style.removeProperty('--parallax-offset-x')
      }
      element = null
    }

    onMounted(mount)
    onBeforeUnmount(destroy)

    if (isRef(target)) {
      watch(
        target,
        () => {
          destroy()
          mount()
        },
        { flush: 'post' }
      )
    }

    return { destroy }
  }

  return {
    observeElement,
    createTiltEffect,
    createParallaxEffect,
    prefersReducedMotion: reduceMotion
  }
}


