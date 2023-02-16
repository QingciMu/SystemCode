<template>
  <div>
    <div class="image">
      <img src="../assets/success.png" height="200" width="200">
    </div>
    <div class="success-btn">
      <el-button @click="jumpList()">Go Task List</el-button>
      <el-button type="primary" @click="jumpTask()">Create New Task</el-button>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    jumpList () {
      this.$router.push({path: '/preList'})
    },
    jumpTask (type) {
      this.$router.push({path: '/testTask'})
    }
  }
}
</script>
<style scoped>
.image {
  text-align: center;
  padding-top: 5%;
}
.success-btn {
  text-align: center;
  margin-top: 20px;
}
</style>
