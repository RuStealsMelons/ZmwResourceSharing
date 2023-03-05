<script setup lang="ts">
import { Sunny, Moon } from '@element-plus/icons-vue';
import { useDark, useToggle } from '@vueuse/core'


/**
 * Element-plus 暗黑模式 
 * isDark -> false -> 白天
 * isDark -> true -> 夜晚
 * toggleDark -> 切换
 */
const isDark = useDark()
const toggleDark: any = useToggle(isDark)

</script>

<template>

    <!-- 路由入口 -->
    <p>
      <router-link to="/backstage"></router-link>
      <router-link to="/reception"></router-link>
    </p>
    <!-- 视图渲染 -->
    <router-view></router-view>

    <!-- 切换暗黑模式的按钮 --> <!--:color="'red'"-->
    <div class="icons">
        <el-icon @click="toggleDark()" :size="30">
            <Sunny v-if="!isDark"/>
            <Moon v-else="isDark"/>
        </el-icon>
    </div>

</template>

<style scoped>
.icons{
    position: absolute;
    bottom: 10%;
    right: 0;
}
</style>
