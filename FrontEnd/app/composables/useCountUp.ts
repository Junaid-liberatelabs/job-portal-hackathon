import { ref, onMounted, onUnmounted } from 'vue'

export function useCountUp(target: number, duration: number = 2000) {
  const count = ref(0)
  let animationFrame: number
  let startTime: number | null = null

  const animate = (timestamp: number) => {
    if (!startTime) startTime = timestamp
    const progress = Math.min((timestamp - startTime) / duration, 1)
    
    // Easing function (ease-out)
    const easeOut = 1 - Math.pow(1 - progress, 3)
    count.value = Math.floor(easeOut * target)
    
    if (progress < 1) {
      animationFrame = requestAnimationFrame(animate)
    } else {
      count.value = target
    }
  }

  const start = () => {
    startTime = null
    count.value = 0
    animationFrame = requestAnimationFrame(animate)
  }

  const stop = () => {
    if (animationFrame) {
      cancelAnimationFrame(animationFrame)
    }
  }

  onUnmounted(() => {
    stop()
  })

  return {
    count,
    start,
    stop
  }
}

