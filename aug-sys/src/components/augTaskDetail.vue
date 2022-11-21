<template>
  <div>
    <div class="title">Task Detail</div>
    <div class = "task-detail">
      <el-form label-width="300px" size="mini">
        <el-form-item label="Task Name:" class="detail">
          <span class="task-info">{{taskName}}</span>
        </el-form-item>
        <el-form-item label="Task Description:" class="detail">
          <span>{{taskDesc}}</span>
        </el-form-item>
        <el-form-item label="Data Set:" class="detail">
          <span>{{dataset}}</span>
        </el-form-item>
        <el-form-item label="Augmentation type:" class="detail">
          <span>{{type}}</span>
        </el-form-item>
        <el-form-item label="Augmentation Times:" class="detail">
          <span>{{times}}</span>
        </el-form-item>
        <el-form-item label="Augmentation Methods:" class="detail">
          <span>{{strMethod}}</span>
        </el-form-item>
        <template v-if="type === 'DeepTest'">
          <template>

          </template>
        </template>
        <template v-else>
        </template>
      </el-form>
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
      strMethod: ''
    }
  },
  mounted () {
    this.getAugDetailInfo()
  },
  methods: {
    getAugDetailInfo () {
      getAugDetail({'taskName': this.$route.query.taskName, 'type': this.$route.query.type}).then(
        JSON => {
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
.task-info {
  font-size: 17px;
}
</style>
<style>
.task-detail .detail .el-form-item__label {
  font-size: 17px;
}
</style>
