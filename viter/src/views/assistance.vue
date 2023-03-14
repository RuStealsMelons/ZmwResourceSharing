<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useNavStore } from '../store/nav'
useNavStore().now = "front"
const navlist = ["所有", "绘画", "视频", "写作"]
const itemlist = [
    {
        title: "FriendsMind",
        img: "https://pic1.afdiancdn.com/user/3a0ac94a429611eb95e052540025c377/common/ddbc797a2ee1687639981b775907fd56_w1440_h360_s705.jpg?imageView2/1/w/634/h/320"
    },
    {
        title: "FriendsMind",
        img: "https://pic1.afdiancdn.com/user/3a0ac94a429611eb95e052540025c377/common/ddbc797a2ee1687639981b775907fd56_w1440_h360_s705.jpg?imageView2/1/w/634/h/320"
    },
    {
        title: "FriendsMind",
        img: "https://pic1.afdiancdn.com/user/3a0ac94a429611eb95e052540025c377/common/ddbc797a2ee1687639981b775907fd56_w1440_h360_s705.jpg?imageView2/1/w/634/h/320"
    },
    {
        title: "FriendsMind",
        img: "https://pic1.afdiancdn.com/user/3a0ac94a429611eb95e052540025c377/common/ddbc797a2ee1687639981b775907fd56_w1440_h360_s705.jpg?imageView2/1/w/634/h/320"
    }
]
const navSelect = (index: number) => {
    const navElements = document.querySelectorAll('.nav');
    navElements.forEach((el, i) => {
        if (i == index) {
            el.classList.add('on');
        } else {
            el.classList.remove('on');
        }
    })
}

onMounted(() => {
    const navElements = document.querySelectorAll('.nav');
    navElements[0].classList.add('on');
})
</script>

<template>
    <div id="box">
        <div id="navs">
            <h1>游戏列表</h1>
            <template :key="i" v-for="(it, i) in navlist">
                <div class="nav" @click="navSelect(i)">
                    {{ it }}
                </div>
                <div style="height: 10px"></div>
            </template>
        </div>
        <div id="room">
            <div class="item-box" :key="i" v-for="(it, i) in itemlist">
                <div class="item">
                    <el-image class="item-img" :src="it.img" fit="fill">
                        <template #error>
                            <div class="image-slot">
                                <el-icon><icon-picture /></el-icon>
                            </div>
                        </template>
                    </el-image>
                    <div class="item-font">
                        <div>
                            {{ it.title }}
                            <span class="item-classify">原神</span>
                        </div>
                        <div class="item-introduction">
                            FriendsMind是希望能延续Tatsuki监督/动物朋友美好的团体
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
#box {
    max-width: 1000px;
    min-width: 500px;
    height: 20px;
    /* background-color: rebeccapurple; */
    display: flex;
}

#navs {
    width: 280px;
}

h1 {
    line-height: 60px;
    font-size: 1.5rem;
    box-sizing: border-box;
}

.nav {
    width: 100%;
    padding: .6666666666666666rem 1.333333333333333rem;
    border-radius: .3333333333333333rem;
    border: 1px solid rgba(0, 0, 0, .1);
    display: flex;
    align-items: center;
    box-sizing: border-box;
    background: #fff;
}

.on {
    border-color: #946ce6;
    color: #946ce6;
}

.nav:hover {
    cursor: pointer;
    background: #f7f7f7;
}

.item-box {
    width: 50%;
    padding: 0.3rem 1.333333333333333rem;
    box-sizing: border-box;
    margin-bottom: 1.333333333333333rem;
    height: 250px;
    /* background-color: #946ce6; */
}

.item {
    width: 100%;
    height: 100%;
    box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.12);
}
.item:hover {
    box-shadow: 0px 12px 32px 4px rgba(0, 0, 0, 0.04),0px 8px 20px rgba(0, 0, 0, 0.08);
}

.item-img {
    width: 100%;
    height: 65%;
}
.item-font{
    width: 100%;
    height: 35%;
    box-sizing: border-box;
    padding: 10px;
}
.item-classify{
    background-color: #946ce6;
    display: inline-flex;
    color: #fff;
    font-size: 12px;
    padding: .08333333333333333rem .5416666666666666rem;
    border-radius: .16666666666666666rem;
}
.item-introduction{
    margin-top: 3px;
    font-size: 13px;
}
#room {
    width: 720px;
    box-sizing: border-box;
    margin: 60px 0px 0px 20px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
</style>
