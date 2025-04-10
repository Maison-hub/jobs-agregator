<script setup lang="ts">
import {useBackend} from "~/composables/useBackend";
import JobPreviewSkeleton from "~/components/JobPreviewSkeleton.vue";

interface offer{
  id: number;
  title: string;
  description: string;
  location: string;
  company: string;
  link: string;
}

interface offerResponse{
  offers: offer[]
}

const offers = ref([] as offer[]);
const loadingOffers = ref(true)

onMounted(async ()=>{
  const response = await useBackend('/offers?limit=6') as offerResponse
  offers.value = response.offers
  loadingOffers.value = false
})

</script>

<template>
  <section class="p-8">
  <div class="flex w-full flex-col md:flex-row items-center justify-center gap-5 relative">
    <NuxtLink to="/offers" class="w-full md:w-1/2 relative">
      <ButtonJobList />
    </NuxtLink>
    <NuxtLink to="/scrape" class="w-full md:w-1/2">
      <ButtonScrape />
    </NuxtLink>
  </div>
  </section>


  <div class="p-8">
    <div id="result-list" class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
      <template v-if="loadingOffers">
        <JobPreviewSkeleton/>
        <JobPreviewSkeleton/>
        <JobPreviewSkeleton/>
        <JobPreviewSkeleton/>
        <JobPreviewSkeleton/>
        <JobPreviewSkeleton/>
      </template>
      <div v-else v-for="job in offers" :key="job.id">
        <JobPreview
            :title="job.title"
            :description="job.description"
            :location="job.location"
            :company="job.company"
            :link="job.link"
        />
      </div>
    </div>
  </div>
</template>