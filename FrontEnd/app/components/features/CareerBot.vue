<template>
  <div class="fixed bottom-6 right-6 z-50">
    <!-- Chat Window -->
    <Transition name="chat-window">
      <div
        v-if="isOpen"
        class="w-[380px] h-[600px] rounded-2xl border border-white/70 bg-white/90 backdrop-blur-lg shadow-2xl flex flex-col overflow-hidden"
        style="box-shadow: 0 20px 60px -15px rgba(35, 111, 195, 0.3);"
      >
        <!-- Header -->
        <div class="bg-gradient-to-r from-brand-500 to-brand-600 px-6 py-4 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="relative">
              <div class="h-10 w-10 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center">
                <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <span
                v-if="isTyping"
                class="absolute -top-1 -right-1 h-3 w-3 bg-emerald-400 rounded-full animate-pulse"
              ></span>
            </div>
            <div>
              <h3 class="text-white font-semibold text-base">CareerBot</h3>
              <p class="text-white/80 text-xs">Your AI career assistant</p>
            </div>
          </div>
          <button
            @click="toggleChat"
            class="text-white/80 hover:text-white transition-colors p-1.5 rounded-lg hover:bg-white/20"
            aria-label="Close chat"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Messages Container -->
        <div ref="messagesContainer" class="flex-1 overflow-y-auto p-4 space-y-4 bg-ink-50/30">
          <div v-if="messages.length === 0" class="flex items-center justify-center h-full">
            <div class="text-center space-y-3">
              <div class="mx-auto h-16 w-16 rounded-full bg-gradient-to-br from-brand-400 to-brand-600 flex items-center justify-center">
                <svg class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <p class="text-ink-600 font-medium">Hi! I'm CareerBot</p>
              <p class="text-sm text-ink-500">Ask me anything about your career journey!</p>
            </div>
          </div>

          <!-- Messages -->
          <div
            v-for="(message, index) in messages"
            :key="index"
            :class="[
              'flex',
              message.type === 'user' ? 'justify-end' : 'justify-start'
            ]"
          >
            <div
              :class="[
                'max-w-[80%] rounded-2xl px-4 py-3',
                message.type === 'user'
                  ? 'bg-gradient-to-r from-brand-500 to-brand-600 text-white'
                  : 'bg-white text-ink-900 border border-ink-200 shadow-sm'
              ]"
            >
              <p class="text-sm leading-relaxed whitespace-pre-wrap">{{ message.content }}</p>
              <p class="text-xs mt-1.5 opacity-70">
                {{ formatTime(message.timestamp) }}
              </p>
            </div>
          </div>

          <!-- Typing Indicator -->
          <div v-if="isTyping" class="flex justify-start">
            <div class="bg-white border border-ink-200 rounded-2xl px-4 py-3 shadow-sm">
              <div class="flex gap-1.5">
                <span class="h-2 w-2 bg-ink-400 rounded-full animate-bounce" style="animation-delay: 0ms"></span>
                <span class="h-2 w-2 bg-ink-400 rounded-full animate-bounce" style="animation-delay: 150ms"></span>
                <span class="h-2 w-2 bg-ink-400 rounded-full animate-bounce" style="animation-delay: 300ms"></span>
              </div>
            </div>
          </div>
        </div>

        <!-- Input Area -->
        <div class="border-t border-ink-200 bg-white p-4">
          <form @submit.prevent="handleSendMessage" class="flex gap-2">
            <input
              v-model="inputMessage"
              type="text"
              placeholder="Type your message..."
              :disabled="isTyping || chatLoading"
              class="flex-1 rounded-xl border border-ink-200 bg-ink-50 px-4 py-2.5 text-sm text-ink-900 placeholder:text-ink-400 focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200 disabled:opacity-50 disabled:cursor-not-allowed"
            />
            <button
              type="submit"
              :disabled="!inputMessage.trim() || isTyping || chatLoading"
              class="rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 text-white px-4 py-2.5 hover:from-brand-600 hover:to-brand-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-md hover:shadow-lg"
            >
              <svg v-if="!chatLoading" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
              <span v-else class="h-5 w-5 animate-spin rounded-full border-2 border-white/80 border-t-transparent block"></span>
            </button>
          </form>
        </div>
      </div>
    </Transition>

    <!-- Floating Button -->
    <Transition name="button-bounce">
      <button
        v-if="!isOpen"
        @click="toggleChat"
        class="h-14 w-14 rounded-full bg-gradient-to-r from-brand-500 to-brand-600 text-white shadow-2xl hover:shadow-brand-500/50 transition-all duration-300 hover:scale-110 flex items-center justify-center relative group"
        aria-label="Open CareerBot"
      >
        <!-- Pulsing Animation -->
        <span class="absolute inset-0 rounded-full bg-brand-500 animate-ping opacity-20"></span>
        
        <!-- Icon -->
        <svg class="h-7 w-7 relative z-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>

        <!-- Notification Badge -->
        <span
          v-if="unreadCount > 0"
          class="absolute -top-1 -right-1 h-5 w-5 rounded-full bg-red-500 text-white text-xs font-bold flex items-center justify-center"
        >
          {{ unreadCount > 9 ? '9+' : unreadCount }}
        </span>
      </button>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick, onMounted } from 'vue'
import { useAgentChat } from '~/composables/useAgentChat'

interface Message {
  type: 'user' | 'bot'
  content: string
  timestamp: Date
}

const auth = useAuthStore()
const { initChat, sendMessage: sendChatMessage, loading: chatLoading } = useAgentChat()

const isOpen = ref(false)
const inputMessage = ref('')
const messages = ref<Message[]>([])
const isTyping = ref(false)
const messagesContainer = ref<HTMLElement | null>(null)
const unreadCount = ref(0)
const threadId = ref<string | null>(null)

const toggleChat = async () => {
  if (!isOpen.value) {
    // Opening chat - initialize if needed
    try {
      if (!threadId.value) {
        threadId.value = await initChat()
      }
    } catch (error) {
      console.error('Failed to initialize chat:', error)
    }
    unreadCount.value = 0
  }
  isOpen.value = !isOpen.value
}

const handleSendMessage = async () => {
  const message = inputMessage.value.trim()
  if (!message || isTyping.value) return

  // Add user message
  messages.value.push({
    type: 'user',
    content: message,
    timestamp: new Date()
  })

  inputMessage.value = ''
  isTyping.value = true

  // Scroll to bottom
  await nextTick()
  scrollToBottom()

  try {
    if (!threadId.value) {
      threadId.value = await initChat()
    }
    const response = await sendChatMessage(message, threadId.value)
    
    // Add bot response
    messages.value.push({
      type: 'bot',
      content: response,
      timestamp: new Date()
    })
  } catch (error: any) {
    messages.value.push({
      type: 'bot',
      content: 'Sorry, I encountered an error. Please try again.',
      timestamp: new Date()
    })
  } finally {
    isTyping.value = false
    await nextTick()
    scrollToBottom()
  }
}

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatTime = (date: Date) => {
  return new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: '2-digit',
    hour12: true
  }).format(date)
}

// Watch for new messages when chat is closed to show notification
watch(messages, (newMessages) => {
  if (!isOpen.value && newMessages.length > 0) {
    const lastMessage = newMessages[newMessages.length - 1]
    if (lastMessage.type === 'bot') {
      unreadCount.value++
    }
  }
}, { deep: true })

onMounted(() => {
  // Initialize chat when component mounts
  // Silent fail - will retry when user opens chat
  initChat().then(id => {
    threadId.value = id
  }).catch(() => {
    // Chat will be initialized when user opens it
  })
})
</script>

<style scoped>
.chat-window-enter-active,
.chat-window-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.chat-window-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

.chat-window-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

.button-bounce-enter-active,
.button-bounce-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.button-bounce-enter-from {
  opacity: 0;
  transform: scale(0.5) rotate(-180deg);
}

.button-bounce-leave-to {
  opacity: 0;
  transform: scale(0.5) rotate(180deg);
}

/* Custom scrollbar */
.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background: #d9deeb;
  border-radius: 3px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background: #bbc2d5;
}
</style>

