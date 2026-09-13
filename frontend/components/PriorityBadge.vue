<script setup lang="ts">
import type {Priority} from '~/types'

defineProps<{
  priority: Priority | null | undefined
}>()

const priorityColorMap: Record<string, string> = {
  LOW: 'primary',
  MEDIUM: 'warning',
  HIGH: 'error',
  URGENT: 'error',
}
</script>

<template>
  <UBadge :color="priorityColorMap[priority?.code ?? '']" variant="subtle" class="whitespace-nowrap">
    {{ priority?.name ?? '—' }}
  </UBadge>
</template>
