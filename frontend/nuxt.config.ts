export default defineNuxtConfig({
    devtools: { enabled: true },
    modules: ['@pinia/nuxt', '@nuxt/ui'],
    icon: {
        localApiEndpoint: '/_nuxt_icon',
        serverBundle: {
            collections: ['heroicons'],
        },
    },
    runtimeConfig: {
        public: {
            apiBase: process.env.NUXT_PUBLIC_API_BASE || '/api/v1',
        },
    },
    routeRules: {
        '/api/**': {
            proxy: `${process.env.BACKEND_URL || 'http://localhost:8000'}/api/**`,
        },
    },
})
