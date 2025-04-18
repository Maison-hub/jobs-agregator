<script setup lang="ts">

const props = defineProps({
  width: {
    type: String,
    default: 'w-full'
  },
  progress: {
    type: String,
    default: '0'
  },
  showNumber: {
    type: Boolean,
    default: true
  }
})

const getColor = (score: number): string => {
  const startColor = { r: 239, g: 68, b: 68 }; // Rouge (#ef4444)
  const endColor = { r: 34, g: 197, b: 94 };  // Vert (#22c55e)

  const ratio = score / 100; // Normalise le score entre 0 et 1

  const r = Math.round(startColor.r + (endColor.r - startColor.r) * ratio);
  const g = Math.round(startColor.g + (endColor.g - startColor.g) * ratio);
  const b = Math.round(startColor.b + (endColor.b - startColor.b) * ratio);

  return `rgb(${r}, ${g}, ${b})`;
};

</script>

<template>
  <div class="flex flex-row items-center gap-2">
    <div v-if="props.showNumber">
      <span>{{props.progress}}</span>
    </div>
    <div class="h-2 bg-surface-800 relative rounded-full" :class="width" >
      <div class="bg-primary shadow-glow-sm h-full rounded-full" :style="`width: ${props.progress}%; background-color: ${getColor(props.progress)}`"></div>
    </div>
  </div>

</template>