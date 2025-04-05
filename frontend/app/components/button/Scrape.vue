<script setup lang="ts">
const isHovered = ref(false)

const sites = [
  { name: 'LinkedIn', logo: '/logos/linkedin.svg' },
  { name: 'Indeed', logo: '/logos/indeed.svg' },
  { name: 'WTTJ', logo: '/logos/wttj.svg' },
]

function getLogoStyle(index: number) {
  const positions = [
    { left: '80px', top: '40px' },
    { left: '290px', top: '0px' },
    { left: '500px', top: '40px' },
  ]
  return {
    ...positions[index],
  }
}

</script>


<template>

  <div class="scrapebtn cursor-pointer z-10 bg-surface-900 w-full flex items-center justify-center h-52 rounded-xl relative group/jobbtn overflow-hidden before:bg-primary-400 after:bg-primary-400 outline-2 outline-transparent hover:outline-primary-400 outline-offset-0 hover:outline-offset-[6px] transition-all ease-in-bounce duration-300 shadow-primary-400/30 hover:shadow-hover-xl"
       @mouseenter="isHovered = true"
       @mouseleave="isHovered = false"
  >

    <!-- Câbles SVG -->
    <svg width="206" class="stroke-surface-800" height="125" viewBox="0 0 206 125" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path id="lbm" d="M203 62.3652H3" stroke="current-color" stroke-width="6" stroke-linecap="round"/>
      <path id="lbt" d="M193.476 62.3652H112.048C95.6544 62.3652 82.3651 75.6546 82.3651 92.0478V92.0478C82.3651 108.441 69.0757 121.73 52.6825 121.73H3" stroke="current-color" stroke-width="6" stroke-linecap="round"/>
      <path id="lbb" d="M193.476 62.3651H112.048C95.6544 62.3651 82.3651 49.0758 82.3651 32.6825V32.6825C82.3651 16.2893 69.0757 3 52.6825 3H3" stroke="current-color" stroke-width="6" stroke-linecap="round"/>

      <rect
          class="circle"
          v-for="(path, i) in ['lbm', 'lbt', 'lbb']"
          :key="i"
          width="12"
          height="12"
          rx="3"
          fill="url(#paint0_radial_730_35)"
          :style="`offset-path: url(#${path}); animation-delay: ${Math.floor(Math.random() * 10000)}ms; animation-duration: ${Math.floor((Math.random() * 600)+800)}ms`"/>
      <defs>
        <defs>
          <radialGradient id="paint0_radial_730_35" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(9 4) rotate(90) scale(4 9)">
            <stop stop-color="#15CD46"/>
            <stop offset="1" stop-color="#0B6723" stop-opacity="0"/>
          </radialGradient>
        </defs>
      </defs>
    </svg>

    <div class="btn-text text-2xl z-10 before:bg-surface-900/10  py-2 px-8 relative">Scrap jobs</div>

    <svg width="206" height="125" viewBox="0 0 206 125" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path id="rbm" d="M3.00001 62.3652H203" stroke="black" stroke-width="6" stroke-linecap="round"/>
      <path id="rbt" d="M12.5238 62.3652H93.9524C110.346 62.3652 123.635 75.6546 123.635 92.0478V92.0478C123.635 108.441 136.924 121.73 153.317 121.73H203" stroke="black" stroke-width="6" stroke-linecap="round"/>
      <path id="rbt" d="M12.5238 62.3651H93.9524C110.346 62.3651 123.635 49.0758 123.635 32.6825V32.6825C123.635 16.2893 136.924 3 153.317 3H203" stroke="black" stroke-width="6" stroke-linecap="round"/>
    </svg>

    <!-- Logos au bout des branches -->
    <img v-for="(site, i) in sites" :key="i" :src="site.logo" class="w-10 h-10 absolute"
         :style="getLogoStyle(i)" />
  </div>

</template>

<style scoped>
.circle{
  transform: translateY(-4px);
  offset-distance: 0;
  animation: follow-path infinite ease-in-out;
  z-index: 100;
}


@keyframes follow-path {
  0%, 10% {
    offset-distance: 0;
  }
  90%, 100% {
    offset-distance: 100%;
  }
}


.btn-text:before{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  border-radius: 100%;
  filter: blur(20px);
}
</style>