<template>
  <div class="relative overflow-hidden bg-ink-50">
    <!-- Hero Section with Typewriter Animation -->
    <section class="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-brand-600 via-brand-700 to-ink-900 text-white overflow-hidden">
      <!-- Hero Background Image -->
      <div class="absolute inset-0">
        <img 
          src="/images/hero-bg.jpg" 
          alt="Career background" 
          class="w-full h-full object-cover"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-brand-600/80 via-brand-700/80 to-ink-900/90"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-ink-900/70 to-transparent"></div>
      </div>
      
      <div class="relative max-w-7xl mx-auto px-6 py-24 text-center z-10">
        <!-- Badge with Pulse Animation -->
        <div class="inline-flex items-center gap-2 rounded-full border-2 border-white/20 bg-white/10 backdrop-blur-md px-5 py-2.5 text-sm font-bold uppercase tracking-wider text-white mb-8 shadow-xl animate-fade-in">
          <span class="relative flex h-3 w-3">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3 w-3 bg-white"></span>
          </span>
          AI-Powered Career Platform
        </div>
        
        <!-- Hero Title with Typewriter Effect -->
        <h1 class="font-display text-5xl md:text-7xl lg:text-8xl font-bold mb-8 leading-tight animate-slide-up">
          <span class="block text-white drop-shadow-2xl mb-4 pb-2">Launch Youth Careers with</span>
          <span class="block min-h-[110px] md:min-h-[130px] lg:min-h-[150px] pb-4">
            <span class="inline-block bg-gradient-to-r from-white via-blue-100 to-white bg-clip-text text-transparent drop-shadow-lg leading-relaxed">
              {{ typedText }}<span class="animate-blink">|</span>
            </span>
          </span>
        </h1>
        
        <!-- Subtitle with better contrast -->
        <p class="text-xl md:text-2xl text-blue-50 max-w-3xl mx-auto mb-12 leading-relaxed drop-shadow-md animate-fade-in-delay font-medium">
          Help youth turn skills into first roles with AI-powered matches, curated learning paths, and expert career guidance.
        </p>
        
        <!-- CTA Buttons with Gradient -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center mb-16 animate-fade-in-delay-2">
          <NuxtLink to="/signup">
            <Button variant="gradient" size="lg" class="min-w-[200px] text-lg shadow-2xl shadow-white/20">
              <template #icon-left>
                <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </template>
              Get Started Free
            </Button>
          </NuxtLink>
          <NuxtLink to="/login">
            <Button variant="outline" size="lg" class="min-w-[200px] text-lg border-white text-white hover:bg-white hover:text-brand-600">
              Sign In
              <template #icon-right>
                <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </template>
            </Button>
          </NuxtLink>
        </div>
        
        <!-- Stats with Animation -->
        <div class="mt-20 grid grid-cols-2 md:grid-cols-4 gap-8 max-w-5xl mx-auto animate-fade-in-delay-3">
          <div v-for="(stat, index) in heroStats" :key="stat.label" 
               :ref="el => statsRefs[index] = el as HTMLElement"
               class="group p-6 rounded-2xl bg-white/10 backdrop-blur-md border border-white/20 hover:bg-white/20 transition-all duration-300 hover:scale-105 hover:shadow-2xl cursor-pointer"
               :style="{ animationDelay: `${index * 100}ms` }">
            <div class="text-5xl font-bold bg-gradient-to-r from-white to-blue-100 bg-clip-text text-transparent mb-2 group-hover:scale-110 transition-transform">
              {{ getAnimatedValue(index) }}
            </div>
            <div class="text-sm text-blue-100 font-semibold">{{ stat.label }}</div>
          </div>
        </div>

        <!-- Scroll Indicator -->
        <div class="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
          <svg class="h-8 w-8 text-white/60" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </div>
      </div>
    </section>

    <section id="features" class="relative border-t border-white/40 bg-white py-24 lg:py-28">
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/50 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
          <div>
            <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Platform chapters</span>
            <h2 class="section-heading mt-3">
              Shape every chapter of the youth career journey<br class="hidden lg:block" />
              with <span class="bg-gradient-to-r from-sky-500 via-emerald-400 to-teal-300 bg-clip-text text-transparent">clear, guided steps</span>.
            </h2>
          </div>
          <p class="section-subheading">
            Capture skills, surface opportunities, and plan learning sprints—without losing the human support that matters most.
          </p>
        </div>

        <div class="mt-16 grid gap-10 lg:grid-cols-2">
          <article
            v-for="(feature, index) in platformFeatures"
            :key="feature.title"
            class="scroll-animate opacity-0 group relative rounded-3xl bg-gradient-to-br from-white to-brand-50/30 p-8 border-2 border-brand-100 shadow-xl hover:shadow-2xl transition-all duration-500 hover:-translate-y-2 hover:border-brand-300 cursor-pointer overflow-hidden"
            :style="{ transitionDelay: `${index * 150}ms` }"
          >
            <!-- Animated Background Gradient -->
            <div class="absolute inset-0 bg-gradient-to-br from-brand-500/5 via-transparent to-brand-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            
            <!-- Content -->
            <div class="relative flex flex-col gap-8 text-ink-900 z-10">
              <header class="space-y-4">
                <GradientIcon size="md" color="brand" class="mb-2">
                  <svg class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </GradientIcon>
                <span class="inline-block px-4 py-2 rounded-full bg-brand-100 text-brand-700 text-xs font-bold uppercase tracking-wider border border-brand-200">
                  {{ feature.badge }}
                </span>
                <div>
                  <h3 class="font-display text-3xl font-bold text-ink-900 group-hover:text-brand-600 transition-colors">{{ feature.title }}</h3>
                  <p class="mt-3 text-base text-ink-600 leading-relaxed">{{ feature.summary }}</p>
                </div>
              </header>

              <ul class="grid gap-4 text-sm text-ink-700">
                <li v-for="point in feature.highlights" :key="point" class="flex items-start gap-3 group/item">
                  <span class="mt-1.5 h-2 w-2 flex-shrink-0 rounded-full bg-brand-500 shadow-lg shadow-brand-500/50 group-hover/item:scale-125 transition-transform"></span>
                  <span class="group-hover/item:text-ink-900 transition-colors">{{ point }}</span>
                </li>
              </ul>

              <div class="flex items-center justify-between rounded-2xl bg-gradient-to-r from-brand-50 to-white p-5 border-2 border-brand-200 shadow-md hover:shadow-lg transition-shadow">
                <div>
                  <p class="text-xs uppercase tracking-wider text-brand-600 font-semibold">{{ feature.metric.label }}</p>
                  <p class="text-3xl font-bold text-brand-600 mt-1">{{ feature.metric.value }}</p>
                </div>
                <NuxtLink :to="feature.cta.to">
                  <Button variant="gradient" size="sm">
                    {{ feature.cta.label }}
                    <template #icon-right>
                      <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    </template>
                  </Button>
                </NuxtLink>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section id="foundations" class="relative border-t border-white/50 bg-ink-50 py-24 lg:py-28">
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/40 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="max-w-2xl space-y-4">
          <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Foundational Pillars</span>
          <h2 class="section-heading">Built for students, mentors, and early-career partners</h2>
          <p class="section-subheading">
            These foundations power today’s release and keep the platform extensible for deeper insights, automation, and partner integrations.
          </p>
        </div>

        <div class="mt-14 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <article
            v-for="(item, index) in platformPillars"
            :key="item.title"
            class="landing-card landing-card--glass p-6 transition hover:-translate-y-1"
          >
            <div class="chip chip--ink mb-4">
              {{ item.tag }}
            </div>
            <h3 class="font-display text-lg font-semibold text-ink-900">{{ item.title }}</h3>
            <p class="mt-3 text-sm text-ink-500">{{ item.summary }}</p>
            <ul class="mt-4 space-y-2 text-sm text-ink-500">
              <li v-for="point in item.points" :key="point" class="flex items-start gap-2">
                <span class="mt-1 h-1.5 w-1.5 rounded-full bg-brand-500"></span>
                <span>{{ point }}</span>
              </li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section id="process" class="relative overflow-hidden bg-ink-900 py-24 text-white lg:py-28">
      <div class="absolute inset-y-0 right-0 hidden w-1/2 bg-gradient-to-l from-brand-500/20 via-ink-900/40 to-transparent lg:block"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="max-w-2xl space-y-4">
          <span class="text-xs font-bold uppercase tracking-[0.4em] text-white">How it works</span>
          <h2 class="font-display text-3xl font-bold sm:text-5xl text-white drop-shadow-lg">From first intake to measurable outcomes</h2>
          <p class="text-base text-white/90 leading-relaxed">
            Orchestrate every interaction—from the first story youth share to the insights employers review—without losing personal empathy.
          </p>
        </div>

        <div class="mt-14 grid gap-10 md:mt-16 md:gap-12">
          <div
            v-for="(step, index) in processJourney"
            :key="step.title"
            class="scroll-animate opacity-0 landing-card landing-card--ink grid gap-6 p-6 text-left md:grid-cols-[auto_1fr] md:items-center md:gap-10 lg:p-8"
          >
            <div class="flex items-center gap-4">
              <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-500/20 text-lg font-semibold text-brand-100 shadow-[0_20px_60px_-30px_rgba(59,130,246,0.75)]">
                {{ step.order }}
              </div>
              <div class="hidden h-full w-px bg-white/10 md:block"></div>
            </div>
            <div class="space-y-3">
              <h3 class="text-xl font-bold text-white">{{ step.title }}</h3>
              <p class="text-sm text-white/90 leading-relaxed">{{ step.copy }}</p>
              <div class="flex flex-wrap gap-3 text-xs text-white/60">
                <span
                  v-for="tag in step.tags"
                  :key="`${step.title}-${tag}`"
                  class="rounded-full border border-white/15 px-3 py-1 uppercase tracking-[0.22em]"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="matching" class="relative bg-white py-24 lg:py-28">
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="grid gap-12 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,0.85fr)] lg:items-center">
          <div class="space-y-6">
            <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Matching</span>
            <h2 class="section-heading">Explainable recommendations for every youth</h2>
            <p class="section-subheading">
              Students, mentors, and employers see exactly why a role or resource was surfaced—so decisions stay transparent and confidence stays high.
            </p>

            <div class="grid gap-6 sm:grid-cols-2">
              <div
                v-for="(highlight, index) in matchingHighlights"
                :key="highlight.title"
                class="landing-card landing-card--brand border-transparent p-5"
              >
                <h3 class="font-display text-lg font-semibold text-ink-900">{{ highlight.title }}</h3>
                <p class="mt-2 text-sm text-ink-600">{{ highlight.copy }}</p>
              </div>
            </div>
          </div>

          <div class="landing-card landing-card--glass relative overflow-hidden border-ink-100/30 bg-gradient-to-br from-white to-ink-50 p-8">
            <div class="relative space-y-6">
              <div class="flex items-center justify-between">
                <span class="text-sm font-medium text-ink-500">Sample match card</span>
                <span class="rounded-full bg-emerald-100 px-4 py-1 text-xs font-semibold text-emerald-700">Track fit</span>
              </div>
              <div class="grid gap-5">
                <div v-for="stat in matchStats" :key="stat.label" class="space-y-2">
                  <div class="flex items-center justify-between text-sm text-ink-500">
                    <span>{{ stat.label }}</span>
                    <span class="font-semibold text-ink-900">{{ stat.value }}</span>
                  </div>
                  <div class="h-2 w-full overflow-hidden rounded-full bg-ink-100">
                    <div
                      class="h-full rounded-full bg-gradient-to-r from-brand-500 via-brand-400 to-emerald-400"
                      :style="{ width: stat.fill }"
                    ></div>
                  </div>
                </div>
              </div>
              <div class="rounded-2xl border border-ink-100 bg-white p-6">
                <p class="text-xs font-semibold uppercase tracking-[0.35em] text-ink-400">What the talent coach sees</p>
                <ul class="mt-4 grid gap-3 text-sm text-ink-500">
                  <li>• Shared skills: JavaScript, Responsive Design, Communication</li>
                  <li>• Growth nudge: strengthen UI storytelling for portfolio</li>
                  <li>• Suggested sprint: build landing page challenge + Figma workshop</li>
                </ul>
              </div>
            </div>

            <div class="pointer-events-none absolute -bottom-12 right-10 h-40 w-40 rounded-full bg-brand-200/40 blur-2xl"></div>
            <div class="pointer-events-none absolute -top-14 left-6 h-36 w-36 rounded-full bg-brand-100/50 blur-2xl"></div>
          </div>
        </div>
      </div>
    </section>

    <section id="roadmap" class="relative border-t border-white/40 bg-white py-24 lg:py-28">
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/50 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="max-w-2xl space-y-4">
          <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Product Roadmap</span>
          <h2 class="section-heading">Momentum toward deeper guidance and automation</h2>
          <p class="section-subheading">
            CareerIn evolves with every cohort. Here’s what we’re building next to amplify youth employment outcomes and mentor workflows.
          </p>
        </div>

        <div class="mt-14 grid gap-6 lg:grid-cols-3">
          <article
            v-for="(milestone, index) in roadmapMilestones"
            :key="milestone.title"
            class="scroll-animate opacity-0 landing-card landing-card--glass p-6"
          >
            <div class="flex items-center gap-3 text-sm font-semibold uppercase tracking-[0.3em] text-brand-500">
              <span class="h-6 w-6 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-mono text-xs">
                {{ milestone.stage }}
              </span>
              {{ milestone.tag }}
            </div>
            <h3 class="mt-4 font-display text-lg font-semibold text-ink-900">{{ milestone.title }}</h3>
            <p class="mt-3 text-sm text-ink-500">{{ milestone.summary }}</p>
            <ul class="mt-4 space-y-2 text-sm text-ink-500">
              <li v-for="point in milestone.points" :key="point" class="flex items-start gap-2">
                <span class="mt-1 h-1.5 w-1.5 rounded-full bg-brand-500"></span>
                <span>{{ point }}</span>
              </li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section id="testimonials" class="border-t border-white/40 bg-ink-50 py-24 lg:py-28">
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="max-w-2xl space-y-4">
          <span class="text-xs font-semibold uppercase tracking-[0.35em] text-ink-400">Testimonials</span>
          <h2 class="section-heading">Trusted by youth, mentors, and hiring partners</h2>
          <p class="section-subheading">
            From students to mentors, CareerIn creates clarity, speed, and trust across every hiring motion.
          </p>
        </div>

        <div class="mt-16 grid gap-8 md:grid-cols-2">
          <figure
            v-for="(testimonial, index) in testimonials"
            :key="testimonial.name"
            class="scroll-animate opacity-0 landing-card landing-card--glass p-8 transition hover:-translate-y-1"
          >
            <div class="absolute -top-6 right-8 text-6xl text-ink-100">“</div>
            <blockquote class="space-y-4 text-sm text-ink-500">
              <p>{{ testimonial.quote }}</p>
            </blockquote>
            <figcaption class="mt-6 flex items-center justify-between">
              <div>
                <p class="text-base font-semibold text-ink-900">{{ testimonial.name }}</p>
                <p class="text-xs text-ink-400">{{ testimonial.role }}</p>
              </div>
              <span class="rounded-full bg-ink-900/5 px-3 py-1 text-xs font-medium text-ink-500">{{ testimonial.type }}</span>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section id="contact" class="relative overflow-hidden bg-ink-900 py-24 text-white lg:py-28">
      <div class="pointer-events-none absolute inset-0">
        <div class="absolute -left-24 top-1/3 h-72 w-72 rounded-full bg-brand-400/40 blur-3xl"></div>
        <div class="absolute right-0 top-0 h-60 w-60 translate-x-1/3 rounded-full bg-emerald-400/40 blur-3xl"></div>
      </div>

        <div class="relative mx-auto max-w-5xl rounded-[36px] border border-white/10 bg-gradient-to-br from-white/10 via-white/5 to-transparent p-10 shadow-[0_45px_140px_-80px_rgba(56,189,248,0.6)] backdrop-blur">
        <div class="flex flex-col items-start gap-8 lg:flex-row lg:items-center lg:justify-between">
          <div class="max-w-xl space-y-4">
            <span class="inline-flex items-center gap-2 rounded-full border-2 border-white/30 bg-white/10 backdrop-blur-sm px-4 py-2 text-xs font-bold uppercase tracking-[0.35em] text-white">
                <span class="h-2 w-2 rounded-full bg-emerald-300 animate-pulse"></span>
                Ready to get started?
            </span>
            <h2 class="font-display text-4xl font-bold sm:text-5xl text-white drop-shadow-2xl">
                Launch your youth talent program in weeks
            </h2>
            <p class="text-base text-white/95 leading-relaxed">
                Schedule a walkthrough to explore talent profiles, opportunity matching, and learning analytics tailored to your organisation.
            </p>
          </div>
          <div class="flex w-full flex-col items-stretch gap-3 lg:w-auto lg:min-w-[260px]">
            <NuxtLink
              to="/signup"
              class="inline-flex items-center justify-center rounded-full bg-white px-6 py-3 text-sm font-semibold text-ink-900 shadow-lg shadow-ink-900/30 transition hover:bg-ink-50"
            >
                Start a pilot
            </NuxtLink>
            <NuxtLink
              to="/login"
              class="inline-flex items-center justify-center rounded-full border border-white/30 px-6 py-3 text-sm font-semibold text-white transition hover:border-white/50"
            >
                Already a partner? Sign in
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, type ComponentPublicInstance } from 'vue'
import Button from '~/components/ui/Button.vue'
import GradientIcon from '~/components/ui/GradientIcon.vue'

definePageMeta({
  layout: 'default'
})

// Typewriter Animation
const words = ['Transparent Matches', 'AI-Powered Insights', 'Curated Learning', 'Career Guidance']
const typedText = ref('')
const currentWordIndex = ref(0)
const currentCharIndex = ref(0)
const isDeleting = ref(false)
let typingTimeout: ReturnType<typeof setTimeout> | null = null

const typeWriter = () => {
  const currentWord = words[currentWordIndex.value]
  
  if (!currentWord) return
  
  if (!isDeleting.value) {
    // Typing
    typedText.value = currentWord.substring(0, currentCharIndex.value + 1)
    currentCharIndex.value++
    
    if (currentCharIndex.value === currentWord.length) {
      // Pause before deleting
      typingTimeout = setTimeout(() => {
        isDeleting.value = true
        typeWriter()
      }, 2000)
      return
    }
    
    typingTimeout = setTimeout(typeWriter, 100)
  } else {
    // Deleting
    typedText.value = currentWord.substring(0, currentCharIndex.value - 1)
    currentCharIndex.value--
    
    if (currentCharIndex.value === 0) {
      isDeleting.value = false
      currentWordIndex.value = (currentWordIndex.value + 1) % words.length
    }
    
    typingTimeout = setTimeout(typeWriter, 50)
  }
}

// Scroll-triggered animation observer
const animateOnScroll = () => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-fade-in-up')
          observer.unobserve(entry.target)
        }
      })
    },
    {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    }
  )

  // Observe all cards and sections
  const elements = document.querySelectorAll('.scroll-animate')
  elements.forEach((el) => observer.observe(el))
}

onMounted(() => {
  typeWriter()
  // Wait for DOM to be fully rendered
  setTimeout(() => {
    animateOnScroll()
  }, 100)
})

onBeforeUnmount(() => {
  if (typingTimeout) {
    clearTimeout(typingTimeout)
  }
})

const heroStats = [
  { label: 'Active Users', value: '2.5k+', numericValue: 2500, suffix: 'k+', divisor: 1000 },
  { label: 'Job Listings', value: '1.8k+', numericValue: 1800, suffix: 'k+', divisor: 1000 },
  { label: 'Success Rate', value: '94%', numericValue: 94, suffix: '%', divisor: 1 },
  { label: 'Partner Companies', value: '150+', numericValue: 150, suffix: '+', divisor: 1 }
]

// Animated counters for stats
const statsRefs = ref<HTMLElement[]>([])
const statCounts = ref([0, 0, 0, 0])
const statsAnimated = ref([false, false, false, false])

// Format the animated value
const getAnimatedValue = (index: number) => {
  const stat = heroStats[index]
  const count = statCounts.value[index] ?? 0
  
  if (!stat) return '0'
  
  if (stat.divisor > 1) {
    const displayValue = (count / stat.divisor).toFixed(1)
    return displayValue + stat.suffix
  }
  
  return count + stat.suffix
}

// Animate a single stat counter
const animateStat = (index: number) => {
  if (statsAnimated.value[index]) return
  
  const stat = heroStats[index]
  if (!stat) return
  
  const duration = 2000
  const startTime = Date.now()
  const startValue = 0
  const endValue = stat.numericValue
  
  const animate = () => {
    const now = Date.now()
    const progress = Math.min((now - startTime) / duration, 1)
    
    // Easing function (ease-out cubic)
    const easeOut = 1 - Math.pow(1 - progress, 3)
    statCounts.value[index] = Math.floor(easeOut * endValue)
    
    if (progress < 1) {
      requestAnimationFrame(animate)
    } else {
      statCounts.value[index] = endValue
      statsAnimated.value[index] = true
    }
  }
  
  animate()
}

// Setup intersection observer for stats
onMounted(() => {
  if (typeof window === 'undefined') return
  
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = statsRefs.value.indexOf(entry.target as HTMLElement)
          if (index !== -1 && !statsAnimated.value[index]) {
            // Add slight delay for staggered effect
            setTimeout(() => animateStat(index), index * 100)
          }
        }
      })
    },
    {
      threshold: 0.5,
      rootMargin: '0px'
    }
  )
  
  // Observe all stat elements
  statsRefs.value.forEach((el) => {
    if (el) observer.observe(el)
  })
  
  // Cleanup
  onUnmounted(() => {
    observer.disconnect()
  })
})

const platformFeatures = [
  {
    id: 'feature-auth',
    badge: 'Secure Onboarding',
    title: 'Create an account in minutes',
    summary:
      'Responsive signup, validation, and track selection help youth and mentors jump in quickly while keeping data protected.',
    highlights: [
      'Guided steps capture education, experience, and preferences',
      'Reduced friction with mobile-friendly flows and password rules',
      'Instant access to the dashboard after verification'
    ],
    metric: { label: 'Accounts activated', value: '8.5k+' },
    cta: { label: 'Preview signup', to: '/signup' },
    gradient: 'from-brand-700 via-ink-900 to-ink-950'
  },
  {
    id: 'feature-profile',
    badge: 'Profile Workspace',
    title: 'Capture your skills & ambitions',
    summary:
      'Turn scattered experience into a living, structured profile. Upload projects, paste CV highlights, and log capabilities so employers see the full story.',
    highlights: [
      'Guided intake for education, experience, and target roles',
      'Skill tagging with proficiency and context notes',
      'Career notes stored for future AI enrichment'
    ],
    metric: { label: 'Skills catalogued', value: '60+' },
    cta: { label: 'View profile tools', to: '/profile' },
    gradient: 'from-slate-900 via-brand-900 to-ink-950'
  },
  {
    id: 'feature-matching',
    badge: 'Opportunity Matching',
    title: 'Discover transparent job matches',
    summary:
      'Surface internships, apprenticeships, and entry-level roles that align to your skills, track, and readiness—always with a clear explanation.',
    highlights: [
      'Explainable overlap between your skills and job requirements',
      'Track-aware filters for web, data, design, marketing, and more',
      'Experience cues reveal when to level up before applying'
    ],
    metric: { label: 'Starter roles listed', value: '20+' },
    cta: { label: 'Browse opportunities', to: '/jobs' },
    gradient: 'from-indigo-900 via-brand-800 to-sky-500'
  },
  {
    id: 'feature-dashboard',
    badge: 'Career Dashboard',
    title: 'See the next best action instantly',
    summary:
      'Youth and mentors track applications, learning sprints, and profile strength in one workspace so progress never stalls.',
    highlights: [
      'Weekly focus cards surface priority jobs and learning',
      'Real-time readiness indicators sync with mentor feedback',
      'Profile reminders keep completeness high'
    ],
    metric: { label: 'Journeys in motion', value: '12k+' },
    cta: { label: 'Open dashboard', to: '/dashboard' },
    gradient: 'from-ink-950 via-slate-900 to-brand-700'
  },
  {
    id: 'feature-learning',
    badge: 'Learning Journeys',
    title: 'Close skill gaps intentionally',
    summary:
      'Connect every growth goal to curated resources—from global MOOCs to local bootcamps—so you always know the next course, challenge, or mentor session.',
    highlights: [
      'Balanced mix of free and paid resources with cost signal',
      'Resources mapped to in-demand and aspirational skills',
      'Playlist support to plan weekly learning sprints'
    ],
    metric: { label: 'Resources mapped', value: '320+' },
    cta: { label: 'Explore learning hub', to: '/resources' },
    gradient: 'from-emerald-600 via-brand-500 to-sky-400'
  },
  {
    id: 'feature-insights',
    badge: 'Impact Analytics',
    title: 'Turn activity into career intelligence',
    summary:
      'Leaders and NGOs monitor placement velocity, skill coverage, and mentor impact with export-ready dashboards.',
    highlights: [
      'Placement progress tracked by cohort, partner, and role type',
      'Skill heatmaps reveal gaps before interviews are scheduled',
      'Benchmarks align programs to SDG-aligned outcomes'
    ],
    metric: { label: 'Insight views/month', value: '18k' },
    cta: { label: 'Review analytics', to: '/#roadmap' },
    gradient: 'from-slate-900 via-blue-900 to-sky-600'
  }
] as const

const platformPillars = [
  {
    tag: 'Onboarding',
    title: 'Secure sign up & identity',
    summary: 'Give every youth a fast, secure way to register and return.',
    points: [
      'Email-based authentication with validation and password rules',
      'Profile basics captured from day one: education, track, experience level',
      'Session awareness keeps navigation simple across devices'
    ]
  },
  {
    tag: 'Profile',
    title: 'Skill-rich storytelling',
    summary: 'Structured fields distill projects, skills, and ambition into a shareable asset.',
    points: [
      'Editable skills list with notes on proficiency and context',
      'Lightweight project/experience cards ready for mentors to review',
      'Career notes field for future AI enrichment'
    ]
  },
  {
    tag: 'Jobs',
    title: 'Seeded opportunity catalog',
    summary: 'Employers and NGOs can publish youth-ready opportunities with clarity.',
    points: [
      '15+ curated roles with skill requirements and experience guidance',
      'Flexible filters for track, job type, and location',
      'Job detail view highlights why the role matters'
    ]
  },
  {
    tag: 'Learning',
    title: 'Mapped learning resources',
    summary: 'Resources cover the skills that matter for first roles and future steps.',
    points: [
      '15+ resources spanning MOOCs, YouTube, local providers',
      'Each resource linked to skills and cost indicator',
      'Dedicated view so mentors can co-plan learning sprints'
    ]
  },
  {
    tag: 'Matching',
    title: 'Rule-based recommendations',
    summary: 'Transparent logic connects profiles to opportunity and learning gaps.',
    points: [
      'Skill overlap explains every job suggestion',
      'Learning prompts highlight missing capabilities',
      'Track preference keeps suggestions relevant'
    ]
  },
  {
    tag: 'Dashboard',
    title: 'Mentor-ready insights',
    summary: 'Dashboard experiences keep students, mentors, and partners in sync.',
    points: [
      'Responsive layout for mobile-first access',
      'Navigation across Dashboard, Jobs, Resources, Profile, Logout',
      'Card system spotlights recent matches and active learning'
    ]
  }
] as const

const processJourney = [
  {
    order: '01',
    title: 'Create your account',
    copy:
      'Register with a secure email and set your preferred career track, experience level, and education background.',
    tags: ['signup', 'foundation', 'secure']
  },
  {
    order: '02',
    title: 'Describe your skills & story',
    copy:
      'Add skills, log projects or internships, and paste CV highlights so the platform understands your starting point.',
    tags: ['skills', 'profile', 'story']
  },
  {
    order: '03',
    title: 'Review opportunity matches',
    copy:
      'Browse curated jobs with skill overlap explanations. Understand which roles need polishing and which you can pursue today.',
    tags: ['jobs', 'matching', 'transparent']
  },
  {
    order: '04',
    title: 'Plan your learning sprint',
    copy:
      'Pick resources for missing skills, drop them into your dashboard, and track progress with mentor or peer support.',
    tags: ['growth', 'resources', 'actionable']
  }
] as const

const matchingHighlights = [
  {
    title: 'Transparent skill overlap',
    copy: 'Each recommendation lists the exact skills shared between your profile and the opportunity.'
  },
  {
    title: 'Track-aware suggestions',
    copy: 'Preferred career tracks steer the jobs and courses you see, keeping everything relevant to your goals.'
  },
  {
    title: 'Learning gap nudges',
    copy: 'Resources highlight the skills you have not logged yet so you know where to focus next.'
  },
  {
    title: 'Mentor-ready context',
    copy: 'Shareable match context helps mentors coach youth toward interviews and learning sprints faster.'
  }
] as const

const matchStats = [
  { label: 'Skill overlap', value: '78%', fill: '78%' },
  { label: 'Track alignment', value: '96%', fill: '96%' },
  { label: 'Experience fit', value: '58%', fill: '58%' },
  { label: 'Learning prompts ready', value: '4 resources', fill: '80%' }
] as const

const roadmapMilestones = [
  {
    stage: 'Q1',
    tag: 'Signals',
    title: 'Readiness telemetry',
    summary: 'Stream skill progress, job activity, and mentor feedback into living dashboards.',
    points: [
      'Confidence sliders capture how youth feel heading into interviews',
      'Sentiment analysis blends qualitative notes with outcomes',
      'Alerts fire when profiles stagnate or skills go stale'
    ]
  },
  {
    stage: 'Q2',
    tag: 'Automation',
    title: 'Smart placement pipeline',
    summary: 'Auto-assemble candidate packets with verified skills, projects, and mentor references.',
    points: [
      'Generate shareable talent profiles for employer partners',
      'Coordinate interviews across cohorts with scheduling assists',
      'Track offer stages and provide AI-generated next steps'
    ]
  },
  {
    stage: 'Q3',
    tag: 'Intelligence',
    title: 'Predictive cohort analytics',
    summary: 'Forecast placement rates, skill demand, and resource ROI for partners and NGOs.',
    points: [
      'Benchmark youth progress across locations and programs',
      'Model the impact of new resources or employer pipelines',
      'Surface SDG-aligned metrics for impact reports'
    ]
  }
] as const

const testimonials = [
  {
    name: 'Amina Yusuf',
    role: 'Final-year CS Student',
    type: 'Student',
    quote:
      'CareerIn translated my campus projects into skills employers recognised. I landed three internship interviews in a week, backed by transparent matches.'
  },
  {
    name: 'David Mensah',
    role: 'Career Mentor',
    type: 'Mentor',
    quote:
      'The dashboard shows my mentees which skills to strengthen next. We collaborate on learning sprints that are easy to track and celebrate.'
  },
  {
    name: 'Priya Nair',
    role: 'Junior UI Designer',
    type: 'Graduate',
    quote:
      'Seeing “Matches: HTML, Portfolio Storytelling” under each role gave me the confidence to apply. The platform made my first job search feel guided.'
  },
  {
    name: 'Luis Ortega',
    role: 'Aspiring Data Analyst',
    type: 'Job Seeker',
    quote:
      'Matching skills to jobs plus nudged learning resources made building my study plan effortless. I always know the next skill to level up.'
  }
] as const

const registerFeatureCard = (el: Element | ComponentPublicInstance | null, index: number) => {
  // Simplified - no animations for now
}
</script>
