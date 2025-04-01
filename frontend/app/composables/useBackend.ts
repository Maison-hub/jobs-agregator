
export function useBackend<T>(
    url: string,
    options?: RequestInit,
) {

  const config = useRuntimeConfig()
  const apiBase = config.public.backend_url

  //create $fetch with base url and api token
  const api = $fetch.create({
    baseURL: apiBase,
    onRequest({ request, options: fetchOptions, error }) {
      // // Merge provided options with default options
      Object.assign(fetchOptions, options);
    },
    async onResponseError({ response }) {
      if (response.status === 401) {
        navigateTo('/login')
      }
    }
  });
  return api(url)
}