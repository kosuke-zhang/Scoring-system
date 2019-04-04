<template>
  <div class="pages-view">
    <header-bar></header-bar>
    <!--:showLeftArrow="true" :leftText="'返回'"-->
    <router-view/>
  </div>
</template>

<script>
import HeaderBar from '../components/HeaderBar'

export default {
  name: 'pages-view',
  components: { HeaderBar },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
