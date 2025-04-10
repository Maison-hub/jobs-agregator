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

</template>