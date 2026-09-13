<script setup lang="ts">
import type {Task} from '~/types'

const props = defineProps<{ task: Task }>()
const emit = defineEmits<{
  edit: [task: Task]
  delete: [id: number]
}>()

const {statuses} = storeToRefs(useStatusesStore())
const {priorities} = storeToRefs(usePrioritiesStore())

const statusColorMap: Record<string, string> = {
  TODO: 'warning',
  IN_PROGRESS: 'secondary',
  DONE: 'primary',
}

const priorityColorMap: Record<string, string> = {
  LOW: 'primary',
  MEDIUM: 'warning',
  HIGH: 'error',
}

const currentStatus = computed(() => statuses.value.find((s) => s.id === props.task.status_id))
const currentPriority = computed(() => priorities.value.find((p) => p.id === props.task.priority_id))

function formatDate(dateStr: string) {
  return new Intl.DateTimeFormat('uk-UA').format(new Date(dateStr))
}

const showDeleteConfirm = ref(false)
const showDetail = ref(false)

function confirmDelete() {
  showDeleteConfirm.value = false
  emit('delete', props.task.id)
}

function handleDetailEdit(task: Task) {
  emit('edit', task)
}

function handleDetailDelete(id: number) {
  showDeleteConfirm.value = true
}
</script>

<template>
  <UCard class="flex flex-col cursor-pointer"
         :ui="{ body: 'flex-1 flex flex-col', footer: 'p-2 sm:px-6 min-h-[50px] flex items-center' }"
         @click="showDetail = true">
    <template #header>
      <div class="flex items-center justify-between grow gap-2">
        <span class="font-semibold truncate">
          <UBadge :color="statusColorMap[currentStatus?.code ?? '']" variant="subtle">
            {{ currentStatus?.name ?? '—' }}
          </UBadge>
          {{ task.title }}
        </span>
        <div class="flex gap-2 shrink-0">
          <UButton
              size="md"
              variant="ghost"
              icon="i-heroicons-pencil-square"
              @click.stop="emit('edit', task)"
              title="Edit"
          />
          <UButton
              size="md"
              variant="ghost"
              icon="i-heroicons-trash"
              color="red"
              @click.stop="showDeleteConfirm = true"
              title="Delete"
          />
        </div>
      </div>
    </template>

    <p v-if="task.description" class="flex-1 text-sm text-gray-600 dark:text-gray-400 whitespace-pre-wrap line-clamp-4">
      {{ task.description }}
    </p>
    <div v-else class="flex-1"/>

    <template #footer>
      <div class="flex items-center justify-between gap-2 grow">
        <div class="flex flex-col gap-0.5 text-xs text-gray-500 dark:text-gray-400 min-w-0">
          <span>Created: {{ formatDate(task.created_at) }}</span>
          <span v-if="task.deadline">Due: {{ formatDate(task.deadline) }}</span>
        </div>
        <UBadge :color="priorityColorMap[currentPriority?.code ?? '']" variant="subtle" class="shrink-0">
          {{ currentPriority?.name ?? '—' }}
        </UBadge>
      </div>
    </template>
  </UCard>

  <TaskDetailModal
      v-model="showDetail"
      :task="task"
      @edit="handleDetailEdit"
      @delete="handleDetailDelete"
  />

  <TaskDeleteModal
      v-model="showDeleteConfirm"
      :task-title="task.title"
      @confirm="confirmDelete"
  />
</template>
