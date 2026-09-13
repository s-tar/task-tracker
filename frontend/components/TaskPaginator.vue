<script setup lang="ts">
const props = defineProps<{
  total: number
  perPage: number
  page: number
}>()

const router = useRouter()
const route = useRoute()

const pageCount = computed(() => Math.ceil(props.total / props.perPage))

function onPageChange(newPage: number) {
  router.push({query: {...route.query, page: newPage}})
}
</script>

<template>
  <div v-if="pageCount > 1" class="flex justify-center mt-8">
    <UPagination
        :page="page"
        :items-per-page="perPage"
        :total="total"
        show-edges
        @update:page="onPageChange"
    />
  </div>
</template>
