<template>
  <div>
    <div class="title">Test Case Augmentation Use SegTest</div>
    <div class="split"></div>
    <div class="task-form">
      <el-form :model="ruleForm" ref="ruleForm" label-width="300px" class="demo-ruleForm">
        <el-form-item label="Choose Raw Data Set" prop="dataset" required>
          <el-select v-model="ruleForm.dataset" placeholder="Please Choose Data Set" class="select-form">
            <el-option v-for="item in DataOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Task Name" prop="taskName" required>
          <el-input placeholder="Please Input Task Name" v-model="ruleForm.taskName" class="task-name">
          </el-input>
        </el-form-item>
        <el-form-item label="Task Description" prop="taskDesc">
          <el-input type="textarea" autosize placeholder="Please Input Task Description" v-model="ruleForm.taskDesc" class="task-name">
          </el-input>
        </el-form-item>
        <el-form-item label="Select times of augmentation" prop="fold" required>
          <el-select v-model="ruleForm.fold" placeholder="Please Select times" class="select-form">
            <el-option v-for="item in foldOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Choose Instances" prop="instances" required>
          <el-cascader v-model="ruleForm.instances" :props="{multiple: true}" :options="instanceOptions" :show-all-levels="true" placeholder="Please Choose Instances" class="select-form">
          </el-cascader>
        </el-form-item>
        <el-form-item label="Choose augment methods" prop="methods" required>
          <el-select v-model="ruleForm.methods" multiple placeholder="Please Choose Methods" class="select-form">
            <el-option v-for="item in methodOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" :loading="isLoading" @click="submitForm('ruleForm')">Start Task</el-button>
          <el-button @click="resetForm('ruleForm')">Reset</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { getDatasetDetail, segTask, showMessage, getInstanceList } from '../api/api.js'
export default {
  name: 'segtest',
  data () {
    return {
      isLoading: false,
      ruleForm: {
        dataset: '',
        taskName: '',
        taskDesc: '',
        fold: null,
        instances: [],
        methods: []
      },
      DataOptions: [],
      foldOptions: [
        {
          value: 1,
          label: 1
        },
        {
          value: 2,
          label: 2
        },
        {
          value: 3,
          label: 3
        },
        {
          value: 4,
          label: 4
        },
        {
          value: 5,
          label: 5
        }
      ],
      instanceOptions: [
        {
          value: 'Car',
          label: 'Car',
          children: []
        },
        {
          value: 'Person',
          label: 'Person',
          children: []
        }
      ],
      methodOptions: [
        {
          value: 'Random',
          label: 'Random'
        },
        {
          value: 'Random Instance',
          label: 'Random Instance'
        },
        {
          value: 'Random Insertion',
          label: 'Random Insertion'
        },
        {
          value: 'SegTest',
          label: 'SegTest'
        }
      ]
    }
  },
  mounted () {
    this.getDataList()
    this.getInstanceDetail()
  },
  methods: {
    jumpSuccess () {
      this.$router.push({path: '/success', query: {type: 'SegTest'}})
    },
    getDataList () {
      getDatasetDetail().then(
        JSON => {
          const detail = JSON.data
          this.DataOptions = []
          detail.data.forEach(i => {
            this.DataOptions.push(
              {
                value: i.fields.name,
                label: i.fields.name
              }
            )
          })
        }
      )
    },
    getInstanceDetail () {
      this.instanceOptions.forEach(i => {
        i.children = []
      })
      getInstanceList().then(
        JSON => {
          this.instanceOptions[0].children = JSON.data.data.car
          this.instanceOptions[1].children = JSON.data.data.person
        }
      )
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.isLoading = true
          segTask(this.ruleForm).then(
            JSON => {
              if (JSON.data.data) {
                this.isLoading = false
                this.jumpSuccess()
              } else {
                this.isLoading = false
                showMessage({ message: JSON.data.msg, type: 'error' })
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
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
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
.method-title {
  font-family: sans-serif;
  font-size: 20px;
  font-weight: bold;
  text-align: left;
}
.task-form {
  margin-top: 20px;
}
.select-form {
    width: 300px;
}
.task-name {
  width: 300px;
}
.split {
  height: 1px;
  background-color:black;
}
.select-num {
  width: 120px;
}
</style>
