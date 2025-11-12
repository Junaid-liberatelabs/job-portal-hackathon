<template>
  <div class="relative overflow-hidden bg-ink-50">
    <section class="relative isolate overflow-hidden">
      <HeroScene />

      <div class="pointer-events-none absolute inset-0">
        <div class="absolute -left-32 top-0 h-[520px] w-[520px] rounded-full bg-brand-100/50 blur-3xl"></div>
        <div class="absolute right-0 top-1/3 h-[520px] w-[520px] translate-x-1/4 rounded-full bg-brand-200/40 blur-3xl"></div>
        <div class="absolute left-1/2 top-40 h-[380px] w-[860px] -translate-x-1/2 rounded-full bg-radial-spot opacity-70"></div>
      </div>

      <div class="relative mx-auto grid max-w-7xl items-center gap-20 px-6 pb-24 pt-32 lg:grid-cols-[minmax(0,1.05fr)_minmax(0,0.9fr)] lg:px-10 lg:pb-32 lg:pt-40">
        <div class="space-y-10 z-10">
          <div class="inline-flex items-center gap-3 rounded-full border border-brand-200/80 bg-white/80 px-5 py-2 text-xs font-semibold uppercase tracking-[0.35em] text-brand-700 shadow-sm shadow-brand-200/60 backdrop-blur" v-scroll-reveal="{ direction: 'up', distance: 32, duration: 720 }">
            <span class="h-2.5 w-2.5 rounded-full bg-emerald-400 shadow-[0_0_12px_rgba(52,211,153,0.75)]"></span>
            Youth employment platform
          </div>

          <div class="space-y-6">
            <h1 class="font-display text-4xl font-semibold tracking-tight text-ink-900 sm:text-5xl lg:text-6xl" v-scroll-reveal="{ direction: 'up', distance: 56, duration: 720 }">
              CareerIn guides students<br class="hidden sm:block" />
              from <span class="bg-gradient-to-r from-brand-600 via-brand-500 to-emerald-400 bg-clip-text text-transparent">skills to first roles</span>.
            </h1>
            <p class="text-lg text-ink-500 sm:max-w-xl" v-scroll-reveal="{ direction: 'up', distance: 52, duration: 720, delay: 140 }">
              Map your strengths, explore entry-level opportunities, and develop a personalised learning path in one place. CareerIn keeps every step transparent,
              actionable, and ready to grow with you.
            </p>
          </div>

          <div class="flex flex-col items-start gap-4 sm:flex-row sm:items-center" v-scroll-reveal="{ direction: 'up', distance: 48, duration: 720, delay: 220 }">
            <NuxtLink
              to="/signup"
              class="inline-flex items-center justify-center rounded-full bg-ink-900 px-6 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink-900/40"
            >
              Create your profile
            </NuxtLink>
            <NuxtLink
              to="/#features"
              class="inline-flex items-center justify-center rounded-full border border-ink-200/80 px-6 py-3 text-sm font-semibold text-ink-600 transition hover:border-brand-200 hover:text-ink-900 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-200"
            >
              See how it works
            </NuxtLink>
          </div>

          <dl class="grid grid-cols-2 gap-8 text-sm text-ink-500 sm:flex sm:flex-wrap sm:gap-12">
            <div v-for="(stat, index) in heroStats" :key="stat.label" class="space-y-1" v-scroll-reveal="{ direction: 'up', distance: 48, duration: 700, delay: index * 120 }">
              <dt class="uppercase tracking-[0.25em] text-ink-400">{{ stat.label }}</dt>
              <dd class="font-display text-3xl font-semibold text-ink-900">{{ stat.value }}</dd>
            </div>
          </dl>
        </div>

        <div class="relative z-10" v-scroll-reveal="{ direction: 'right', distance: 80, duration: 760 }">
          <HeroOrbit />
        </div>
      </div>
    </section>

    <section id="features" class="relative border-t border-white/40 bg-white py-24 lg:py-28">
      <div class="pointer-events-none absolute inset-0 -z-10 opacity-60">
        <HeroScene color-a="#1d4ed8" color-b="#38bdf8" :density="0.45" />
      </div>
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/50 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
          <div v-scroll-reveal="{ direction: 'up', distance: 44, duration: 680 }">
            <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Platform</span>
            <h2 class="section-heading mt-3">Everything you need to launch youth careers</h2>
          </div>
          <p class="section-subheading" v-scroll-reveal="{ direction: 'up', distance: 44, duration: 680, delay: 160 }">
            CareerIn gives young talent one place to define their skills, discover real opportunities, and stay aligned with growth goals.
          </p>
        </div>

        <div class="mt-16 grid gap-10 lg:grid-cols-2">
          <article
            v-for="(feature, index) in featureCards"
            :key="feature.title"
            class="group relative overflow-hidden rounded-[32px] border border-white/20 bg-gradient-to-br p-8 shadow-floating-card transition duration-500 hover:-translate-y-2 hover:shadow-[0_50px_150px_-60px_rgba(37,99,235,0.45)]"
            :class="feature.gradient"
            v-scroll-reveal="{ direction: index % 2 === 0 ? 'left' : 'right', distance: 80, duration: 760, delay: index * 140 }"
          >
            <div class="pointer-events-none absolute inset-0 opacity-60 mix-blend-screen">
              <div class="absolute inset-0 bg-gradient-to-br from-white/25 via-white/10 to-transparent"></div>
            </div>
            <div class="relative flex flex-col gap-8 text-white">
              <header class="space-y-4">
                <span class="inline-flex rounded-full bg-white/20 px-3 py-1 text-xs font-semibold uppercase tracking-[0.25em] text-white/70">
                  {{ feature.pill }}
                </span>
                <div>
                  <h3 class="font-display text-2xl font-semibold">{{ feature.title }}</h3>
                  <p class="mt-3 text-sm text-white/80">{{ feature.subtitle }}</p>
                </div>
              </header>

              <ul class="grid gap-4 text-sm text-white/80">
                <li v-for="point in feature.points" :key="point" class="flex items-start gap-3">
                  <span class="mt-1 h-2 w-2 flex-shrink-0 rounded-full bg-white/70 shadow-[0_0_6px_rgba(255,255,255,0.6)]"></span>
                  <span>{{ point }}</span>
                </li>
              </ul>

              <div class="flex items-center justify-between rounded-2xl bg-white/10 p-4 text-white/90 ring-1 ring-white/15 backdrop-blur">
                <div>
                  <p class="text-xs uppercase tracking-[0.25em] text-white/60">{{ feature.highlight.label }}</p>
                  <p class="text-xl font-semibold">{{ feature.highlight.value }}</p>
                </div>
                <NuxtLink :to="feature.cta.to" class="inline-flex items-center gap-2 text-sm font-semibold transition hover:text-white/80">
                  {{ feature.cta.label }}
                  <span aria-hidden="true">→</span>
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
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 44, duration: 700 }">
          <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Foundational Pillars</span>
          <h2 class="section-heading">Built for students, mentors, and early-career partners</h2>
          <p class="section-subheading">
            These foundations power today’s release and keep the platform extensible for deeper insights, automation, and partner integrations.
          </p>
        </div>

        <div class="mt-14 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <article
            v-for="(item, index) in platformFoundations"
            :key="item.title"
            class="group relative overflow-hidden rounded-3xl border border-white/70 bg-white p-6 shadow-[0_35px_90px_-60px_rgba(15,23,42,0.4)] transition hover:-translate-y-1"
            v-scroll-reveal="{ direction: index % 3 === 0 ? 'left' : index % 3 === 1 ? 'up' : 'right', distance: 64, duration: 720, delay: index * 120 }"
          >
            <div class="mb-4 inline-flex items-center gap-2 rounded-full bg-brand-50 px-3 py-1 text-xs font-semibold uppercase tracking-[0.3em] text-brand-600">
              <span class="text-brand-500">{{ item.tag }}</span>
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
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 48, duration: 720 }">
          <span class="text-xs font-semibold uppercase tracking-[0.4em] text-brand-200/90">How it works</span>
          <h2 class="font-display text-3xl font-semibold sm:text-4xl">From first login to your next opportunity</h2>
          <p class="text-sm text-white/70">
            A guided experience keeps students, graduates, and mentors aligned on next actions and outcomes.
          </p>
        </div>

        <div class="mt-14 grid gap-10 md:mt-16 md:gap-12">
          <div
            v-for="(step, index) in processSteps"
            :key="step.title"
            class="relative grid gap-6 rounded-[28px] border border-white/10 bg-white/5 p-6 text-left shadow-[0_35px_120px_-70px_rgba(59,130,246,0.6)] backdrop-blur md:grid-cols-[auto_1fr] md:items-center md:gap-10 lg:p-8"
            v-scroll-reveal="{ direction: 'up', distance: 72, duration: 760, delay: index * 130 }"
          >
            <div class="flex items-center gap-4">
              <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-500/20 text-lg font-semibold text-brand-100">
                {{ step.order }}
              </div>
              <div class="hidden h-full w-px bg-white/10 md:block"></div>
            </div>
            <div class="space-y-3">
              <h3 class="text-xl font-semibold">{{ step.title }}</h3>
              <p class="text-sm text-white/80">{{ step.copy }}</p>
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
      <div class="pointer-events-none absolute inset-0 -z-10 opacity-45">
        <HeroScene color-a="#0ea5e9" color-b="#2563eb" :density="0.35" />
      </div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="grid gap-12 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,0.85fr)] lg:items-center">
          <div class="space-y-6">
            <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500" v-scroll-reveal="{ direction: 'up', distance: 40, duration: 680 }">Matching</span>
            <h2 class="section-heading" v-scroll-reveal="{ direction: 'up', distance: 56, duration: 720, delay: 120 }">Understand why every recommendation appears</h2>
            <p class="section-subheading" v-scroll-reveal="{ direction: 'up', distance: 48, duration: 720, delay: 220 }">
              We combine AI scoring, structured mentor feedback, and real employer demand to explain every match. Students get clarity and trust; employers see fit and
              readiness instantly.
            </p>

            <div class="grid gap-6 sm:grid-cols-2">
              <div
                v-for="(highlight, index) in matchingHighlights"
                :key="highlight.title"
                class="rounded-3xl border border-brand-100 bg-brand-50/60 p-5 shadow-[0_25px_80px_-50px_rgba(37,99,235,0.4)]"
                v-scroll-reveal="{ direction: index % 2 === 0 ? 'left' : 'right', distance: 72, duration: 720, delay: index * 140 }"
              >
                <h3 class="font-display text-lg font-semibold text-ink-900">{{ highlight.title }}</h3>
                <p class="mt-2 text-sm text-ink-600">{{ highlight.copy }}</p>
              </div>
            </div>
          </div>

          <div class="relative overflow-hidden rounded-[32px] border border-ink-100 bg-gradient-to-br from-white to-ink-50 p-8 shadow-[0_30px_90px_-45px_rgba(15,23,42,0.3)]" v-scroll-reveal="{ direction: 'up', distance: 64, duration: 760, delay: 260 }">
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
                <p class="text-xs font-semibold uppercase tracking-[0.35em] text-ink-400">What the user sees</p>
                <ul class="mt-4 grid gap-3 text-sm text-ink-500">
                  <li>• Matching skills: HTML, CSS, Communication</li>
                  <li>• Missing skill prompt: Responsive Design Basics</li>
                  <li>• Learning suggestion: Free Figma starter course</li>
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
      <div class="pointer-events-none absolute inset-0 -z-10 opacity-35">
        <HeroScene color-a="#1e3a8a" color-b="#38bdf8" :density="0.28" />
      </div>
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/50 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 44, duration: 700 }">
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
            class="relative overflow-hidden rounded-3xl border border-ink-100 bg-ink-50 p-6 shadow-[0_30px_80px_-55px_rgba(15,23,42,0.35)]"
            v-scroll-reveal="{ direction: index === 0 ? 'left' : index === 1 ? 'up' : 'right', distance: 68, duration: 720, delay: index * 150 }"
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
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 44, duration: 700 }">
          <span class="text-xs font-semibold uppercase tracking-[0.35em] text-ink-400">Testimonials</span>
          <h2 class="section-heading">See how CareerIn transforms hiring outcomes</h2>
          <p class="section-subheading">
            From students to mentors, CareerIn creates clarity, speed, and trust across every hiring motion.
          </p>
        </div>

        <div class="mt-16 grid gap-8 md:grid-cols-2">
          <figure
            v-for="(testimonial, index) in testimonials"
            :key="testimonial.name"
            class="relative overflow-hidden rounded-[28px] border border-white/60 bg-white p-8 shadow-[0_35px_100px_-60px_rgba(15,23,42,0.35)] transition hover:-translate-y-1"
            v-scroll-reveal="{ direction: index % 2 === 0 ? 'left' : 'right', distance: 70, duration: 720, delay: index * 150 }"
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

      <div class="relative mx-auto max-w-5xl rounded-[36px] border border-white/10 bg-gradient-to-br from-white/10 via-white/5 to-transparent p-10 shadow-[0_45px_140px_-80px_rgba(56,189,248,0.6)] backdrop-blur" v-scroll-reveal="{ direction: 'up', distance: 64, duration: 760 }">
        <div class="flex flex-col items-start gap-8 lg:flex-row lg:items-center lg:justify-between">
          <div class="max-w-xl space-y-4">
            <span class="inline-flex items-center gap-2 rounded-full border border-white/20 px-3 py-1 text-xs uppercase tracking-[0.35em] text-white/80">
              <span class="h-1.5 w-1.5 rounded-full bg-emerald-300"></span>
              Let’s build the future of work
            </span>
            <h2 class="font-display text-3xl font-semibold sm:text-4xl">
              Your next role starts with the right platform
            </h2>
            <p class="text-sm text-white/70">
              Set up your profile, explore matched opportunities, and move forward with a personal learning plan today.
            </p>
          </div>
          <div class="flex w-full flex-col items-stretch gap-3 lg:w-auto lg:min-w-[260px]">
            <NuxtLink
              to="/signup"
              class="inline-flex items-center justify-center rounded-full bg-white px-6 py-3 text-sm font-semibold text-ink-900 shadow-lg shadow-ink-900/30 transition hover:bg-ink-50"
            >
              Create free account
            </NuxtLink>
            <NuxtLink
              to="/login"
              class="inline-flex items-center justify-center rounded-full border border-white/30 px-6 py-3 text-sm font-semibold text-white transition hover:border-white/50"
            >
              Already registered? Sign in
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import HeroOrbit from '~/components/HeroOrbit.vue'
import HeroScene from '~/components/HeroScene.vue'

const heroStats = [
  { label: 'Career tracks covered', value: '8' },
  { label: 'Starter roles curated', value: '20+' },
  { label: 'Learning resources', value: '30+' },
  { label: 'Skills catalogued', value: '60+' }
]

const featureCards = [
  {
    pill: 'Profile Workspace',
    title: 'Capture your skills & goals',
    subtitle: 'Build a living profile with education, experiences, skills, and CV notes so the platform understands where you are starting from.',
    points: [
      'Add unlimited skills with context and proficiency',
      'Log projects, internships, and volunteer work in seconds',
      'Capture CV highlights to unlock deeper insights and automation'
    ],
    highlight: { label: 'Skills logged', value: '60+' },
    cta: { label: 'See the profile flow', to: '/#process' },
    gradient: 'from-brand-700 via-brand-600 to-ink-900'
  },
  {
    pill: 'Job Explorer',
    title: 'Discover youth-focused opportunities',
    subtitle: 'Browse internships, fellowships, and entry-level roles with transparent skill requirements and experience expectations.',
    points: [
      'Filter by track, location, and job type in one view',
      'See real-time skill overlaps with your profile',
      'Spot recommended experience levels before applying'
    ],
    highlight: { label: 'Starter roles listed', value: '20+' },
    cta: { label: 'Review job catalogue', to: '/#matching' },
    gradient: 'from-ink-900 via-brand-900 to-ink-950'
  },
  {
    pill: 'Learning Hub',
    title: 'Close your skill gaps intentionally',
    subtitle: 'Connect each target skill to curated learning resources across YouTube, Coursera, Udemy, and local platforms.',
    points: [
      'Balance free and paid content with clear cost labels',
      'Tag courses directly to skills you want to strengthen',
      'Track completion plans alongside job applications'
    ],
    highlight: { label: 'Resources linked', value: '30+' },
    cta: { label: 'Explore the resource hub', to: '/#matching' },
    gradient: 'from-brand-600 via-brand-500 to-emerald-400'
  },
  {
    pill: 'Career Dashboard',
    title: 'Stay on top of next actions',
    subtitle: 'Launch directly into a dashboard that summarises your profile, job matches, and recommended learning paths.',
    points: [
      'Glanceable profile snapshot with education and track',
      'Recommended jobs with “Matches: HTML, CSS” callouts',
      'Learning suggestions nudging you toward target roles'
    ],
    highlight: { label: 'Cards surfaced', value: 'Personalised view' },
    cta: { label: 'Preview the dashboard', to: '/#process' },
    gradient: 'from-ink-900 via-ink-800 to-brand-700'
  }
]

const platformFoundations = [
  {
    tag: 'AUTH',
    title: 'Authentication & Accounts',
    summary: 'Secure, student-friendly authentication with contextual onboarding.',
    points: [
      'Enforce email validation and password strength',
      'Store name, education, experience level, and preferred track',
      'Provide login/logout with session awareness'
    ]
  },
  {
    tag: 'PROFILE',
    title: 'Skill-rich user profiles',
    summary: 'Give every user a workspace to capture skills, experiences, and ambitions.',
    points: [
      'Editable skills list with proficiency or context',
      'Text area for CV highlights or career notes',
      'Project and experience snippets that surface in the dashboard'
    ]
  },
  {
    tag: 'JOBS',
    title: 'Seeded job opportunities',
    summary: 'Curate internships and entry roles with transparent expectations.',
    points: [
      'Support filters by track, job type, and location',
      'Show recommended experience level (Fresher, Junior, etc.)',
      'Display required skills for each listing'
    ]
  },
  {
    tag: 'LEARN',
    title: 'Learning resources hub',
    summary: 'Connect every skill to curated courses, playlists, and local opportunities.',
    points: [
      'Mix free and paid resources with clear cost labels',
      'Include platform, URL, and skill mapping fields',
      'Expose resources in a dedicated “Learning” view'
    ]
  },
  {
    tag: 'MATCH',
    title: 'Rule-based recommendations',
    summary: 'Offer transparent matches for jobs and learning paths with explainable logic.',
    points: [
      'Highlight shared skills in each recommendation',
      'Include guidance when required skills are missing',
      'Extend the same approach to learning resource suggestions'
    ]
  },
  {
    tag: 'UI',
    title: 'Youth-centric dashboard',
    summary: 'Serve actionable insights across devices for students, mentors, and partners.',
    points: [
      'Responsive layout accessible on mobile and desktop',
      'Navigation covering Dashboard, Jobs, Resources, Profile, Logout',
      'Cards that make youth progress visible to mentors and partners'
    ]
  }
]

const processSteps = [
  {
    order: '01',
    title: 'Create your account',
    copy: 'Register with email, set your education background, experience level, and preferred career track.',
    tags: ['signup', 'foundation']
  },
  {
    order: '02',
    title: 'Describe your skills & story',
    copy: 'Add skills, log projects or internships, and paste CV highlights so CareerIn understands your starting point.',
    tags: ['skills', 'profile']
  },
  {
    order: '03',
    title: 'Review job matches',
    copy: 'Browse opportunities filtered to your track with skill overlap badges that show exactly why a role fits.',
    tags: ['jobs', 'matching']
  },
  {
    order: '04',
    title: 'Plan your learning sprint',
    copy: 'Pick learning resources mapped to the skills you want to grow and monitor them from your dashboard.',
    tags: ['resources', 'growth']
  }
]

const matchHighlights = [
  {
    title: 'Transparent skill overlap',
    copy: 'Each recommendation lists the exact skills shared between your profile and the opportunity.',
    icon: 'SO'
  },
  {
    title: 'Track-aware suggestions',
    copy: 'Preferred career tracks steer the jobs and courses you see, keeping everything relevant to your goals.',
    icon: 'CT'
  },
  {
    title: 'Learning gap nudges',
    copy: 'Resources highlight the skills you have not logged yet so you know where to focus your next sprint.',
    icon: 'LG'
  }
]

const matchingHighlights = [
  {
    title: 'Transparent skill overlap',
    copy: 'Each recommendation lists the exact skills shared between your profile and the opportunity.',
    icon: 'SO'
  },
  {
    title: 'Track-aware suggestions',
    copy: 'Preferred career tracks steer the jobs and courses you see, keeping everything relevant to your goals.',
    icon: 'CT'
  },
  {
    title: 'Learning gap nudges',
    copy: 'Resources highlight the skills you have not logged yet so you know where to focus your next sprint.',
    icon: 'LG'
  }
]

const matchStats = [
  { label: 'Skill overlap', value: '75%', fill: '75%' },
  { label: 'Track alignment', value: '100%', fill: '100%' },
  { label: 'Experience fit', value: '50%', fill: '50%' },
  { label: 'Learning boosts suggested', value: '3 resources', fill: '60%' }
]

const roadmapMilestones = [
  {
    stage: '01',
    tag: 'AI Matching',
    title: 'Vector similarity & CV parsing',
    summary: 'Use embeddings to map CV snippets and profile text to job descriptions with higher precision.',
    points: [
      'Generate vector representations for skills, roles, and resources',
      'Parse uploaded CV text to auto-suggest missing skills',
      'Explain AI matches alongside existing rule-based scores'
    ]
  },
  {
    stage: '02',
    tag: 'Insights',
    title: 'Growth analytics for SDG 8 reporting',
    summary: 'Track youth employment indicators and surface dashboards for mentors and NGOs.',
    points: [
      'Capture application outcomes and interview milestones',
      'Visualise job placement velocity and skill adoption trends',
      'Export SDG-aligned metrics for programme partners'
    ]
  },
  {
    stage: '03',
    tag: 'Mentor Loop',
    title: 'Guided feedback & action plans',
    summary: 'Enable mentors to review matches, leave feedback, and assign learning sprints.',
    points: [
      'Mentor view of mentee profile strength and gaps',
      'Suggested learning playlists generated by AI prompts',
      'Notifications for new matches and plan updates'
    ]
  }
]

const testimonials = [
  {
    quote: 'CareerIn helped me translate my campus projects into skills employers recognise. I landed three internship interviews in a week.',
    name: 'Amina Yusuf',
    role: 'Final-year CS student',
    type: 'Student'
  },
  {
    quote: 'The dashboard shows my mentees exactly which skills to improve next. It keeps our shared goals tangible and trackable.',
    name: 'David Mensah',
    role: 'Career mentor',
    type: 'Mentor'
  },
  {
    quote: 'As a bootcamp graduate, I loved seeing “Matches: HTML, CSS” beneath each role. It gave me confidence to apply.',
    name: 'Priya Nair',
    role: 'Junior UI Designer',
    type: 'Graduate'
  },
  {
    quote: 'Matching skills to jobs plus suggested courses made building my learning sprint effortless. I know exactly what to study next.',
    name: 'Luis Ortega',
    role: 'Aspiring Data Analyst',
    type: 'Job Seeker'
  }
]
</script>
