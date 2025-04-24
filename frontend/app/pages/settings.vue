<script setup>
import { ref, onMounted } from 'vue';
import { useBackend } from '@/composables/useBackend';
import Textarea from 'primevue/textarea';
import InputText from 'primevue/inputtext';

const form = ref({
  job_title: '',
  profile_description: '',
  location: '',
  ollama_url: '',
  ollama_score_model: '',
  ollama_cv_model: '',
});

const { get, put } = useBackend();

const fetchPreferences = async () => {
  try {
    const response = await get('/user/preferences');
    form.value = response.data;
  } catch (error) {
    console.error('Erreur lors de la récupération des préférences :', error);
  }
};

const updatePreferences = async () => {
  try {
    await put('/user/preferences', form.value);
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
    <h1 class="text-2xl font-bold mb-4">Modifier les paramètres utilisateur</h1>
    <form @submit.prevent="updatePreferences" class="space-y-4">
      <div class="flex flex-col">
        <label for="job_title" class="font-medium">Titre du poste</label>
        <InputText id="job_title" v-model="form.job_title" class="p-inputtext w-full" />
      </div>
      <div class="flex flex-col">
        <label for="profile_description" class="font-medium">Description du profil</label>
        <Textarea id="profile_description" v-model="form.profile_description" class="w-full" rows="3" />
      </div>
      <div class="flex flex-col">
        <label for="location" class="font-medium">Localisation</label>
        <InputText id="location" v-model="form.location" class="p-inputtext w-full" />
      </div>
      <div class="flex flex-col">
        <label for="ollama_url" class="font-medium">URL Ollama</label>
        <InputText id="ollama_url" v-model="form.ollama_url" class="p-inputtext w-full" />
      </div>
      <div class="flex flex-col">
        <label for="ollama_score_model" class="font-medium">Modèle de score Ollama</label>
        <InputText id="ollama_score_model" v-model="form.ollama_score_model" class="p-inputtext w-full" />
      </div>
      <div class="flex flex-col">
        <label for="ollama_cv_model" class="font-medium">Modèle de CV Ollama</label>
        <InputText id="ollama_cv_model" v-model="form.ollama_cv_model" class="p-inputtext w-full" />
      </div>
      <Button label="Enregistrer" type="submit" class="p-button w-full mt-4" />
    </form>
  </div>
</template>
