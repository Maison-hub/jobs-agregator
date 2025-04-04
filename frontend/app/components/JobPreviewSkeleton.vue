<script setup lang="ts">

import Skeleton from 'primevue/skeleton';




</script>


<template>
  <div class="bg-surface-900 border border-surface-700 rounded-xl transition-all duration-300  hover:-translate-y-0.5 shadow-primary-400/20 shadow-none hover:shadow-xl cursor-pointer">
    <div class="p-4 flex flex-row items-center justify-between">
      <Skeleton width="18rem" height="2rem"></Skeleton>
      <Skeleton size="2.5rem"></Skeleton>
    </div>
    <div class="px-4">
      <div>
      <!--tree line of skeleton text style -->
        <Skeleton class="mb-2" borderRadius="16px"></Skeleton>
        <Skeleton class="mb-2" borderRadius="16px"></Skeleton>
        <Skeleton class="mb-2" borderRadius="16px"></Skeleton>
        <Skeleton class="mb-2" borderRadius="16px"></Skeleton>
      </div>
    </div>
    <div>
      <div class="p-4 flex flex-row items-center justify-between">
        <Skeleton width="8rem" height="1.5rem"></Skeleton>
        <span class="flex flex-row items-center gap-2">
          <Skeleton size="2rem"></Skeleton>
          <Skeleton size="2rem"></Skeleton>
        </span>
      </div>
    </div>

  </div>
</template>