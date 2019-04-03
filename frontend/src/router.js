import Vue from 'vue'
import Router from 'vue-router'
import PagesView from './views/PagesView'
import CompetitionList from "./components/CompetitionList";
import CompositionList from "./views/CompositionList";
import JudgeView from "./views/JudgeView";

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: '/pages/'
    },
    {
      path: '/pages',
      component: PagesView,
      children: [
        {
          path: '',
          redirect: '/pages/competition'
        },
        {
          path: 'competition',
          name: 'CompetitionList',
          component: CompetitionList
        },
        {
          path: 'composition/:id',
          name: 'CompositionList',
          component: CompositionList
        },
        {
          path: 'judge/:id',
          name: 'JudgeView',
          component: JudgeView
        }
      ],
    }
  ]
})
