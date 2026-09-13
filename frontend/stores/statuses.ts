import type { Status, SelectOption } from '~/types'

export const useStatusesStore = defineStore('StatusesStore', () => {
    const config = useRuntimeConfig()
    const base = config.public.apiBase

    const loading = ref(false)
    const error = ref<string | null>(null)
    const statuses = ref<Status[]>([])

    async function loadStatuses() {
        if (statuses.value.length) return
        loading.value = true
        error.value = null
        try {
            statuses.value = await $fetch<Status[]>(`${base}/statuses`)
        } catch (e: unknown) {
            error.value = (e as Error)?.message ?? 'Failed to load statuses'
        } finally {
            loading.value = false
        }
    }

    const statusOptions = computed<SelectOption[]>(() =>
        statuses.value.map((s) => ({ label: s.name, value: s.id }))
    )

    return { loading, error, statuses, statusOptions, loadStatuses }
})
