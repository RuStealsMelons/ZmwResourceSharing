<script setup lang="ts">
import NavigationComponents from "../../components/reception/navigationComponents.vue"
import TagComponents from "../../components/reception/tagComponents.vue"
import { Search } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus'
import { ref } from 'vue'

// 搜索的分类
const select = ref("")
// 搜索框输入
const search = ref("")

const searchMsg = () => {
    ElMessage({
        message: "你在`"+select.value+"`选项下搜索了："+search.value,
        type: 'success',
    })
}

let count = ref(8)
const load = () => {
    if (count.value < 100) count.value += 4
    console.log("ss")
}

</script>

<template>
    <div class="common-layout" >
        <el-container>
            <!-- 顶部区域 -->
            <div class="second-box" style="position:fixed; width: 100%; background-color: white; box-sizing: border-box;">
                <!-- 顶部区域第一行 -->
                <el-row :gutter="24" class="topList">
                    <!-- 左侧区域 -->
                    <el-col :span="12" class="logo-box">
                        <!-- logo -->
                        <el-image class="vite-logo" src="https://cn.vitejs.dev/logo.svg" fit="fit" />
                        明瑞科技
                    </el-col>
                    <!-- 右侧区域 -->
                    <el-col :span="12" class="input-box">
                        <!-- 搜索框 -->
                        <el-input v-model="search" placeholder="搜索" class="input-with-select changeInput">
                            <template #prepend>
                                <el-select v-model="select" placeholder="文章" style="width: 80px">
                                    <el-option label="视频" value="1" />
                                </el-select>
                            </template>
                            <!-- 搜索按钮 -->
                            <template #append>
                                <el-button :icon="Search" @click="searchMsg()"/>
                            </template>
                        </el-input>
                        <!-- 登录和注册按钮 -->
                        <el-button class="loginButton">登录</el-button>
                        <el-button class="loginButton">快速注册</el-button>

                    </el-col>
                </el-row>
                <!-- 顶部区域第二行 -->

                <el-row :gutter="24">
                    <!-- 导航栏 -->
                    <el-col :span="24">
                        <NavigationComponents />
                    </el-col>
                </el-row>
            </div>
            <el-main  class="main" style="margin-top: 100px; height: 500px;"  infinite-scroll-distance="100"  v-infinite-scroll="load" infinite-scroll-delay="200">
                    <span v-for="i in count" :key="i + 1" class="infinite-list-item" >
                        <TagComponents />
                    </span>

            </el-main>
            <el-footer>Footer</el-footer>
        </el-container>
    </div>
</template>

<style scoped>
::-webkit-scrollbar {
  height: 0;
  width: 0;
  /* color: transparent; */
}

.infinite-list {
  height: 100%;
  padding: 0;
  margin: 0;
  list-style: none;
}

.logo-box {
    display: flex !important;

    align-items: center;

}

.vite-logo {
    width: 30px;
    height: 30px;
    margin-left: 2%;
}

.changeInput {
    width: 40%;
    margin-left: 32%;
}

.loginButton {
    margin-left: 20px;
    color: #999;

}

.topList {
    margin-top: 0vh;
    padding-top: 10px;
}

.second-box {
    border-bottom: 1px solid #ccc;
    box-shadow: 0px 10px 30px 2px rgba(125, 125, 125, 0.2);

}

.main {
    margin-top: 30px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
}
</style>
