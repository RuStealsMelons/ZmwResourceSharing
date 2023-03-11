<script setup lang="ts">
import { Search } from '@element-plus/icons-vue'
import logo from './assets/logo.png'
// const 

const linkClick = () => {

} 
</script>

<template>
    <!-- 视图渲染 -->
    <div id="page">
        <div id="head-box">
            <div id="head-core-box">
                <a id="logo">
                    <img id="logo-img" :src="logo" alt="logo" />
                    <span id="logo-font">爱发电</span>
                </a>
                <a id="nav" @click="linkClick()">首页</a>
                <a @click="linkClick()">游戏辅助</a>
                <a @click="linkClick()">软件分享</a>
                <div id="logo">
                    <Search style="opacity: 0.3;width: 1.5em; height: 1.5em; margin-right: 8px" />
                    <input placeholder="搜索..." id="search" />
                </div>
                <div style="width: 200px;">
                    <el-button type="primary" @click="$router.push('/login')" plain>登录</el-button>
                    <el-button type="success" @click="$router.push('/register')"  plain>注册</el-button>
                </div>
            </div>
        </div>
        <div style="height: 66.66px"></div>
        <div id="context">
            
        <router-view></router-view>
        
    </div>

        
    </div>
</template>

<style scoped>
#page {
    width: 100%;
    height: 100%;
    min-height: 700px;
    display: flex;
    background-color: #f7f7f7;
    flex-direction: column;
}

#head-box {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    background: #f7f7f7;
    box-sizing: border-box;
    z-index: 99;
    height: 66.66px;
    display: flex;
}

#head-core-box {
    border-bottom: 1px solid #e3e3e3;
    box-sizing: border-box;
    max-width: 1000px;
    margin: 0 auto;
    width: 100%;
    height: 66.66px;
    align-items: center;
    justify-content: space-between;
    display: flex;
    white-space: nowrap;
}

#logo {
    display: flex;
    align-items: center;
}

#logo-img {
    width: 3.333333333333333rem;
    height: 3.333333333333333rem;
    margin-right: 16px !important;
}

#logo-font {
    color: #946ce6;
    font-size: 24px;
}

#nav {
    margin-left: 2rem;
    font-size: 16px !important;
    /* height: 100%; */
    /* border: 1px solid #946ce6; */
}

#search {
    background-color: transparent;
    border-style: none;
    width: 200px;
    height: 40px;
    font-size: 24px;
}

#search::-webkit-input-placeholder {
    font-size: 16px;
    opacity: 0.8;
}
#context{
    display: flex;
    justify-content: center;
}
.icons {
    position: absolute;
    bottom: 10%;
    right: 0;
}
</style>
