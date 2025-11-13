<template>
  <nav
    class="experience-nav"
    :class="{ 'experience-nav--visible': isVisible }"
    role="navigation"
    aria-label="Experience section navigation"
  >
    <ul>
      <li v-for="section in sections" :key="section.id">
        <button
          type="button"
          :class="['experience-nav__link', { 'experience-nav__link--active': activeSection === section.id }]"
          @click="scrollToSection(section.id)"
        >
          <span class="experience-nav__dot" aria-hidden="true"></span>
          <span class="experience-nav__label">{{ section.label }}</span>
        </button>
      </li>
    </ul>
  </nav>
</template>

<script setup lang="ts">
import type { Ref } from 'vue'
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useNuxtApp } from '#app'

type SectionConfig = {
  id: string
  label: string
  offset?: number
}

const props = withDefaults(
  defineProps<{
    sections: SectionConfig[]
    alwaysVisible?: boolean
    showFrom?: number
    offset?: number
  }>(),
  {
    alwaysVisible: false,
    showFrom: 320,
    offset: 0
  }
)

const activeSection = ref<string>(props.sections[0]?.id ?? '')
const hasMounted = ref(false)
const isVisible = ref(props.alwaysVisible)
const nuxtApp = useNuxtApp()

const scrollTargets = computed(() =>
  props.sections.map((section) => ({
    ...section,
    element: document.getElementById(section.id)
  }))
)

let observers: IntersectionObserver[] = []

const disconnectObservers = () => {
  observers.forEach((observer) => observer.disconnect())
  observers = []
}

const handleIntersection = (entries: IntersectionObserverEntry[]) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      activeSection.value = (entry.target as HTMLElement).id
    }
  })
}

const setupObservers = () => {
  disconnectObservers()

  const viewportHeight = window.innerHeight || 1
  const rootMargin = `-${viewportHeight * 0.3}px 0px -${viewportHeight * 0.5}px 0px`

  scrollTargets.value.forEach((target) => {
    if (!target.element) return

    const observer = new IntersectionObserver(handleIntersection, {
      rootMargin,
      threshold: [0, 0.5, 1]
    })

    observer.observe(target.element)
    observers.push(observer)
  })
}

const updateVisibility = () => {
  if (props.alwaysVisible) {
    isVisible.value = true
    return
  }
  isVisible.value = window.scrollY > props.showFrom
}

const handleScroll = () => {
  updateVisibility()
}

const scrollToSection = (id: string) => {
  const target = document.getElementById(id)
  if (!target) return

  const offset = props.offset
  const targetPosition = target.getBoundingClientRect().top + window.scrollY - offset

  if (nuxtApp.$scrollTo) {
    nuxtApp.$scrollTo(targetPosition, { duration: 1, easing: (t) => 1 - Math.pow(1 - t, 1.9) })
  } else {
    window.scrollTo({ top: targetPosition, behavior: 'smooth' })
  }
}

onMounted(() => {
  hasMounted.value = true
  setupObservers()
  updateVisibility()
  window.addEventListener('scroll', handleScroll, { passive: true })
  window.addEventListener('resize', setupObservers, { passive: true })
})

onBeforeUnmount(() => {
  disconnectObservers()
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', setupObservers)
})

watch(
  () => props.sections,
  () => {
    if (!hasMounted.value) return
    setupObservers()
  },
  { deep: true }
)
</script>

<style scoped>
.experience-nav {
  position: fixed;
  top: 50%;
  left: 40px;
  z-index: 40;
  display: flex;
  transform: translateY(-50%) translateX(-120%);
  transition: transform 320ms cubic-bezier(0.22, 1, 0.36, 1), opacity 320ms ease;
  opacity: 0;
}

.experience-nav--visible {
  transform: translateY(-50%) translateX(0);
  opacity: 1;
}

.experience-nav ul {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding: 1.4rem 1rem;
  min-width: 190px;
  border-radius: 28px;
  background: rgba(255, 255, 255, 0.32);
  backdrop-filter: blur(24px);
  box-shadow:
    0 25px 80px -45px rgba(15, 23, 42, 0.45),
    inset 0 1px 0 rgba(255, 255, 255, 0.7),
    inset 0 -10px 25px rgba(15, 23, 42, 0.05);
  border: 1px solid rgba(148, 163, 184, 0.28);
}

.experience-nav__link {
  display: inline-flex;
  align-items: center;
  justify-content: flex-start;
  gap: 0.65rem;
  width: 100%;
  padding: 0.55rem 1rem;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: rgba(71, 88, 114, 0.88);
  border-radius: 9999px;
  background: transparent;
  border: none;
  cursor: pointer;
  transition: color 200ms ease, background 200ms ease, box-shadow 200ms ease;
}

.experience-nav__link:hover,
.experience-nav__link:focus-visible {
  color: rgba(17, 24, 39, 0.98);
  background: rgba(255, 255, 255, 0.28);
  outline: none;
}

.experience-nav__link--active {
  color: rgba(15, 23, 42, 0.98);
  background: rgba(59, 130, 246, 0.18);
  box-shadow:
    inset 0 0 0 1px rgba(59, 130, 246, 0.25),
    0 12px 32px -20px rgba(37, 99, 235, 0.45);
}

.experience-nav__dot {
  width: 9px;
  height: 9px;
  border-radius: 9999px;
  background: rgba(148, 163, 184, 0.5);
  box-shadow: 0 0 0 2px rgba(148, 163, 184, 0.18);
  transition: transform 200ms ease, background 200ms ease, box-shadow 200ms ease;
}

.experience-nav__link--active .experience-nav__dot {
  transform: scale(1.25);
  background: rgba(59, 130, 246, 0.95);
  box-shadow: 0 0 16px rgba(59, 130, 246, 0.45);
}

.experience-nav__label {
  white-space: nowrap;
}

@media (max-width: 1023px) {
  .experience-nav {
    display: none;
  }
}
</style>

