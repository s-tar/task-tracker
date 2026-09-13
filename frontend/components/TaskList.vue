<script setup lang="ts">
import type {Task} from '~/types'

defineProps<{
  tasks: Task[]
  loading: boolean
  error: string | null
}>()

defineEmits<{
  edit: [task: Task]
  delete: [id: number]
}>()
</script>

<template>
  <div>
    <UAlert v-if="error" color="red" :description="error" class="mb-6"/>

    <div v-if="loading" class="flex justify-center py-20">
      <UIcon name="i-heroicons-arrow-path" class="animate-spin text-4xl"/>
    </div>

    <div v-else-if="tasks.length === 0" class="text-center py-20 text-gray-500">
      Nothing found...
    </div>

    <div v-else class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      <TaskCard
          v-for="task in tasks"
          :key="task.id"
          :task="task"
          @edit="(task) => $emit('edit', task)"
          @delete="(id) => $emit('delete', id)"
      />
    </div>
  </div>
</template>
