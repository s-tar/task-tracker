<script setup lang="ts">
import type {Task} from '~/types'

const props = defineProps<{ task: Task }>()
const emit = defineEmits<{
  edit: [task: Task]
  delete: [id: number]
}>()

const { statuses } = storeToRefs(useStatusesStore())
const { priorities } = storeToRefs(usePrioritiesStore())

const statusColorMap: Record<string, string> = {
  TODO: 'gray',
  IN_PROGRESS: 'blue',
  DONE: 'green',
}

const priorityColorMap: Record<string, string> = {
  LOW: 'green',
  MEDIUM: 'yellow',
  HIGH: 'red',
}

const currentStatus = computed(() => statuses.value.find((s) => s.id === props.task.status_id))
const currentPriority = computed(() => priorities.value.find((p) => p.id === props.task.priority_id))

const showDeleteConfirm = ref(false)

function confirmDelete() {
  showDeleteConfirm.value = false
  emit('delete', props.task.id)
}
</script>

<template>
  <UCard class="flex flex-col" :ui="{ body: { base: 'flex-1 flex flex-col' } }">
    <template #header>
      <div class="flex items-center justify-between gap-2">
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
              @click="emit('edit', task)"
              title="Edit"
          />
          <UButton
              size="md"
              variant="ghost"
              icon="i-heroicons-trash"
              color="red"
              @click="showDeleteConfirm = true"
              title="Delete"
          />
        </div>
      </div>
    </template>

    <p v-if="task.description" class="flex-1 text-sm text-gray-600 dark:text-gray-400 whitespace-pre-wrap">
      {{ task.description }}
    </p>
    <div v-else class="flex-1"/>

    <template #footer>
      <div class="flex items-center justify-between gap-2">
        <div class="flex flex-col gap-0.5 text-xs text-gray-500 dark:text-gray-400 min-w-0">
          <span>Created: {{ new Date(task.created_at).toLocaleDateString() }}</span>
          <span v-if="task.deadline">Due: {{ new Date(task.deadline).toLocaleDateString() }}</span>
        </div>
        <UBadge :color="priorityColorMap[currentPriority?.code ?? '']" variant="subtle" class="shrink-0">
          {{ currentPriority?.name ?? '—' }}
        </UBadge>
      </div>
    </template>
  </UCard>

  <TaskDeleteModal
      v-model="showDeleteConfirm"
      :task-title="task.title"
      @confirm="confirmDelete"
  />
</template>
