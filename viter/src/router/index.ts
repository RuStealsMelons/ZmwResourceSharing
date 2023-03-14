import { createRouter, createWebHistory } from "vue-router";

import backstage from '../views/backstage.vue';
import reception from '../views/reception.vue';
import login from '../views/login.vue';
import register from '../views/register.vue';
import assistance from '../views/assistance.vue';
import invitation from '../views/invitation.vue';
import article from '../views/article.vue';
import classify from '../views/classify.vue';
// classify
const routes = [
    // 不加任何路由时，重定向到前台页面
    {
        path: "/",
        redirect: '/',
        children: [
            // 前台页面路由
            {
                path: "/reception",
                name: "reception",
                component: reception
            },
            // 后台页面路由
            {
                path: "/backstage",
                name: "backstage",
                component: backstage
            },
            // 登录
            {
                path: "/login",
                name: "login",
                component: login
            },
            // 注册
            {
                path: "/register",
                name: "register",
                component: register
            },
            // 辅助
            {
                path: "/assistance",
                name: "assistance",
                component: assistance
            },
            {
                path: "/invitation",
                name: "invitation",
                component: invitation
            },
            {
                path: "/article",
                name: "article",
                component: article
            },
            {
                path: "/classify",
                name: "classify",
                component: classify
            },
        ]
    },


]

export const router = createRouter({
    history: createWebHistory(),
    routes: routes
})