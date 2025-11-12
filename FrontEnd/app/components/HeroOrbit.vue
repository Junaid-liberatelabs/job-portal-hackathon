<template>
  <div
    ref="wrapper"
    class="relative mx-auto h-[440px] w-full max-w-xl cursor-pointer select-none"
    @pointermove="handlePointerMove"
    @pointerleave="resetTilt"
    @touchmove.passive="handleTouchMove"
    @touchend="resetTilt"
  >
    <div class="absolute inset-0 rounded-[36px] bg-gradient-to-br from-brand-400/45 via-brand-500/35 to-emerald-300/35 blur-3xl"></div>

    <div class="relative h-full w-full overflow-visible" :style="{ perspective: '1200px' }">
      <div
        class="relative h-full w-full rounded-[32px] bg-ink-900/80 p-8 shadow-[0_35px_140px_-55px_rgba(30,64,175,0.55)] ring-1 ring-white/10 backdrop-blur-2xl transition-shadow duration-500"
        :style="{
          transform: `rotateX(${tilt.x}deg) rotateY(${tilt.y}deg)`,
          transformStyle: 'preserve-3d'
        }"
      >
        <div class="pointer-events-none absolute inset-0 -z-10 rounded-[32px] bg-gradient-to-br from-white/20 via-transparent to-white/5"></div>

        <div class="grid h-full grid-rows-[auto_1fr_auto] gap-8 text-white">
          <div class="flex items-center justify-between">
            <span class="rounded-full bg-white/10 px-4 py-2 text-xs font-semibold uppercase tracking-[0.25em] text-white/70 ring-1 ring-white/15">
              Profile snapshot
            </span>
            <span class="text-sm font-medium text-brand-100/90">Updated moments ago</span>
          </div>

          <div class="grid gap-6">
            <div>
              <p class="text-xs uppercase tracking-[0.35em] text-white/70">Launch readiness</p>
              <p class="mt-2 text-6xl font-semibold leading-none text-white">
                82<span class="text-emerald-300">%</span>
              </p>
            </div>
            <div class="grid gap-3 rounded-2xl bg-white/8 p-4 backdrop-blur-md ring-1 ring-white/12">
              <p class="text-sm font-semibold text-white/80">Highlights</p>
              <div class="grid gap-2 text-xs text-white/70">
                <p>• Skill coverage: HTML, CSS, Communication</p>
                <p>• Track focus: Frontend Development</p>
                <p>• Learning boost queued: Accessible UI basics</p>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div>
              <p class="text-xs uppercase tracking-[0.3em] text-white/60">Next action</p>
              <p class="text-lg font-semibold text-white">Apply • Junior Frontend Fellowship</p>
            </div>
            <div class="relative h-16 w-16">
              <div class="absolute inset-0 rounded-full border border-white/25"></div>
              <div class="absolute inset-2 rounded-full border border-white/40"></div>
              <div class="absolute left-1/2 top-1/2 h-2 w-2 -translate-x-1/2 -translate-y-1/2 rounded-full bg-emerald-300 shadow-[0_0_12px_rgba(16,185,129,0.8)]"></div>
            </div>
          </div>
        </div>

        <div
          class="pointer-events-none absolute -left-12 top-8 h-28 w-28 rounded-full bg-gradient-to-br from-emerald-300/90 via-teal-300/80 to-transparent opacity-80 shadow-[0_15px_45px_-15px_rgba(16,185,129,0.6)] backdrop-blur-sm"
          :style="floatingStyle(-18, 12, 1)"
        ></div>

        <div
          class="pointer-events-none absolute -right-8 bottom-8 h-40 w-40 rounded-full bg-gradient-to-br from-brand-500/70 via-brand-300/70 to-transparent opacity-70 shadow-[0_15px_55px_-25px_rgba(59,130,246,0.8)] backdrop-blur-sm"
          :style="floatingStyle(22, -10, 1.4)"
        ></div>

        <div
          class="pointer-events-none absolute -top-12 right-1/2 h-56 w-56 rounded-full bg-gradient-to-br from-white/20 via-white/5 to-transparent opacity-50 backdrop-blur"
          :style="floatingStyle(0, 0, 2)"
        ></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, reactive, ref } from 'vue'

const wrapper = ref<HTMLElement | null>(null)

const tilt = reactive({ x: 0, y: 0 })
const target = reactive({ x: 0, y: 0 })

let animationFrame: number | null = null

const animate = () => {
  tilt.x += (target.x - tilt.x) * 0.08
  tilt.y += (target.y - tilt.y) * 0.08

  animationFrame = requestAnimationFrame(animate)
}

onMounted(() => {
  animationFrame = requestAnimationFrame(animate)
})

onBeforeUnmount(() => {
  if (animationFrame) {
    cancelAnimationFrame(animationFrame)
  }
})

const calculateTarget = (xRatio: number, yRatio: number) => {
  target.x = (0.5 - yRatio) * 18
  target.y = (xRatio - 0.5) * 18
}

const handlePointerMove = (event: PointerEvent) => {
  const rect = wrapper.value?.getBoundingClientRect()
  if (!rect) return
  const xRatio = (event.clientX - rect.left) / rect.width
  const yRatio = (event.clientY - rect.top) / rect.height
  calculateTarget(xRatio, yRatio)
}

const handleTouchMove = (event: TouchEvent) => {
  const touch = event.touches[0]
  if (!touch) return
  const rect = wrapper.value?.getBoundingClientRect()
  if (!rect) return
  const xRatio = (touch.clientX - rect.left) / rect.width
  const yRatio = (touch.clientY - rect.top) / rect.height
  calculateTarget(xRatio, yRatio)
}

const resetTilt = () => {
  target.x = 0
  target.y = 0
}

const floatingStyle = (xOffset: number, yOffset: number, depth: number) => ({
  transform: `translate3d(${xOffset}px, ${yOffset}px, ${depth * 30}px)`
})
</script>

<style scoped>
@media (max-width: 767px) {
  .cursor-pointer {
    cursor: default;
  }
}
</style>

