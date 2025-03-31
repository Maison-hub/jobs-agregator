<script>
</script>

<template>
  <div>
    <div class="p-8">
      <Menubar>
        <template #end>
          <Button icon="pi pi-cog" variant="text" severity="secondary" aria-label="Filter" v-tooltip.bottom="'Settings'" />
        </template>
      </Menubar>
    </div>
    <NuxtPage />
  </div>
</template>
