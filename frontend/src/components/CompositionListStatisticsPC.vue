<template>
    <el-main>
        <v-chart :options="chart" autoresize ref="bar"/>
    </el-main>
</template>

<style>
    /**
     * 默认尺寸为 600px×400px，如果想让图表响应尺寸变化，可以像下面这样
     * 把尺寸设为百分比值（同时请记得为容器设置尺寸）。
     */
    .echarts {
        width: 100vw;
        height: 100vh;
        text-align: center;
    }
</style>

<script>
    import ECharts from 'vue-echarts'
    import 'echarts'

    export default {
        name: "CompositionListStatisticsPC",
        components: {
            'v-chart': ECharts,
        },
        data() {
            return {
                chart: {
                    legend: {
                        data: ['比赛成绩', '打分人数']
                    },
                    toolbox: {
                        show: true, //是否显示工具栏组件
                        feature: {
                            saveAsImage: { show: true },
                            dataView: { show: true },
                            magicType: {
                                type: ['line', 'bar']
                            },
                            restore: { show: true },
                        },
                        right: '10%'
                    },
                    xAxis: {data: []},
                    yAxis: [
                        {
                            type: 'value',
                            scale: true,
                            name: '比赛成绩',
                            min: 0,
                            boundaryGap: [0.2, 0.2],
                        },
                        {
                            type: 'value',
                            scale: true,
                            name: '打分人数',
                            min: 0,
                            minInterval: 1,
                            boundaryGap: [0.2, 0.2]
                        }
                    ],
                    series: [
                        {
                            name: '比赛成绩',
                            type: 'bar',
                            yAxisIndex: 0,
                            data: [],
                            markPoint: {
                                data: [
                                    { type: 'max', name: '最大值' },
                                ]
                            },
                            markLine: {
                                data: [
                                    {type: 'average', name: '平均值'},
                                ]
                            }
                        }, {
                            name: '打分人数',
                            type: 'bar',
                            yAxisIndex: 1,
                            data: []
                        }]

                }
            }
        },
        created() {
            let self = this;
            self.id = this.$route.params.id
        },
        methods: {
            alert: function (message) {
                let self = this;
                this.$notify({
                    title: '获取统计信息失败',
                    message: self.$createElement(
                        'i', {
                            style: 'color: red'
                        },
                        message
                    )
                });
            },
            statistics: function () {
                let self = this;
                self.$http
                    .get('/api/listcomposition/?competition=' + self.id)
                    .then(res => {
                        self.list = res.data;
                        let score = [];
                        let judged = [];
                        let composition = [];
                        res.data.forEach((v, i) => {
                            composition.push(v.name);
                            score.push(v.score_amount);
                            judged.push(v.judged_count);
                        });
                        self.$refs.bar.mergeOptions(
                            {
                                xAxis: {data: composition},
                                series: [
                                    {
                                        name: '比赛成绩',
                                        data: score
                                    }, {
                                        name: '打分人数',
                                        data: judged
                                    }]
                            }
                        )
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
        },
        mounted: function () {
            let self = this;
            self.statistics();
            setInterval(
                ()=>self.statistics(),
                10000
            )
        }
    }
</script>
