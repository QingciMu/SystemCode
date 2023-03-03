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
      <div class="step-title">{{title}}</div>
      <div class="form-content">
        <template v-if="active === 0">
          <el-form :model="basic" ref="basic" label-width="45%">
            <el-form-item label="Task Name" prop="taskName" required>
              <el-input v-model="basic.taskName" clearable placeholder="Please input task name" class="select-form">
              </el-input>
            </el-form-item>
            <el-form-item label="Task Description" prop="taskDesc">
              <el-input v-model="basic.taskDesc" type="textarea" clearable placeholder="Please input task descriptionx" class="select-form">
              </el-input>
            </el-form-item>
          </el-form>
        </template>
        <template v-if="active === 1">
          <el-form :model="datas" ref="datas" label-width="45%">
            <el-form-item label="Choose Model" prop="model" required>
              <el-select v-model="datas.model" placeholder="Please Choose Model" class="select-form">
                <el-option v-for="item in modelOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Choose Test Case" prop="testCase" required>
              <el-cascader v-model="datas.testCase" :props="{multiple: true}" :options="testCaseOptions" :show-all-levels="true" placeholder="Please Choose Test Case" class="select-form">
              </el-cascader>
            </el-form-item>
          </el-form>
        </template>
        <template v-if="active === 2">
          <el-form :model="metrics" ref="metrics" label-width="45%">
            <el-form-item label="IOU:" prop="UseIOU" required>
              <el-radio-group v-model="metrics.UseIOU">
                <el-radio :label=1>Yes</el-radio>
                <el-radio :label=0>No</el-radio>
              </el-radio-group>
            </el-form-item>
            <template v-if="metrics.UseIOU === 1">
              <el-form-item label="IOU threshold:" prop="IOU">
                <el-input-number v-model="metrics.IOU"
                  size="small"
                  :precision="2"
                  :step="0.1"
                  :min="0"
                  :max="1">
                </el-input-number>
              </el-form-item>
            </template>
            <el-form-item label="OSE:" prop="UseOSE" required>
              <el-radio-group v-model="metrics.UseOSE">
                <el-radio :label=1>Yes</el-radio>
                <el-radio :label=0>No</el-radio>
              </el-radio-group>
            </el-form-item>
            <template v-if="metrics.UseOSE === 1">
              <el-form-item label="OSE threshold:" prop="OSE">
                <el-input-number v-model="metrics.IOU"
                  size="small"
                  :precision="2"
                  :step="0.1"
                  :min="0"
                  :max="1">
                </el-input-number>
              </el-form-item>
            </template>
            <el-form-item label="USE:" prop="UseUSE" required>
              <el-radio-group v-model="metrics.UseUSE">
                <el-radio :label=1>Yes</el-radio>
                <el-radio :label=0>No</el-radio>
              </el-radio-group>
            </el-form-item>
            <template v-if="metrics.UseUSE === 1">
              <el-form-item label="USE threshold:" prop="USE">
                <el-input-number v-model="metrics.USE"
                  size="small"
                  :precision="2"
                  :step="0.1"
                  :min="0"
                  :max="1">
                </el-input-number>
              </el-form-item>
            </template>
          </el-form>
        </template>
      </div>
      <div class="form-button">
        <el-form style="text-align:right">
          <el-form-item>
            <el-button v-show="active !== 0" @click="previous()">Previous</el-button>
            <el-button v-show="active !== 2" @click="nextStep()">Next</el-button>
            <el-button v-show="active === 2" type="primary" :loading="isLoading" @click="submit('metrics')">Submit</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import { getTestCase, getModel, startTest, showMessage } from '../api/api'
export default {
  data () {
    return {
      isLoading: false,
      titleLst: ['Basic Task Information', 'Set the Model and DataSet', 'Set the Evaluation Metrics'],
      title: 'Basic Task Information',
      active: 0,
      basic: {
        taskName: '',
        taskDesc: ''
      },
      datas: {
        model: '',
        testCase: []
      },
      metrics: {
        UseIOU: 1,
        UseUSE: 1,
        UseOSE: 1,
        IOU: 0.5,
        USE: 0.5,
        OSE: 0.5
      },
      modelOptions: [],
      testCaseOptions: [
        {
          value: 'DataSet',
          label: 'DataSet',
          children: []
        },
        {
          value: 'AugResult',
          label: 'AugResult',
          children: []
        }
      ],
      formName: ['basic', 'datas', 'metrics'],
      formData: {}
    }
  },
  mounted () {
    this.getAllTest()
    this.getAllModel()
  },
  methods: {
    jumpSuccess () {
      this.$router.push({path: '/testSuccess'})
    },
    getAllModel () {
      getModel().then(
        JSON => {
          this.modelOptions = []
          const lst = JSON.data.data
          lst.forEach(i => {
            this.modelOptions.push(
              {
                value: i.name,
                label: i.name
              }
            )
          })
        }
      )
    },
    getAllTest () {
      getTestCase().then(
        JSON => {
          const detail = JSON.data.data
          this.testCaseOptions[0].children = detail.dataSet
          this.testCaseOptions[1].children = detail.augResult
        }
      )
    },
    validateForm (formName) {
      this.$refs[formName].validate(validate => {
        if (validate) {
          this.next()
        }
      })
    },
    noValidateForm (formName) {
      this.$refs[formName].clearValidate()
    },
    previous () {
      this.noValidateForm(this.formName[this.active])
      this.active -= 1
      this.title = this.titleLst[this.active]
    },
    next () {
      this.active += 1
      this.title = this.titleLst[this.active]
    },
    nextStep () {
      this.validateForm(this.formName[this.active])
    },
    submit (formName) {
      this.$refs[formName].validate(validate => {
        if (validate) {
          const formData = Object.assign(this.basic, this.datas, this.metrics)
          this.isLoading = true
          startTest(formData).then(
            JSON => {
              if (JSON.data.data) {
                this.isLoading = false
                this.jumpSuccess()
              }
            }
          ).catch(e => {
            this.isLoading = false
            showMessage({ message: e.msg, type: 'error' })
          })
        } else {
          return false
        }
      })
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
  min-height:500px;
  max-height: 80%;
  border: solid;
  border-radius: 10px;
  border-color: black;
}
.select-form {
    width: 300px;
}
.form-content {
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.form-button {
  margin-top: 20px;
  margin-right: 10%;
  text-align: right;
}
</style>
