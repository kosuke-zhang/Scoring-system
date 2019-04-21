<template>
    <div class="pages-view">
        <header-bar-statistics/>
        <!--:showLeftArrow="true" :leftText="'返回'"-->
        <router-view/>
    </div>
</template>

<script>
    import HeaderBarStatistics from "../components/HeaderBarStatistics";

    export default {
        name: 'pages-view-statistics',
        components: {HeaderBarStatistics},
        data() {
            return {}
        },
        methods: {}
    }
</script>

<style scoped>

</style>
