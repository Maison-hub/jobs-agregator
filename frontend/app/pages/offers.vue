<script setup lang="ts">
import Paginator from 'primevue/paginator';
import {useBackend} from "~/composables/useBackend";
import JobPreviewSkeleton from "~/components/JobPreviewSkeleton.vue";
import InputText from 'primevue/inputtext';
import MultiSelect from 'primevue/multiselect';
import Button from 'primevue/button';
import Select from 'primevue/select';


interface offer{
  id: string;
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

const drawerVisible = ref(false); // État pour gérer l'ouverture du Drawer
const selectedOffer = ref<Offer | null>(null); // Stocke les détails de l'offre sélectionnée

// Fonction pour ouvrir le Drawer et fetch les détails de l'offre
const openOfferDetails = async (offerId: string) => {
  drawerVisible.value = true; // Ouvre le Drawer
  selectedOffer.value = null; // Réinitialise les données précédentes
  try {
    const offer = await useBackend(`/offers/${offerId}`) as Offer;
    selectedOffer.value = offer; // Remplit les détails de l'offre
  } catch (error) {
    console.error('Erreur lors du fetch des détails de l\'offre :', error);
  }
};

const selectedOfferSite = computed(() => {
  return $sites.find((s) => selectedOffer.value.url?.includes(s.domain));
});

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
            :id="job.id"
            :title="job.title"
            :description="job.description"
            :location="job.location"
            :company="job.company"
            :link="job.url"
            @click="openOfferDetails(job.id)"
        />
      </div>
    </div>
  </div>
  <div class="fixed bottom-0 w-full">
    <Paginator @update:rows="(n) => {page = 1 ;fetchOffers(0, n)}" @page="(o) => {fetchOffers(o.page, o.rows); console.log(o);}" :rows="offersPerPage" :totalRecords="total_count" :rowsPerPageOptions="[12, 20, 30, 50]"></Paginator>
  </div>

  <Drawer v-model:visible="drawerVisible" :dismissable="true" class="!w-screen md:!w-[75vw]">
    <template #header>
      <div v-if="selectedOffer" class="text-2xl font-bold">
          {{selectedOffer.title}}
      </div>
    </template>
    <template v-if="selectedOffer">
      <div class="w-full flex flex-row items-center justify-start gap-2">
        <img
            v-if="selectedOfferSite"
            :src="`/images/icons/sites/${selectedOfferSite.logo}`"
            :alt="selectedOfferSite.name"
            class="w-12 h-12 rounded-sm"
            v-tooltip.left="`From ${selectedOfferSite.name}`"
        />
        <a :href="selectedOffer.url" target="_blank">
          <Button icon="pi pi-external-link" severity="secondary" aria-label="Filter" size="large" />
        </a>
      </div>
      <p class="text-sm text-gray-200 py-4">{{ selectedOffer.description }}</p>
      <div class="flex flex-col gap-3">
        <span class="text-white/50 text-sm">
          <i class="pi pi-map-marker"></i>
          {{ selectedOffer.location }}
        </span>
        <span class="text-white/50 text-sm">
          <i class="pi pi-building"></i>
          {{ selectedOffer.company }}
        </span>
      </div>
    </template>
    <template v-else>
      <p>Chargement des détails...</p>
    </template>
  </Drawer>
</template>