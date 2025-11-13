<template>
  <div class="relative bg-ink-50 py-16">
    <div class="mx-auto max-w-4xl px-6 lg:px-10">
      <div class="space-y-8 rounded-[32px] border border-white/70 bg-white/80 p-10 shadow-[0_40px_120px_-60px_rgba(15,23,42,0.25)] backdrop-blur">
        <div class="space-y-3">
          <p class="inline-flex items-center gap-2 rounded-full border border-brand-200/70 bg-brand-50/60 px-3 py-1 text-xs font-semibold uppercase tracking-[0.35em] text-brand-700">
            Legal
          </p>
          <h1 class="font-display text-3xl font-semibold text-ink-900 sm:text-4xl">Terms of Service</h1>
          <p class="text-sm text-ink-500">Last updated: {{ lastUpdated }}</p>
        </div>

        <div class="prose prose-ink max-w-none space-y-6">
          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">1. Acceptance of Terms</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              By accessing or using CareerConnect ("the Platform"), you agree to be bound by these Terms of Service. 
              If you do not agree to these terms, please do not use the Platform. We reserve the right to update these 
              terms at any time, and your continued use constitutes acceptance of any changes.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">2. Eligibility</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              You must be at least 13 years old to use this Platform. If you are under 18, we recommend using this 
              Platform with parental or guardian supervision. By creating an account, you represent that you meet these 
              age requirements and that all information you provide is accurate and truthful.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">3. User Accounts</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              You are responsible for:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>Maintaining the confidentiality of your account credentials</li>
              <li>All activities that occur under your account</li>
              <li>Providing accurate and up-to-date profile information</li>
              <li>Notifying us immediately of any unauthorized access to your account</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">4. Acceptable Use</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              You agree NOT to:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>Provide false or misleading information about your skills, education, or experience</li>
              <li>Use the Platform for any unlawful purpose or in violation of any regulations</li>
              <li>Harass, threaten, or impersonate other users</li>
              <li>Attempt to gain unauthorized access to our systems or other users' accounts</li>
              <li>Scrape, data mine, or use automated tools without permission</li>
              <li>Upload viruses, malware, or any harmful code</li>
              <li>Interfere with the proper functioning of the Platform</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">5. Job Applications and Opportunities</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              The Platform provides job recommendations and facilitates connections with potential employers. However:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>We do not guarantee job placement or employment</li>
              <li>We are not responsible for the accuracy of job postings</li>
              <li>Employment decisions are made solely by employers</li>
              <li>You are responsible for your own job search and application materials</li>
              <li>We do not endorse any particular employer or opportunity</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">6. Learning Resources</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We provide recommendations for learning resources, courses, and educational content. However:
            </p>
            <ul class="list-disc space-y-2 pl-6 text-sm text-ink-600">
              <li>Resources are suggested for informational purposes only</li>
              <li>We do not guarantee the quality or effectiveness of third-party content</li>
              <li>You are responsible for evaluating resources before use</li>
              <li>Some resources may require separate payment or registration</li>
            </ul>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">7. Intellectual Property</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              The Platform and its content (excluding user-generated content) are owned by CareerConnect and protected 
              by copyright, trademark, and other intellectual property laws. You may not copy, modify, distribute, or 
              create derivative works without our express permission.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">8. User Content</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              You retain ownership of the content you submit (profile information, skills, etc.). However, by using 
              the Platform, you grant us a license to use this content to provide and improve our services, including 
              showing your profile to potential employers and generating recommendations.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">9. Termination</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              We reserve the right to suspend or terminate your account at any time for violations of these Terms or 
              for any other reason at our discretion. You may also delete your account at any time through your profile 
              settings. Upon termination, your right to use the Platform immediately ceases.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">10. Disclaimers</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              THE PLATFORM IS PROVIDED "AS IS" WITHOUT WARRANTIES OF ANY KIND. WE DO NOT GUARANTEE THAT THE PLATFORM 
              WILL BE UNINTERRUPTED, ERROR-FREE, OR SECURE. WE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING 
              WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">11. Limitation of Liability</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              TO THE MAXIMUM EXTENT PERMITTED BY LAW, WE SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, 
              CONSEQUENTIAL, OR PUNITIVE DAMAGES, OR ANY LOSS OF PROFITS OR REVENUES, WHETHER INCURRED DIRECTLY OR 
              INDIRECTLY, OR ANY LOSS OF DATA, USE, OR OTHER INTANGIBLE LOSSES.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">12. Governing Law</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              These Terms shall be governed by and construed in accordance with applicable laws, without regard to 
              conflict of law principles. Any disputes shall be resolved through binding arbitration.
            </p>
          </section>

          <section class="space-y-3">
            <h2 class="text-xl font-semibold text-ink-900">13. Contact Information</h2>
            <p class="text-sm leading-relaxed text-ink-600">
              If you have questions about these Terms of Service, please contact us through our 
              <NuxtLink to="/#contact" class="font-semibold text-brand-600 transition hover:text-brand-500">contact page</NuxtLink> 
              or email us at legal@careerconnect.com.
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
            to="/privacy"
            class="inline-flex items-center gap-2 rounded-full bg-ink-900 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-ink-900/25 transition hover:bg-ink-800"
          >
            View Privacy Policy →
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

