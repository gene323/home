<template>
	<nav class="h-12 flex shadow-md">
		<!-- nav main -->
		<div class="container mx-auto flex items-center gap-x-5 max-w-3xl relative px-10">
			<button
				class="text-3xl cursor-pointer select-none animate__animated animate__tada"
				:key="emojis[index]"
				@click="switchEmoji()"
			>
				{{ emojis[index] }}
			</button>
			<RouterLink :class="{'text-orange-300': $route.path ===  '/'}" to="/">Home</RouterLink>
			<RouterLink :class="{'text-orange-300': $route.path ===  '/blog'}" to="/blog">Blog</RouterLink>
			<button
				class="ms-auto animate__animated"
				:class="[icon.animation]"
				:key="icon.icon"
				@click="toggle"
			>
				<i class="bi"
					:class="[icon.icon]"
					:style="{'color': icon.color}"
					:key="icon.icon"
				>
				</i>
			</button>
		</div>
		<cat-rain v-if="times >= 3" :rain-drops="rainDrops"></cat-rain>
	</nav>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { RouterLink } from 'vue-router';
import CatRain from './CatRain.vue';

const icon = ref({
	icon: 'bi-moon-fill',
	color: 'mediumpurple',
	animation: 'animate__slideInDown',
})
const emojis = ref(['😼', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾'])
const index = ref(0)
const times = ref(0)
const rainDrops = ref(15)

const switchEmoji = () => {
	let newVal = Math.floor(Math.random() * (emojis.value.length - 1))
	if (newVal === index.value) {
		switchEmoji()
		return 
	}
	index.value = newVal
	times.value++
}
const toggle = () => {
	if (icon.value.icon === 'bi-moon-fill') {
		icon.value.icon = 'bi-brightness-high-fill'
		icon.value.color = 'orange'
		document.documentElement.setAttribute('data-theme', 'light')
	} else {
		icon.value.icon = 'bi-moon-fill'
		icon.value.color = 'mediumpurple'
		document.documentElement.setAttribute('data-theme', 'dark')
	}
}

onMounted(() => {
})

</script>

<style lang="scss" scoped>
[data-theme=dark] {
	nav {
		background-color: var(--gene-bg-1);
		box-shadow: 0 0 10px 1px black;
	}
}
[data-theme=light] {
	nav {
		background-color: white;
	}
}
</style>