import { onMounted, onUnmounted, ref } from 'vue'

export function useScrollAnimation(options: {
  threshold?: number
  rootMargin?: string
  animationClass?: string
} = {}) {
  const {
    threshold = 0.1,
    rootMargin = '0px 0px -100px 0px',
    animationClass = 'animate-fade-in-up'
  } = options

  const elements = ref<Set<HTMLElement>>(new Set())
  let observer: IntersectionObserver | null = null

  const registerElement = (el: HTMLElement | null) => {
    if (!el) return
    elements.value.add(el)
    if (observer) {
      observer.observe(el)
    }
  }

  const unregisterElement = (el: HTMLElement | null) => {
    if (!el) return
    elements.value.delete(el)
    if (observer) {
      observer.unobserve(el)
    }
  }

  onMounted(() => {
    if (typeof window === 'undefined') return

    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add(animationClass)
            entry.target.classList.remove('opacity-0', 'translate-y-8')
            observer?.unobserve(entry.target)
          }
        })
      },
      {
        threshold,
        rootMargin
      }
    )

    elements.value.forEach((el) => {
      el.classList.add('opacity-0', 'translate-y-8', 'transition-all', 'duration-700')
      observer?.observe(el)
    })
  })

  onUnmounted(() => {
    if (observer) {
      observer.disconnect()
      observer = null
    }
    elements.value.clear()
  })

  return {
    registerElement,
    unregisterElement
  }
}

