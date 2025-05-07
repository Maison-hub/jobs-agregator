<script setup>
import { ref, onMounted } from 'vue';
import { useBackend } from '@/composables/useBackend';
import Textarea from 'primevue/textarea';
import InputText from 'primevue/inputtext';
import {useToast} from "primevue/usetoast";

const settingsForm = ref({
  job_title: '',
  profile_description: '',
  location: '',
  ollama_url: '',
  ollama_score_model: '',
  ollama_cv_model: '',
  franceTravail_url: '',
  helloWork_url: '',
  welcomeToTheJungle_url: '',
});

const toast = useToast()


const fetchPreferences = async () => {
  try {
    const response = await useBackend('/user/preferences');
    settingsForm.value = response;
  } catch (error) {
    toast.add({ severity: 'error', summary: 'Failed to get note', detail: 'Erreur lors de la récupération des préférences', life: 3000 });
    console.error('Erreur lors de la récupération des préférences :', error);
  }
};

const updatePreferences = async () => {
  try {
    await useBackend('/user/preferences', {
      method: 'PUT',
      body: JSON.stringify(settingsForm.value),
    });

    toast.add({ severity: 'success', summary: 'Prérérences mise a jour !', detail: 'Vos préférences ont été mise a jour avec succès', life: 3000 });
  } catch (error) {
    console.error('Erreur lors de la mise à jour des préférences :', error);
    toast.add({ severity: 'error', summary: 'Erreur lors de la mise à jour des préférences', detail: 'vos préférences n\'ont pas été mise a jour ', life: 3000 });
  }
};

onMounted(fetchPreferences);
</script>

<template>
  <div class="p-8">
    <h1 class="text-3xl font-bold mb-6">Modifier les paramètres utilisateur</h1>
    <form @submit.prevent="updatePreferences"
      class="space-y-4">
      <div class="flex flex-col gap-4 pb-8">
        <div class="w-full flex flex-row gap-4">
          <h2 class="text-xl text-nowrap  text-white/50">Paramètres utilisateur</h2>
          <Divider />
        </div>
        <div class="flex flex-row gap-4 w-full [&>*]:w-full">
          <FloatLabel variant="in">
            <InputText id="job_title"
              v-model="settingsForm.job_title"
              class="p-inputtext w-full"
              fluid />
            <label for="job_title"
              class="font-medium">Titre du poste</label>
          </FloatLabel>
          <FloatLabel variant="in">
            <InputText id="location"
              v-model="settingsForm.location"
              class="p-inputtext w-full"
              fluid />
            <label for="location"
              class="font-medium">Localisation</label>
          </FloatLabel>
        </div>
        <div class="flex flex-col">
          <FloatLabel variant="in">
            <label for="profile_description"
              class="font-medium">Description du profil</label>
            <Textarea id="profile_description"
              v-model="settingsForm.profile_description"
              class="w-full"
              rows="3" />
          </FloatLabel>
        </div>
      </div>
      <div class="flex flex-col gap-4">
        <div class="w-full flex flex-row gap-4">
          <h2 class="text-xl text-nowrap  text-white/50">Intelligence Artificielle</h2>
          <Divider />
        </div>
        <div class="flex flex-col">
          <FloatLabel variant="in">
            <label for="ollama_url"
              class="font-medium">URL Ollama</label>
            <InputText id="ollama_url"
              v-model="settingsForm.ollama_url"
              class="p-inputtext w-full" />
          </FloatLabel>
        </div>
        <div class="flex flex-row gap-4 w-full [&>*]:w-full">
          <FloatLabel variant="in">
            <label for="ollama_score_model"
              class="font-medium">Modèle de score Ollama</label>
            <InputText id="ollama_score_model"
              v-model="settingsForm.ollama_score_model"
              class="p-inputtext w-full" />
          </FloatLabel>

          <FloatLabel variant="in">
            <label for="ollama_cv_model"
              class="font-medium">Modèle de CV Ollama</label>
            <InputText id="ollama_cv_model"
              v-model="settingsForm.ollama_cv_model"
              class="p-inputtext w-full" />
          </FloatLabel>
        </div>
      </div>

      <!-- Scrapers Options -->
      <div class="flex flex-col gap-4 pb-8">
        <div class="w-full flex flex-row gap-4">
          <h2 class="text-xl text-nowrap  text-white/50">Scrapers configuration</h2>
          <Divider />
        </div>
        <div class="flex flex-col gap-3">
          <!-- France travail URL-->
          <FloatLabel variant="in">
            <label for="franceTravail_url"
              class="font-medium">France Travail URL</label>
            <InputText id="franceTravail_url"
              v-model="settingsForm.franceTravail_url"
              class="p-inputtext w-full" />
          </FloatLabel>
          <!-- Hello Work URL-->
          <FloatLabel variant="in">
            <label for="helloWork_url"
              class="font-medium">Hello Work URL</label>
            <InputText id="helloWork_url"
              v-model="settingsForm.helloWork_url"
              class="p-inputtext w-full" />
          </FloatLabel>
          <!-- Welcome to the Jungle URL-->
          <FloatLabel variant="in">
            <label for="welcomeToTheJungle_url"
              class="font-medium">Welcome to the Jungle URL</label>
            <InputText id="welcomeToTheJungle_url"
              v-model="settingsForm.welcomeToTheJungle_url"
              class="p-inputtext w-full" />
          </FloatLabel>
        </div>
      </div>
      <Button label="Enregistrer"
        type="submit"
        class="p-button w-full mt-4" />
    </form>
  </div>
</template>
