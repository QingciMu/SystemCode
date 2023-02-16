<template>
  <div>
    <div class="title">Predict Task List</div>
    <div>
      <el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
          border style="width: 100%">
        <el-table-column fixed prop="taskName" label="Task Name" width="220">
        </el-table-column>
        <el-table-column prop="testCase" label="Test Case" width="100">
        </el-table-column>
        <el-table-column prop="fileNum" label="File Num" width="120">
        </el-table-column>
        <el-table-column prop="Model" label="Model" width="120">
        </el-table-column>
        <el-table-column prop="Status" label="Status" width="100"
        :filters="[{ text: 'Running', value:'Running'}, { text: 'Finished', value: 'Finished'}]"
        :filter-method="filterTag"
        filter-palcement="bottom-end">
        <template slot-scope="scope">
          <el-tag
          :type="scope.row.Status === 'Running' ? 'primary' : 'success'"
          close-transition>{{scope.row.Status}}</el-tag>
        </template>
        </el-table-column>
        <el-table-column prop="createTime" label="Create Time" width="195">
        </el-table-column>
        <el-table-column fixed="right" label="Operations">
          <template slot-scope="scope">
            <template v-if="scope.row.Status === 'Success'">
              <el-button
                size="mini"
                @click="handleDetail(scope.row.taskName)">Detail</el-button>
              <el-button
                size="mini"
                type="primary"
                @click="handleDownload(scope.row)">Download</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.row.taskName)">Delete</el-button>
            </template>
          </template>
        </el-table-column>
      </el-table>
      <el-dialog :visible.sync="delVisible" title="Tips" width="30%" center>
          <span>Are you sure you want to delete? Can't be recovered after deletion.</span>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="closeDel">Cancel</el-button>
              <el-button type="primary" :loading="isLoading" @click="confirmDelete()">
                Confirm
              </el-button>
            </span>
          </template>
      </el-dialog>
    </div>
    <div class="split-page">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-sizes="[10, 20, 50]"
        :page-size="pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.length">
      </el-pagination>
    </div>
  </div>
</template>
<script>
import { getTestTask, deleteTestTask } from '../api/api.js'
export default {
  name: 'preList',
  data () {
    return {
      currentPage: 1,
      pagesize: 10,
      tableData: [],
      search: '',
      delVisible: false,
      isLoading: false,
      deleteName: ''
    }
  },
  mounted () {
    this.getTestTaskInfo()
  },
  methods: {
    getTestTaskInfo () {
      getTestTask().then(
        JSON => {
          this.tableData = []
          const detail = JSON.data
          this.tableData = detail.data
        }
      )
    },
    handleSizeChange (size) {
      this.pagesize = size
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    handleDetail (taskName) {
      this.$router.push({path: '/preTaskDetail', query: { taskName: taskName }})
    },
    closeDel () {
      this.delVisible = false
    },
    handleDelete (taskName) {
      this.delVisible = true
      this.deleteName = taskName
    },
    showMessage (parms) {
      this.$message({
        message: parms.message,
        type: parms.type
      })
    },
    handleDownload (row) {
      const fileUrl = `http://127.0.0.1:8081/report/${row.taskName}.pdf`
      const link = document.createElement('a')
      link.href = fileUrl
      link.style.display = 'none'
      link.click()
    },
    confirmDelete () {
      this.isLoading = true
      deleteTestTask({ 'taskName': this.deleteName }).then(
        JSON => {
          if (JSON.data.data) {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Task deleted successfully', type: 'success' })
            this.getTaskInfo()
          } else {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Failed to delete task', type: 'error' })
          }
        }
      )
    }
  }
}
</script>
<style scoped>
.title {
  font-family: sans-serif;
  font-size: 25px;
  font-weight: bold;
  text-align: left;
  margin-bottom: 20px;
}
.split-page {
  text-align: center;
  margin-top: 20px;
}
</style>
