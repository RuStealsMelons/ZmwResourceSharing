import { createRouter,createWebHistory} from "vue-router";

import backstage from '../views/backstage/index.vue';
import reception from '../views/reception/index.vue';

const routes = [
    // 不加任何路由时，重定向到前台页面
    {
        path: "/",
        redirect: '/reception'
    },
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

]

export const router = createRouter({
    history: createWebHistory(),
    routes: routes
})