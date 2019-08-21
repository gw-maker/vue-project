<template>
  <div>
    <!--搜索框-->
    <el-row>
        <el-col :span="3" class="grid">
        <el-input type="text" v-model="input1" placeholder="请输入渠道" size="mini"></el-input>
      </el-col>
      <el-col :span="3" class="grid">
        <el-input type="text" v-model="input2" placeholder="请输入版本" size="mini"></el-input>
      </el-col>
      <el-col :span="1" class="grid">
        <el-button type="success" icon="el-icon-search" size="mini" @click.prevent="listBlog()">搜索</el-button>
      </el-col>
    </el-row>
    <br>
    <!--表格数据及操作-->
    <!-- 加载设置 -->
    <el-table
      element-loading-text="拼命加载中"
      element-loading-spinner="el-icon-loading"
      element-loading-background="rgba(0, 0, 0, 0.8)"
      fit
      :data="tableData" border style="width: 100%" ref="multipleTable" tooltip-effect="dark"  @selection-change="handleSelectionChange">
      <!--勾选框-->
      <!-- <el-table-column type="selection" width="55"></el-table-column> -->
      <!--索引-->
      <!-- <el-table-column type="index" :index="indexMethod"></el-table-column> -->
      <el-table-column type="selection" width="100"></el-table-column>
      <el-table-column prop="apk_name" label="名称" sortable></el-table-column>
      <el-table-column prop="remark" label="标题"></el-table-column>
      <el-table-column prop="channel" label="渠道"></el-table-column>
      <el-table-column prop="apk_version" label="APP版本"></el-table-column>
      <el-table-column prop="create_time" label="日期" :formatter="dateFormat" sortable></el-table-column>
      <el-table-column prop="username" label="操作人"></el-table-column>
      <!--            <el-table-column prop="tag" label="显隐" ></el-table-column>-->
      <el-table-column width="150px" label="操作">
        <template slot-scope="scope">
          <el-button type="danger" icon="el-icon-delete" size="mini"
                         @click.prevent="deleteBlog(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="page.totalCount"
      :page-size="page.pageSize"
      :current-page="page.currentPage"
      @current-change="handleCurrentChange"
      style="float:right;margin:10px 20px 0 0;">
    </el-pagination>
    <!--新增按钮-->
    <el-col :span="5" class="grid">
      <el-button type="primary" icon="el-icon-edit" size="mini" round
                      @click="speedupCheckbox">升级</el-button>
      <router-link to="/addBlog">
        <el-button type="success" icon="el-icon-circle-plus-outline" size="mini" round>新增</el-button>
      </router-link>
    </el-col>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  created () {
    this.listBlog()
  },
  data () {
    return {
      // 查询输入框数据
      tableData: [],
      input1: '',
      input2: '',
      multipleSelection: [],
      page: {
        currentPage: 1, // 当前页
        pageSize: 10, // 每页显示条目个数
        totalCount: 0 // 总条目数
      },
      isPage: true
    }
  },
  methods: {
    listBlog (pageNo) {
      // eslint-disable-next-line no-undef
      let params = {'channel': this.input1, 'apk_version': this.input2, 'page': pageNo}
      // eslint-disable-next-line no-undef
      axios.get('http://localhost:5000/search/', {params}).then(response => {
        var result = response.data.data
        if (String(response.data.code) === '0000') {
          this.tableData = []
          this.tableData = result
          this.page.totalCount = response.data.count
          this.page.pageSize = response.data.page_size
          console.log(response.data.count)
        } else {
          alert('列表显示失败！')
        }
      })
    },
    // 时间格式化
    dateFormat: function (row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return '未填'
      }
      return this.$moment(date).format('YYYY-MM-DD HH:mm:ss')
    },
    deleteBlog: function (index, row) {
      let params = {apk_name: row.apk_name}
      // eslint-disable-next-line no-undef
      axios.get('http://localhost:5000/delete/', {params}
      ).then(result => {
        if (String(result.data.code) === '0000') {
          // 删除成功
          this.$message.success('删除成功')
          this.listBlog()
        } else {
          this.$message.error('删除失败！')
        }
      })
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    speedupData () {
      var arr = this.multipleSelection
      let multis1 = ''
      let multis2 = ''
      let fd = new FormData()
      for (var i = 0; i < arr.length; i++) {
        multis1 = multis1 + arr[i].channel + ','
        multis2 = multis2 + arr[i].apk_version + ','
      }
      fd.append('channel', multis1)
      fd.append('apk_versions', multis2)
      console.log(multis1, multis2)
      axios.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
      axios.post('http://localhost:5000/upgrade_install', fd).then(res => {
        if (multis2.length !== null && String(res.data.code) === '0000') {
          this.$message.success('升级成功')
        } else {
          this.$message.error(String(res.data.msg))
        }
      })
      this.$refs.multipleTable.clearSelection()
    },
    speedupCheckbox () {
      if (this.multipleSelection.length === 0) {
        this.$message({
          message: '请至少勾选一项，再进行操作',
          type: 'warning'
        })
      } else {
        this.speedupData()
      }
    },
    handleCurrentChange (val) {
      this.listBlog(val)
    }
  }
}
</script>
