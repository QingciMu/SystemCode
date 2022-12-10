<template>
  <div>
    <div class="title">Create Test Task</div>
    <div class="split"></div>
    <div class="test-task">
      <el-steps :active="active" align-center finish-status="success">
        <el-step title="Step1" description="">
        </el-step>
        <el-step title="Step2" description=""></el-step>
        <el-step title="Step3" description=""></el-step>
      </el-steps>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      active: 0
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
.split {
  height: 1px;
  background-color:black;
}
.test-task {
  margin-top: 20px;
}
</style>
