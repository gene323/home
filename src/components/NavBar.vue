<template>
	<nav class="h-12 flex shadow-md">
		<div class="container mx-auto flex items-center gap-x-5 max-w-3xl relative px-10">
			<RouterLink to="/" class="">
				<img src="@/assets/icons/favicon.ico" alt="" width="32" class="">
			</RouterLink>
			<RouterLink :class="{'text-orange-300': $route.path ===  '/'}" to="/">Home</RouterLink>
			<RouterLink :class="{'text-orange-300': $route.path ===  '/blog'}" to="/blog">Blog</RouterLink>
			<button class="ms-auto animate__animated"
				:class="[icon.animation]"
				:key="icon.icon"
				@click="toggle"
			>
				<i class="bi"
					:class="[icon.icon]"
					:style="{'color': icon.color}"
					:key="icon.icon">
				</i>
			</button>
		</div>
	</nav>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const icon = ref({
	icon: 'bi-moon-fill',
	color: 'mediumpurple',
	animation: 'animate__slideInDown',
})
const burger = ref()

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
</style>