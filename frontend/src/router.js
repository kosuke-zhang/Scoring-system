import Vue from 'vue'
import Router from 'vue-router'
import PagesView from './views/PagesView'
import CompetitionList from "./components/CompetitionList";
import CompositionList from "./views/CompositionList";
import JudgeView from "./views/JudgeView";
// import Home from "./views/Home";
import LoginView from "./views/LoginView";
import Rules from "./components/Rules";

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: '/competition/',
      component: PagesView,
      children: [
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
        },
        {
          path: 'rules',
          name: 'rules',
          component: Rules
        },
      ],

    },
    {
      path: '/login',
      component: LoginView,
    }
  ]
})
