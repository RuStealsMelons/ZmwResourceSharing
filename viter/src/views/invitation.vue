<script setup lang="ts">
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useNavStore } from '../store/nav'
import type { TabPaneName } from 'element-plus'
import { ElMessage } from 'element-plus'
const NavStore = useNavStore()
NavStore.now = "back"

const invitationList = ref([])  // 数据列表
const active = ref('all')  // 被选中的选项卡
const total = ref(0)  // 总条数
const pagesize = ref(20)  // 每页的数量
const currentpage = ref(1)  // 当前页数
const generateNum = ref(1)  // 生成邀请码的数量
const exportNum = ref(1)  // 导出邀请码的数量
const dialog = ref(false)
const exportRes = ref("")
onMounted(async () => {
    refresh(active.value, 1, pagesize.value)
})


const refresh = async (tagName: string, currentpage: number, pagesize: number) => {
    const { data } = await axios.get("/api/Invitation/" + tagName + "/" + currentpage + "/" + pagesize)
    invitationList.value = data.data
    total.value = data.length
}



const handleClick = (name: TabPaneName) => {
    refresh(active.value, 1, pagesize.value)
}

const exprotALL = async () => {
    const { data } = await axios.get("/api/export/0")
    exportRes.value = data.data
    dialog.value = true
}
const exportInvitation = async () => {
    const { data } = await axios.get("/api/export/" + exportNum.value)
    exportRes.value = data.data
    dialog.value = true
}

const generateInvitation = async () => {
    const { data } = await axios.get("/api/Generate/" + generateNum.value)
    if (data.success == true) {
        ElMessage({
            message: data.mess,
            type: 'success',
        })
    } else {
        ElMessage.error('生成失败！')
    }
}


</script>

<template>
    <div id="box">

        <el-tabs v-model="active" type="card" @tab-change="handleClick">
            <el-tab-pane label="全部" name="all">
                <el-table :data="invitationList" style="width: 100%">
                    <el-table-column prop="Invitation_id" label="邀请码ID" width="180" />
                    <el-table-column prop="Invitation_code" label="邀请码" width="180" />
                    <el-table-column prop="create_time" label="创建时间" width="180" />
                    <el-table-column prop="use_time" label="使用时间" width="180" />
                    <el-table-column prop="user_name" label="使用者" width="180" />
                </el-table>
                <div class="page-tag">
                    <el-pagination @current-change="refresh(active, currentpage, pagesize)" :page-size="pagesize"
                        v-model:current-page="currentpage" background layout="prev, pager, next" :total="total" />
                </div>

            </el-tab-pane>
            <el-tab-pane label="已使用" name="used">
                <el-table :data="invitationList" style="width: 100%">
                    <el-table-column prop="Invitation_id" label="邀请码ID" width="180" />
                    <el-table-column prop="Invitation_code" label="邀请码" width="180" />
                    <el-table-column prop="create_time" label="创建时间" width="180" />
                    <el-table-column prop="use_time" label="使用时间" width="180" />
                    <el-table-column prop="user_name" label="使用者" width="180" />
                </el-table>
                <div class="page-tag">
                    <el-pagination @current-change="refresh(active, currentpage, pagesize)" :page-size="pagesize"
                        v-model:current-page="currentpage" background layout="prev, pager, next" :total="total" />
                </div>
            </el-tab-pane>
            <el-tab-pane label="未使用" name="unused">
                <el-table :data="invitationList" style="width: 100%">
                    <!-- <el-table-column type="selection" width="55" /> -->
                    <el-table-column prop="Invitation_id" label="邀请码ID" width="180" />
                    <el-table-column prop="Invitation_code" label="邀请码" width="180" />
                    <el-table-column prop="create_time" label="创建时间" width="180" />
                    <el-table-column prop="use_time" label="使用时间" width="180" />
                    <el-table-column prop="user_name" label="使用者" width="180" />
                </el-table>
                <div class="page-tag">
                    <el-pagination @current-change="refresh(active, currentpage, pagesize)" :page-size="pagesize" background
                        layout="prev, pager, next" :total="total" />
                </div>
            </el-tab-pane>
            <el-tab-pane label="生成" name="Generate">
                <div class="from-box">


                    <div class="from-item" style="align-items: center; justify-content: space-around;">
                        <h1>导出邀请码</h1>
                        <div><el-input-number v-model="exportNum" :min="1" /></div>
                        <el-button plain @click="exportInvitation">导出</el-button>
                    </div>
                    <div class="from-item" style="align-items: center; justify-content: space-around;">
                        <h1>全部导出</h1>
                        <el-button plain @click="exprotALL()">导出</el-button>
                    </div>
                    <div class="from-item" style="align-items: center; justify-content: space-around;">
                        <h1>生成新的邀请码</h1>
                        <div><el-input-number v-model="generateNum" :min="1" /></div>
                        <el-button plain @click="generateInvitation()">生成</el-button>
                    </div>

                </div>
            </el-tab-pane>
        </el-tabs>
    </div>

    <el-dialog v-model="dialog" title="导出结果" width="30%" draggable>
        <span>
            <el-input v-model="exportRes" :autosize="{ minRows: 2, maxRows: 4 }" type="textarea"
                placeholder="xxxx-xxxx" /></span>
        <template #footer>
            <span class="dialog-footer">
                <el-button type="primary" @click="dialog = false">
                    关闭
                </el-button>
            </span>
        </template>
    </el-dialog>
</template>

<style scoped>
#box {
    width: 1000px;
    margin-top: 10px;
}

.page-tag {
    display: flex;
    justify-content: center;
}

.from-box {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
}

.from-item {
    width: 400px;
    height: 100px;
    background-color: antiquewhite;
    margin: 20px;
    display: flex;
}
</style>
