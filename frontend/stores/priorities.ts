import type { Priority, SelectOption } from '~/types'

export const usePrioritiesStore = defineStore('PrioritiesStore', () => {
    const config = useRuntimeConfig()
    const base = config.public.apiBase

    const loading = ref(false)
    const error = ref<string | null>(null)
    const priorities = ref<Priority[]>([])

    async function loadPriorities() {
        if (priorities.value.length) return
        loading.value = true
        error.value = null
        try {
            priorities.value = await $fetch<Priority[]>(`${base}/priorities`)
        } catch (e: unknown) {
            error.value = (e as Error)?.message ?? 'Failed to load priorities'
        } finally {
            loading.value = false
        }
    }

    const priorityOptions = computed<SelectOption[]>(() =>
        priorities.value.map((p) => ({ label: p.name, value: p.id }))
    )

    return { loading, error, priorities, loadPriorities, priorityOptions }
})
