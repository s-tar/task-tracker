<script setup lang="ts">
defineEmits<{ 'new-task': [] }>()
</script>

<template>
  <div class="flex items-center justify-between mb-8">
    <h1 class="text-3xl font-bold">Task Tracker</h1>
    <UButton icon="i-heroicons-plus" @click="$emit('new-task')">New Task</UButton>
  </div>
</template>
