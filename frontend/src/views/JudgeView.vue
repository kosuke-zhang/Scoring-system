<template>
    <div>
        <van-cell-group>
            <van-field
                    @click-right-icon="$toast(question)"
                    clearable
                    label="创新"
                    placeholder="请输入评分"
                    required
                    right-icon="question-o"
                    v-model="innovateScore"
            />
            <van-field
                    @click-right-icon="$toast(question)"
                    clearable
                    label="实用"
                    placeholder="请输入评分"
                    required
                    right-icon="question-o"
                    v-model="functionalScore"
            />
        </van-cell-group>
        <van-button @click="submit" size="large">提交成绩</van-button>
    </div>
</template>

<script>
    export default {
        name: "JudgeView",
        data() {
            return {
                id: null,
                score: null,
                question: "百分制",
                innovateScore: null,
                functionalScore: null,
                title: '评分'
            }
        },
        created() {
            let self = this;
            self.id = this.$route.params.id
        },
        methods: {
            alert: function (message) {
                let self = this;
                self.$dialog.alert({
                    title: '提交失败',
                    message: message
                })
            },
            submit: function () {
                let self = this;
                if (self.innovateScore && self.functionalScore) {
                    self.score = parseInt(self.innovateScore) + parseInt(self.functionalScore)
                } else {
                    self.alert('请填写全部的分项');
                    return
                }
                self.$http
                    .post('/api/grade/', {'composition': self.id, 'score': self.score})
                    .then(res => {
                        self.$toast('提交成功，请继续为其他团队评分');
                        self.$router.go(-1)
                    })
                    .catch(function (error) {
                        let message = error;
                        if (error.response) {
                            // 请求已发出，但服务器响应的状态码不在 2xx 范围内
                            if (error.response.status === 400){
                                message = JSON.stringify(error.response.data)
                                self.alert(message)
                                return
                            }
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
    }
</script>

<style scoped>

</style>