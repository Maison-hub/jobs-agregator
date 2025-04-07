<script setup lang="ts">


import Skeleton from "primevue/skeleton";
</script>


<template>
    <div class="joblistbtn cursor-pointer z-10 bg-surface-900 w-full flex items-center justify-center h-52 rounded-xl relative group/jobbtn overflow-hidden before:bg-primary-400 after:bg-primary-400 outline-2 outline-transparent hover:outline-primary-400 outline-offset-0 hover:outline-offset-[6px] transition-all ease-in-bounce duration-300 shadow-primary-400/30 hover:shadow-hover-xl">
        <div class="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 left-0 flex flex-col gap-2 ">
          <div
              v-for="(item, index) in 3"
              :key="index"
              class="bg-surface-900 border rounded-md p-2 w-48"
              :class="index === 1 ? 'border-primary-400 transition-all ease-in-bounce duration-300 group-hover/jobbtn:translate-x-4': 'border-surface-700'"
          >
            <div class="flex flex-row items-center justify-between">
              <div class="h-2 w-18 rounded-xl" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="h-3 w-3 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
            </div>
            <div class="py-2 flex flex-col gap-1">
              <div class="w-full h-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="w-full h-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="w-full h-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
            </div>
            <div class="flex flex-row items-center justify-between">
              <div class="h-1.5 w-18 rounded-xl" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="flex flex-row gap-0.5">
                <div class="h-2 w-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
                <div class="h-2 w-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              </div>
            </div>
          </div>
        </div>

          <div class="text-2xl font-bold">Your Jobs list</div>

        <div class="absolute top-1/2 -translate-y-1/2 translate-x-1/2 right-0 flex flex-col gap-2 ">
          <div
              v-for="(item, index) in 3"
              :key="index"
              class="bg-surface-900 border rounded-md p-2 w-48"
              :class="index === 1 ? 'border-primary-400 transition-all ease-in-bounce duration-300 group-hover/jobbtn:-translate-x-4': 'border-surface-700'"
          >
            <div class="flex flex-row items-center justify-between">
              <div class="h-2 w-18 rounded-xl" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="h-3 w-3 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
            </div>
            <div class="py-2 flex flex-col gap-1">
              <div class="w-full h-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="w-full h-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="w-full h-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
            </div>
            <div class="flex flex-row items-center justify-between">
              <div class="h-1.5 w-18 rounded-xl" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              <div class="flex flex-row gap-0.5">
                <div class="h-2 w-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
                <div class="h-2 w-2 rounded" :class="index === 1 ? 'bg-primary-400': 'bg-surface-800'"></div>
              </div>
            </div>
          </div>
        </div>

    </div>
</template>

<style scoped>

.joblistbtn:before, .joblistbtn:after{
  content: "";
  z-index: -1;
  position: absolute;
  left: 0;
  height: 100%;
  width: 100%;
  border-radius: 50%;
  filter: blur(50px);
  opacity: 0;
  transition: all .5s ease-in-out;
}

.joblistbtn:hover:before, .joblistbtn:hover:after{
  opacity: 0.2;
  border-radius: 100%;
}

.joblistbtn:before{
  bottom: -100%;
}

.joblistbtn:after{
  top: -100%;
}

.joblistbtn:hover:before{
  bottom: -90%;
}

.joblistbtn:hover:after{
  top: -90%;
}

</style>