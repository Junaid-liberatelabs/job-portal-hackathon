<template>
  <div class="relative bg-ink-50 min-h-screen py-8">
    <div class="mx-auto flex max-w-7xl flex-col gap-8 px-4 sm:px-6 lg:px-8">
      <!-- Profile Header -->
      <div class="rounded-3xl border border-white/70 bg-white/80 p-8 shadow-lg backdrop-blur">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <div class="flex items-start gap-6">
            <!-- Avatar -->
            <div class="relative">
              <div class="h-24 w-24 rounded-full bg-gradient-to-br from-brand-400 to-brand-600 flex items-center justify-center shadow-lg">
                <span class="text-white font-bold text-3xl">{{ userInitials }}</span>
              </div>
            </div>
            
            <!-- User Info -->
            <div class="space-y-3">
              <div>
                <h1 class="font-display text-3xl font-semibold text-ink-900">Your Profile</h1>
                <p class="text-sm text-ink-500 mt-1">Manage your skills, experience, and career preferences</p>
              </div>
              <div class="flex flex-wrap items-center gap-4 text-sm text-ink-600">
                <div class="flex items-center gap-2">
                  <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                  {{ auth.user?.email }}
                </div>
                <div class="flex items-center gap-2">
                  <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  Member since {{ memberSince }}
                </div>
              </div>
            </div>
          </div>

          <!-- Profile Completion -->
          <div class="flex flex-col items-center gap-3">
            <div class="relative h-24 w-24">
              <svg class="h-24 w-24 transform -rotate-90">
                <circle
                  cx="48"
                  cy="48"
                  r="40"
                  stroke="currentColor"
                  stroke-width="8"
                  fill="none"
                  class="text-ink-100"
                />
                <circle
                  cx="48"
                  cy="48"
                  r="40"
                  stroke="currentColor"
                  stroke-width="8"
                  fill="none"
                  :stroke-dasharray="circumference"
                  :stroke-dashoffset="progressOffset"
                  class="text-brand-500 transition-all duration-500"
                  stroke-linecap="round"
                />
              </svg>
              <div class="absolute inset-0 flex items-center justify-center">
                <span class="text-2xl font-bold text-brand-600">{{ profileCompletion }}%</span>
              </div>
            </div>
            <p class="text-sm font-semibold text-ink-600">Profile Complete</p>
          </div>
        </div>
      </div>

      <!-- Tabs Navigation -->
      <nav class="flex gap-2 rounded-3xl border border-white/70 bg-white/90 p-2 shadow-sm backdrop-blur">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          :class="[
            'flex-1 rounded-2xl px-6 py-3 text-sm font-semibold transition-all duration-200',
            activeTab === tab.id
              ? 'bg-brand-500 text-white shadow-lg shadow-brand-500/30'
              : 'text-ink-600 hover:bg-ink-50 hover:text-ink-900'
          ]"
          @click="activeTab = tab.id"
        >
          {{ tab.label }}
        </button>
      </nav>

      <!-- Personal Information Tab -->
      <section v-show="activeTab === 'personal'" class="space-y-8">
        <div class="grid gap-6 lg:grid-cols-2">
          <!-- Basic Information -->
          <Card variant="glass" class="p-8">
            <h2 class="font-display text-xl font-semibold text-ink-900 mb-6">Basic Information</h2>
            <form class="space-y-5" @submit.prevent="handleUpdateBasic">
              <div class="grid gap-5 sm:grid-cols-2">
                <div class="space-y-2">
                  <label for="first_name" class="text-sm font-medium text-ink-700">First Name</label>
                  <input
                    id="first_name"
                    v-model="form.first_name"
                    type="text"
                    placeholder="John"
                    class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                  />
                </div>
                <div class="space-y-2">
                  <label for="last_name" class="text-sm font-medium text-ink-700">Last Name</label>
                  <input
                    id="last_name"
                    v-model="form.last_name"
                    type="text"
                    placeholder="Doe"
                    class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                  />
                </div>
              </div>

              <div class="space-y-2">
                <label for="email" class="text-sm font-medium text-ink-700">Email Address</label>
                <input
                  id="email"
                  :value="auth.user?.email"
                  type="email"
                  disabled
                  class="w-full rounded-xl border border-ink-200 bg-ink-50 px-4 py-2.5 text-sm text-ink-600 cursor-not-allowed"
                />
              </div>

              <div class="space-y-2">
                <label for="phone" class="text-sm font-medium text-ink-700">Phone Number</label>
                <input
                  id="phone"
                  v-model="form.phone"
                  type="tel"
                  placeholder="+1 (555) 123-4567"
                  class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                />
              </div>

              <div class="space-y-2">
                <label for="location" class="text-sm font-medium text-ink-700">Location</label>
                <input
                  id="location"
                  v-model="form.location"
                  type="text"
                  placeholder="City, State, Country"
                  class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                />
              </div>

              <Button type="submit" :disabled="auth.loading" class="w-full">
                <span v-if="auth.loading" class="flex items-center justify-center gap-2">
                  <span class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
                  Saving...
                </span>
                <span v-else>Save Changes</span>
              </Button>
              <p v-if="statusMessage" class="text-sm text-emerald-600 text-center">{{ statusMessage }}</p>
            </form>
          </Card>

          <!-- Education -->
          <Card variant="glass" class="p-8">
            <h2 class="font-display text-xl font-semibold text-ink-900 mb-6">Education</h2>
            <form class="space-y-5" @submit.prevent="handleUpdateEducation">
              <div class="space-y-2">
                <label for="education_level" class="text-sm font-medium text-ink-700">Highest Education Level</label>
                <select
                  id="education_level"
                  v-model="form.education_level"
                  class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                >
                  <option value="">Select education level</option>
                  <option value="High School">High School</option>
                  <option value="Associate Degree">Associate Degree</option>
                  <option value="Bachelor's Degree">Bachelor's Degree</option>
                  <option value="Master's Degree">Master's Degree</option>
                  <option value="Ph.D.">Ph.D.</option>
                </select>
              </div>

              <div class="space-y-2">
                <label for="field_of_study" class="text-sm font-medium text-ink-700">Field of Study</label>
                <input
                  id="field_of_study"
                  v-model="form.field_of_study"
                  type="text"
                  placeholder="Computer Science, Engineering, etc."
                  class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                />
              </div>

              <div class="space-y-2">
                <label for="university" class="text-sm font-medium text-ink-700">University/Institution</label>
                <input
                  id="university"
                  v-model="form.university"
                  type="text"
                  placeholder="University name"
                  class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                />
              </div>

              <div class="grid gap-5 sm:grid-cols-2">
                <div class="space-y-2">
                  <label for="graduation_year" class="text-sm font-medium text-ink-700">Graduation Year</label>
                  <input
                    id="graduation_year"
                    v-model="form.graduation_year"
                    type="number"
                    placeholder="2023"
                    min="1950"
                    :max="new Date().getFullYear() + 10"
                    class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                  />
                </div>
                <div class="space-y-2">
                  <label for="gpa" class="text-sm font-medium text-ink-700">GPA (Optional)</label>
                  <input
                    id="gpa"
                    v-model="form.gpa"
                    type="text"
                    placeholder="3.5"
                    class="w-full rounded-xl border border-ink-200 bg-white px-4 py-2.5 text-sm text-ink-900 transition focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200"
                  />
                </div>
              </div>

              <Button type="submit" :disabled="auth.loading" class="w-full">
                <span v-if="auth.loading" class="flex items-center justify-center gap-2">
                  <span class="h-4 w-4 animate-spin rounded-full border-2 border-white/80 border-t-transparent"></span>
                  Saving...
                </span>
                <span v-else>Save Education</span>
              </Button>
            </form>
          </Card>
        </div>
      </section>

      <section v-show="activeTab === 'skills'" class="space-y-6 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(16,185,129,0.22)] backdrop-blur">
        <div class="space-y-2">
          <h2 class="font-display text-2xl font-semibold text-ink-900">Skill library</h2>
          <p class="text-sm text-ink-500">Add skills to improve job matches and resource recommendations.</p>
        </div>

        <Card variant="glass" class="p-6">
          <SkillChart
            v-if="auth.user?.skills && auth.user.skills.length > 0"
            :skills="auth.user.skills"
            :chart-type="chartType"
          />
          <div v-else class="py-10 text-center">
            <p class="text-sm text-ink-500">Add skills below to visualize your skill profile</p>
          </div>
          
          <div class="mt-4 flex gap-2">
            <Button
              v-for="type in ['pie', 'radar', 'bar']"
              :key="type"
              :variant="chartType === type ? 'primary' : 'outline'"
              size="sm"
              @click="chartType = type as 'pie' | 'radar' | 'bar'"
            >
              {{ type.charAt(0).toUpperCase() + type.slice(1) }} chart
            </Button>
          </div>
        </Card>

        <div class="space-y-4">
          <h3 class="text-sm font-semibold text-ink-700">Manage skills</h3>
          <form class="flex flex-wrap items-center gap-3" @submit.prevent="handleAddSkill">
            <FormInput
              v-model="skillInput"
              type="text"
              placeholder="Add a new skill (e.g., React, Python, Communication)"
              class="flex-1"
            />
            <Button type="submit">
              Add skill
            </Button>
          </form>

          <div class="flex flex-wrap gap-3">
            <div
              v-for="skill in categorizedSkills"
              :key="skill.name"
              :class="[
                'inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-semibold',
                getCategoryColor(skill.category)
              ]"
            >
              {{ skill.name }}
              <button
                type="button"
                class="transition hover:text-red-600"
                @click="removeSkill(skill.name)"
              >
                ✕
              </button>
            </div>
            <p v-if="!auth.user?.skills?.length" class="w-full text-sm text-ink-500">
              No skills added yet. Share your strengths to unlock better matches.
            </p>
          </div>
        </div>

        <div v-if="suggestedSkills.length > 0" class="space-y-3">
          <h3 class="text-sm font-semibold text-ink-700">Suggested skills based on your track</h3>
          <div class="flex flex-wrap gap-2">
            <button
              v-for="skill in suggestedSkills"
              :key="skill"
              class="rounded-full bg-brand-50 px-4 py-2 text-sm font-semibold text-brand-700 ring-1 ring-brand-200 transition hover:bg-brand-100"
              @click="addSuggestedSkill(skill)"
            >
              + {{ skill }}
            </button>
          </div>
        </div>
      </section>

      <section v-show="activeTab === 'analytics'" class="space-y-6 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_45px_140px_-80px_rgba(168,85,247,0.22)] backdrop-blur">
        <div class="space-y-2">
          <h2 class="font-display text-2xl font-semibold text-ink-900">Your impact</h2>
          <p class="text-sm text-ink-500">Track your progress and engagement metrics</p>
        </div>

        <div class="grid gap-6 md:grid-cols-3">
          <Card variant="glass" class="p-6">
            <div class="space-y-2">
              <p class="text-xs font-semibold uppercase tracking-[0.3em] text-ink-400">Total skills</p>
              <p class="font-display text-4xl font-semibold text-ink-900">{{ auth.user?.skills?.length || 0 }}</p>
              <p class="text-sm text-ink-500">Skills in your profile</p>
            </div>
          </Card>

          <Card variant="glass" class="p-6">
            <div class="space-y-2">
              <p class="text-xs font-semibold uppercase tracking-[0.3em] text-brand-600">Job matches</p>
              <p class="font-display text-4xl font-semibold text-ink-900">{{ jobMatchCount }}</p>
              <p class="text-sm text-ink-500">Roles aligned with you</p>
            </div>
          </Card>

          <Card variant="glass" class="p-6">
            <div class="space-y-2">
              <p class="text-xs font-semibold uppercase tracking-[0.3em] text-emerald-600">Learning resources</p>
              <p class="font-display text-4xl font-semibold text-ink-900">{{ resourceMatchCount }}</p>
              <p class="text-sm text-ink-500">Resources matched to you</p>
            </div>
          </Card>
        </div>

        <Card variant="glass" class="p-6">
          <div class="space-y-4">
            <h3 class="font-display text-lg font-semibold text-ink-900">Skill distribution</h3>
            <div class="space-y-3">
              <div v-for="category in skillCategories" :key="category.name" class="space-y-1">
                <div class="flex items-center justify-between text-sm">
                  <span class="font-semibold text-ink-700">{{ category.name }}</span>
                  <span class="text-ink-500">{{ category.count }} skills</span>
                </div>
                <div class="h-2 w-full rounded-full bg-ink-100">
                  <div
                    :class="['h-full rounded-full', category.color]"
                    :style="{ width: `${category.percentage}%` }"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </Card>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref, watchEffect, computed } from 'vue'
import { definePageMeta, useAsyncData } from '#imports'
import { useAuthStore, type ExperienceLevel, type UpdateProfilePayload } from '~/stores/auth'
import { useApi } from '~/composables/useApi'
import Button from '~/components/ui/Button.vue'
import Card from '~/components/ui/Card.vue'
import FormInput from '~/components/ui/FormInput.vue'
import SkillChart from '~/components/features/SkillChart.vue'

definePageMeta({
  middleware: 'auth'
})

const tabs = [
  { id: 'personal', label: 'Personal Information' },
  { id: 'skills', label: 'Skills & Expertise' },
  { id: 'experience', label: 'Experience' },
  { id: 'career', label: 'Career Preferences' }
]

const tracks = ['Web Development', 'Data & Analytics', 'Design', 'Marketing', 'Product', 'Cybersecurity']
const auth = useAuthStore()
const api = useApi()

await auth.fetchProfile()

const activeTab = ref('personal')
const chartType = ref<'pie' | 'radar' | 'bar'>('pie')

// Parse full name into first and last
const parseFullName = (fullName: string) => {
  const parts = fullName.trim().split(' ')
  return {
    first_name: parts[0] || '',
    last_name: parts.slice(1).join(' ') || ''
  }
}

const nameParts = auth.user?.full_name ? parseFullName(auth.user.full_name) : { first_name: '', last_name: '' }

const form = reactive({
  first_name: nameParts.first_name,
  last_name: nameParts.last_name,
  phone: '',
  location: '',
  education_level: auth.user?.education_level ?? '',
  field_of_study: '',
  university: '',
  graduation_year: null as number | null,
  gpa: '',
  experience_level: (auth.user?.experience_level || 'student') as ExperienceLevel,
  preferred_career_track: auth.user?.preferred_career_track ?? tracks[0]
})

watchEffect(() => {
  if (!auth.user) return
  const nameParts = parseFullName(auth.user.full_name)
  form.first_name = nameParts.first_name
  form.last_name = nameParts.last_name
  form.education_level = auth.user.education_level
  form.experience_level = (auth.user.experience_level || 'student') as ExperienceLevel
  form.preferred_career_track = auth.user.preferred_career_track
})

const userInitials = computed(() => {
  if (!auth.user?.full_name) return '?'
  const names = auth.user.full_name.split(' ')
  return names.map(n => n[0]).join('').toUpperCase().slice(0, 2)
})

const memberSince = computed(() => {
  return new Date().getFullYear()
})

// Profile completion calculation
const profileCompletion = computed(() => {
  if (!auth.user) return 0
  let completed = 0
  const total = 10
  
  if (auth.user.full_name) completed++
  if (auth.user.email) completed++
  if (auth.user.education_level) completed++
  if (auth.user.preferred_career_track) completed++
  if (auth.user.experience_level) completed++
  if (auth.user.skills && auth.user.skills.length > 0) completed++
  if (auth.user.skills && auth.user.skills.length >= 5) completed++
  if (form.phone) completed++
  if (form.location) completed++
  if (form.university) completed++
  
  return Math.round((completed / total) * 100)
})

const circumference = 2 * Math.PI * 40
const progressOffset = computed(() => {
  return circumference - (profileCompletion.value / 100) * circumference
})

const statusMessage = ref('')

const handleUpdateBasic = async () => {
  const full_name = `${form.first_name} ${form.last_name}`.trim()
  const payload: UpdateProfilePayload = {
    full_name,
    education_level: form.education_level,
    experience_level: form.experience_level,
    preferred_career_track: form.preferred_career_track
  }

  const result = await auth.updateProfile(payload)
  statusMessage.value = result ? 'Profile updated successfully.' : ''
  if (result) {
    setTimeout(() => {
      statusMessage.value = ''
    }, 3000)
  }
}

const handleUpdateEducation = async () => {
  const full_name = `${form.first_name} ${form.last_name}`.trim()
  const payload: UpdateProfilePayload = {
    full_name,
    education_level: form.education_level,
    experience_level: form.experience_level,
    preferred_career_track: form.preferred_career_track
  }

  const result = await auth.updateProfile(payload)
  statusMessage.value = result ? 'Education updated successfully.' : ''
  if (result) {
    setTimeout(() => {
      statusMessage.value = ''
    }, 3000)
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

const addSuggestedSkill = async (skill: string) => {
  await auth.addSkill(skill)
}

interface CategorySkill {
  name: string
  category: string
}

const categorizedSkills = computed<CategorySkill[]>(() => {
  const skills = auth.user?.skills || []
  return skills.map(skill => {
    const lower = skill.toLowerCase()
    let category = 'other'
    
    if (['react', 'vue', 'angular', 'javascript', 'typescript', 'python', 'java', 'c++', 'html', 'css'].some(kw => lower.includes(kw))) {
      category = 'programming'
    } else if (['design', 'figma', 'photoshop', 'ui', 'ux', 'sketch'].some(kw => lower.includes(kw))) {
      category = 'design'
    } else if (['communication', 'leadership', 'teamwork', 'management', 'presentation'].some(kw => lower.includes(kw))) {
      category = 'soft-skills'
    } else if (['sql', 'database', 'mongodb', 'postgresql', 'analytics', 'data'].some(kw => lower.includes(kw))) {
      category = 'data'
    }
    
    return { name: skill, category }
  })
})

const getCategoryColor = (category: string) => {
  const colors: Record<string, string> = {
    programming: 'bg-blue-100 text-blue-700 ring-1 ring-blue-200',
    design: 'bg-purple-100 text-purple-700 ring-1 ring-purple-200',
    'soft-skills': 'bg-emerald-100 text-emerald-700 ring-1 ring-emerald-200',
    data: 'bg-amber-100 text-amber-700 ring-1 ring-amber-200',
    other: 'bg-ink-100 text-ink-700 ring-1 ring-ink-200'
  }
  return colors[category] || colors.other
}

const suggestedSkills = computed(() => {
  const track = auth.user?.preferred_career_track?.toLowerCase() || ''
  const existing = new Set((auth.user?.skills || []).map(s => s.toLowerCase()))
  
  const suggestions: Record<string, string[]> = {
    'web development': ['React', 'Node.js', 'TypeScript', 'HTML', 'CSS', 'JavaScript', 'Git'],
    'data & analytics': ['Python', 'SQL', 'Excel', 'Tableau', 'Statistics', 'Machine Learning'],
    'design': ['Figma', 'Adobe XD', 'Photoshop', 'UI/UX', 'Prototyping', 'Visual Design'],
    'marketing': ['SEO', 'Content Marketing', 'Social Media', 'Google Analytics', 'Copywriting'],
    'product': ['Product Strategy', 'User Research', 'Agile', 'Roadmapping', 'Stakeholder Management'],
    'cybersecurity': ['Network Security', 'Penetration Testing', 'Python', 'Linux', 'Security Analysis']
  }
  
  const trackKey = Object.keys(suggestions).find(key => track.includes(key.toLowerCase()))
  const trackSkills = trackKey ? suggestions[trackKey] : []
  
  return trackSkills.filter(skill => !existing.has(skill.toLowerCase())).slice(0, 5)
})

const skillCategories = computed(() => {
  const categories = categorizedSkills.value.reduce((acc, { category }) => {
    acc[category] = (acc[category] || 0) + 1
    return acc
  }, {} as Record<string, number>)
  
  const total = Object.values(categories).reduce((sum, count) => sum + count, 0) || 1
  
  const categoryColors: Record<string, string> = {
    programming: 'bg-blue-500',
    design: 'bg-purple-500',
    'soft-skills': 'bg-emerald-500',
    data: 'bg-amber-500',
    other: 'bg-ink-500'
  }
  
  const categoryLabels: Record<string, string> = {
    programming: 'Programming',
    design: 'Design',
    'soft-skills': 'Soft Skills',
    data: 'Data & Analytics',
    other: 'Other'
  }
  
  return Object.entries(categories)
    .map(([name, count]) => ({
      name: categoryLabels[name] || name,
      count,
      percentage: Math.round((count / total) * 100),
      color: categoryColors[name] || categoryColors.other
    }))
    .sort((a, b) => b.count - a.count)
})

const { data: jobsData } = await useAsyncData('profile-jobs', () =>
  api('/jobs/', { query: { limit: 100 } }),
  { server: false }
)

const { data: resourcesData } = await useAsyncData('profile-resources', () =>
  api('/resources/', { query: { limit: 200 } }),
  { server: false }
)

const jobMatchCount = computed(() => {
  const jobs = jobsData.value || []
  const userSkills = new Set((auth.user?.skills || []).map(s => s.toLowerCase()))
  
  return jobs.filter((job: any) => 
    job.required_skills?.some((skill: string) => userSkills.has(skill.toLowerCase()))
  ).length
})

const resourceMatchCount = computed(() => {
  const resources = resourcesData.value || []
  const userSkills = new Set((auth.user?.skills || []).map(s => s.toLowerCase()))
  
  return resources.filter((resource: any) =>
    resource.tags?.some((tag: string) => userSkills.has(tag.toLowerCase()))
  ).length
})
</script>
