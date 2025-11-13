import type { FetchOptions } from 'ofetch'
import { useRuntimeConfig, useRouter } from '#imports'
import { useAuthStore } from '~/stores/auth'

export type ApiFetchOptions<T> = FetchOptions<T> & { suppressAuthError?: boolean }

export const useApi = () => {
  const config = useRuntimeConfig()
  const auth = useAuthStore()
  const router = useRouter()

  return async function apiFetch<T>(path: string, options: ApiFetchOptions<T> = {}) {
    const headers = new Headers(options.headers as HeadersInit | undefined)

    if (auth.token) {
      headers.set('Authorization', `${auth.tokenType ?? 'Bearer'} ${auth.token}`)
    }

    const suppressAuthError = options.suppressAuthError ?? false

    try {
      return await $fetch<T>(`${config.public.apiBase}${path}`, {
        ...options,
        headers,
        onResponseError: ({ response }) => {
          if (response.status === 401 && !suppressAuthError) {
            auth.logout()
            if (router.currentRoute.value.path !== '/login') {
              router.push('/login')
            }
          }
        }
      })
    } catch (error) {
      throw error
    }
  }
}
