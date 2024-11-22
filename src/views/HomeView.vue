<template>
  <div class="container mx-auto max-w-3xl">
    <main class="pt-6 px-3 flex">
      <img class="rounded-full animate__animated animate__tada animate__delay-1s w-[150px] h-[150px] sm:w-[250px] sm:h-[250px]"
        src="@/assets/selfie.jpg"
        alt="selfie"
        id="selfie"
      >
      <div class="flex flex-col flex-1 p-3 sm:p-8">
        <h1 class="text-yellow-500 sm:text-3xl">Hello, I'm Gene</h1>
        <h5 class="text-xs sm:text-lg">coding | jogging | cat</h5>
        <div class="flex gap-2 mt-auto">
          <a href="https://github.com/gene323" class="sm:text-xl">
            <i class="bi bi-github"></i>
          </a>
          <a href="https://instagram.com/hochienn" class="sm:text-xl">
            <i class="bi bi-instagram"></i>
          </a>
          <a href="mailto:geneho323@gmail.com" class="sm:text-xl">
            <i class="bi bi-envelope-fill"></i>
          </a>
        </div>
      </div>
    </main>

    <div id="area">
      <div id="cat"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="scss" scoped>

[data-theme=light] {
  .bi {
    color: black;
  }
  #selfie {
    box-shadow: 2px 0px 8px 5px gray;
  }
}

[data-theme=dark] {
  #selfie {
    box-shadow: 2px 0px 8px 5px black;
  }
}


#area {
  position: fixed;
  width: 100%;
  left: 0px;
  bottom: 0px;
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
