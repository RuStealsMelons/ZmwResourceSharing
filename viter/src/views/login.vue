<script setup lang="ts">

import { useUserStore } from '../store/user'
const { loginFrom, login } = useUserStore()



</script>

<template>
    <el-card shadow="never" id="login-card">
        <template #header>
            <div class="card-header">
                <span>登录</span>
                <el-button class="button" text>注册></el-button>
            </div>
        </template>
        <el-form :model="loginFrom" label-width="100px" id="from">
            <el-form-item label="账号:">
                <el-input v-model="loginFrom.username"  placeholder="请输入账号！"/>
            </el-form-item>
            <el-form-item label="密码:">
                <el-input type="password" placeholder="请输入密码！" show-password
                    v-model="loginFrom.password" />
            </el-form-item>
            <el-button type="primary" @click="login()">登录</el-button>
        </el-form>
    </el-card>
</template>

<style scoped>
#login-card {
    margin-top: 10%;
    min-width: 600px;
    max-width: 800px;
}
.el-form-item__label-wrap {
  margin-left: 0px !important;
}
#from{
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
