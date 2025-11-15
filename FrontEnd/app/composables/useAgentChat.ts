interface AgentInitResponse {
  thread_id: string
}

interface AgentChatMessageRequest {
  user_message: string
  thread_id: string
}

interface AgentChatMessageResponse {
  response: string
}

interface ConversationMessage {
  content: string
  type: string
}

interface ConversationResponse {
  thread_id: string
  messages: ConversationMessage[]
}

export const useAgentChat = () => {
  const api = useApi()
  const loading = ref(false)
  const error = ref<string | null>(null)

  const initChat = async () => {
    loading.value = true
    error.value = null
    try {
      const data = await api<AgentInitResponse>('/agent-chat/agent-chat/init', {
        method: 'POST'
      })
      return data.thread_id
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to initialize chat'
      throw err
    } finally {
      loading.value = false
    }
  }

  const sendMessage = async (message: string, threadId: string) => {
    if (!threadId) {
      throw new Error('Thread ID is required')
    }
    
    loading.value = true
    error.value = null
    try {
      const data = await api<AgentChatMessageResponse>('/agent-chat/agent-chat/message', {
        method: 'POST',
        body: {
          user_message: message,
          thread_id: threadId
        } as AgentChatMessageRequest
      })
      return data.response
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to send message'
      throw err
    } finally {
      loading.value = false
    }
  }

  const getAllConversations = async (): Promise<string[]> => {
    loading.value = true
    error.value = null
    try {
      const data = await api<string[]>('/agent-chat/agent-chat/conversation', {
        method: 'POST'
      })
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch conversations'
      throw err
    } finally {
      loading.value = false
    }
  }

  const getConversationHistory = async (threadId: string): Promise<ConversationResponse> => {
    if (!threadId) {
      throw new Error('Thread ID is required')
    }
    
    loading.value = true
    error.value = null
    try {
      const data = await api<ConversationResponse>(`/agent-chat/agent-chat/conversation/${threadId}`, {
        method: 'GET'
      })
      return data
    } catch (err: any) {
      error.value = err?.response?._data?.detail ?? 'Failed to fetch conversation history'
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    loading,
    error,
    initChat,
    sendMessage,
    getAllConversations,
    getConversationHistory
  }
}

