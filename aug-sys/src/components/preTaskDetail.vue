<template>
  <div style="display:flex">
    <el-button @click="back()" style="display:flex;margin-top: 5px; justify-content:center;align-items:center;width:10px;height:20px;padding-left: 12px;padding-right: 12px;"><i class="el-icon-back"></i></el-button>
    <div class="task-body">
      <div class="title">Task Detail</div>
      <div class = "task-detail">
        <el-form label-width="300px" size="mini">
          <el-form-item label="Task Name:" class="detail">
            <span class="task-info">{{taskName}}</span>
          </el-form-item>
          <el-form-item label="Task Description:" class="detail">
            <span class="task-info">{{taskDesc}}</span>
          </el-form-item>
          <el-form-item label="Data Set:" class="detail">
            <span class="task-info">{{dataset}}</span>
          </el-form-item>
          <el-form-item label="Augmentation type:" class="detail">
            <span class="task-info">{{type}}</span>
          </el-form-item>
          <el-form-item label="Augmentation Times:" class="detail">
            <span class="task-info">{{times}}</span>
          </el-form-item>
          <el-form-item label="Augmentation Methods:" class="detail">
            <span class="task-info">{{strMethod}}</span>
          </el-form-item>
          <template v-if="type === 'DeepTest'">
            <template v-if="lstMethod.includes('translation')">
              <div class="method-title">Method Translation</div>
              <el-form-item label="Range of X-axis translation:" class="detail">
                <span class="task-info">{{tranXmin}}-{{tranXmax}}</span>
              </el-form-item>
              <el-form-item label="Range of Y-axis translation:" class="detail">
                <span class="task-info">{{tranYmin}}-{{tranYmax}}</span>
              </el-form-item>
            </template>
            <template v-if="lstMethod.includes('scale')">
              <div class="method-title">Method Scale</div>
              <el-form-item label="Range of X-axis scale:" class="detail">
                <span class="task-info">{{scaleXmin}}-{{scaleXmax}}</span>
              </el-form-item>
              <el-form-item label="Range of Y-axis scale:" class="detail">
                <span class="task-info">{{scaleYmin}}-{{scaleYmax}}</span>
              </el-form-item>
            </template>
            <template v-if="lstMethod.includes('rotation')">
              <div class="method-title">Method Rotation</div>
              <el-form-item label="Range of rotation degree:" class="detail">
                <span class="task-info">{{degreeMin}}-{{degreeMax}}</span>
              </el-form-item>
            </template>
            <template v-if="lstMethod.includes('brightness')">
              <div class="method-title">Method Brightness</div>
              <el-form-item label="Range of bias:" class="detail">
                <span class="task-info">{{biasMin}}-{{biasMax}}</span>
              </el-form-item>
            </template>
            <template v-if="lstMethod.includes('blur')">
              <div class="method-title">Method Blur</div>
              <el-form-item label="Strategy of blur:" class="detail">
                <span class="task-info">{{strategyContent}}</span>
              </el-form-item>
            </template>
          </template>
          <template v-else>
          </template>
        </el-form>
      </div>
    </div>
  </div>
</template>
<script>
import { getAugDetail } from '../api/api'
export default {
  name: 'augList',
  data () {
    return {
      taskName: this.$route.query.taskName,
      type: this.$route.query.type,
      taskDesc: '',
      dataset: '',
      times: null,
      lstMethod: [],
      strMethod: '',
      tranXmin: null,
      tranXmax: null,
      tranYmin: null,
      tranYmax: null,
      scaleXmin: null,
      scaleXmax: null,
      scaleYmin: null,
      scaleYmax: null,
      degreeMin: null,
      degreeMax: null,
      biasMin: null,
      biasMax: null,
      strategy: [],
      strategyContent: ''
    }
  },
  mounted () {
    this.getAugDetailInfo()
  },
  watch: {
    strategy: function (newStrategy, oldStrategy) {
      this.strategyContent = ''
      for (let i = 0; i < newStrategy.length; i++) {
        if (i !== 0) {
          this.strategyContent += '、'
          this.strategyContent += newStrategy[i]
        } else {
          this.strategyContent += newStrategy[i]
        }
      }
    }
  },
  methods: {
    getAugDetailInfo () {
      getAugDetail({'taskName': this.$route.query.taskName, 'type': this.$route.query.type}).then(
        JSON => {
          const dataInfo = JSON.data
          let {taskName, taskDesc, dataset, type, times, lstMethod} = dataInfo.data.taskInfo
          this.taskName = taskName
          this.taskDesc = taskDesc || '-'
          this.dataset = dataset
          this.type = type
          this.times = times
          this.lstMethod = lstMethod
          for (let i = 0; i < lstMethod.length; i++) {
            if (i !== lstMethod.length - 1) {
              this.strMethod += lstMethod[i]
              this.strMethod += '、'
            } else {
              this.strMethod += lstMethod[i]
            }
          }
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
.task-info {
  display: flex;
  flex-wrap: wrap;
  width: 400px;
  max-width: 400px;
  font-size: 17px;
}
.method-title {
  font-family: sans-serif;
  font-size: 20px;
  font-weight: bold;
  text-align: left;
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
