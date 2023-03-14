<script setup lang="ts">
import { Plus } from '@element-plus/icons-vue'
const navlist = ["所有", "绘画", "视频", "写作"]
</script>

<template>
    <div id="box">
        <div id="navs">
            <h1>游戏列表</h1>
            <template :key="i" v-for="(it, i) in navlist">
                <div class="nav">
                    {{ it }}
                </div>
                <div style="height: 10px"></div>
            </template>
            <el-button type="primary" :icon="Plus" circle />
        </div>
    </div>
</template>

<style scoped>
#box {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 1000px;
}

#navs {
    width: 280px;
    text-align: center;
    /* display: flex; */
}

h1 {
    line-height: 60px;
    font-size: 1.5rem;
    box-sizing: border-box;
}

.nav {
    width: 100%;
    padding: .6666666666666666rem 1.333333333333333rem;
    border-radius: .3333333333333333rem;
    border: 1px solid rgba(0, 0, 0, .1);
    display: flex;
    align-items: center;
    box-sizing: border-box;
    background: #fff;
}
</style>
