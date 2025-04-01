export default defineNuxtPlugin((nuxtApp) => {
    const url = useRuntimeConfig().public.backend_url
    const backend = $fetch.create({
        baseURL: url,
        onRequest({ request, options, error }) {
            //Pre request code here
        },
        async onResponseError({ response }) {
            // if (response.status === 401) {
            //     await nuxtApp.runWithContext(() => navigateTo('/login'))
            // }
        }
    })

    // Expose to useNuxtApp().$backend
    return {
        provide: {
            backend
        }
    }
})