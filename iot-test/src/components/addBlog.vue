<template>
  <div>
    <el-form  label-width="80px">
      <el-form-item label="标题" >
        <el-input v-model="remark"></el-input>
      </el-form-item>
      <el-form-item label="APP版本">
        <el-upload
          class="upload-demo"
          drag
          ref="newupload"
          :action="upload_url"
          :auto-upload="false"
          :before-upload="beforeUpload"
          accept=".apk">
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div slot="tip" class="el-upload__tip">只能传(.apk)文件</div>
        </el-upload>
      </el-form-item>
      <el-form-item label="操作人">
        <el-input v-model="username"></el-input>
      </el-form-item>
      <el-form-item>
        <!--        <el-button size="mid" @click="addApk">+添加版本</el-button>-->
        <el-button size="mid" type="primary" @click="newSubmitForm()">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      upload_url: 'updemo',
      remark: '',
      email: '',
      username: '',
      file: null
    }
  },
  methods: {
    beforeUpload (file) {
      let fd = new FormData()
      fd.append('file', file)
      fd.append('remark', this.remark)
      fd.append('username', this.username)
      console.log(fd)
      axios.post('http://localhost:5000/upload', fd).then(result => {
        // eslint-disable-next-line eqeqeq
        if (String(result.data.code) === '0000') {
          this.$message.success('上传成功')
        } else {
          this.$message.error('上传失败，请重新上传')
        }
      })
    },
    newSubmitForm () {
      this.$refs.newupload.submit()
    }
  }
}
</script>
