<template>
  <div>
    <div style="display:flex; margin-bottom: 20px;">
      <div class="title">Instance List</div>
      <el-button type="primary" size="mini" @click="handleDownload()">Download</el-button>
    </div>
    <el-tabs v-model="activeName" type="border-card" style="min-height:700px">
      <el-tab-pane label="All Instance" name="first">
        <InstanceTable
        :tableData = 'tableData'>
        </InstanceTable>
      </el-tab-pane>
      <el-tab-pane label="Car Instance" name="second">
        <InstanceTable
        :tableData = 'carData'>
        </InstanceTable>
      </el-tab-pane>
      <el-tab-pane label="Person Instance" name="third">
        <InstanceTable
        :tableData = 'personData'>
        </InstanceTable>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
import { getInstance, downloadInstance } from '../api/api.js'
import InstanceTable from './instanceTable.vue'
export default {
  name: 'instanceList',
  components: {
    InstanceTable
  },
  data () {
    return {
      tableData: [],
      search: '',
      dataList: [],
      delVisible: false,
      index: 0,
      isLoading: false,
      activeName: 'first',
      carData: [],
      personData: []
    }
  },
  mounted () {
    this.getInstanceInfo()
  },
  methods: {
    showMessage (parms) {
      this.$message({
        message: parms.message,
        type: parms.type
      })
    },
    getInstanceInfo () {
      getInstance().then(
        JSON => {
          const detail = JSON.data
          this.tableData = detail.data
          this.carData = this.tableData.filter(i => i.type === 'Car')
          this.personData = this.tableData.filter(i => i.type === 'Person')
        }
      )
    },
    handleDownload () {
      downloadInstance().then(
        JSON => {
          const success = JSON.data.data
          if (success) {
            const fileUrl = `http://127.0.0.1:8081/InstancePool.zip`
            const link = document.createElement('a')
            link.href = fileUrl
            link.style.display = 'none'
            link.download = `InstancePool.zip`
            link.click()
          } else {
            this.showMessage({ message: JSON.data.msg, type: 'error' })
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
  margin-right: 30px;
}
.upload-demo {
  margin-bottom: 20px;
}
</style>
