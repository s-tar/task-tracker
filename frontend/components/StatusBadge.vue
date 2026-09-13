<script setup lang="ts">
import type {Status} from '~/types'

defineProps<{
  status: Status | null | undefined
}>()

const statusColorMap: Record<string, string> = {
  TODO: 'warning',
  IN_PROGRESS: 'secondary',
  DONE: 'primary',
}
</script>

<template>
  <UBadge :color="statusColorMap[status?.code ?? '']" variant="subtle" class="whitespace-nowrap">
    {{ status?.name ?? '—' }}
  </UBadge>
</template>
