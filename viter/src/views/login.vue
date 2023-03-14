<script setup lang="ts">
import CryptoJS from "crypto-js";
import { ElMessage } from 'element-plus'
import { useUserStore } from '../store/user'
import axios from 'axios'
const { loginFrom } = useUserStore()

const offsetNumber = (num: number) => {
    let str = num.toString(); 
    let offset = 10;

    let result = "";
    for (let i = 0; i < str.length; i++) {
        let code = str.charCodeAt(i);
        code += offset;
        result += String.fromCharCode(code);
    }
    return result
}

const login = async () => {
    if ((loginFrom.username.length < 1 || loginFrom.username.length > 12) || (loginFrom.password.length < 6 || loginFrom.password.length > 12)) {
        ElMessage({ message: '账号或密码长度不符合要求！', type: 'warning', })
        return;
    }
    let ts = 0;
    do { ts = Date.now(); } while (ts % 1000 == 0);

    const { data } = await axios.post('/api/login', {
        username: loginFrom.username,
        password: CryptoJS.MD5(loginFrom.password).toString(),
        ts: offsetNumber(ts)
    })

}

</script>

<template>
    <div style="padding-top: 150px;">
        <div class="register-container">
            <h2>登录</h2>
            <form>
                <div class="form-group">
                    <label for="username">用户名</label>
                    <input type="text" id="username" v-model="loginFrom.username" placeholder="1-12 非空字符" name="username"
                        required>
                </div>
                <div class="form-group">
                    <label for="password">密码</label>
                    <input type="password" id="password" v-model="loginFrom.password" placeholder="6-12 非空字符"
                        name="password" required>
                </div>
                <el-button type="primary" style="height: 40px;" @click="login()">登录</el-button>
                <!-- <button type="submit">注册</button> -->
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
}
</style>
