<script setup lang="ts">
import { useNavStore } from '../store/nav'
const NavStore = useNavStore()
NavStore.now = "back"

console.log(NavStore.now)
</script>

<template>
    backstage
</template>

<style scoped>
.icons {
    position: absolute;
    bottom: 10%;
    right: 0;
}
</style>
