<template>
  <div style="display:flex;justify-content:center;width: 100%;">
    <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" border
      style="width:70%;max-width: 70%;">
      <el-table-column prop="name" label="Instance Name" :sortable="true" width="200">
      </el-table-column>
      <el-table-column prop="type" label="Instance Type" width="150">
      </el-table-column>
      <el-table-column prop="size" label="Size" width="160">
      </el-table-column>
      <el-table-column align="right">
        <template slot="header" slot-scope="scope">
          <el-input v-model="search" size="mini" placeholder="Please enter a keyword to search" />
        </template>
        <template slot-scope="scope">
          <el-button size="mini" @click="handelDetail(scope.row)">Detail</el-button>
        </template>
      </el-table-column>
    </el-table>
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
      search: ''
    }
  },
  methods: {
    handelDetail (row) {
      const fileUrl = `http://127.0.0.1:8081/InstancePool/${row.type}/${row.name}.png`
      const link = document.createElement('a')
      link.href = fileUrl
      link.target = '_blank'
      link.style.display = 'none'
      link.click()
    }
  }
}
</script>

<style>
.el-table .el-table__cell.is-right {
  text-align: left;
}
</style>
