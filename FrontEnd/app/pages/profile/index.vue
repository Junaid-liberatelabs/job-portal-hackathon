<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto flex max-w-5xl flex-col gap-10 px-6 lg:px-10">
      <header class="space-y-4">
        <p class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/70 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-600">
          Profile workspace
        </p>
        <div class="space-y-3">
          <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Tell your story with clarity</h1>
          <p class="text-sm text-ink-500">
            Keep your background, skills, and ambitions current so matches stay relevant and mentors can support quickly.
          </p>
        </div>
      </header>

      <section class="space-y-6 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(59,130,246,0.25)] backdrop-blur">
        <form class="grid gap-5 md:grid-cols-2" @submit.prevent="handleUpdate">
          <div class="space-y-2 md:col-span-2">
            <label for="full_name" class="text-sm font-medium text-ink-600">Full name</label>
            <input
              id="full_name"
              v-model="form.full_name"
              type="text"
              required
              class="w-full rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
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
              <option v-for="track in tracks" :key="track" :value="track">{{ track }}</option>
            </select>
          </div>

          <div class="md:col-span-2 flex flex-wrap items-center gap-3">
            <button
              type="submit"
              :disabled="auth.loading"
              class="inline-flex items-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <span v-if="auth.loading" class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
              <span>{{ auth.loading ? 'Saving...' : 'Save changes' }}</span>
            </button>
            <p v-if="statusMessage" class="text-sm text-emerald-600">{{ statusMessage }}</p>
            <p v-if="auth.error" class="text-sm text-red-600">{{ auth.error }}</p>
          </div>
        </form>
      </section>

      <section class="space-y-5 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(16,185,129,0.22)] backdrop-blur">
        <header class="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h2 class="font-display text-2xl font-semibold text-ink-900">Skill library</h2>
            <p class="text-sm text-ink-500">Add skills to improve job matches and resource recommendations.</p>
          </div>
        </header>

        <form class="flex flex-wrap items-center gap-3" @submit.prevent="handleAddSkill">
          <input
            v-model="skillInput"
            type="text"
            placeholder="Add a new skill"
            class="flex-1 rounded-2xl border border-ink-200/70 bg-white px-4 py-3 text-sm text-ink-700 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-200/60"
          />
          <button
            type="submit"
            class="inline-flex items-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800"
          >
            Add skill
          </button>
        </form>

        <div class="flex flex-wrap gap-3 text-xs text-ink-600">
          <div
            v-for="skill in auth.user?.skills || []"
            :key="skill"
            class="inline-flex items-center gap-2 rounded-full bg-ink-900/5 px-4 py-2 font-semibold"
          >
            {{ skill }}
            <button type="button" class="text-ink-400 transition hover:text-red-500" @click="removeSkill(skill)">
              ✕
            </button>
          </div>
          <p v-if="!auth.user?.skills?.length" class="text-sm text-ink-500">No skills added yet. Share your strengths to unlock better matches.</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, watchEffect } from 'vue'
import { definePageMeta } from '#imports'
import { useAuthStore, type ExperienceLevel, type UpdateProfilePayload } from '~/stores/auth'

definePageMeta({
  middleware: 'auth'
})

const tracks = ['Web Development', 'Data & Analytics', 'Design', 'Marketing', 'Product', 'Cybersecurity']
const auth = useAuthStore()

await auth.fetchProfile()

const form = reactive({
  full_name: auth.user?.full_name ?? '',
  education_level: auth.user?.education_level ?? '',
  experience_level: (auth.user?.experience_level || 'student') as ExperienceLevel,
  preferred_career_track: auth.user?.preferred_career_track ?? tracks[0]
})

watchEffect(() => {
  if (!auth.user) return
  form.full_name = auth.user.full_name
  form.education_level = auth.user.education_level
  form.experience_level = (auth.user.experience_level || 'student') as ExperienceLevel
  form.preferred_career_track = auth.user.preferred_career_track
})

const statusMessage = ref('')

const handleUpdate = async () => {
  const payload: UpdateProfilePayload = {
    full_name: form.full_name,
    education_level: form.education_level,
    experience_level: form.experience_level,
    preferred_career_track: form.preferred_career_track
  }

  const result = await auth.updateProfile(payload)
  statusMessage.value = result ? 'Profile updated successfully.' : ''
  if (result) {
    setTimeout(() => {
      statusMessage.value = ''
    }, 4000)
  }
}

const skillInput = ref('')

const handleAddSkill = async () => {
  const value = skillInput.value.trim()
  if (!value) return
  await auth.addSkill(value)
  skillInput.value = ''
}

const removeSkill = async (skill: string) => {
  await auth.removeSkill(skill)
}
</script>
