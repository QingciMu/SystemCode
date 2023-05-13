<template>
  <div style="display:flex">
    <el-button @click="back()" style="display:flex;margin-top: 5px; justify-content:center;align-items:center;width:10px;height:20px;padding-left: 12px;padding-right: 12px;"><i class="el-icon-back"></i></el-button>
    <div class="task-body">
      <div class="title">Test Report</div>
      <div class = "task-detail">
        <el-form label-width="300px" size="small">
          <el-form-item label="Task Name:" class="detail">
            <span class="task-info">{{taskName}}</span>
          </el-form-item>
          <el-form-item label="Task Description:" class="detail">
            <span class="task-info">{{taskDesc}}</span>
          </el-form-item>
          <el-form-item label="Data Set:" class="detail" >
            <span class="task-info">{{dataset}}</span>
          </el-form-item>
          <el-form-item label="Test Model:" class="detail">
            <span class="task-info">{{model}}</span>
          </el-form-item>
        </el-form>
        <!-- <div class="title1">Test Result</div> -->
          <div class="sub-title">Test Result</div>
          <el-form label-width="200px" >
            <el-form-item>
              <el-table :data="datasetInfo" style="width:100%" size="big">
                <el-table-column
                  prop="dataset"
                  label="Dataset"
                  width="180">
                </el-table-column>
                <el-table-column
                  prop="r1"
                  label="ϵ=0.05"
                  width="180">
                </el-table-column>
                <el-table-column
                  prop="r2"
                  label="ϵ=0.10"
                  width="180">
                </el-table-column>
                <el-table-column
                  prop="r3"
                  label="ϵ=0.15"
                  width="180">
                </el-table-column>
                <el-table-column
                  prop="r4"
                  label="ϵ=0.20"
                  width="180">
                </el-table-column>
              </el-table>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
</template>
<script>
import { getTestDetail } from '../api/api'
export default {
  name: 'augList',
  data () {
    return {
      taskName: this.$route.query.taskName,
      taskDesc: '',
      dataset: '',
      model: '',
      metricData: [],
      datasetInfo: []
    }
  },
  mounted () {
    this.getTestDetailInfo()
  },
  methods: {
    getTestDetailInfo () {
      getTestDetail({'taskName': this.$route.query.taskName}).then(
        JSON => {
          const dataInfo = JSON.data
          let {taskName, taskDesc, dataset, model} = dataInfo.data.taskInfo
          this.taskName = taskName
          this.taskDesc = taskDesc || '-'
          this.dataset = dataset
          this.model = model
          this.datasetInfo = dataInfo.data.datasetInfo
        }

      )
    },
    back () {
      this.$router.push({ path: '/preList' })
    }
  }
}

</script>
<style scoped>
.task-body {
  margin-left: 20px;
}
.title {
  display: flex;
  align-items: center;
  font-family: sans-serif;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
}

.title1 {
  display: flex;
  align-items: center;
  font-family: sans-serif;
  font-size: 15px;
  font-weight: bold;
  text-align: center;
}
.sub-title {
  display: flex;
  align-items: center;
  font-family: sans-serif;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}
.task-info {
  display: flex;
  flex-wrap: wrap;
  width: 800px;
  max-width: 800px;
  font-size: 17px;
}
.task-detail {
  margin-top: 20px;
}
</style>

<style>
.task-detail .detail .el-form-item__label {
  font-size: 17px;
}
</style>
