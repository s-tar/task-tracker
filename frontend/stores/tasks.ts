import type {Pagination, Task, TaskCreatePayload, TaskUpdatePayload} from '~/types'

export const useTasksStore = defineStore('TasksStore', () => {
    const config = useRuntimeConfig()
    const base = config.public.apiBase

    const tasks = ref<Task[]>([])
    const loading = ref(false)
    const error = ref<string | null>(null)
    const pagination = ref<Omit<Pagination<never>, 'items'>>({page: 1, per_page: 12, total: 0})
    const filterStatusId = ref<number | null>(null)
    const filterPriorityId = ref<number | null>(null)
    const filterSearch = ref<string | null>(null)
    const filterOrderBy = ref<string>('deadline')

    function setFilters(statusId: number | null, priorityId: number | null, search: string | null = filterSearch.value) {
        filterStatusId.value = statusId
        filterPriorityId.value = priorityId
        filterSearch.value = search
    }

    function setOrderBy(orderBy: string) {
        filterOrderBy.value = orderBy
    }

    async function fetchTasks(page = 1, perPage = 12) {
        loading.value = true
        error.value = null
        try {
            const query: Record<string, string | number> = {page, per_page: perPage}
            if (filterStatusId.value) query.status_id = filterStatusId.value
            if (filterPriorityId.value) query.priority_id = filterPriorityId.value
            if (filterSearch.value) query.search = filterSearch.value
            query.order_by = filterOrderBy.value
            const res = await $fetch<Pagination<Task>>(`${base}/tasks`, {query})
            tasks.value = res.items
            pagination.value = {page: res.page, per_page: res.per_page, total: res.total}
        } catch (e: unknown) {
            error.value = (e as Error)?.message ?? 'Failed to load tasks'
        } finally {
            loading.value = false
        }
    }

    async function createTask(data: TaskCreatePayload) {
        return await $fetch<Task>(`${base}/tasks`, {
            method: 'POST',
            body: data,
        })
    }

    async function updateTask(id: number, data: TaskUpdatePayload) {
        const task = await $fetch<Task>(`${base}/tasks/${id}`, {
            method: 'PATCH',
            body: data,
        })
        const idx = tasks.value.findIndex((t) => t.id === id)
        if (idx !== -1) tasks.value[idx] = task
        return task
    }

    async function deleteTask(id: number) {
        await $fetch(`${base}/tasks/${id}`, {method: 'DELETE'})
        tasks.value = tasks.value.filter((t) => t.id !== id)
    }

    return {
        tasks,
        loading,
        error,
        pagination,
        filterStatusId,
        filterPriorityId,
        filterSearch,
        filterOrderBy,
        setFilters,
        setOrderBy,
        fetchTasks,
        createTask,
        updateTask,
        deleteTask,
    }
})
