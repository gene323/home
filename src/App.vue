<template>
  <NavBar />
  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';

</script>

<style>
#app {
  font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
html {
  transition: .5s ease;
  min-height: 100%;
}
[data-theme=dark] {
  background-color: var(--gene-bg-2);
  color: white;
}
</style>
