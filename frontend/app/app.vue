<script>
</script>

<template>
  <Toast/>
  <div class="min-h-screen">
    <div class="p-8 navbar">
      <div class="rounded-lg bg-surface-900 flex flex-row justify-between p-2 shadow-2xl" >
        <div class="flex flex-row items-center gap-2">
          <NuxtLink to="/" class="flex flex-row items-center gap-2">
            <Button icon="pi pi-home" variant="text" label="home" severity="secondary" aria-label="Filter"/>
          </NuxtLink>
          <NuxtLink to="/offers">
            <Button icon="pi pi-briefcase" variant="text" label="List of jobs" severity="secondary"/>
          </NuxtLink>
          <NuxtLink to="/scrape">
            <Button icon="pi pi-asterisk" variant="text" label="Scrape" severity="secondary" />
          </NuxtLink>
        </div>
        <div>
          <Button icon="pi pi-cog" variant="text" severity="secondary" aria-label="Filter" v-tooltip.bottom="'Settings'" />
        </div>
      </div>
    </div>
    <NuxtPage />
  </div>
</template>

<style>

.navbar{
  --p-menubar-submenu-border-radius: 12px
}

</style>
