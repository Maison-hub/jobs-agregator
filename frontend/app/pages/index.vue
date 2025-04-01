<script setup lang="ts">

const { $backend } = useNuxtApp();
const data = ref(null);
onMounted(async () => {
  data.value = await useAsyncData('modules', () => $backend('/offers')).data
  console.log('DATA : ', data.value.offers);
});

</script>

<template>
  <div class="p-8">
    <div id="result-list" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" v-if="data">
      <div v-for="job in data.offers" :key="job.id">
        <JobPreview
            :title="job.title"
            :description="job.description"
            :location="job.location"
            :company="job.company"
            :link="job.link"
        />
      </div>
    </div>
    <div v-else>
      <div class="rounded border border-surface-200 dark:border-surface-700 p-6 bg-surface-0 dark:bg-surface-900">
        <div class="flex mb-4">
          <Skeleton shape="circle" size="4rem" class="mr-2"></Skeleton>
          <div>
            <Skeleton width="10rem" class="mb-2"></Skeleton>
            <Skeleton width="5rem" class="mb-2"></Skeleton>
            <Skeleton height=".5rem"></Skeleton>
          </div>
        </div>
        <Skeleton width="100%" height="150px"></Skeleton>
        <div class="flex justify-between mt-4">
          <Skeleton width="4rem" height="2rem"></Skeleton>
          <Skeleton width="4rem" height="2rem"></Skeleton>
        </div>
      </div>
    </div>
  </div>
</template>