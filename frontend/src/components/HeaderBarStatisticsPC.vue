<template>
    <div class="header-bar-pc">
        <el-menu :default-active="activeIndex" @select="competitionSelect" class="el-menu-cxy" mode="horizontal">
            <el-menu-item index="competition">比赛</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: 'header-bar-statistics-pc',
        data() {
            return {
                activeIndex: "competition"
            }
        },
        methods: {
            competitionSelect(key, keyPath) {
                self = this;
                this.$router.push('/pc-statistics/competition')
            }
        }
    }
</script>

<style lang="scss" scoped>
</style>
