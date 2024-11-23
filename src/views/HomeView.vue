<template>
  <div class="container mx-auto max-w-3xl relative">
    <main ref="imageSection">
      <h1 class="text-yellow-500 text-4xl text-center py-6 animate__animated animate__tada">A Ju</h1>
      <swiper-container init="false" class=" w-[230px] md:w-full" ref="swiper">
        <swiper-slide v-for="image in images" :key="image" class="">
          <img class="aju-image" :src="`./aju/${image}.jpg`" alt="">
        </swiper-slide>
      </swiper-container>
    </main>
    <div id="area">
      <div id="cat"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, reactive } from 'vue';
import { register } from 'swiper/element/bundle';

const images = ref(9)
const swiper = ref()
const imageSection = ref()

onMounted(() => {
  register();

  // tablet or wider device
  if (document.body.offsetWidth >= 1024) {
    Object.assign(swiper.value, {
      slidesPerView: 3,
      effect: 'coverflow',
    })
  } else {
    imageSection.value.style.overflow = 'hidden'
    Object.assign(swiper.value, {
      effect: 'cards',
      autoHeight: true,
    })
  }

  swiper.value.initialize();
})



</script>

<style lang="scss" scoped>

[data-theme=light] {
  .bi {
    color: black;
  }
  
}

#area {
  position: absolute;
  width: 100%;
  left: 0px;
  bottom: -150px;
}

#cat {
  width: 142px;
  height: 98px;
  background: url("@/assets/cat_sprite.png") repeat-x;
  animation: walk .8s steps(3) infinite, forward 20s linear infinite;
  position: relative;
}

@keyframes walk {
  0% { background-position: 0px; }
  100% { background-position: -428px; }
}
@keyframes forward {
  0% { left: -30%; }
  100% { left: 120%; }
}
</style>
