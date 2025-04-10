<script setup lang="ts">
import Paginator from 'primevue/paginator';
import {useBackend} from "~/composables/useBackend";
import JobPreviewSkeleton from "~/components/JobPreviewSkeleton.vue";
import InputText from 'primevue/inputtext';
import MultiSelect from 'primevue/multiselect';
import Button from 'primevue/button';
import Select from 'primevue/select';


interface offer{
  id: number;
  title: string;
  description: string;
  location: string;
  company: string;
  url: string;
}

interface offerResponse{
  total_count: number
  offers: offer[]
}

const { $sites } = useNuxtApp();


const offersPerPage = ref(12)
const total_count = ref(0)
const page = ref(1)
const searchValue = ref('')

const orderBy = ref<{name: string, value: string}>({name: 'Title', value: 'title'})

const offers = ref([] as offer[]);
const loadingOffers = ref()

const selectedSites = ref<sites[]>([]);

const onSearch = async ()=>{
  console.log(orderBy.value)
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
    sitesQuery += `&domain=${sites.domain}`
  })
  if(orderBy.value){
    sitesQuery += `&order_by=${orderBy.value}`
  }

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
        <InputText type="text" v-model="searchValue" placeholder="Search" />
      </div>

      <!--Sites select-->
      <div class="card flex justify-center">
        <MultiSelect v-model="selectedSites" :options="$sites" optionLabel="name" placeholder="Select Sites" display="chip" class="w-full md:w-80">
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
        <div class="flex flex-row gap-2">
          <Button label="Search" icon="pi pi-search" class="w-full md:w-40" @click="onSearch" />
        </div>
    </div>
    <div>

    </div>
  </section>


  <div class="p-8 mb-12">
    <div v-if="!loadingOffers">
      <div class="flex flex-row items-center justify-start gap-4 py-5">
        <p class="text-surface-600 text-nowrap">Found {{total_count}} results</p>
        <div class="h-[1px] bg-surface-600 w-full"></div>
        <Select v-model="orderBy" :options="[
          {name: 'Title', value: 'title'},
          {name: 'Score', value: 'score'},
          {name: 'Location', value: 'location'}]"
                optionLabel="name" optionValue="value" placeholder="Order by" class="w-full md:w-56"   @change="onSearch">
          <template #dropdownicon>
            <i class="pi pi-sort-alt" />
          </template>
        </Select>
      </div>
    </div>
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
            :link="job.url"
        />
      </div>
    </div>
  </div>
  <div class="fixed bottom-0 w-full">
    <Paginator @update:rows="(n) => {page = 1 ;fetchOffers(0, n)}" @page="(o) => {fetchOffers(o.page, o.rows); console.log(o);}" :rows="offersPerPage" :totalRecords="total_count" :rowsPerPageOptions="[12, 20, 30, 50]"></Paginator>
  </div>
</template>