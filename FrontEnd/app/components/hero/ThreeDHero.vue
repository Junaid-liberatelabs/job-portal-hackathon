<template>
  <section class="three-d-hero">
    <div class="three-d-hero__bg">
      <HeroScene :color-a="sceneColors.a" :color-b="sceneColors.b" :density="sceneDensity" />

      <div class="three-d-hero__gradient" />

      <video
        v-if="shouldPlayVideo"
        ref="videoRef"
        class="three-d-hero__video"
        autoplay
        muted
        loop
        playsinline
        :poster="videoPoster"
      >
        <source :src="videoSrc" type="video/mp4" />
      </video>
    </div>

    <div class="three-d-hero__content">
      <div class="three-d-hero__copy" v-scroll-reveal="{ direction: 'up', distance: 28, duration: 720 }">
        <div class="three-d-hero__badge" v-scroll-reveal="{ direction: 'up', distance: 24, duration: 720 }">
          <span class="three-d-hero__badge-dot" />
          {{ badge }}
        </div>

        <div class="three-d-hero__headline">
          <h1 class="font-display text-4xl font-semibold tracking-tight text-ink-900 sm:text-5xl lg:text-6xl">
            <slot name="headline" />
          </h1>
          <p class="text-lg text-ink-500 sm:max-w-xl" v-if="description">
            {{ description }}
          </p>
        </div>

        <div class="three-d-hero__actions">
          <NuxtLink
            v-if="primaryCta"
            :to="primaryCta.to"
            class="three-d-hero__primary"
          >
            {{ primaryCta.label }}
          </NuxtLink>
          <NuxtLink
            v-if="secondaryCta"
            :to="secondaryCta.to"
            class="three-d-hero__secondary"
          >
            {{ secondaryCta.label }}
          </NuxtLink>
        </div>

        <dl class="three-d-hero__stats">
          <div
            v-for="(stat, index) in stats"
            :key="stat.label"
            class="three-d-hero__stat"
            v-scroll-reveal="{ direction: 'up', distance: 32, duration: 700, delay: index * 120 }"
          >
            <dt>{{ stat.label }}</dt>
            <dd>{{ stat.value }}</dd>
          </div>
        </dl>
      </div>

      <div class="three-d-hero__visual" ref="visualRef">
        <HeroOrbit />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ComputedRef, computed, onBeforeUnmount, onMounted, ref } from 'vue'
import HeroScene from '~/components/HeroScene.vue'
import HeroOrbit from '~/components/HeroOrbit.vue'
import { useScrollAnimation } from '~/composables/useScrollAnimation'

type HeroStat = {
  label: string
  value: string
}

type HeroCta = {
  label: string
  to: string
}

const props = withDefaults(
  defineProps<{
    stats: HeroStat[]
    badge?: string
    description?: string
    primaryCta?: HeroCta | null
    secondaryCta?: HeroCta | null
    videoSrc?: string
    videoPoster?: string
    sceneColors?: { a: string; b: string }
    sceneDensity?: number
  }>(),
  {
    badge: 'Youth careers in motion',
    description: '',
    primaryCta: null,
    secondaryCta: null,
    videoSrc: 'https://cdn.coverr.co/videos/coverr-collaboration-in-the-office-1667325214078/1080p.mp4',
    videoPoster: '',
    sceneColors: () => ({ a: '#1d4ed8', b: '#38bdf8' }),
    sceneDensity: 0.8
  }
)

const videoRef = ref<HTMLVideoElement | null>(null)
const visualRef = ref<HTMLElement | null>(null)
const shouldPlayVideo = ref(false)
const { createParallaxEffect } = useScrollAnimation()
let detachParallax: (() => void) | null = null

const sceneColors: ComputedRef<{ a: string; b: string }> = computed(() => props.sceneColors ?? { a: '#1d4ed8', b: '#38bdf8' })
const sceneDensity = computed(() => props.sceneDensity ?? 0.8)

const enableVideo = () => {
  if (!videoRef.value) return
  const playPromise = videoRef.value.play()
  if (playPromise !== undefined) {
    playPromise.catch(() => {
      /* ignore autoplay block */
    })
  }
}

const setupParallax = () => {
  if (!visualRef.value) return
  const parallaxHandle = createParallaxEffect(visualRef, { intensity: 0.12, axis: 'y' })
  detachParallax = parallaxHandle.destroy
}

onMounted(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)')
  shouldPlayVideo.value = !prefersReducedMotion.matches

  if (shouldPlayVideo.value) {
    enableVideo()
  }

  setupParallax()
})

onBeforeUnmount(() => {
  if (detachParallax) {
    detachParallax()
    detachParallax = null
  }
})

const badge = computed(() => props.badge || 'Youth careers in motion')
const description = computed(() => props.description)
const stats = computed(() => props.stats ?? [])
const primaryCta = computed(() => props.primaryCta ?? undefined)
const secondaryCta = computed(() => props.secondaryCta ?? undefined)
</script>

<style scoped>
.three-d-hero {
  position: relative;
  overflow: hidden;
}

.three-d-hero__bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}

.three-d-hero__gradient {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 20% 20%, rgba(59, 130, 246, 0.22), transparent 60%);
  mix-blend-mode: screen;
}

.three-d-hero__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.25;
  mix-blend-mode: screen;
}

.three-d-hero__content {
  position: relative;
  z-index: 1;
  display: grid;
  max-width: 80rem;
  margin: 0 auto;
  padding: 8rem 1.5rem 6rem;
  gap: 4rem;
}

.three-d-hero__copy {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.three-d-hero__badge {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.55rem 1.25rem;
  border-radius: 9999px;
  border: 1px solid rgba(191, 219, 254, 0.65);
  background: rgba(255, 255, 255, 0.75);
  text-transform: uppercase;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.35em;
}

.three-d-hero__badge-dot {
  width: 10px;
  height: 10px;
  border-radius: 9999px;
  background: rgba(52, 211, 153, 1);
  box-shadow: 0 0 14px rgba(52, 211, 153, 0.75);
}

.three-d-hero__headline {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.three-d-hero__actions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.three-d-hero__primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.9rem 1.75rem;
  border-radius: 9999px;
  background: #0f172a;
  color: #fff;
  font-size: 0.9rem;
  font-weight: 600;
  box-shadow: 0 25px 50px -20px rgba(15, 23, 42, 0.45);
  transition: transform 200ms ease, background 200ms ease;
}

.three-d-hero__primary:hover {
  transform: translateY(-2px);
  background: #111c3c;
}

.three-d-hero__secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.9rem 1.75rem;
  border-radius: 9999px;
  border: 1px solid rgba(15, 23, 42, 0.2);
  font-size: 0.9rem;
  font-weight: 600;
  color: #1f2937;
  transition: border 200ms ease, color 200ms ease;
}

.three-d-hero__secondary:hover {
  border-color: rgba(59, 130, 246, 0.5);
  color: #0f172a;
}

.three-d-hero__stats {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.5rem;
}

.three-d-hero__stat dt {
  text-transform: uppercase;
  letter-spacing: 0.25em;
  font-size: 0.7rem;
  color: rgba(71, 85, 105, 0.75);
}

.three-d-hero__stat dd {
  font-family: 'Plus Jakarta Sans', 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-size: 1.9rem;
  font-weight: 600;
  color: #0f172a;
}

.three-d-hero__visual {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  pointer-events: none;
}

@media (min-width: 1024px) {
  .three-d-hero__content {
    grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
    padding: 10rem 2.5rem 7.5rem;
  }

  .three-d-hero__actions {
    flex-direction: row;
  }

  .three-d-hero__stats {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

@media (prefers-reduced-motion: reduce) {
  .three-d-hero__video {
    display: none;
  }
}
</style>

