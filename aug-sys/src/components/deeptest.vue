<template>
  <div>
    <div class="title">Test Case Augmentation Use Deeptest</div>
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
        <el-form-item label="Choose augment methods" prop="methods" required>
          <el-select v-model="ruleForm.methods" multiple placeholder="Please Choose Methods" class="select-form">
            <el-option v-for="item in methodOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <template v-if="ruleForm.methods.includes('translation')">
          <div class="method-title">Method Translation</div>
          <el-form-item label="Select the range of X-axis translation" required>
            <div style="display:flex;width:300px;justify-content: space-between;align-items: center;">
              <el-input-number
                class="select-num"
                v-model="ruleForm.trans_x.min"
                size="small"
                :min="10"
                :max="100"/>
              <div>-</div>
              <el-input-number
                class="select-num"
                v-model="ruleForm.trans_x.max"
                size="small"
                :min="10"
                :max="100"/>
            </div>
          </el-form-item>
          <el-form-item label="Select the range of Y-axis translation" required>
            <div style="display:flex;width:300px;justify-content: space-between;align-items: center;">
              <el-input-number
                class="select-num"
                v-model="ruleForm.trans_y.min"
                size="small"
                :min="10"
                :max="100"/>
              <div>-</div>
              <el-input-number
                class="select-num"
                v-model="ruleForm.trans_y.max"
                size="small"
                :min="10"
                :max="100"/>
            </div>
          </el-form-item>
        </template>
        <template v-if="ruleForm.methods.includes('scale')">
          <div class="method-title">Method Scale</div>
          <el-form-item label="Select the range of X-axis scale" required>
            <div style="display:flex;width:300px;justify-content: space-between;align-items: center;">
              <el-input-number
                class="select-num"
                v-model="ruleForm.scale_x.min"
                size="small"
                :min="2"
                :max="6"/>
              <div>-</div>
              <el-input-number
                class="select-num"
                v-model="ruleForm.scale_x.max"
                size="small"
                :min="2"
                :max="6"/>
            </div>
          </el-form-item>
          <el-form-item label="Select the range of Y-axis scale" required>
            <div style="display:flex;width:300px;justify-content: space-between;align-items: center;">
              <el-input-number
                class="select-num"
                v-model="ruleForm.scale_y.min"
                size="small"
                :min="2"
                :max="6"/>
              <div>-</div>
              <el-input-number
                class="select-num"
                v-model="ruleForm.scale_y.max"
                size="small"
                :min="2"
                :max="6"/>
            </div>
          </el-form-item>
        </template>
        <!--
        <template v-if="ruleForm.methods.includes('shear')">
          <div class="method-title">Method Shear</div>
          <el-form-item label="Choose augment methods" prop="methods">
          <el-select v-model="ruleForm.methods" multiple placeholder="Please Choose Methods" class="select-form">
            <el-option v-for="item in methodOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        </template>
        <template v-if="ruleForm.methods.includes('contrast')">
          <div class="method-title">Method Contrast</div>
          <el-form-item label="Choose augment methods" prop="methods">
          <el-select v-model="ruleForm.methods" multiple placeholder="Please Choose Methods" class="select-form">
            <el-option v-for="item in methodOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        </template>
        -->
        <template v-if="ruleForm.methods.includes('rotation')">
          <div class="method-title">Method Rotation</div>
          <el-form-item label="Select the range of rotation degree" prop="degree" required>
            <div style="display:flex;width:300px;justify-content: space-between;align-items: center;">
              <el-input-number
                class="select-num"
                v-model="ruleForm.degree.min"
                size="small"
                :min="3"
                :max="30"/>
              <div>-</div>
              <el-input-number
                class="select-num"
                v-model="ruleForm.degree.max"
                size="small"
                :min="3"
                :max="30"/>
            </div>
          </el-form-item>
        </template>
        <template v-if="ruleForm.methods.includes('brightness')">
          <div class="method-title">Method Brightness</div>
          <el-form-item label="Select the range of bias" prop="bias" required>
            <div style="display:flex;width:300px;justify-content: space-between;align-items: center;">
              <el-input-number
                class="select-num"
                v-model="ruleForm.bias.min"
                size="small"
                :min="10"
                :max="100"/>
              <div>-</div>
              <el-input-number
                class="select-num"
                v-model="ruleForm.bias.max"
                size="small"
                :min="10"
                :max="100"/>
            </div>
          </el-form-item>
        </template>
        <template v-if="ruleForm.methods.includes('blur')">
          <div class="method-title">Method Blur</div>
          <el-form-item label="Choose blur strategy" prop="strategy" required>
          <el-select v-model="ruleForm.strategy" multiple placeholder="Please Choose Strategy" class="select-form">
            <el-option v-for="item in strategyOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        </template>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">Start Task</el-button>
          <el-button @click="resetForm('ruleForm')">Reset</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { getDatasetDetail, deepTask } from '../api/api.js'
export default {
  name: 'deeptest',
  data () {
    return {
      ruleForm: {
        dataset: '',
        taskName: '',
        taskDesc: '',
        fold: null,
        methods: [],
        trans_x: {
          min: 10,
          max: 100
        },
        trans_y: {
          min: 10,
          max: 100
        },
        scale_x: {
          min: 2,
          max: 6
        },
        scale_y: {
          min: 2,
          max: 6
        },
        degree: {
          min: 3,
          max: 30
        },
        bias: {
          min: 10,
          max: 100
        },
        strategy: []
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
      methodOptions: [
        {
          value: 'translation',
          label: 'translation'
        },
        {
          value: 'scale',
          label: 'scale'
        },
        {
          value: 'shear',
          label: 'shear'
        },
        {
          value: 'contrast',
          label: 'contrast'
        },
        {
          value: 'rotation',
          label: 'rotation'
        },
        {
          value: 'brightness',
          label: 'brightness'
        },
        {
          value: 'blur',
          label: 'blur'
        }
      ],
      strategyOptions: [
        {
          value: 'Averaging',
          label: 'Averaging'
        },
        {
          value: 'Gaussian',
          label: 'Gaussian'
        },
        {
          value: 'Median',
          label: 'Median'
        },
        {
          value: 'Bilateral Filter',
          label: 'Bilateral Filter'
        }
      ]
    }
  },
  mounted () {
    this.getDataList(this.ruleForm)
  },
  methods: {
    jumpList () {
      this.$router.push({path: '/dataset'})
    },
    getDataList () {
      getDatasetDetail().then(
        JSON => {
          const detail = JSON.data
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
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          deepTask(this.ruleForm)
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
