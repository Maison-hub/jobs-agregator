<script setup lang="ts">
import Paginator from 'primevue/paginator';
import {useBackend} from "~/composables/useBackend";
import JobPreviewSkeleton from "~/components/JobPreviewSkeleton.vue";
import InputText from 'primevue/inputtext';
import MultiSelect from 'primevue/multiselect';
import Button from 'primevue/button';

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

const offersPerPage = ref(12)
const total_count = ref(0)
const page = ref(1)
const searchValue = ref('')

const offers = ref([] as offer[]);
const loadingOffers = ref()

const selectedSites = ref([]);
const sites = ref([
  { name: 'Welcome To The jungle', domain: 'welcometothejungle.com', logo:'welcomeToTheJungle.svg' },
  { name: 'LinkedIn', domain: "linkedin.com", logo: 'linkedIn.svg' },
  { name: 'Hello Work', domain: "hellowork.com", logo: 'helloWork.svg' },
  { name: 'France Travail', domain: "france-travail.fr", logo: 'franceTravail.svg' },
]);

const onSearch = async ()=>{
  await fetchOffers();
}

const fetchOffers = async (newPageValue?: number, newLimit?: number) => {
  loadingOffers.value = true
  if (newPageValue) {
    page.value = newPageValue + 1
  }
  if (newLimit) {
    offersPerPage.value = newLimit
  }
  let sitesQuery = ''
  selectedSites.value.forEach((sites)=>{
    console.log(sites)
    sitesQuery += `&domain=${sites.domain}`
  })
  const response = await useBackend(`/offers?page=${page.value}&limit=${offersPerPage.value}${sitesQuery}`) as offerResponse
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

  <section id="filters" class="px-8 py-8 flex flex-col items-center justify-center gap-5 ">
    <div class="flex flex-row gap-5 items-start justify-start w-full">
      <div class="flex flex-row gap-2">
        <InputText type="text" v-model="searchValue" placeholder="Keywords" />
      </div>

      <!--Sites select-->
      <div class="card flex justify-center">
        <MultiSelect v-model="selectedSites" :options="sites" optionLabel="name" placeholder="Select Sites" display="chip" class="w-full md:w-80">
          <template #option="slotProps">
            <div class="flex items-center">
              <img :alt="slotProps.option.name" :src="`/images/icons/sites/${slotProps.option.logo}`" :class="`mr-2 rounded-xs aspect-square`" style="width: 18px" />
              <div>{{ slotProps.option.name }}</div>
            </div>
          </template>
          <template #chip="{ value, removeCallback }">
            <div class="flex flex-row gap-1 items-center justify-center bg-white/10 p-1 relative h-full rounded-sm">
              <img
                  :alt="value.name"
                  :src="`/images/icons/sites/${value.logo}`"
                  class="rounded-xs aspect-square h-4"
                  v-tooltip.top="value.name"
              />
              <div @click.stop="removeCallback" class="cursor-pointer text-surface-600 flex items-center justify-center">
                <i class="pi pi-times" style="font-size: 0.75rem"></i>
              </div>
            </div>
          </template>
        </MultiSelect>
      </div>
    </div>
    <div>
      <div class="flex flex-row gap-2">
        <Button label="Search" icon="pi pi-search" class="w-full md:w-40" @click="onSearch" />
      </div>
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
  <div>
    <Paginator @update:rows="(n) => fetchOffers(0, n)" @page="(o) => fetchOffers(o.page, o.rows)" :rows="offersPerPage" :totalRecords="total_count" :rowsPerPageOptions="[12, 20, 30, 50]"></Paginator>
  </div>
</template>