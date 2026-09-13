<script setup lang="ts">
import type {Task} from '~/types'

const props = defineProps<{
  modelValue: boolean
  task: Task
}>()

const emit = defineEmits<{
  'update:modelValue': [boolean]
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

function close() {
  emit('update:modelValue', false)
}

function handleEdit() {
  close()
  emit('edit', props.task)
}

function handleDelete() {
  close()
  emit('delete', props.task.id)
}
</script>

<template>
  <UModal :open="modelValue" @update:open="emit('update:modelValue', $event)">
    <template #content>
      <UCard>
        <template #header>
          <div class="flex items-center justify-between gap-3">
            <h2 class="text-lg font-semibold leading-tight grow">{{ task.title }}</h2>
            <div class="flex flex-wrap gap-2 text-xs text-gray-500">
              <UBadge v-if="currentPriority" :color="priorityColorMap[currentPriority.code ?? '']" variant="subtle">
                {{ currentPriority.name }}
              </UBadge>
              <UBadge v-if="currentStatus" :color="statusColorMap[currentStatus.code ?? '']" variant="subtle">
                {{ currentStatus.name }}
              </UBadge>
            </div>
            <UButton
                variant="ghost"
                icon="i-heroicons-x-mark"
                size="sm"
                class="shrink-0"
                @click="close"
            />
          </div>
        </template>

        <div class="flex flex-col gap-4">
          <div class="flex flex-col gap-4">
            <p v-if="task.description" class="text-sm text-gray-600 dark:text-gray-400 whitespace-pre-wrap">
              {{ task.description }}
            </p>
            <p v-else class="text-sm text-gray-400 dark:text-gray-500 italic">No description</p>
          </div>


          <div class="flex flex-col gap-1 text-xs text-gray-500 dark:text-gray-400">
            <span>Created: {{ formatDate(task.created_at) }}</span>
            <span v-if="task.deadline">Due: {{ formatDate(task.deadline) }}</span>
          </div>
        </div>

        <template #footer>
          <div class="flex justify-end gap-2">
            <UButton variant="ghost" icon="i-heroicons-pencil-square" @click="handleEdit">Edit</UButton>
            <UButton color="red" variant="ghost" icon="i-heroicons-trash" @click="handleDelete">Delete</UButton>
          </div>
        </template>
      </UCard>
    </template>
  </UModal>
</template>
