import type { FetchOptions } from 'ofetch'
import { useRuntimeConfig, useRouter } from '#imports'
import { useAuthStore } from '~/stores/auth'

export type ApiFetchOptions = FetchOptions & { suppressAuthError?: boolean }

export const useApi = () => {
  const config = useRuntimeConfig()
  const auth = useAuthStore()
  const router = useRouter()

  return async function apiFetch<T = any>(path: string, options: ApiFetchOptions = {}) {
    const suppressAuthError = options.suppressAuthError ?? false
    
    // Extract and remove custom properties
    const { suppressAuthError: _, ...fetchOptions } = options
    
    // Build headers object
    const headers: Record<string, string> = {}
    
    // Copy existing headers if any
    if (options.headers) {
      if (options.headers instanceof Headers) {
        options.headers.forEach((value, key) => {
          headers[key] = value
        })
      } else if (typeof options.headers === 'object') {
        Object.assign(headers, options.headers)
      }
    }
    
    // Set Content-Type for JSON if body is an object (not FormData or URLSearchParams)
    if (fetchOptions.body && 
        typeof fetchOptions.body === 'object' && 
        !(fetchOptions.body instanceof FormData) && 
        !(fetchOptions.body instanceof URLSearchParams) &&
        !headers['Content-Type'] && 
        !headers['content-type']) {
      headers['Content-Type'] = 'application/json'
    }
    
    // Add auth token if available
    if (auth.token) {
      headers['Authorization'] = `${auth.tokenType ?? 'Bearer'} ${auth.token}`
    }

    console.log(`API Request: ${options.method || 'GET'} ${path}`, {
      headers,
      body: fetchOptions.body
    })

    try {
      const response = await $fetch<T>(`${config.public.apiBase}${path}`, {
        ...fetchOptions,
        headers,
        onResponseError: ({ response }: any) => {
          console.error(`API Response Error: ${response.status}`, response._data)
          if (response.status === 401 && !suppressAuthError) {
            auth.logout()
            if (router.currentRoute.value.path !== '/login') {
              router.push('/login')
            }
          }
        }
      } as any)
      
      console.log(`API Response: ${options.method || 'GET'} ${path}`, response)
      return response
    } catch (error) {
      console.error(`API Error: ${options.method || 'GET'} ${path}`, error)
      throw error
    }
  }
}
