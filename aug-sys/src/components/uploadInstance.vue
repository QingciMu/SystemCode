<template>
  <div>
    <el-tabs v-model="activeName" type="border-card" style="min-height: 650px;text-align: center; margin-top: 2%;">
      <el-tab-pane label="Upload Car Instance" name="Car">
        <el-upload
          class="upload-demo"
          drag
          ref="CarUpload"
          action="http://127.0.0.1:8000/api/uploadCar"
          multiple
          :limit="1"
          :file-list="carList"
          :on-success="updateCar">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Drag file to here, or <em>click here</em></div>
          <div class="el-upload__tip" slot="tip">1.Upload only one instance, please upload png</div>
          <div class="el-upload__tip" slot="tip">2.Upload many instances,please upload zip file</div>
        </el-upload>
      </el-tab-pane>
      <el-tab-pane label="Upload Person Instance" name="Person">
        <el-upload
          class="upload-demo"
          drag
          ref="PersonUpload"
          action="http://127.0.0.1:8000/api/uploadPerson"
          multiple
          :limit="1"
          :file-list="personList"
          :on-success="updatePerson">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Drag file to here, or <em>click here</em></div>
          <div class="el-upload__tip" slot="tip">1.Upload only one instance, please upload png</div>
          <div class="el-upload__tip" slot="tip">2.Upload many instances,please upload zip file</div>
        </el-upload>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
export default {
  name: 'instanceUpload',
  data () {
    return {
      activeName: 'Car',
      carList: [],
      personList: []
    }
  },
  methods: {
    showMessage (parms) {
      this.$message({
        message: parms.message,
        type: parms.type
      })
    },
    jumpSuccess () {
      this.$router.push({ path: '/uploadSuccess' })
    },
    updateCar () {
      this.$refs.CarUpload.clearFiles()
      this.jumpSuccess()
    },
    updatePerson () {
      this.$refs.PersonUpload.clearFiles()
      this.jumpSuccess()
    }
  }
}

</script>
<style scoped>
.upload-demo {
  margin-top: 10%;

}
</style>
