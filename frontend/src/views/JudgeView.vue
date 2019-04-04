<template>
    <div>
        <van-cell-group>
            <van-field
                    v-model="innovateScore"
                    required
                    clearable
                    label="创新"
                    right-icon="question-o"
                    placeholder="请输入评分"
                    @click-right-icon="$toast(question)"
            />
            <van-field
                    v-model="functionalScore"
                    required
                    clearable
                    label="实用"
                    right-icon="question-o"
                    placeholder="请输入评分"
                    @click-right-icon="$toast(question)"
            />
        </van-cell-group>
        <van-button size="large" @click="submit">提交成绩</van-button>
    </div>
</template>

<script>
    export default {
        name: "JudgeView",
        data() {
            return {
                question: "百分制",
                innovateScore: null,
                functionalScore: null,
                title: '评分'
            }
        },
        methods: {
            submit: function () {
                // TODO 提交成绩
                let result = 'sucess'
                if (result === 'sucess') {
                    this.$toast('提交成功，请继续为其他团队评分')
                    this.$router.go(-1)
                } else if (result === 'neterror') {
                    this.$dialog.alert(
                        {
                            title: '失败',
                            message: '网络连接失败，请稍后再试'
                        }
                    )
                } else {
                    this.$dialog.alert(
                        {
                            title: '未知错误',
                            message: '请联系开发人员解决\n' + result
                        }
                    )
                }
            }
        }
    }
</script>

<style scoped>

</style>