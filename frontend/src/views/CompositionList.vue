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
                :to="{name: 'JudgeView', params: { id: item.id }}"
        />
    </van-list>
</template>

<script>
    export default {
        name: "CompositionList",
        data() {
            return {
                finished: true,
                loading: false,
                list: [
                    {
                        "id": 1,
                        "number": 1,
                        "name": "vectory智能降噪音响",
                        "competition": 1
                    },
                    {
                        "id": 2,
                        "number": 2,
                        "name": "智能养殖",
                        "competition": 1
                    },
                    {
                        "id": 3,
                        "number": 3,
                        "name": "摘椰机器人",
                        "competition": 1
                    },
                ]
            }
        },
        created() {
            const id = this.$route.params.id
        }
    }
</script>

<style scoped>

</style>