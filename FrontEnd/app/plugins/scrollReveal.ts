export default defineNuxtPlugin((nuxtApp) => {
  const getOptions = (binding?: { value?: Record<string, unknown> }) => {
    const raw = binding?.value || {}
    const toNumber = (value: unknown, fallback: number) => {
      const parsed = Number(value)
      return Number.isFinite(parsed) ? parsed : fallback
    }

    const distance = toNumber(raw.distance, 48)
    const duration = toNumber(raw.duration, 600)
    const delay = toNumber(raw.delay, 0)
    const direction = typeof raw.direction === 'string' ? raw.direction.toLowerCase() : 'up'

    const transform = (() => {
      switch (direction) {
        case 'down':
          return `translate3d(0, -${distance}px, 0)`
        case 'left':
          return `translate3d(${distance * -1}px, 0, 0)`
        case 'right':
          return `translate3d(${distance}px, 0, 0)`
        case 'up':
        default:
          return `translate3d(0, ${distance}px, 0)`
      }
    })()

    return { transform, duration, delay }
  }

  const applyStyles = (el: HTMLElement, options: { transform: string; duration: number; delay: number }) => {
    el.classList.add('sr-base')
    el.style.setProperty('--sr-transform', options.transform)
    el.style.setProperty('--sr-duration', `${options.duration}ms`)
    if (options.delay) {
      el.style.setProperty('--sr-delay', `${options.delay}ms`)
      el.style.transitionDelay = `${options.delay}ms`
    } else {
      el.style.removeProperty('--sr-delay')
      el.style.removeProperty('transition-delay')
    }
  }

  const directive = {
    beforeMount(el: HTMLElement, binding: { value?: Record<string, unknown> }) {
      const options = getOptions(binding)
      applyStyles(el, options)
    },
    mounted(el: HTMLElement, binding: { value?: Record<string, unknown> }) {
      if (!import.meta.client) return

      const options = getOptions(binding)
      applyStyles(el, options)

      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              el.classList.add('sr-visible')
              observer.unobserve(entry.target as Element)
            }
          })
        },
        { threshold: 0.15 }
      )

      observer.observe(el)
      ;(el as HTMLElement & { __srObserver?: IntersectionObserver }).__srObserver = observer
    },
    unmounted(el: HTMLElement) {
      const target = el as HTMLElement & { __srObserver?: IntersectionObserver }
      if (target.__srObserver) {
        target.__srObserver.disconnect()
        delete target.__srObserver
      }
    },
    getSSRProps(binding: { value?: Record<string, unknown> }) {
      const options = getOptions(binding)
      const styleParts = [
        `--sr-transform:${options.transform}`,
        `--sr-duration:${options.duration}ms`
      ]

      if (options.delay) {
        styleParts.push(`--sr-delay:${options.delay}ms`)
        styleParts.push(`transition-delay:${options.delay}ms`)
      }

      return {
        class: 'sr-base',
        style: styleParts.join(';')
      }
    }
  }

  nuxtApp.vueApp.directive('scroll-reveal', directive)
})

