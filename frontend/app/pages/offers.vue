<script setup lang="ts">
import Paginator from 'primevue/paginator';
import {useBackend} from "~/composables/useBackend";
import JobPreviewSkeleton from "~/components/JobPreviewSkeleton.vue";

const offersPerPage = ref(12)
const total_count = ref(0)
const page = ref(1)

interface offer{
  id: number;
  title: string;
  description: string;
  location: string;
  company: string;
  link: string;
}

interface offerResponse{
  total_count: number
  offers: offer[]
}

const offers = ref([] as offer[]);
const loadingOffers = ref(true)

const fetchOffers = async (newPageValue?: number, newLimit?: number) => {
  loadingOffers.value = true
  if (newPageValue) {
    page.value = newPageValue + 1
  }
  if (newLimit) {
    offersPerPage.value = newLimit
  }
  const response = await useBackend(`/offers?page=${page.value}&limit=${offersPerPage.value}`) as offerResponse
  total_count.value = response.total_count
  offers.value = response.offers
  loadingOffers.value = false
}

onMounted(async ()=>{
  await fetchOffers()
  loadingOffers.value = false
})

</script>

<template>

  <section id="filters">

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
  <div>
    <Paginator @update:rows="(n) => fetchOffers(0, n)" @page="(o) => fetchOffers(o.page, o.rows)" :rows="offersPerPage" :totalRecords="total_count" :rowsPerPageOptions="[12, 20, 30, 50]"></Paginator>
  </div>
</template>