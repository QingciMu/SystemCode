<template>
  <div class="task-body">
    <div class="title">Create Test Task</div>
    <div class="split"></div>
    <div class="task-process">
      <el-steps :active="active" align-center finish-status="success">
        <el-step title="Step1" description="">
        </el-step>
        <el-step title="Step2" description=""></el-step>
        <el-step title="Step3" description=""></el-step>
      </el-steps>
    </div>
    <div class="test-task">
      <el-form :model="taskData" ref="taskData" label-width="40%">
        <template v-if="active === 0">
            <div class="step-title">Choose the Model and DataSet</div>
            <el-form-item label="Choose Model" prop="model" required>
              <el-select v-model="taskData.model" placeholder="Please Choose Model" class="select-form">
                <el-option v-for="item in modelOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Choose Test Case" prop="dataset" required>
              <el-select v-model="taskData.dataset" multiple placeholder="Please Choose Test Case" class="select-form">
                <el-option v-for="item in dataOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>
        </template>
      </el-form>
      <template v-if="active === 1">

      </template>
      <template v-if="active === 2">

      </template>
    </div>
  </div>
</template>

<script>
import { getDatasetDetail } from '../api/api'
export default {
  data () {
    return {
      active: 0,
      taskData: {
        model: '',
        dataset: []
      },
      modelOptions: [],
      dataOptions: []
    }
  },
  mounted () {
    this.getDataList()
  },
  methods: {
    getDataList () {
      getDatasetDetail().then(
        JSON => {
          const detail = JSON.data
          detail.data.forEach(i => {
            this.dataOptions.push(
              {
                value: i.fields.name,
                label: i.fields.name
              }
            )
          })
        }
      )
    }
  }
}
</script>
<style scoped>
.task-body {
}
.title {
  font-family: sans-serif;
  font-size: 25px;
  font-weight: bold;
  text-align: left;
}
.step-title {
  font-family: sans-serif;
  font-size: 20px;
  font-weight: bold;
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}
.split {
  height: 1px;
  background-color:black;
}
.task-process {
  margin-top: 20px;
}
.test-task {
  margin-top: 20px;
  margin-left: 5%;
  margin-right: 5%;
  min-height:400px;
  border: solid;
  border-radius: 10px;
  border-color: black;
}
.select-form {
    width: 300px;
}
</style>
