<template>
  <div class="mx-auto flex min-h-[calc(100vh-160px)] max-w-5xl flex-col justify-center px-6 py-16 lg:px-10">
    <div class="space-y-6 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_40px_120px_-60px_rgba(15,23,42,0.25)] backdrop-blur">
      <div class="space-y-3">
        <p class="inline-flex items-center gap-2 rounded-full border border-emerald-200/80 bg-emerald-50/70 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-emerald-600">
          Join the cohort
        </p>
        <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Create your CareerIn account</h1>
        <p class="text-sm text-ink-500">
          Log your skills, unlock transparent job matches, and map your next learning sprint.
        </p>
      </div>

      <form class="grid gap-5 md:grid-cols-2" @submit.prevent="handleSubmit">
        <div class="md:col-span-2 space-y-2">
          <label for="full_name" class="text-sm font-medium text-ink-600">Full name</label>
          <input
            id="full_name"
            v-model="form.full_name"
            type="text"
            required
            autocomplete="name"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="Alex Doe"
          />
        </div>

        <div class="space-y-2">
          <label for="email" class="text-sm font-medium text-ink-600">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            required
            autocomplete="email"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="you@example.com"
          />
        </div>

        <div class="space-y-2">
          <label for="password" class="text-sm font-medium text-ink-600">Password</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            minlength="8"
            required
            autocomplete="new-password"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="At least 8 characters"
          />
        </div>

        <div class="space-y-2">
          <label for="education_level" class="text-sm font-medium text-ink-600">Education level</label>
          <input
            id="education_level"
            v-model="form.education_level"
            type="text"
            required
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="e.g., BSc Computer Science"
          />
        </div>

        <div class="space-y-2">
          <label for="experience_level" class="text-sm font-medium text-ink-600">Experience level</label>
          <select
            id="experience_level"
            v-model="form.experience_level"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
          >
            <option value="student">Student</option>
            <option value="entry">Entry</option>
            <option value="junior">Junior</option>
          </select>
        </div>

        <div class="space-y-2 md:col-span-2">
          <label for="track" class="text-sm font-medium text-ink-600">Preferred career track</label>
          <select
            id="track"
            v-model="form.preferred_career_track"
            required
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
          >
            <option disabled value="">Select a track</option>
            <option v-for="track in tracks" :key="track" :value="track">{{ track }}</option>
          </select>
        </div>

        <div class="space-y-2 md:col-span-2">
          <label for="skills" class="text-sm font-medium text-ink-600">Key skills (comma separated)</label>
          <input
            id="skills"
            v-model="skillsInput"
            type="text"
            class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
            placeholder="JavaScript, Communication, Figma"
          />
        </div>

        <p v-if="auth.error" class="md:col-span-2 rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-600">
          {{ auth.error }}
        </p>

        <button
          type="submit"
          :disabled="auth.loading"
          class="md:col-span-2 inline-flex w-full items-center justify-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800 disabled:cursor-not-allowed disabled:opacity-60"
        >
          <span v-if="auth.loading" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
          <span>{{ auth.loading ? 'Creating account...' : 'Create account' }}</span>
        </button>
      </form>

      <p class="text-sm text-ink-500">
        Already have an account?
        <NuxtLink to="/login" class="font-semibold text-brand-600 transition hover:text-brand-500">Sign in</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter, useRoute, definePageMeta } from '#imports'
import { useAuthStore, type ExperienceLevel, type RegisterPayload } from '~/stores/auth'

definePageMeta({
  middleware: 'guest'
})

const tracks = ['Web Development', 'Data & Analytics', 'Design', 'Marketing', 'Product', 'Cybersecurity']
const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const form = reactive({
  full_name: '',
  email: '',
  password: '',
  education_level: '',
  preferred_career_track: '',
  experience_level: 'student' as ExperienceLevel
})

const skillsInput = ref('')

const handleSubmit = async () => {
  const skills = skillsInput.value
    .split(',')
    .map((skill) => skill.trim())
    .filter((skill) => Boolean(skill))

  const payload: RegisterPayload = {
    full_name: form.full_name,
    email: form.email,
    password: form.password,
    education_level: form.education_level,
    preferred_career_track: form.preferred_career_track,
    skills: skills.length ? skills : undefined
  }

  const success = await auth.register(payload)
  if (success) {
    if (form.experience_level) {
      await auth.updateProfile({ experience_level: form.experience_level })
    }
    const redirect = typeof route.query.redirect === 'string' ? route.query.redirect : '/dashboard'
    await router.push(redirect)
  }
}
</script>
