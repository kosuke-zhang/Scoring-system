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
                :to="{name: 'CompositionList', params: { id: item.id }}"
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
                list: [
                    {
                        "id": 1,
                        "name": "互联网+（创意组）",
                        "judger": [
                            1,
                            2,
                            3
                        ]
                    },
                    {
                        "id": 2,
                        "name": "互联网+（初创组）",
                        "judger": [
                            1,
                            2
                        ]
                    }
                ]
            }
        },
    }
</script>

<style scoped>

</style>