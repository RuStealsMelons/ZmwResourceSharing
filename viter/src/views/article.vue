<script setup lang="ts">
import { useNavStore } from '../store/nav'
import { UploadFilled } from '@element-plus/icons-vue'
import Editor from '../components/Editor.vue'
import EditorHide from '../components/EditorHide.vue'
import { ref,reactive,inject } from 'vue'
import {storeToRefs} from "pinia"
import { useArticleStore } from '../store/article'
const NavStore = useNavStore()
NavStore.now = "back"
const ArticleStore = useArticleStore()
const capacity = ref("123")
const { context, hide } = storeToRefs(ArticleStore)
const articleFrom = reactive({
    title: "",
    subText: "",
    classify: "",
    imgurl: "",
    context: "",
    hide: ""
})
const options = [
  {
    label: '游戏辅助',
    options: [
      {
        value: 'LOL',
        label: 'LOL',
      },
      {
        value: '原神',
        label: '原神',
      },
    ],
  },
  {
    label: '软件破解',
    options: [
      {
        value: '腾讯',
        label: '腾讯',
      },
      {
        value: '网易',
        label: '网易',
      },
      {
        value: '解压',
        label: '解压',
      },
    ],
  },
]
const submit = () => {
    articleFrom.context = context.value
    articleFrom.hide = hide.value
    console.log(articleFrom)
}

const success = (v: any) => {
    console.log(v)
}
</script>

<template>
    <div>
        <div style="width: 100%; display: flex;">
            <div style="width: 50%">
                <div style=" margin-top: 10px;">
                    <h1 style="margin: 20px;">标题：</h1>
                    <el-input v-model="articleFrom.title" placeholder="输入标题用于列表展示" />
                </div>
                <div style=" margin-top: 10px;">
                    <h1 style="margin: 20px;">简介：</h1>
                    <el-input v-model="articleFrom.subText" style="width: 100%" type="textarea" :autosize="{ minRows: 2, maxRows: 4 }" placeholder="简介" />
                </div>
            </div>
            <div style="width: 50%">
                <div
                    style="height: 45%; display: flex; flex-direction: row; justify-content: space-evenly; align-items: center;">
                    <el-button type="primary" @click="submit()">提交</el-button>
                    <el-button type="success">重置</el-button>
                </div>
                <div style="height: 50%; box-sizing: border-box; padding: 0 30px;">
                    <div style=" margin-top: 10px;">
                        <h1 style="margin: 20px;">分类:</h1>
                        <el-select style="width: 100%;" size="large" v-model="articleFrom.classify" placeholder="选择分类">
                            <el-option-group v-for="group in options" :key="group.label" :label="group.label">
                                <el-option v-for="item in group.options" :key="item.value" :label="item.label"
                                    :value="item.value" />
                            </el-option-group>
                        </el-select>
                    </div>
                </div>
            </div>
        </div>
        <div style="width: 1000px; margin-top: 10px;">
            <h1 style="margin: 20px;">封面上传：</h1>
            <el-upload @success="success" class="upload-demo" v-model="articleFrom.imgurl" drag action="/api/uploader"
                multiple>
                <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                <div class="el-upload__text">
                    拖拽文件或 <em>点击上传</em>
                </div>
            </el-upload>
        </div>
        <div style="width: 1000px; margin-top: 10px;">
            <h1 style="margin: 20px;">正文内容：</h1>
            <Editor />
        </div>
        <div style="width: 1000px; margin-top: 10px;">
            <h1 style="margin: 20px;">隐藏类容：</h1>
            <EditorHide />
        </div>
    </div>
</template>

<style scoped></style>
