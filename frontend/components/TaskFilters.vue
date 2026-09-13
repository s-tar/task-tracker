<script setup lang="ts">
const tasksStore = useTasksStore()
const {filterStatusId, filterPriorityId, filterSearch} = storeToRefs(tasksStore)
const {statusOptions} = storeToRefs(useStatusesStore())
const {priorityOptions} = storeToRefs(usePrioritiesStore())

const hasFilters = computed(() => filterStatusId.value !== null || filterPriorityId.value !== null || filterSearch.value !== null)

function onStatusChange(val: number | null) {
  tasksStore.setFilters(val, filterPriorityId.value)
}

function onPriorityChange(val: number | null) {
  tasksStore.setFilters(filterStatusId.value, val)
}

let searchTimer: ReturnType<typeof setTimeout> | null = null

function onSearchChange(val: string) {
  if (searchTimer) clearTimeout(searchTimer)
  searchTimer = setTimeout(() => {
    tasksStore.setFilters(filterStatusId.value, filterPriorityId.value, val || null)
  }, 1000)
}
</script>

<template>
  <div class="flex flex-wrap items-center gap-3">
    <span class="text-sm font-medium text-gray-500 dark:text-gray-400">Filter:</span>
    <UInput
        :model-value="filterSearch ?? ''"
        placeholder="Search by title"
        class="w-48"
        icon="i-heroicons-magnifying-glass"
        @update:model-value="onSearchChange"
    />
    <USelect
        :model-value="filterStatusId"
        :items="statusOptions"
        value-key="value"
        placeholder="By Status"
        class="w-44"
        @update:model-value="onStatusChange"
    />
    <USelect
        :model-value="filterPriorityId"
        :items="priorityOptions"
        value-key="value"
        placeholder="By Priority"
        class="w-44"
        @update:model-value="onPriorityChange"
    />
    <UButton
        v-if="hasFilters"
        variant="subtle"
        color="neutral"
        icon="i-heroicons-x-mark"
        @click="tasksStore.setFilters(null, null, null)"
    >
      Clear
    </UButton>
  </div>
</template>
