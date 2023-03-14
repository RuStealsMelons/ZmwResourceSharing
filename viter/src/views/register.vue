<script setup lang="ts">
import CryptoJS from "crypto-js";
import { ElMessage } from 'element-plus'
import { useUserStore } from '../store/user'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useNavStore } from '../store/nav'
useNavStore().now = "front"
const { registerFrom } = useUserStore()
const router = useRouter()
const registe = async () => {
    if (registerFrom.password != registerFrom.password_) {
        ElMessage({ message: '你的两次密码不一致！', type: 'warning', })
        return;
    }
    if ((registerFrom.username.length < 1 || registerFrom.username.length > 12) || (registerFrom.password.length < 6 || registerFrom.password.length > 12)) {
        ElMessage({ message: '账号或密码长度不符合要求！', type: 'warning', })
        return;
    }

    const { data } = await axios.post('/api/register', { 
        username: registerFrom.username,
        password: CryptoJS.MD5(registerFrom.password).toString(),
        invitation: window.btoa(registerFrom.invitation),
    })
    if(data.success == false){
        ElMessage.error(data.mess)
        return
    }else{
        ElMessage({ message: data.mess, type: 'success',})
        router.push("/login")
        return
    }
}
const openNewWindow = (url: string, name: string, specs: string) => {
    window.open(url, name, specs);
}

</script>

<template>
    <div style="padding-top: 50px;">
        <div class="register-container">
            <h2>注册</h2>
            <form>
                <div class="form-group">
                    <label for="username">用户名</label>
                    <input type="text" id="username" placeholder="1-12 非空字符" name="username" v-model="registerFrom.username"
                        required>
                </div>
                <div class="form-group">
                    <label for="password">密码</label>
                    <input type="password" id="password" placeholder="6-12 非空字符" name="password"
                        v-model="registerFrom.password" required>
                </div>
                <div class="form-group">
                    <label for="confirm-password">确认密码</label>
                    <input type="password" id="confirm-password" placeholder="6-12 非空字符" name="confirm-password"
                        v-model="registerFrom.password_" required>
                </div>
                <div class="form-group">
                    <label for="invite-code">邀请码</label>
                    <input type="text" id="invite-code" name="invite-code" placeholder="赞助后，私信查看！"
                        v-model="registerFrom.invitation" required>
                </div>
                <!-- <button type="submit">注册</button> -->
                <el-button type="success" style="height: 40px;" @click="registe()">注册</el-button>
                <button type="submit" style="margin-top: 10px;"
                    @click="openNewWindow('https://afdian.net/order/create?plan_id=a9502350bf1b11edb0405254001e7c00&product_type=0', '_blank', 'height=400,width=600')">赞助一下</button>
            </form>
        </div>
    </div>
</template>

<style scoped>
.register-container {

    min-width: 400px;
    margin: auto;
    padding: 20px;
    background-color: #f2f2f2;
    border-radius: 10px;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}

form {
    display: flex;
    flex-direction: column;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"],
input[type="password"],
input[type="email"] {
    padding: 10px;
    border: none;
    border-radius: 5px;
}

button[type="submit"] {
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}</style>
