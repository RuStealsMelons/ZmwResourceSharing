<script setup lang="ts">
import CryptoJS from "crypto-js";
import { ElMessage } from 'element-plus'
import { useUserStore } from '../store/user'
import { useRouter } from 'vue-router'
const { registerFrom, register, registerResponse } = useUserStore()
const router = useRouter()
const registe = () => {
    if (registerFrom.password != registerFrom.password_) {
        ElMessage({
            message: '你的两次密码不一致！',
            type: 'warning',
        })
        return;
    }
    if ((registerFrom.username.length < 1 || registerFrom.username.length > 12) || (registerFrom.password.length < 6 || registerFrom.password.length > 12)) {
        ElMessage({
            message: '账号或密码长度不符合要求！',
            type: 'warning',
        })
        return;
    }
    registerFrom.sign =
        registerFrom.password = CryptoJS.MD5(registerFrom.password + registerFrom.invitation).toString().slice(0, registerFrom.password.length);
    registerFrom.password_ = CryptoJS.MD5(registerFrom.password + registerFrom.invitation).toString().split('').reverse().slice(0, registerFrom.password.length).reverse().join('');

    registerFrom.sign = CryptoJS.MD5(registerFrom.password + registerFrom.password_ + registerFrom.username).toString()

    register()
    if (registerResponse.success == true) {
        ElMessage({
            message: registerResponse.mess,
            type: 'success',
        })
        
        router.push("/login")

    } else if(registerResponse.success == false) {
        ElMessage.error(registerResponse.mess)
    }
    
}

</script>

<template>
    <el-card shadow="never" id="login-card">
        <template #header>
            <div class="card-header">
                <el-button class="button" text>&lt;登录</el-button>
                <span>注册</span>
            </div>
        </template>
        <el-form :model="registerFrom" label-width="100" id="from">
            <el-form-item label="账号:">
                <el-input v-model="registerFrom.username" placeholder="长度为1-12位的任意非空字符" />
                <!-- <div style="width: 100px"></div> -->
            </el-form-item>
            <el-form-item label="密码:">
                <el-input type="password" placeholder="长度为6-12位的任意非空字符" show-password v-model="registerFrom.password" />
            </el-form-item>
            <el-form-item label="再次确认:">
                <el-input type="password" placeholder="请再次输入密码！" show-password v-model="registerFrom.password_" />
            </el-form-item>
            <el-form-item label="邀请码:">
                <el-input type="password" placeholder="填写邀请码" show-password v-model="registerFrom.invitation" />
            </el-form-item>
            <el-button type="primary" @click="registe()">注册</el-button>
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

#from {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
