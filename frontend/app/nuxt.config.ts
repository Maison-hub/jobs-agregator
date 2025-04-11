import Aura from '@primeuix/themes/aura';
import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  runtimeConfig: {
    public:{
      backend_url: "http://localhost:8000",
    }
  },
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
