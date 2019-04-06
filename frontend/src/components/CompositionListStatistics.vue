<template>
    <van-list
            v-model="loading"
            :finished="finished"
            finished-text="没有更多了"
    >
        <van-cell
                v-for="item in list"
                :key="item.id"
                :title="title(item)"
        />
    </van-list>
</template>

<script>
    export default {
        name: "CompositionList",
        data() {
            return {
                id: null,
                finished: true,
                loading: false,
                list: []
            }
        },
        created() {
            let self = this
            self.id = this.$route.params.id
        },
        methods: {
            title: function(item){
                return item.name + ' 总分 ' + item.score_amount + ' 已评 ' + item.judged_count
            },
            alert: function (message) {
                let self = this
                self.$dialog.alert({
                    title: '获取团队信息失败',
                    message: message
                })
            },
        },
        mounted: function () {
            let self = this
            self.$http
                .get('/api/listcomposition/?competition=' + self.id)
                .then(res => {
                    self.list = res.data
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