export default defineNuxtPlugin((nuxtApp) => {
    const url = useRuntimeConfig().public.backend_url
    const backend = $fetch.create({
        baseURL: url,
    })

    // Expose to useNuxtApp().$backend
    return {
        provide: {
            backend
        }
    }
})