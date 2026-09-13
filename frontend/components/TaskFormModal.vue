<script setup lang="ts">
import type {Task, TaskCreatePayload, SelectOption} from '~/types'

const props = defineProps<{
  modelValue: boolean
  task?: Task | null
  priorityOptions: SelectOption[]
  statusOptions: SelectOption[]
  fieldErrors?: Record<string, string>
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
  emit('save', {...form})
}
</script>

<template>
  <UModal :open="modelValue" @update:open="close">
    <template #content>
      <UCard>
        <template #header>
          <h2 class="text-lg font-semibold">{{ isEdit ? 'Edit Task' : 'New Task' }}</h2>
        </template>

        <div class="space-y-4">
          <UFormField label="Title" required :error="fieldErrors?.title">
            <UInput v-model="form.title" placeholder="Task title" class="w-full"/>
          </UFormField>
          <UFormField label="Description" :error="fieldErrors?.description">
            <UTextarea v-model="form.description" placeholder="Optional description" class="w-full"/>
          </UFormField>
          <UFormField label="Deadline" :error="fieldErrors?.deadline">
            <UInput v-model="form.deadline" type="date"/>
          </UFormField>
          <div class="grid grid-cols-2 gap-4">
            <UFormField label="Priority" :error="fieldErrors?.priority_id">
              <USelect v-model="form.priority_id" :items="priorityOptions" value-key="value" class="w-full"/>
            </UFormField>
            <UFormField label="Status" :error="fieldErrors?.status_id">
              <USelect v-model="form.status_id" :items="statusOptions" value-key="value" class="w-full"/>
            </UFormField>
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
    </template>
  </UModal>
</template>
