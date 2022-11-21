<template>
  <div>
    <div class="title">Upload Data Set</div>
    <div>
      <el-upload class="upload-demo" ref="datasetUpload" action="http://127.0.0.1:8000/api/uploadDataset" multiple
        :limit="1" :file-list="dataList" :on-success="updateDataset">
        <el-button size="small" type="primary">Upload Data Set</el-button>
      </el-upload>
      <div class="title">Data Set List</div>
      <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
          border style="width: 100%">
        <el-table-column fixed prop="id" label="id" width="150">
        </el-table-column>
        <el-table-column prop="name" label="Data Set" width="200">
        </el-table-column>
        <el-table-column prop="num" label="Test Case Num" width="200">
        </el-table-column>
        <el-table-column prop="uploadTime" label="Upload Time" width="200">
        </el-table-column>
        <el-table-column fixed="right">
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" size="mini" placeholder="Please enter a keyword to search" />
          </template>
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
              <el-button
              size="mini"
              type="primary"
              @click="handleDownload(scope.row)">Download</el-button>
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
import { getDatasetDetail, deleteDataset } from '../api/api.js'
export default {
  name: 'deeptest',
  data () {
    return {
      tableData: [],
      search: '',
      dataList: [],
      delVisible: false,
      index: 0,
      isLoading: false
    }
  },
  mounted () {
    this.getDatasetInfo()
  },
  methods: {
    getDatasetInfo () {
      getDatasetDetail().then(
        JSON => {
          const detail = JSON.data
          detail.data.forEach(i => {
            this.tableData.push({
              id: i.pk,
              name: i.fields.name,
              num: i.fields.num,
              uploadTime: i.fields.uploadTime
            })
          })
        }
      )
    },
    updateDataset () {
      this.$refs.datasetUpload.clearFiles()
      this.getDatasetInfo()
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
      const fileUrl = `http://127.0.0.1:8081/Dataset/${row.name}.zip`
      const link = document.createElement('a')
      link.href = fileUrl
      link.style.display = 'none'
      link.download = `${row.name}.zip`
      link.click()
    },
    confirmDelete () {
      this.isLoading = true
      deleteDataset({ 'id': this.index }).then(
        JSON => {
          if (JSON.data.data) {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Data Set deleted successfully', type: 'success' })
            this.getDatasetInfo()
          } else {
            this.isLoading = false
            this.closeDel()
            this.showMessage({ message: 'Failed to delete data set', type: 'error' })
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
.upload-demo {
  margin-bottom: 20px;
}
</style>
