// @ts-ignore - lenis doesn't have perfect TypeScript definitions
import Lenis from '@studio-freight/lenis'
// Note: @studio-freight/lenis doesn't include CSS - we'll add it manually if needed
// The newer 'lenis' package (not @studio-freight/lenis) includes CSS at 'lenis/dist/lenis.css'

export default defineNuxtPlugin(() => {
  let lenis: any = null

  if (typeof window !== 'undefined') {
    // Initialize Lenis with recommended settings from official docs
    // https://github.com/darkroomengineering/lenis
    lenis = new Lenis({
      duration: 1.2,
      easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // easeOutExpo
      orientation: 'vertical', // vertical, horizontal
      gestureOrientation: 'vertical', // vertical, horizontal, both
      smoothWheel: true,
      wheelMultiplier: 1,
      // Note: smoothTouch and touchMultiplier are available in newer versions
      // Uncomment if using lenis@latest:
      // smoothTouch: false, // Recommended: false for better mobile performance
      // touchMultiplier: 2,
      infinite: false,
      autoResize: true, // Automatically resize on window resize
      // Prevent smooth scroll on specific elements (nested scroll)
      // You can use data-lenis-prevent, data-lenis-prevent-wheel, data-lenis-prevent-touch
      prevent: (node: any) => {
        return (
          node.hasAttribute('data-lenis-prevent') ||
          node.hasAttribute('data-lenis-prevent-wheel') ||
          node.hasAttribute('data-lenis-prevent-touch')
        )
      },
    } as any)

    // Use requestAnimationFrame for smooth scroll updates (recommended approach)
    function raf(time: number) {
      lenis.raf(time)
      requestAnimationFrame(raf)
    }

    requestAnimationFrame(raf)

    // Optional: Listen for scroll events
    lenis.on('scroll', (e: any) => {
      // Can be used for scroll-based animations or analytics
      // console.log('Scroll event:', e)
    })

    // Handle anchor links with smooth scroll
    const handleAnchorLinks = () => {
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
          const href = anchor.getAttribute('href')
          if (!href || href === '#') return

          e.preventDefault()
          const target = document.querySelector(href)
          
          if (target) {
            lenis.scrollTo(target, {
              offset: -80, // Offset for fixed header
              duration: 1.5,
              easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            })
          }
        })
      })
    }

    // Initialize anchor handling
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', handleAnchorLinks)
    } else {
      handleAnchorLinks()
    }

    // Handle route changes
    const router = useRouter()
    
    router.afterEach(() => {
      // Scroll to top on route change with immediate mode
      lenis.scrollTo(0, { immediate: true })
      
      // Reinitialize anchor links for new page content
      setTimeout(handleAnchorLinks, 100)
    })

    // Cleanup on app unmount
    window.addEventListener('beforeunload', () => {
      if (lenis && typeof lenis.destroy === 'function') {
        lenis.destroy()
      }
    })
  }

  return {
    provide: {
      lenis,
    },
  }
})

