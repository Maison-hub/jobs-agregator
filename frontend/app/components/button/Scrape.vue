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
  <div class="scrapebtn cursor-pointer z-10 bg-surface-900 flex items-center justify-center h-52 rounded-xl relative group/scrapebtn overflow-hidden before:bg-primary-400 after:bg-primary-400 outline-2 outline-transparent hover:outline-primary-400 outline-offset-0 hover:outline-offset-[6px] transition-all ease-in-bounce duration-300 shadow-primary-400/30 hover:shadow-hover-xl"
       @mouseenter="isHovered = true"
       @mouseleave="isHovered = false"
  >
    <div class="logos h-full flex flex-col justify-evenly *:rounded-md p-3">
      <img src="~/assets/images/icons/sites/franceTravail.svg" alt="" class="-translate-y-4 -translate-x-5 -rotate-12 grayscale">
      <img src="~/assets/images/icons/sites/helloWork.svg" alt="" class="-translate-x-4 grayscale">
      <img src="~/assets/images/icons/sites/linkedIn.svg" alt="" class="translate-y-4 -translate-x-5 rotate-12 grayscale">
    </div>
    <!-- Câbles Gauche -->
    <svg width="206" class="stroke-surface-800" height="125" viewBox="0 0 206 125" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path id="lbm" d="M204 62.3652H3" stroke="current-color"  stroke-width="6" stroke-linecap="round"/>
      <path id="lbt" d="M194.476 62.3652H167.561C158.16 62.3652 149.065 65.7028 141.895 71.7833L115.183 94.4367C94.4051 112.058 68.0458 121.73 40.8017 121.73H3" stroke="current-color"  stroke-width="6" stroke-linecap="round"/>
      <path id="lbb" d="M194.476 62.3651H167.561C158.16 62.3651 149.065 59.0275 141.895 52.947L115.183 30.2936C94.4051 12.6723 68.0458 3 40.8017 3H3" stroke="current-color"  stroke-width="6" stroke-linecap="round"/>

      <rect
          :class="`circle ${isHovered ? 'hover' : ''}`"
          v-for="(path, i) in ['lbm', 'lbt', 'lbb']"
          :key="i"
          width="12"
          height="12"
          rx="3"
          fill="url(#paint0_radial_730_35)"
          :style="`offset-path: url(#${path}); animation-duration: ${Math.floor((Math.random() * 600)+800)}ms`"/>
      <defs>
        <defs>
          <radialGradient id="paint0_radial_730_35" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(9 4) rotate(90) scale(4 9)">
            <stop stop-color="#15CD46"/>
            <stop offset="1" stop-color="#0B6723" stop-opacity="0"/>
          </radialGradient>
        </defs>
      </defs>
    </svg>

    <div class="btn-text text-2xl z-10 before:bg-surface-900/10  py-2 px-4 relative text-nowrap">Scrap jobs</div>

    <!-- Câbles Droite -->
    <svg class="stroke-surface-800"  width="206" height="125" viewBox="0 0 206 125" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path id="rbm" d="M3 62.3652H204" stroke="current-color" stroke-width="6" stroke-linecap="round"/>
      <path id="rbb" d="M12.5238 62.3652H39.4388C48.8398 62.3652 57.9355 65.7028 65.1053 71.7833L91.8169 94.4367C112.595 112.058 138.954 121.73 166.198 121.73H204" stroke="current-color" stroke-width="6" stroke-linecap="round"/>
      <path id="rbt" d="M12.5238 62.3651H39.4388C48.8398 62.3651 57.9355 59.0275 65.1053 52.947L91.8169 30.2936C112.595 12.6723 138.954 3 166.198 3H204" stroke="current-color" stroke-width="6" stroke-linecap="round"/>

      <rect
          :class="`circle ${isHovered ? 'hover' : ''}`"
          v-for="(path, i) in ['rbm', 'rbt', 'rbb']"
          :key="i"
          width="12"
          height="12"
          rx="3"
          fill="url(#paint0_radial_730_35)"
          :style="`offset-path: url(#${path}); animation-duration: ${Math.floor((Math.random() * 600)+800)}ms`"/>
      <defs>
        <defs>
          <radialGradient id="paint0_radial_730_35" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(9 4) rotate(90) scale(4 9)">
            <stop stop-color="#15CD46"/>
            <stop offset="1" stop-color="#0B6723" stop-opacity="0"/>
          </radialGradient>
        </defs>
      </defs>
    </svg>

    <div class="logos h-full flex flex-col justify-evenly *:rounded-md p-3">
      <img src="~/assets/images/icons/sites/welcomeToTheJungle.svg" alt="" class="-translate-y-4 translate-x-5 -rotate-12 grayscale">
      <img src="~/assets/images/icons/sites/indeed.svg" alt="" class="translate-x-5 grayscale">
      <img src="~/assets/images/icons/sites/franceTravail.svg" alt="" class="translate-y-4 translate-x-5 rotate-12 grayscale">
    </div>
  </div>
</template>

<style scoped>
.circle{
  transform: translateY(-4px);
  offset-distance: 0;
  z-index: 100;
  opacity: 0;
}
.circle.hover{
  animation: follow-path infinite ease-in-out;
}

@keyframes follow-path {
  0% {
    offset-distance: 0;
    opacity: 0;
  }
  30%{
    opacity: 80%;
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

.scrapebtn:hover .logos img{
  filter: grayscale(0);
  translate: none;
  rotate: none;
}

.logos img{
  width: 35px;
  height: 35px;
  aspect-ratio: 1/1;
  min-width: 35px;
  min-height: 35px;
  transition: all .4s var(--ease-in-bounce);
}

.scrapebtn:before, .scrapebtn:after{
  content: "";
  z-index: -1;
  position: absolute;
  left: 0;
  height: 100%;
  width: 100%;
  border-radius: 50%;
  filter: blur(50px);
  opacity: 0;
  transition: all .5s ease-in-out;
}

.scrapebtn:hover:before, .scrapebtn:hover:after{
  opacity: 0.2;
  border-radius: 100%;
}

.scrapebtn:before{
  bottom: -100%;
}

.scrapebtn:after{
  top: -100%;
}

.scrapebtn:hover:before{
  bottom: -90%;
}

.scrapebtn:hover:after{
  top: -90%;
}
</style>