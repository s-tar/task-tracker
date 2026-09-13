<script setup lang="ts">
import type { Task, TaskCreatePayload, SelectOption } from '~/types'

const props = defineProps<{
  modelValue: boolean
  task?: Task | null
  priorityOptions: SelectOption[]
  statusOptions: SelectOption[]
}>()

const emit = defineEmits<{
  'update:modelValue': [boolean]
  save: [data: TaskCreatePayload]
}>()

const form = reactive<TaskCreatePayload>({
  title: '',
  description: null,
  deadline: null,
  status_id: null,
  priority_id: null,
})

watch(() => props.modelValue, (open) => {
  if (!open) return
  if (props.task) {
    form.title = props.task.title
    form.description = props.task.description
    form.deadline = props.task.deadline
    form.status_id = props.task.status_id
    form.priority_id = props.task.priority_id
  } else {
    form.title = ''
    form.description = null
    form.deadline = null
    form.status_id = props.statusOptions[0]?.value ?? null
    form.priority_id = props.priorityOptions[0]?.value ?? null
  }
})

const isEdit = computed(() => !!props.task)

function close() {
  emit('update:modelValue', false)
}

function handleSave() {
  emit('save', { ...form })
}
</script>

<template>
  <UModal :model-value="modelValue" @update:model-value="close">
    <UCard>
      <template #header>
        <h2 class="text-lg font-semibold">{{ isEdit ? 'Edit Task' : 'New Task' }}</h2>
      </template>

      <div class="space-y-4">
        <UFormGroup label="Title" required>
          <UInput v-model="form.title" placeholder="Task title"/>
        </UFormGroup>
        <UFormGroup label="Description">
          <UTextarea v-model="form.description" placeholder="Optional description"/>
        </UFormGroup>
        <UFormGroup label="Deadline">
          <UInput v-model="form.deadline" type="date"/>
        </UFormGroup>
        <div class="grid grid-cols-2 gap-4">
          <UFormGroup label="Priority">
            <USelect v-model="form.priority_id" :options="priorityOptions"/>
          </UFormGroup>
          <UFormGroup label="Status">
            <USelect v-model="form.status_id" :options="statusOptions"/>
          </UFormGroup>
        </div>
      </div>

      <template #footer>
        <div class="flex justify-end gap-2">
          <UButton variant="ghost" @click="close">Cancel</UButton>
          <UButton :disabled="!form.title" @click="handleSave">
            {{ isEdit ? 'Save' : 'Create' }}
          </UButton>
        </div>
      </template>
    </UCard>
  </UModal>
</template>
