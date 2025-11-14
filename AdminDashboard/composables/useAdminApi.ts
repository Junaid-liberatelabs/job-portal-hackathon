import type { FetchOptions } from 'ofetch'

export const useAdminApi = () => {
  const config = useRuntimeConfig()

  return async function adminApiFetch<T = any>(path: string, options: FetchOptions = {}) {
    const headers: Record<string, string> = {}
    
    if (options.headers) {
      if (options.headers instanceof Headers) {
        options.headers.forEach((value, key) => {
          headers[key] = value
        })
      } else if (typeof options.headers === 'object') {
        Object.assign(headers, options.headers)
      }
    }
    
    if (options.body && 
        typeof options.body === 'object' && 
        !(options.body instanceof FormData) && 
        !(options.body instanceof URLSearchParams) &&
        !headers['Content-Type'] && 
        !headers['content-type']) {
      headers['Content-Type'] = 'application/json'
    }

    console.log(`Admin API Request: ${options.method || 'GET'} ${path}`, {
      headers,
      body: options.body
    })

    try {
      const response = await $fetch<T>(`${config.public.apiBase}${path}`, {
        ...options,
        headers,
        onResponseError: ({ response }: any) => {
          console.error(`Admin API Response Error: ${response.status}`, response._data)
        }
      } as any)
      
      console.log(`Admin API Response: ${options.method || 'GET'} ${path}`, response)
      return response
    } catch (error: any) {
      console.error(`Admin API Error: ${options.method || 'GET'} ${path}`, error)
      // Extract FastAPI validation error details
      if (error.data?.detail) {
        if (Array.isArray(error.data.detail)) {
          // Multiple validation errors
          const errorMessages = error.data.detail.map((err: any) => 
            `${err.loc?.join('.')}: ${err.msg}`
          ).join(', ')
          error.message = errorMessages
        } else if (typeof error.data.detail === 'string') {
          error.message = error.data.detail
        }
      }
      throw error
    }
  }
}

