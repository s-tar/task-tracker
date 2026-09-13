<script setup lang="ts">
const tasksStore = useTasksStore()
const { filterStatusId, filterPriorityId } = storeToRefs(tasksStore)
const { statusOptions } = storeToRefs(useStatusesStore())
const { priorityOptions } = storeToRefs(usePrioritiesStore())

const hasFilters = computed(() => filterStatusId.value !== null || filterPriorityId.value !== null)

function onStatusChange(val: number | null) {
  tasksStore.setFilters(val, filterPriorityId.value)
}

function onPriorityChange(val: number | null) {
  tasksStore.setFilters(filterStatusId.value, val)
}
</script>

<template>
  <div class="flex flex-wrap items-center gap-3 mb-6">
    <span class="text-sm font-medium text-gray-500 dark:text-gray-400">Filter:</span>
    <USelect
      :model-value="filterStatusId"
      :options="statusOptions"
      placeholder="By Status"
      class="w-44"
      @update:model-value="onStatusChange"
    />
    <USelect
      :model-value="filterPriorityId"
      :options="priorityOptions"
      placeholder="By Priority"
      class="w-44"
      @update:model-value="onPriorityChange"
    />
    <UButton
      v-if="hasFilters"
      variant="ghost"
      color="gray"
      icon="i-heroicons-x-mark"
      @click="tasksStore.setFilters(null, null)"
    >
      Clear
    </UButton>
  </div>
</template>
