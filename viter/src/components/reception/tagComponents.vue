<script setup lang="ts">

const tag = {
    "src": "https://eixgo.com/wp-content/uploads/thumb/2023/03/fill_w576_h356_g0_mark_image.png",
    "title": "原神3.5最新Acrepi-v1.0.7(原Akebi CG 科技)下载2023-03-02更新",
    "subText": "使用教程 使用方法：解压文件夹到桌面，以管理员方式运行injector.exe,找到原神游戏的Genshin Impact game目录下选择yuanshen.exe（genshin.exe）找不到的话直接全盘搜索“yuanshen.exe”（在未启动游戏时开启修改器，修改器会自动打开原神），初次运行修改器会查找偏移量，待数据处理完成后，登入游戏 使用F1打开菜单。",
    "classify": "原神辅助",
    "watch": "3.2k",
    "love": "0",
    "sourceImg": "https://eixgo.com/wp-content/uploads/thumb/2023/01/fill_w120_h120_g0_mark_4b397b16a646be036e54ec77567c85ba_w677_h677_s339_1_avatar_ZHke519833.jpg",
    "source": "易科软件园",
    "time": "2天"
}


</script>

<template>
    <div class="tag-box">
        <div  class="content-box" >
            <img :src="tag.src" class="topImg">
            <p class="title">{{ tag.title }}</p>
            <p class="text">{{ tag.subText }}</p>
            <div class="type-box">
                <span class="smallLeft">{{ tag.classify }}</span>
                <div class="small-box">
                    <span>{{ tag.watch }}</span>
                    <span>{{ tag.love }}</span>
                </div>
            </div>
            <div class="bottom-box">
                <div class="bottom-box-left">
                    <img :src="tag.sourceImg" class="box-left-img">
                    <span>{{ tag.source }}</span>
                </div>
                <span class="bottom-right">{{ tag.time }}</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.tag-box{
    height: 333px;
    width: 299px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.content-box {
    height: 313px;
    border: 1px solid #f8f8f8;
    width: 279px;
}

.topImg {
    height: 60%;
    width: 100%;

}

.title {
    font-size: 1vw;
    font-weight: bold;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-left: 10px;
    margin-top: 10px;
}

.text {
    font-size: 0.8vw;
    color: #797c80;
    margin-left: 10px;
    margin-top: 10px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    overflow: hidden;
    text-overflow: ellipsis;
}

.type-box {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    color: #797c80;
}

.smallLeft {
    margin-left: 10px;
}

.small-box {
    margin-right: 10px;
    width: 30%;
    display: flex;
    justify-content: space-around;
}

.bottom-box {
    height: 15%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.box-left-img {
    border-radius: 25px;
    height: 20px;
    width: 20px;
    display: inline-block;
    margin-right: 5px;
}

.bottom-box-left {
    margin-left: 10px;
}

.bottom-right {
    margin-right: 15px;
}
.content-box:hover{
    box-shadow: 0 0 5px rgba(125,125,125,0.5);
}
.content-box{
    transition: 0.2s;
}
</style>
