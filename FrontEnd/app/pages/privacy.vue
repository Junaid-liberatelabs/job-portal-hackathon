<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto max-w-4xl px-6 lg:px-10">
      <div class="space-y-8 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_40px_120px_-60px_rgba(15,23,42,0.25)] backdrop-blur">
        <div class="space-y-3">
          <p class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/60 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-700">
            Legal
          </p>
          <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Privacy Policy</h1>
          <p class="text-sm text-ink-500">Last updated: {{ lastUpdated }}</p>
        </div>

        <div class="prose prose-ink max-w-none space-y-6">
          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">1. Information We Collect</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We collect information that you provide directly to us when creating an account, including your name, email address, 
              education level, preferred career track, and skills. We also collect information about your usage of the platform, 
              such as jobs viewed, resources accessed, and profile updates.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">2. How We Use Your Information</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We use the information we collect to:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>Provide personalized job recommendations based on your skills and preferences</li>
              <li>Suggest relevant learning resources to help you develop your career</li>
              <li>Improve our matching algorithms and platform features</li>
              <li>Communicate with you about your account and platform updates</li>
              <li>Ensure the security and integrity of our platform</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">3. Information Sharing</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We do not sell your personal information. We may share your information with:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>Potential employers when you explicitly apply for a job through our platform</li>
              <li>Service providers who help us operate our platform (with appropriate safeguards)</li>
              <li>Law enforcement when required by law or to protect our users' safety</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">4. Data Security</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We implement industry-standard security measures to protect your personal information. This includes encryption 
              of sensitive data, secure authentication, and regular security audits. However, no method of transmission over 
              the Internet is 100% secure, and we cannot guarantee absolute security.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">5. Your Rights</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              You have the right to:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>Access and update your personal information through your profile settings</li>
              <li>Delete your account and associated data at any time</li>
              <li>Export your data in a machine-readable format</li>
              <li>Opt out of non-essential communications</li>
              <li>Request clarification about how your data is used</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">6. Cookies and Tracking</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We use cookies and similar technologies to enhance your experience on our platform. These help us remember 
              your preferences, understand how you use our platform, and improve our services. You can control cookie 
              settings through your browser.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">7. Children's Privacy</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              Our platform is designed for youth starting their careers, including students. For users under 18, we implement 
              additional privacy protections and recommend parental involvement. We do not knowingly collect information from 
              children under 13 without verifiable parental consent.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">8. Changes to This Policy</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We may update this Privacy Policy from time to time. We will notify you of any significant changes by email 
              or through a prominent notice on our platform. Your continued use of the platform after such changes constitutes 
              acceptance of the updated policy.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">9. Contact Us</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              If you have questions about this Privacy Policy or how we handle your information, please contact us through 
              our <NuxtLink to="/#contact" class="font-semibold text-brand-600 transition hover:text-brand-500">contact page</NuxtLink> 
              or email us at privacy@careerconnect.com.
            </p>
          </section>
        </div>

        <div class="flex flex-wrap gap-3 border-t border-ink-100 pt-6">
          <NuxtLink
            to="/"
            class="inline-flex items-center gap-2 rounded-full border border-ink-200/70 px-5 py-3 text-sm font-semibold text-ink-600 transition hover:border-brand-200 hover:text-ink-900"
          >
            ← Back to home
          </NuxtLink>
          <NuxtLink
            to="/terms"
            class="inline-flex items-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800"
          >
            View Terms of Service →
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

definePageMeta({
  layout: 'default'
})

const lastUpdated = computed(() => {
  return new Date().toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
})
</script>

