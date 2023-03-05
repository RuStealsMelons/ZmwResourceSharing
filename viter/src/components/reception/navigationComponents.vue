<!-- 前台页面导航栏组件 -->

<script setup lang="ts">
import { useNavigationStore } from '../../store/reception/navigation'

const navigationStore = useNavigationStore()
navigationStore.loadNavs()

</script>

<template>
    <el-menu class="el-menu-demo center" mode="horizontal">
        <template v-for="item in navigationStore.navs">
            <el-menu-item v-if="item.data.length == 0" :index="item.id">{{ item.title }}</el-menu-item>
            <el-sub-menu v-else="item.data.length == 0" :index="item.id">
                <template #title>{{ item.title }}</template>
                <el-menu-item v-for="child in item.data" :index="item.id + '-' + child.id">{{ child.title
                }}</el-menu-item>
            </el-sub-menu>
        </template>
    </el-menu>
</template>

<style scoped>
.center {
    display: flex;
    /* justify-content: center;
    align-items: center; */

}
</style>
