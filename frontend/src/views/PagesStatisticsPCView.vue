<template>
    <el-container>
        <el-header>
            <header-bar-statistics-p-c></header-bar-statistics-p-c>
        </el-header>
        <br>
        <el-container>
            <router-view />
        </el-container>
    </el-container>
</template>

<script>
    import HeaderBarStatisticsPC from "../components/HeaderBarStatisticsPC";

    export default {
        name: "pages-view-statistics-pc",
        components: {
            HeaderBarStatisticsPC
        }
    }
</script>

<style scoped>

</style>