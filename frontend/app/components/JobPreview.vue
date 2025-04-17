<script setup lang="ts">

const { $sites } = useNuxtApp();

const props = defineProps({
  title: String,
  description: String,
  location: String,
  company: String,
  link: String,
})

const site = computed(() => {
  return $sites.find((s) => props.link?.includes(s.domain));
});
</script>

<template>
  <div class="bg-surface-900 border border-surface-700 rounded-xl transition-all duration-300 shadow-primary-400/20 outline-transparent outline-2 hover:outline-primary-400 outline-offset-0 hover:outline-offset-[6px] ease-in-bounce shadow-none hover:shadow-xl cursor-pointer">
    <div class="p-4 flex flex-row items-center justify-between">
      <span class="font-bold font-lg">
        {{props.title}}
      </span>
      <Button icon="pi pi-star" severity="secondary" aria-label="Filter" v-tooltip.bottom="'Add to favorite'" />
    </div>
    <div class="px-4">
      <div>
        <p class="line-clamp-4 text-sm text-white/70">
          {{ props.description }}
        </p>
      </div>
    </div>
    <div>
      <div class="p-4 flex flex-row items-center justify-between">
          <span class="text-white/50 text-sm">
            <i class="pi pi-map-marker"></i>
            Nancy, Grand Est
          </span>
        <span class="flex flex-row items-center gap-2">
          <img
              v-if="site"
              :src="`/images/icons/sites/${site.logo}`"
              :alt="site.name"
              class="w-8 h-8 rounded-sm"
              v-tooltip.left="`From ${site.name}`"
          />
          <a :href="link" target="_blank">
              <Button icon="pi pi-external-link" severity="secondary" aria-label="Filter" size="small" />
            </a>
        </span>
      </div>
    </div>

  </div>
</template>