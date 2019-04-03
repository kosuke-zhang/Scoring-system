<template>
    <van-cell-group>
        <van-field
                v-model="score"
                required
                clearable
                label="创意"
                right-icon="question-o"
                placeholder="请输入评分"
                @click-right-icon="$toast(question)"
        />
        <van-field
                v-model="score"
                required
                clearable
                label="实用"
                right-icon="question-o"
                placeholder="请输入评分"
                @click-right-icon="$toast(question)"
        />
    </van-cell-group>
</template>

<script>
    export default {
        name: "JudgeView",
        data() {
            return {
                question: "百分制",
                score: null,
                title: '评分'
            }
        },
        created() {
            const id = this.$route.params.id
            this.$emit("getData", this.title);
        }
    }
</script>

<style scoped>

</style>