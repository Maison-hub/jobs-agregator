<script setup lang="ts">
import MultiSelect from "primevue/multiselect";
import ToggleSwitch from 'primevue/toggleswitch';
import { Vue3Lottie } from 'vue3-lottie'


const selectedSites = ref<sites[]>([]);
const { $sites } = useNuxtApp();

const config = useRuntimeConfig()
const backApi = config.public.backend_url

const useAi = ref(false);

const isScraping = ref(false);
const scrapingDone = ref(false);
const currentMessage = ref('');


const startScraping = async () => {
  isScraping.value = true;
  const response = await fetch(`${ backApi }/scrape?sites=hellowork`) as Response;
  if (!response.body) {
    console.error('ReadableStream not yet supported in this browser.');
    return;
  }
  const reader = response.body.getReader();
  const decoder = new TextDecoder('utf-8');
  let done = false;

  while (!done) {
    const {value, done: readerDone} = await reader.read();
    done = readerDone;
    if (value) {
      const chunk = decoder.decode(value, {stream: true});
      const lines = chunk.split('\n').filter((line) => line);
      if (lines.length > 0) {
        currentMessage.value = lines[lines.length - 1]; // Met à jour avec le dernier message
      }
    }
  }
  isScraping.value = false;
  scrapingDone.value = true;
}

</script>

<template>
  <section class="p-8">
    <div class="flex flex-row items-center gap-4 flex-wrap">

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
      <div class="flex flex-row items-center gap-2">
        <ToggleSwitch v-model="useAi" inputId="useAi" />
        <label for="useAi" class="text-surface-600 text-sm">Use AI</label>
      </div>
    </div>
  </section>

  <section >

    <div class="w-full flex flex-col gap-6 justify-center items-center">
      <Button v-slot="slotProps" asChild>
        <button
            @click="startScraping()"
            v-bind="slotProps.a11yAttrs"
            class="rounded-lg text-black border-none w-fit text-xl px-7 py-4 outline-2 outline-transparent hover:outline-primary-400 outline-offset-0 hover:outline-offset-[6px] duration-300 bg-primary-500 cursor-pointer ring-offset-surface-0 dark:ring-offset-surface-900 ring-primary transition-all ease-in-bounce"
        >
          Lunch Scrape 🚀
        </button>
      </Button>
      <div v-if="isScraping" class="flex flex-col items-center justify-center gap-2">
        <client-only>
          <Vue3Lottie
              animationLink="animations/scrape_loader.json"
              loop
              :height="200"
              :width="300"
          />
        </client-only>
        <span class="text-sm text-surface-600">
          {{ currentMessage }}
        </span>
      </div>
      <div v-if="scrapingDone" class="flex flex-col items-center justify-center gap-2">
        <span class="text-lg font-semibold text-primary-500">
          Scraping Finished
        </span>
        <client-only>
          <Vue3Lottie
              animationLink="animations/scrape_done.json"
              :height="200"
              :width="200"
              :loop="1"
          />
        </client-only>
        <NuxtLink to="/offers">
          <Button icon="pi pi-briefcase" variant="outlined" label="View in list of jobs" severity="secondary"/>
        </NuxtLink>
      </div>
    </div>

  </section>

</template>