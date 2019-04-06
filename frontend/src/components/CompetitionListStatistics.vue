<template>
    <van-list
            v-model="loading"
            :finished="finished"
            finished-text="没有更多了"
    >
        <van-cell
                v-for="item in list"
                :key="item.id"
                :title="item.name"
                :to="{name: 'CompositionListStatistics', params: { id: item.id }}"
        />
    </van-list>
</template>

<script>
    export default {
        name: "CompetitionList",
        data() {
            return {
                finished: true,
                loading: false,
                list: []
            }
        },
        methods: {
            alert: function (message) {
                let self = this
                self.$dialog.alert({
                    title: '获取比赛信息失败',
                    message: message
                })
            },
        },
        mounted: function () {
            let self = this
            this.$http
                .get('/api/listcompetition/')
                .then(res => {
                    self.list = res.data
                    console.log(res)
                })
                .catch(function (error) {
                    let message = error
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