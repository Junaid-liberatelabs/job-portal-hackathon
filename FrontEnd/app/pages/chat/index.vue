<template>
  <div class="flex h-[calc(100vh-4rem)] bg-ink-50">
    <!-- Sidebar -->
    <div class="w-64 bg-white border-r border-ink-200 flex flex-col">
      <!-- New Chat Button -->
      <div class="p-4 border-b border-ink-200">
        <button
          @click="createNewThread"
          :disabled="creatingThread"
          class="w-full flex items-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 text-white font-semibold text-sm hover:from-brand-600 hover:to-brand-700 transition-all shadow-md hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          {{ creatingThread ? 'Creating...' : 'New Chat' }}
        </button>
      </div>

      <!-- Threads List -->
      <div class="flex-1 overflow-y-auto p-2">
        <div v-if="loadingThreads" class="text-center py-8 px-4">
          <div class="h-5 w-5 animate-spin rounded-full border-2 border-brand-500 border-t-transparent mx-auto"></div>
          <p class="text-xs text-ink-500 mt-3">Loading conversations...</p>
        </div>
        <div v-else-if="threads.length === 0" class="text-center py-8 px-4">
          <svg class="h-12 w-12 text-ink-300 mx-auto mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
          </svg>
          <p class="text-sm text-ink-500">No chats yet</p>
          <p class="text-xs text-ink-400 mt-1">Start a new conversation</p>
        </div>

        <div v-else class="space-y-1">
          <button
            v-for="thread in threads"
            :key="thread.id"
            @click="selectThread(thread.id)"
            :disabled="loadingHistory && activeThreadId === thread.id"
            :class="[
              'w-full text-left px-3 py-2.5 rounded-lg transition-all group',
              activeThreadId === thread.id
                ? 'bg-brand-50 text-brand-700 border border-brand-200'
                : 'text-ink-700 hover:bg-ink-50',
              loadingHistory && activeThreadId === thread.id ? 'opacity-50 cursor-wait' : ''
            ]"
          >
            <div class="flex items-center justify-between gap-2">
              <div class="flex items-center gap-2 min-w-0 flex-1">
                <svg class="h-4 w-4 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
                <span class="text-sm font-medium truncate">{{ thread.title || 'New Chat' }}</span>
              </div>
              <button
                v-if="threads.length > 1"
                @click.stop="deleteThread(thread.id)"
                class="opacity-0 group-hover:opacity-100 p-1 rounded hover:bg-red-50 text-red-500 transition-all"
                aria-label="Delete thread"
              >
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </div>
            <p v-if="thread.lastMessage" class="text-xs text-ink-500 mt-1 truncate">
              {{ thread.lastMessage }}
            </p>
            <p class="text-xs text-ink-400 mt-0.5">
              {{ formatDate(thread.updatedAt) }}
            </p>
          </button>
        </div>
      </div>
    </div>

    <!-- Main Chat Area -->
    <div class="flex-1 flex flex-col bg-white">
      <!-- Chat Header -->
      <div class="border-b border-ink-200 px-6 py-4 bg-white">
        <div class="flex items-center gap-3">
          <div class="h-10 w-10 flex items-center justify-center">
            <img src="/images/oppy.svg" alt="Oppy" class="h-8 w-8" />
          </div>
          <div>
            <h2 class="font-semibold text-ink-900">Oppy</h2>
            <p class="text-xs text-ink-500">Your AI career assistant</p>
          </div>
        </div>
      </div>

      <!-- Messages Container -->
      <div ref="messagesContainer" class="flex-1 overflow-y-auto p-6 bg-ink-50/30 relative">
        <div v-if="loadingHistory && activeThreadId" class="flex items-center justify-center h-full">
          <div class="text-center space-y-4">
            <div class="h-8 w-8 animate-spin rounded-full border-2 border-brand-500 border-t-transparent mx-auto"></div>
            <p class="text-sm text-ink-500">Loading conversation...</p>
          </div>
        </div>
        <div v-else-if="!activeThreadId" class="flex items-center justify-center h-full">
          <div class="text-center space-y-4 max-w-md">
            <div class="mx-auto h-20 w-20 flex items-center justify-center">
              <img src="/images/oppy.svg" alt="Oppy" class="h-16 w-16" />
            </div>
            <h3 class="text-xl font-semibold text-ink-900">Welcome to Oppy</h3>
            <p class="text-sm text-ink-600">Start a new conversation to get career guidance, job search tips, and personalized advice.</p>
            <button
              @click="createNewThread"
              class="mt-4 inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 text-white font-semibold hover:from-brand-600 hover:to-brand-700 transition-all shadow-md hover:shadow-lg"
            >
              <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
              Start New Chat
            </button>
          </div>
        </div>

        <div v-else class="space-y-6 max-w-4xl mx-auto">
          <!-- Messages -->
          <div
            v-for="(message, index) in activeMessages"
            :key="index"
            :class="[
              'flex gap-4',
              message.type === 'user' ? 'justify-end' : 'justify-start'
            ]"
          >
            <div
              v-if="message.type === 'bot'"
              class="h-8 w-8 flex items-center justify-center flex-shrink-0"
            >
              <img src="/images/oppy.svg" alt="Oppy" class="h-6 w-6" />
            </div>
            <div
              :class="[
                'max-w-[85%] rounded-2xl px-5 py-4',
                message.type === 'user'
                  ? 'bg-gradient-to-r from-brand-500 to-brand-600 text-white'
                  : 'bg-white text-ink-900 border border-ink-200 shadow-sm'
              ]"
            >
              <p class="text-sm leading-relaxed whitespace-pre-wrap">{{ message.content }}</p>
            </div>
            <div
              v-if="message.type === 'user'"
              class="h-8 w-8 rounded-full bg-ink-100 flex items-center justify-center flex-shrink-0 border border-ink-200"
            >
              <svg class="h-5 w-5 text-ink-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
          </div>

          <!-- Typing Indicator -->
          <div v-if="isTyping" class="flex justify-start gap-4">
            <div class="h-8 w-8 flex items-center justify-center flex-shrink-0">
              <img src="/images/oppy.svg" alt="Oppy" class="h-6 w-6" />
            </div>
            <div class="bg-white border border-ink-200 rounded-2xl px-5 py-4 shadow-sm">
              <div class="flex gap-1.5">
                <span class="h-2 w-2 bg-ink-400 rounded-full animate-bounce" style="animation-delay: 0ms"></span>
                <span class="h-2 w-2 bg-ink-400 rounded-full animate-bounce" style="animation-delay: 150ms"></span>
                <span class="h-2 w-2 bg-ink-400 rounded-full animate-bounce" style="animation-delay: 300ms"></span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Input Area - Center when no messages, bottom when messages exist -->
      <div 
        v-if="activeThreadId" 
        :class="[
          'bg-white transition-all duration-500 ease-in-out',
          hasMessages 
            ? 'border-t border-ink-200 p-4' 
            : 'absolute inset-x-0 top-1/2 -translate-y-1/2 p-6 z-10'
        ]"
      >
        <form @submit.prevent="handleSendMessage" class="max-w-4xl mx-auto">
          <div class="flex gap-3">
            <div class="flex-1 relative">
              <textarea
                v-model="inputMessage"
                @keydown.enter.exact.prevent="handleSendMessage"
                @keydown.enter.shift.exact="inputMessage += '\n'"
                rows="1"
                placeholder="Message Oppy..."
                :disabled="isTyping || chatLoading"
                class="w-full rounded-xl border border-ink-200 bg-ink-50 px-4 py-3 text-sm text-ink-900 placeholder:text-ink-400 focus:border-brand-400 focus:outline-none focus:ring-2 focus:ring-brand-200 disabled:opacity-50 disabled:cursor-not-allowed resize-none max-h-32 overflow-y-auto"
                style="min-height: 48px;"
                @input="autoResize"
              ></textarea>
            </div>
            <button
              type="submit"
              :disabled="!inputMessage.trim() || isTyping || chatLoading"
              class="rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 text-white px-6 py-3 hover:from-brand-600 hover:to-brand-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-md hover:shadow-lg flex items-center justify-center"
            >
              <svg v-if="!chatLoading" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
              <span v-else class="h-5 w-5 animate-spin rounded-full border-2 border-white/80 border-t-transparent block"></span>
            </button>
          </div>
          <p v-if="!hasMessages" class="text-xs text-ink-400 mt-3 text-center">Press Enter to send, Shift+Enter for new line</p>
          <p v-else class="text-xs text-ink-400 mt-2 text-center">Press Enter to send, Shift+Enter for new line</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, nextTick, onMounted } from 'vue'
import { useAgentChat } from '~/composables/useAgentChat'
import { useAuthStore } from '~/stores/auth'

definePageMeta({
  middleware: 'auth'
})

interface Message {
  type: 'user' | 'bot'
  content: string
  timestamp: Date
  isStreaming?: boolean
}

interface Thread {
  id: string
  title: string | null
  messages: Message[]
  lastMessage: string | null
  updatedAt: Date
  createdAt: Date
}

const auth = useAuthStore()
const { initChat, sendMessage: sendChatMessage, loading: chatLoading, getAllConversations, getConversationHistory } = useAgentChat()

const threads = ref<Thread[]>([])
const activeThreadId = ref<string | null>(null)
const inputMessage = ref('')
const isTyping = ref(false)
const messagesContainer = ref<HTMLElement | null>(null)
const creatingThread = ref(false)
const loadingThreads = ref(false)
const loadingHistory = ref(false)


const activeMessages = computed(() => {
  if (!activeThreadId.value) return []
  const thread = threads.value.find(t => t.id === activeThreadId.value)
  return thread?.messages || []
})

const hasMessages = computed(() => {
  return activeMessages.value.length > 0
})

const createNewThread = async () => {
  creatingThread.value = true
  try {
    const threadId = await initChat()
    const newThread: Thread = {
      id: threadId,
      title: null,
      messages: [],
      lastMessage: null,
      updatedAt: new Date(),
      createdAt: new Date()
    }
    // Add to beginning of list
    threads.value.unshift(newThread)
    activeThreadId.value = threadId
    inputMessage.value = ''
    
    // Focus on input after creating thread
    await nextTick()
    const textarea = document.querySelector('textarea') as HTMLTextAreaElement
    if (textarea) {
      textarea.focus()
    }
  } catch (error) {
    console.error('Failed to create thread:', error)
  } finally {
    creatingThread.value = false
  }
}

const selectThread = async (threadId: string) => {
  if (activeThreadId.value === threadId) return
  
  activeThreadId.value = threadId
  inputMessage.value = ''
  
  // Check if thread already has messages loaded
  const thread = threads.value.find(t => t.id === threadId)
  if (thread && thread.messages.length > 0) {
    await nextTick()
    scrollToBottom()
    return
  }
  
  // Load conversation history from backend
  await loadConversationHistory(threadId)
}

const loadConversationHistory = async (threadId: string) => {
  const thread = threads.value.find(t => t.id === threadId)
  if (!thread) return
  
  loadingHistory.value = true
  try {
    const history = await getConversationHistory(threadId)
    
    // Convert API messages to UI format
    thread.messages = history.messages.map(msg => ({
      type: msg.type === 'assistant' ? 'bot' : 'user',
      content: msg.content,
      timestamp: new Date()
    }))
    
    // Update thread title and last message from history
    if (thread.messages.length > 0) {
      const firstUserMessage = thread.messages.find(m => m.type === 'user')
      if (firstUserMessage && !thread.title) {
        thread.title = firstUserMessage.content.length > 30 
          ? firstUserMessage.content.substring(0, 30) + '...' 
          : firstUserMessage.content
      }
      
      const lastMessage = thread.messages[thread.messages.length - 1]
      if (lastMessage) {
        thread.lastMessage = lastMessage.content.length > 50 
          ? lastMessage.content.substring(0, 50) + '...' 
          : lastMessage.content
      }
      
      thread.updatedAt = new Date()
    }
    
    await nextTick()
    scrollToBottom()
  } catch (error) {
    console.error('Failed to load conversation history:', error)
  } finally {
    loadingHistory.value = false
  }
}

const loadAllThreads = async () => {
  loadingThreads.value = true
  try {
    const threadIds = await getAllConversations()
    
    // Create thread objects for each thread_id
    const loadedThreads: Thread[] = threadIds.map(threadId => ({
      id: threadId,
      title: null,
      messages: [],
      lastMessage: null,
      updatedAt: new Date(),
      createdAt: new Date()
    }))
    
    threads.value = loadedThreads
    
    // Load history for the first thread if available
    if (threads.value.length > 0 && !activeThreadId.value && threads.value[0]) {
      activeThreadId.value = threads.value[0].id
      await loadConversationHistory(threads.value[0].id)
    }
  } catch (error) {
    console.error('Failed to load threads:', error)
  } finally {
    loadingThreads.value = false
  }
}

const deleteThread = (threadId: string) => {
  const index = threads.value.findIndex(t => t.id === threadId)
  if (index !== -1) {
    threads.value.splice(index, 1)
    if (activeThreadId.value === threadId) {
      activeThreadId.value = threads.value.length > 0 && threads.value[0] ? threads.value[0].id : null
    }
  }
}

const handleSendMessage = async () => {
  const message = inputMessage.value.trim()
  if (!message || isTyping.value || !activeThreadId.value) return

  const thread = threads.value.find(t => t.id === activeThreadId.value)
  if (!thread) return

  // Add user message
  const userMessage: Message = {
    type: 'user',
    content: message,
    timestamp: new Date()
  }
  thread.messages.push(userMessage)
  thread.lastMessage = message.length > 50 ? message.substring(0, 50) + '...' : message
  thread.updatedAt = new Date()

  // Generate title from first message if not set
  if (!thread.title && thread.messages.length === 1) {
    thread.title = message.length > 30 ? message.substring(0, 30) + '...' : message
  }

  inputMessage.value = ''
  isTyping.value = true

  // Scroll to bottom
  await nextTick()
  scrollToBottom()

  try {
    const response = await sendChatMessage(message, activeThreadId.value)
    
    // Hide typing indicator
    isTyping.value = false
    
    // Add bot message placeholder for streaming
    const botMessage: Message = {
      type: 'bot',
      content: '',
      timestamp: new Date(),
      isStreaming: true
    }
    thread.messages.push(botMessage)
    
    // Get the message index for direct updates
    const messageIndex = thread.messages.length - 1
    
    // Scroll to show the new message
    await nextTick()
    scrollToBottom()
    
    // Stream the response character by character
    await streamResponse(response, thread.messages, messageIndex)
    
    thread.lastMessage = response.length > 50 ? response.substring(0, 50) + '...' : response
    thread.updatedAt = new Date()
  } catch (error: any) {
    thread.messages.push({
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

const streamResponse = async (fullText: string, messages: Message[], messageIndex: number) => {
  if (!fullText || messageIndex < 0 || !messages[messageIndex]) return
  
  let currentText = ''
  const chars = Array.from(fullText)
  
  // Process characters one by one with delays
  for (let i = 0; i < chars.length; i++) {
    const char = chars[i]
    if (char === undefined) continue
    
    currentText += char
    
    // Update message directly in array to ensure reactivity
    if (messages[messageIndex]) {
      messages[messageIndex].content = currentText
    }
    
    // Realistic typing speed: 15-30ms per character
    // Faster for spaces and punctuation, normal for letters
    const isSpaceOrPunct = /[\s.,!?;:]/.test(char)
    const delay = isSpaceOrPunct ? 3 : 8
    
    // Wait before processing next character
    await new Promise(resolve => setTimeout(resolve, delay))
    
    // Force Vue reactivity update after delay
    await nextTick()
    
    // Scroll to bottom periodically
    if (i % 3 === 0 || i === chars.length - 1) {
      scrollToBottom()
    }
  }
  
  // Final scroll and mark streaming as complete
  if (messages[messageIndex]) {
    messages[messageIndex].isStreaming = false
  }
  await nextTick()
  scrollToBottom()
}

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatDate = (date: Date) => {
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const minutes = Math.floor(diff / 60000)
  const hours = Math.floor(diff / 3600000)
  const days = Math.floor(diff / 86400000)

  if (minutes < 1) return 'Just now'
  if (minutes < 60) return `${minutes}m ago`
  if (hours < 24) return `${hours}h ago`
  if (days < 7) return `${days}d ago`
  return date.toLocaleDateString()
}

const autoResize = (event: Event) => {
  const textarea = event.target as HTMLTextAreaElement
  textarea.style.height = 'auto'
  textarea.style.height = `${Math.min(textarea.scrollHeight, 128)}px`
}

// Watch for new messages to auto-scroll
watch(activeMessages, () => {
  nextTick(() => {
    scrollToBottom()
  })
}, { deep: true })

onMounted(async () => {
  // Load all existing threads from backend
  await loadAllThreads()
  
  // If no threads exist, don't auto-create one - let user click "New Chat"
})
</script>

<style scoped>
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

.input-slide-enter-active,
.input-slide-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.input-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.input-slide-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
</style>

