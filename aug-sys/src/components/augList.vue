<template>
  <div>
    <div class="title">Augmentation Task List</div>
    <div>
      <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
          border style="width: 100%">
        <el-table-column fixed prop="taskName" label="Task Name" width="220">
        </el-table-column>
        <el-table-column prop="fileType" label="File Type" width="100">
        </el-table-column>
        <el-table-column prop="fileNum" label="File Num" width="120">
        </el-table-column>
        <el-table-column prop="Method" label="Method" width="120">
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
        <el-table-column fixed="right">
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" size="mini" placeholder="Enter a keyword to search" />
          </template>
          <template slot-scope="scope">
            <template v-if="scope.row.Status === 'Success'">
              <el-button
                size="mini"
                @click="handleDetail(scope.row.taskName, scope.row.Method)">Detail</el-button>
              <el-button
                size="mini"
                type="primary"
                @click="handleDownload(scope.row)">Download</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
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
  </div>
</template>
<script>
import { getTask, deleteTask } from '../api/api.js'
export default {
  name: 'augList',
  data () {
    return {
      tableData: [],
      search: '',
      delVisible: false,
      index: 0,
      isLoading: false
    }
  },
  mounted () {
    this.getTaskInfo()
  },
  methods: {
    getTaskInfo () {
      getTask().then(
        JSON => {
          const detail = JSON.data
          this.tableData = detail.data
        }
      )
    },
    handleDetail (taskName, type) {
      this.$router.push({path: '/augTaskDetail', query: {taskName: taskName, type: type}})
    },
    closeDel () {
      this.delVisible = false
    },
    handleDelete (index, row) {
      this.delVisible = true
      this.index = index + 1
    },
    showMessage (parms) {
      this.$message({
        message: parms.message,
        type: parms.type
      })
    },
    handleDownload (row) {
      const fileUrl = `http://127.0.0.1:8081/AugResult/${row.name}.zip`
      const link = document.createElement('a')
      link.href = fileUrl
      link.style.display = 'none'
      link.download = `${row.name}.zip`
      link.click()
    },
    confirmDelete () {
      this.isLoading = true
      deleteTask({ 'id': this.index }).then(
        JSON => {
          if (JSON.data.data) {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Task deleted successfully', type: 'success' })
            this.getDatasetInfo()
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
</style>
