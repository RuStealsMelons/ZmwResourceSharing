import { defineStore } from 'pinia';


// 定义容器
export const useNavStore = defineStore('nav', {
    state: () => {
        return {
            navs: [
                {title: "首页", router: "/assistance"},
                {title: "游戏辅助", router: "/assistance"},
                {title: "软件分享", router: "/share"},
            ],
            front: [
                {title: "首页", router: "/"},
                {title: "游戏辅助", router: "/assistance"},
                {title: "软件分享", router: "/share"},
            ],
            back: [
                {title: "首页", router: "/assistance"},
                {title: "用户", router: "/#"},
                {title: "分类", router: "/classify"},
                {title: "文章", router: "/article"},
                {title: "邀请码", router: "/invitation"},
            ],
            now: "front"
        }
    },

    getters: {

    },

    actions: {

    }
})