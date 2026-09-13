<script setup lang="ts">
import type {Task, TaskCreatePayload} from '~/types'
import {useTasksStore} from '~/stores/tasks'
import {usePrioritiesStore} from '~/stores/priorities'
import {useStatusesStore} from '~/stores/statuses'

const route = useRoute()
const router = useRouter()

const tasksStore = useTasksStore()
const prioritiesStore = usePrioritiesStore()
const statusesStore = useStatusesStore()

const {tasks, loading, error, pagination, filterStatusId, filterPriorityId} = storeToRefs(tasksStore)
const {priorityOptions} = storeToRefs(prioritiesStore)
const {statusOptions} = storeToRefs(statusesStore)

const PER_PAGE = 3
const page = computed(() => Number(route.query.page) || 1)

const showModal = ref(false)
const currentTask = ref<Task | null>(null)

watch(showModal, (open) => {
  if (!open) currentTask.value = null
})

function openCreateForm() {
  currentTask.value = null
  showModal.value = true
}

function openEditForm(task: Task) {
  currentTask.value = task
  showModal.value = true
}

async function loadTasksList() {
  await tasksStore.fetchTasks(page.value, PER_PAGE)
}

onMounted(async () => {
  tasksStore.setFilters(
    route.query.status_id ? Number(route.query.status_id) : null,
    route.query.priority_id ? Number(route.query.priority_id) : null,
  )
  await Promise.all([prioritiesStore.loadPriorities(), statusesStore.loadStatuses()])
  await loadTasksList()
})

// Store → URL: push when user changes filters via TaskFilters
watch([filterStatusId, filterPriorityId], ([sId, pId]) => {
  const urlStatus = route.query.status_id ? Number(route.query.status_id) : null
  const urlPriority = route.query.priority_id ? Number(route.query.priority_id) : null
  if (sId === urlStatus && pId === urlPriority) return
  const query: Record<string, string> = {}
  if (sId) query.status_id = String(sId)
  if (pId) query.priority_id = String(pId)
  router.push({query})
})

// URL → store + reload: covers page changes, back/forward, and post-filter-push navigation
watch([page, () => route.query.status_id, () => route.query.priority_id], ([, sId, pId]) => {
  const newStatus = sId ? Number(sId as string) : null
  const newPriority = pId ? Number(pId as string) : null
  if (newStatus !== filterStatusId.value || newPriority !== filterPriorityId.value) {
    tasksStore.setFilters(newStatus, newPriority)
  }
  loadTasksList()
})

async function handleSave(data: TaskCreatePayload) {
  if (currentTask.value) {
    await tasksStore.updateTask(currentTask.value.id, data)
  } else {
    await tasksStore.createTask(data)
    await loadTasksList()
  }
  showModal.value = false
}

async function handleDelete(id: number) {
  await tasksStore.deleteTask(id)
  if (tasks.value.length === 0 && page.value > 1) {
    await router.push({query: {...route.query, page: page.value - 1}})
  } else {
    await loadTasksList()
  }
}
</script>

<template>
  <UContainer class="py-10">
    <Header @new-task="openCreateForm"/>

    <TaskFilters/>

    <TaskList
        :tasks="tasks"
        :loading="loading"
        :error="error"
        @edit="openEditForm"
        @delete="handleDelete"
    />

    <TaskPaginator
        :total="pagination.total"
        :per-page="PER_PAGE"
        :page="page"
    />

    <TaskFormModal
        v-model="showModal"
        :task="currentTask"
        :priority-options="priorityOptions"
        :status-options="statusOptions"
        @save="handleSave"
    />
  </UContainer>
</template>
