<template>
  <el-form ref="newform" :model="newform" :rules="rules">
    <el-form-item label="" prop="expvmInstruction">
      <el-upload
        class="upload-demo"
        drag
        ref="uploadhtml"
        :action="upload_url"
        :auto-upload="false"
        :before-upload="newHtml"
        accept=".html, .htm">
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div slot="tip" class="el-upload__tip">实验信息上传，只能传(.html/.htm)文件</div>
      </el-upload>
    </el-form-item>
    <el-form-item style="text-align:center">
      <el-button type="primary" @click="newSubmitForm()" class="yes-btn">
        确 定
      </el-button>
      <el-button @click="resetForm('newform')">
        重 置
      </el-button>
    </el-form-item>
  </el-form>
</template>>
<script>
export default {
  data () {
    return {
      upload_url: 'aaa',
      uploadForm: new FormData(),
      rules: {},
      newform: {
        expName: '',
        groupName: '',
        expSn: '',
        subGroupName: '',
        expvmDifficulty: 1
      }
    }
  },
  methods: {
    newSubmitForm () {
      this.$refs['newform'].validate((valid) => {
        if (valid) {
          this.uploadForm.append('expName', this.newform.expName)
          this.uploadForm.append('expSn', this.newform.expSn)
          this.uploadForm.append('groupId', this.newgroupId)
          this.uploadForm.append('subGroupId', this.newsubgroupId)
          this.uploadForm.append('expvmDifficulty', this.newform.expvmDifficulty)

          // eslint-disable-next-line no-undef
          newExp(this.uploadForm).then(res => {
            if (res.code === 400) {
              this.$message.error(res.error)
            } else if (res.code === 200) {
              this.$message.success('上传成功！')
            }
          })
          this.$refs.uploadhtml.submit()
          this.$refs.uploadfile.submit()
          this.$refs.uploadvideo.submit()
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    newHtml (file) {
      this.uploadForm.append('html', file)
      return false
    },
    newFiles (file) {
      this.uploadForm.append('file[]', file)
      return false
    },
    newVideo (file) {
      this.uploadForm.append('video', file)
      return false
    }
  }
}
</script>
