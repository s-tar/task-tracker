<script setup lang="ts">
const tasksStore = useTasksStore()
const {filterOrderBy} = storeToRefs(tasksStore)

const orderOptions = [
    {label: 'Deadline ↓', value: 'deadline_desc'},
    {label: 'Deadline ↑', value: 'deadline'},
    {label: 'Created ↓', value: 'date_created_desc'},
    {label: 'Created ↑', value: 'date_created'},
    {label: 'Title A→Z', value: 'title'},
    {label: 'Title Z→A', value: 'title_desc'},
]
</script>

<template>
    <div class="flex items-center gap-3">
        <span class="text-sm font-medium text-gray-500 dark:text-gray-400">Sort:</span>
        <USelect
            :model-value="filterOrderBy"
            :items="orderOptions"
            value-key="value"
            class="w-44"
            @update:model-value="tasksStore.setOrderBy"
        />
    </div>
</template>
