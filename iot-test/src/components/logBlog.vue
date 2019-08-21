<template>
    <div>
        <!--搜索框-->
        <el-row>
            <el-col :span="3" class="grid">
                <el-input v-model="input" placeholder="请输入id" size="mini"></el-input>
            </el-col>
            <el-col :span="1" class="grid">
                <el-button type="success" icon="el-icon-search" size="mini" @click.prevent="search()">搜索</el-button>
            </el-col>
        </el-row>
        <br>
    </div>
</template>
<script>
</script>
