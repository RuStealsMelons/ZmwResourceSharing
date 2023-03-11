import { defineStore } from 'pinia';
import axios from 'axios';

interface LoginFrom {
    username: string,
    password: string
}

interface RegisterFrom {
    username: string,
    password: string,
    password_: string,
    invitation: string,
    sign: string
}

interface RegisterResponse {
    mess: string,
    success: boolean
}

// 定义容器

export const useUserStore = defineStore('user', {
    state: () => {
        return {
            loginFrom: {} as LoginFrom,
            registerFrom: { username: "", password: "", password_: "", invitation: "", sign: "" } as RegisterFrom,
            registerResponse: {} as RegisterResponse
        }
    },

    getters: {

    },

    actions: {
        async register() {
            const { data } = await axios.post('/api/register', { ...this.registerFrom, invitation: window.btoa(this.registerFrom.invitation) })
            this.registerResponse = data
        },
        async login() {
            let ts = 0;
            do {
                ts = Date.now();
            } while (ts % 1000 == 0);
            

            const { data } = await axios.post('/api/login', { ...this.loginFrom, ts: ts })
            console.log(data)
        }
    }
})