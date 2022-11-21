<template>
  <div>
    <el-alert class="warnTip"
      title="If uploading a model with the same name will overwrite the original model, please upload with caution!"
      type="warning" show-icon>
    </el-alert>
    <div class="upload-button">
      <el-upload class="upload-demo" ref="SegUpload" action="http://127.0.0.1:8000/api/uploadSegModel" multiple
        :limit="1" :file-list="segList" :on-success="updateSegList">
        <el-button size="small" type="primary">Upload SegNet Model</el-button>
      </el-upload>
      <el-upload class="upload-demo" ref="HrUpload" action="http://127.0.0.1:8000/api/uploadHrModel" multiple :limit="1"
        :file-list="hrList" :on-change="updateHrList">
        <el-button size="small" type="success">Upload HRNet Model</el-button>
      </el-upload>
    </div>
    <div>
      <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
        border
        style="width: 100%"
        :default-sort ="{prop: 'id', order: 'ascending'}">
        <el-table-column fixed prop="id" label="Id" sortable width="150">
        </el-table-column>
        <el-table-column prop="name" label="Model Name" width="200">
        </el-table-column>
        <el-table-column prop="modelType" label="Model Type" width="150">
        </el-table-column>
        <el-table-column prop="uploadTime" label="Upload Time" sortable width="250">
        </el-table-column>
        <el-table-column align="right">
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" size="mini" placeholder="Please enter a keyword to search" />
          </template>
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
            <el-button size="mini" type="primary" @click="handleDownload(scope.row)">Download</el-button>
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
import { getModel, deleteModel } from '../api/api.js'
export default {
  name: 'deeptest',
  data () {
    return {
      tableData: [],
      search: '',
      segList: [],
      hrList: [],
      delVisible: false,
      index: 0,
      isLoading: false
    }
  },
  mounted () {
    this.getModelInfo()
  },
  methods: {
    getModelInfo () {
      getModel().then(
        JSON => {
          const detail = JSON.data
          this.tableData = detail.data
        }
      )
    },
    updateSegList () {
      this.$refs.SegUpload.clearFiles()
      this.getModelInfo()
    },
    updateHrList () {
      this.$refs.HrUpload.clearFiles()
      this.getModelInfo()
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
    confirmDelete () {
      this.isLoading = true
      deleteModel({ 'id': this.index }).then(
        JSON => {
          if (JSON.data.data) {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Model deleted successfully', type: 'success' })
            this.getModelInfo()
          } else {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Failed to delete model', type: 'error' })
          }
        }
      )
    },
    handelDetail (index, row) {

    },
    handleDownload (row) {
      const fileUrl = `http://127.0.0.1:8081/Model/${row.name}`
      const link = document.createElement('a')
      link.href = fileUrl
      link.style.display = 'none'
      link.download = `${row.name}`
      link.click()
    }
  }
}

</script>
<style scoped>
.upload-button {
  display: flex;
  margin-bottom: 20px;
}

.upload-demo {
  width: 200px;
  text-align: left;
}

.warnTip {
  margin-bottom: 10px;
}
</style>
<style>
.el-table .el-table__cell.is-right {
  text-align: left;
}
</style>
