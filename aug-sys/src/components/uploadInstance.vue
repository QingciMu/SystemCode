<template>
  <div>
    <el-tabs v-model="activeName" type="border-card" style="min-height:700px;text-align: center; margin-top: 10%;">
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
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">1.上传单个实例，只能上传jpg/png文件</div>
          <div class="el-upload__tip" slot="tip">2.上传多个实例，请上传Zip压缩文件</div>
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
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">1.上传单个实例，只能上传jpg/png文件</div>
          <div class="el-upload__tip" slot="tip">2.上传多个实例，请上传Zip压缩文件</div>
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
