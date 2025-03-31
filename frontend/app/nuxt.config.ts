import Aura from '@primeuix/themes/aura';
import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  css: ['~/assets/css/main.css'],
  modules: [
    '@primevue/nuxt-module'
  ],
  primevue: {
    directives: {
      include: ['Tooltip']
    },
    options: {
      theme: {
        preset: Aura
      }
    }
  }
})
