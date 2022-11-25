<template>
  <div>
    <el-form label-width="200px">
      <el-form-item label="Search:">
        <el-input v-model="search" placeholder="Please enter a keyword to search"
          style="width:300px;margin-right:15px" size="small"></el-input>
          <el-button type="primary" size="small" @click="Search(search)">Search</el-button>
          <el-button size="small" @click="Reset()">Reset</el-button>
      </el-form-item>
    </el-form>
    <div style="display:flex;justify-content:center;width: 100%;">
      <el-table :data="pageData.slice((currentPage-1)*pagesize,currentPage*pagesize)" border
        style="width:70%;max-width: 70%;">
        <el-table-column prop="name" label="Instance Name" :sortable="true" width="200">
        </el-table-column>
        <el-table-column prop="type" label="Instance Type" width="150">
        </el-table-column>
        <el-table-column prop="size" label="Size" width="160">
        </el-table-column>
        <el-table-column fixed="right" label="Operations" width="200">
          <template slot-scope="scope">
            <el-button size="mini" @click="handelDetail(scope.row)">Detail</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="split-page">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-sizes="[10, 20, 50]"
        :page-size="pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="pageData.length">
      </el-pagination>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    tableData: {
      default: []
    }
  },
  data () {
    return {
      search: '',
      currentPage: 1,
      pagesize: 10,
      pageData: [],
      fullData: []
    }
  },
  watch: {
    tableData: function (newData, oldData) {
      this.pageData = newData
      this.fullData = newData
    }
  },
  methods: {
    handleSizeChange (size) {
      this.pagesize = size
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    handelDetail (row) {
      const fileUrl = `http://127.0.0.1:8081/InstancePool/${row.type}/${row.name}.png`
      const link = document.createElement('a')
      link.href = fileUrl
      link.target = '_blank'
      link.style.display = 'none'
      link.click()
    },
    Search (search) {
      this.pageData = this.fullData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))
    },
    Reset () {
      this.search = ''
      this.pageData = this.fullData
    }
  }
}
</script>

<style>
.split-page {
  text-align: center;
  margin-top: 20px;
}
.el-table .el-table__cell.is-right {
  text-align: left;
}
</style>
