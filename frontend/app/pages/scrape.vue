<script setup lang="ts">
import MultiSelect from "primevue/multiselect";
import ToggleSwitch from 'primevue/toggleswitch';

const selectedSites = ref<sites[]>([]);
const { $sites } = useNuxtApp();


const useAi = ref(false);

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

    <div class="w-full flex justify-center">
      <Button v-slot="slotProps" asChild>
        <button
            v-bind="slotProps.a11yAttrs"
            class="rounded-lg text-black border-none text-xl px-7 py-4 outline-2 outline-transparent hover:outline-primary-400 outline-offset-0 hover:outline-offset-[6px] duration-300 bg-primary-500 cursor-pointer ring-offset-surface-0 dark:ring-offset-surface-900 ring-primary transition-all ease-in-bounce"
        >
          Lunch Scrape 🚀
        </button>
      </Button>
    </div>

  </section>

</template>