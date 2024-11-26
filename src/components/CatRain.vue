<template>
	<div class="fixed left-0 top-0 w-full h-full pointer-events-none overflow-hidden -z-10">
		<p
			v-for="i in rainDrops"
			:key="i"
			class="text-xl absolute drop"
			:style="getRandomStyle()"
		>
		{{ emojis[i-1] }}
		</p>
	</div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';

const props = defineProps<{
	rainDrops: number,
}>() 

const emojis = ref(['😼', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾'])

const getRandomStyle = () => {
	const x = Math.random() * 100
	const delay = Math.random() * 5
	const duration = Math.random() * 5 + 3

	return {
		left: `${x}%`,
		animationDelay: `${delay}s`,
		animationDuration: `${duration}s`,
	}
}

onMounted(() => {
})
</script>

<style lang="scss" scoped>
.drop {
	animation: fall 5s linear infinite;
}

@keyframes fall {
	from {
		transform: translateY(-100px) rotate(0deg);
	}
	to {
		transform: translateY(100vh) rotate(360deg);
	}
}
</style>