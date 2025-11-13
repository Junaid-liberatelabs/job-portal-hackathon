// @ts-ignore - animejs doesn't have TypeScript definitions
import anime from 'animejs'

export default defineNuxtPlugin(() => {
  return {
    provide: {
      anime
    }
  }
})

