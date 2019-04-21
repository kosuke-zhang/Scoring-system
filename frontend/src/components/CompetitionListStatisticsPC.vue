<template>
    <el-main>
        <el-table
                :data="list"
                :default-sort="{prop: 'date', order: 'descending'}"
                @row-click="rowSelect"
                stripe
                style="width: 200%">
            <el-table-column
                    label="编号"
                    prop="id"
                    sortable
                    width="130">
            </el-table-column>
            <el-table-column
                    label="比赛名称"
                    prop="name"
                    sortable>
            </el-table-column>
            <el-table-column
                    label="日期"
                    prop="date"
                    sortable
                    width="180">
            </el-table-column>
        </el-table>
    </el-main>
</template>

<script>
    export default {
        name: "CompetitionListStatisticsPC",
        data() {
            return {
                list: []
            }
        },
        methods: {
            rowSelect: function (row, column, event) {
                let self = this;
                self.$router.push(
                    {
                        path: '/pc-statistics/composition/' + row.id
                    }
                );
            },
            alert: function (message) {
                let self = this;
                this.$notify({
                    title: '获取比赛信息失败',
                    message: self.$createElement(
                        'i', {
                            style: 'color: red'
                        },
                        message
                    )
                });
            },
        },
        mounted: function () {
            let self = this;
            this.$http
                .get('/api/listcompetition/')
                .then(res => {
                    self.list = res.data;
                })
                .catch(function (error) {
                    let message = error;
                    if (error.response) {
                        // 请求已发出，但服务器响应的状态码不在 2xx 范围内
                        self.alert(message)
                    } else if (error.request) {
                        // 发送了请求但是没有响应
                        self.alert(message)
                    } else {
                        // 其他错误
                        self.alert(message)
                    }
                })
        }
    }
</script>

<style scoped>

</style>