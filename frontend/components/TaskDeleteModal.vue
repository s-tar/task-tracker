<script setup lang="ts">
defineProps<{
  modelValue: boolean
  taskTitle: string
}>()

const emit = defineEmits<{
  'update:modelValue': [boolean]
  confirm: []
}>()
</script>

<template>
  <UModal :model-value="modelValue" @update:model-value="emit('update:modelValue', $event)">
    <UCard>
      <template #header>
        <h2 class="text-lg font-semibold">Delete Task</h2>
      </template>

      <p class="text-sm text-gray-600 dark:text-gray-400">
        Are you sure you want to delete
        <span class="font-medium text-gray-900 dark:text-white">{{ taskTitle }}</span>?
        This action cannot be undone.
      </p>

      <template #footer>
        <div class="flex justify-end gap-2">
          <UButton variant="ghost" @click="emit('update:modelValue', false)">Cancel</UButton>
          <UButton color="red" @click="emit('confirm')">Delete</UButton>
        </div>
      </template>
    </UCard>
  </UModal>
</template>
