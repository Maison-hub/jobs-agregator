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

    alert('Préférences mises à jour avec succès !');
  } catch (error) {
    console.error('Erreur lors de la mise à jour des préférences :', error);
    alert('Une erreur est survenue.');
  }
};

onMounted(fetchPreferences);
</script>

<template>
  <div class="p-8">
    <h1 class="text-3xl font-bold mb-6">Modifier les paramètres utilisateur</h1>
    <form @submit.prevent="updatePreferences" class="space-y-4">
      <div class="flex flex-col gap-4 pb-8">
        <div class="w-full flex flex-row gap-4">
          <h2 class="text-xl text-nowrap  text-white/50">Paramètres utilisateur</h2>
          <Divider />
        </div>
        <div class="flex flex-row gap-4 w-full [&>*]:w-full">
          <FloatLabel variant="in">
            <InputText id="job_title" v-model="settingsForm.job_title" class="p-inputtext w-full" fluid />
            <label for="job_title" class="font-medium">Titre du poste</label>
          </FloatLabel>
          <FloatLabel variant="in">
              <InputText id="location" v-model="settingsForm.location" class="p-inputtext w-full" fluid />
              <label for="location" class="font-medium">Localisation</label>
          </FloatLabel>
        </div>
        <div class="flex flex-col">
          <FloatLabel variant="in">
            <label for="profile_description" class="font-medium">Description du profil</label>
            <Textarea id="profile_description" v-model="settingsForm.profile_description" class="w-full" rows="3" />
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
            <label for="ollama_url" class="font-medium">URL Ollama</label>
            <InputText id="ollama_url" v-model="settingsForm.ollama_url" class="p-inputtext w-full" />
          </FloatLabel>
        </div>
        <div class="flex flex-row gap-4 w-full [&>*]:w-full">
          <FloatLabel variant="in">
            <label for="ollama_score_model" class="font-medium">Modèle de score Ollama</label>
            <InputText id="ollama_score_model" v-model="settingsForm.ollama_score_model" class="p-inputtext w-full" />
          </FloatLabel>

          <FloatLabel variant="in">
            <label for="ollama_cv_model" class="font-medium">Modèle de CV Ollama</label>
            <InputText id="ollama_cv_model" v-model="settingsForm.ollama_cv_model" class="p-inputtext w-full" />
          </FloatLabel>
        </div>
      </div>
      <Button label="Enregistrer" type="submit" class="p-button w-full mt-4" />
    </form>
  </div>
</template>
