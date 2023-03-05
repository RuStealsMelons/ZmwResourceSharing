import { defineStore } from 'pinia';
import { Navigation } from '../../api/reception/navigation'

// 定义容器
export const useNavigationStore = defineStore('navigationStore', {
    state: () => {
        return {
            navs: [] as Navigation[]
            // [
            //     {"name": "首页", data: []},
            //     {"name": "实用工具", data: [
            //         {"name": "软件推荐", data: []},
            //     ]},
            //     {"name": "游戏专题", data: [

            //     ]},
            //     {"name": "教程分享", data: []},
            //     {"name": "源码分享", data: []},
            //     {"name": "驱动下载", data: []},
            // ]
        }
    },

    getters: {

    },

    actions: {
        loadNavs(){
            this.navs = [
                {id:1, title: "首页", data: []},
                {id:2, title: "实用工具", data: [
                    {id:1, title: "软件推荐", data: []},
                    {id:2, title: "游戏工具", data: []},
                    {id:3, title: "日常生活", data: []},
                    {id:4, title: "浏览器插件", data: []},
                ]},
                {id:3, title: "游戏专题", data: [
                    {id:1, title: "娱乐辅助", data: []},
                    {id:2, title: "游戏主题", data: []},
                    {id:3, title: "实用辅助", data: []},
                    {id:4, title: "老游戏分享", data: []},
                ]},
                {id:4, title: "教程分享", data: [
                    {id:1, title: "wordpress", data: []},
                    {id:2, title: "办公", data: []},
                    {id:3, title: "游戏教程", data: []},
                ]},
                {id:5, title: "源码分享", data: [
                    {id:1, title: "E语言源码", data: []},
                    {id:2, title: "wordpress主题", data: []},
                ]},
                {id:6, title: "驱动下载", data: [
                    {id:1, title: "打印机", data: []},
                    {id:2, title: "数位板", data: []},
                ]},
            ]
        }
    }
})