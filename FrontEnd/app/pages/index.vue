<template>
  <div class="relative overflow-hidden bg-ink-50">
    <ExperienceNav :sections="navSections" :offset="navOffset" />

    <ThreeDHero
      :stats="heroStats"
      description="Help youth turn skills into first roles with transparent matches, curated learning, and mentor-ready insights."
      :primary-cta="{ label: 'Book a walkthrough', to: '/#contact' }"
      :secondary-cta="{ label: 'Explore platform', to: '/#features' }"
      :scene-colors="{ a: '#1d4ed8', b: '#38bdf8' }"
      :scene-density="0.9"
    >
      <template #headline>
        Launch youth careers with transparent matches<br class="hidden sm:block" />
        and <span class="bg-gradient-to-r from-sky-500 via-emerald-400 to-teal-300 bg-clip-text text-transparent">actionable learning paths</span>.
      </template>
    </ThreeDHero>

    <section id="features" class="relative border-t border-white/40 bg-white py-24 lg:py-28">
      <div class="pointer-events-none absolute inset-0 -z-10 opacity-60">
        <HeroScene color-a="#1d4ed8" color-b="#38bdf8" :density="0.45" />
      </div>
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/50 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
          <div v-scroll-reveal="{ direction: 'up', distance: 32, duration: 720 }">
            <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500">Platform chapters</span>
            <h2 class="section-heading mt-3">
              Shape every chapter of the youth career journey<br class="hidden lg:block" />
              with <span class="bg-gradient-to-r from-sky-500 via-emerald-400 to-teal-300 bg-clip-text text-transparent">clear, guided steps</span>.
            </h2>
          </div>
          <p class="section-subheading" v-scroll-reveal="{ direction: 'up', distance: 24, duration: 720, delay: 160 }">
            Capture skills, surface opportunities, and plan learning sprints—without losing the human support that matters most.
          </p>
        </div>

        <div class="mt-16 grid gap-10 lg:grid-cols-2">
          <article
            v-for="(feature, index) in platformFeatures"
            :key="feature.title"
            class="landing-card tilt-layer group p-8"
            :class="feature.gradient"
            :ref="(el) => registerFeatureCard(el, index)"
          >
            <div class="landing-card__halo"></div>
            <div class="pointer-events-none absolute inset-0 opacity-60 mix-blend-screen">
              <div class="absolute inset-0 bg-gradient-to-br from-white/25 via-white/10 to-transparent"></div>
            </div>
            <div class="relative flex flex-col gap-8 text-ink-900">
              <header class="space-y-4">
                <span class="chip chip--frosted">
                  {{ feature.badge }}
                </span>
                <div>
                  <h3 class="font-display text-2xl font-semibold">{{ feature.title }}</h3>
                  <p class="mt-3 text-sm text-ink-600">{{ feature.summary }}</p>
                </div>
              </header>

              <ul class="grid gap-4 text-sm text-ink-600">
                <li v-for="point in feature.highlights" :key="point" class="flex items-start gap-3">
                  <span class="mt-1 h-2 w-2 flex-shrink-0 rounded-full bg-brand-400 shadow-[0_0_6px_rgba(59,130,246,0.4)]"></span>
                  <span>{{ point }}</span>
                </li>
              </ul>

              <div class="flex items-center justify-between rounded-2xl bg-white/70 p-4 text-ink-700 ring-1 ring-white/40 backdrop-blur">
                <div>
                  <p class="text-xs uppercase tracking-[0.25em] text-ink-400">{{ feature.metric.label }}</p>
                  <p class="text-xl font-semibold text-ink-900">{{ feature.metric.value }}</p>
                </div>
                <NuxtLink :to="feature.cta.to" class="inline-flex items-center gap-2 text-sm font-semibold text-brand-700 transition hover:text-brand-500">
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
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 32, duration: 720 }">
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
            v-scroll-reveal="{ direction: 'up', distance: 40, duration: 920, delay: index * 140 }"
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
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 36, duration: 720 }">
          <span class="text-xs font-semibold uppercase tracking-[0.4em] text-brand-200/90">How it works</span>
          <h2 class="font-display text-3xl font-semibold sm:text-4xl">From first intake to measurable outcomes</h2>
          <p class="text-sm text-white/70">
            Orchestrate every interaction—from the first story patients share to the insights leadership reviews—without losing clinical empathy.
          </p>
        </div>

        <div class="mt-14 grid gap-10 md:mt-16 md:gap-12">
          <div
            v-for="(step, index) in processJourney"
            :key="step.title"
            class="landing-card landing-card--ink grid gap-6 p-6 text-left md:grid-cols-[auto_1fr] md:items-center md:gap-10 lg:p-8"
            v-scroll-reveal="{ direction: 'up', distance: 48, duration: 960, delay: index * 160 }"
          >
            <div class="flex items-center gap-4">
              <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-500/20 text-lg font-semibold text-brand-100 shadow-[0_20px_60px_-30px_rgba(59,130,246,0.75)]">
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
            <span class="text-xs font-semibold uppercase tracking-[0.35em] text-brand-500" v-scroll-reveal="{ direction: 'up', distance: 24, duration: 720 }">Matching</span>
            <h2 class="section-heading" v-scroll-reveal="{ direction: 'up', distance: 24, duration: 760, delay: 120 }">Explainable recommendations for every youth</h2>
            <p class="section-subheading" v-scroll-reveal="{ direction: 'up', distance: 16, duration: 760, delay: 220 }">
              Students, mentors, and employers see exactly why a role or resource was surfaced—so decisions stay transparent and confidence stays high.
            </p>

            <div class="grid gap-6 sm:grid-cols-2">
              <div
                v-for="(highlight, index) in matchingHighlights"
                :key="highlight.title"
                class="landing-card landing-card--brand border-transparent p-5"
                v-scroll-reveal="{ direction: 'up', distance: 40, duration: 940, delay: index * 160 }"
              >
                <h3 class="font-display text-lg font-semibold text-ink-900">{{ highlight.title }}</h3>
                <p class="mt-2 text-sm text-ink-600">{{ highlight.copy }}</p>
              </div>
            </div>
          </div>

          <div class="landing-card landing-card--glass relative overflow-hidden border-ink-100/30 bg-gradient-to-br from-white to-ink-50 p-8" v-scroll-reveal="{ direction: 'up', distance: 36, duration: 980, delay: 220 }">
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
      <div class="pointer-events-none absolute inset-0 -z-10 opacity-35">
        <HeroScene color-a="#1e3a8a" color-b="#38bdf8" :density="0.28" />
      </div>
      <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-200/50 to-transparent"></div>
      <div class="mx-auto max-w-7xl px-6 lg:px-10">
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 32, duration: 720 }">
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
            class="landing-card landing-card--glass p-6"
            v-scroll-reveal="{ direction: 'up', distance: 44, duration: 920, delay: index * 150 }"
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
        <div class="max-w-2xl space-y-4" v-scroll-reveal="{ direction: 'up', distance: 32, duration: 720 }">
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
            class="landing-card landing-card--glass p-8 transition hover:-translate-y-1"
            v-scroll-reveal="{ direction: 'up', distance: 48, duration: 940, delay: index * 170 }"
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

      <div class="relative mx-auto max-w-5xl rounded-[36px] border border-white/10 bg-gradient-to-br from-white/10 via-white/5 to-transparent p-10 shadow-[0_45px_140px_-80px_rgba(56,189,248,0.6)] backdrop-blur" v-scroll-reveal="{ distance: 0, duration: 960 }">
        <div class="flex flex-col items-start gap-8 lg:flex-row lg:items-center lg:justify-between">
          <div class="max-w-xl space-y-4">
            <span class="inline-flex items-center gap-2 rounded-full border border-white/20 px-3 py-1 text-xs uppercase tracking-[0.35em] text-white/80">
                <span class="h-1.5 w-1.5 rounded-full bg-emerald-300"></span>
                Let’s reinvent clinical storytelling
            </span>
            <h2 class="font-display text-3xl font-semibold sm:text-4xl">
                Launch your youth talent program in weeks
            </h2>
            <p class="text-sm text-white/70">
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
import { onBeforeUnmount, type ComponentPublicInstance } from 'vue'
import HeroScene from '~/components/HeroScene.vue'
import { useScrollAnimation } from '~/composables/useScrollAnimation'
import ExperienceNav from '~/components/layout/ExperienceNav.vue'
import ThreeDHero from '~/components/hero/ThreeDHero.vue'

const heroStats = [
  { label: 'Career tracks supported', value: '18' },
  { label: 'Opportunities indexed', value: '2.1k+' },
  { label: 'Learning resources mapped', value: '320+' },
  { label: 'Youth placed to date', value: '4.6k+' }
] 

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

const { createTiltEffect, observeElement } = useScrollAnimation()

const featureRevealCleanup = new Map<HTMLElement, () => void>()
const featureTiltCleanup = new Map<HTMLElement, () => void>()

const registerFeatureCard = (el: Element | ComponentPublicInstance | null, index: number) => {
  if (!import.meta.client) return

  const element = el instanceof HTMLElement ? el : null
  if (!element) return

  featureRevealCleanup.get(element)?.()
  featureTiltCleanup.get(element)?.()

  element.classList.add('sr-base')
  element.style.setProperty('--sr-transform', 'translate3d(0, 48px, 0)')
  element.style.setProperty('--sr-duration', '940ms')
  element.style.setProperty('--sr-delay', `${index * 140}ms`)

  const { stop } = observeElement(element, {
    threshold: 0.28,
    once: true,
    onEnter: () => {
      requestAnimationFrame(() => {
        element.classList.add('sr-visible')
      })
    }
  })

  featureRevealCleanup.set(element, stop)

  const { destroy } = createTiltEffect(element, { maxAngle: 6, perspective: 960 })
  featureTiltCleanup.set(element, destroy)
}

onBeforeUnmount(() => {
  featureRevealCleanup.forEach((stop) => stop())
  featureRevealCleanup.clear()
  featureTiltCleanup.forEach((destroy) => destroy())
  featureTiltCleanup.clear()
})

const navSections = [
  { id: 'features', label: 'Features' },
  { id: 'foundations', label: 'Pillars' },
  { id: 'process', label: 'Journey' },
  { id: 'matching', label: 'Matching' },
  { id: 'roadmap', label: 'Roadmap' },
  { id: 'testimonials', label: 'Proof' },
  { id: 'contact', label: 'Demo' }
] as { id: string; label: string }[]

const navOffset = 96
</script>
