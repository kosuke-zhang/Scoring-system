import Vue from 'vue'
import Router from 'vue-router'
import PagesView from './views/PagesView'
import CompetitionList from "./components/CompetitionList";
import CompositionList from "./components/CompositionList";
import JudgeView from "./views/JudgeView";
import LoginView from "./views/LoginView";
import CompetitionListStatistics from "./components/CompetitionListStatistics";
import CompositionListStatistics from "./components/CompositionListStatistics";
import PagesStatisticsView from "./views/PagesStatisticsView";
import PagesStatisticsPCView from "./views/PagesStatisticsPCView";
import CompositionListStatisticsPC from "./components/CompositionListStatisticsPC";
import CompetitionListStatisticsPC from "./components/CompetitionListStatisticsPC";

Vue.use(Router);

const router = new Router({
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
            ],

        },
        {
            path: '/login',
            component: LoginView,
        },
        {
            path: '/statistics',
            redirect: '/statistics/competition',
            component: PagesStatisticsView,
            children: [
                {
                    path: '/statistics/competition',
                    name: 'CompetitionListStatistics',
                    component: CompetitionListStatistics
                },
                {
                    path: '/statistics/composition/:id',
                    name: 'CompositionListStatistics',
                    component: CompositionListStatistics
                }
            ],
        },
        {
            path: '/pc-statistics',
            redirect: '/pc-statistics/competition',
            component: PagesStatisticsPCView,
            children: [
                {
                    path: '/pc-statistics/competition',
                    name: 'CompetitionListStatisticsPC',
                    component: CompetitionListStatisticsPC
                },
                {
                    path: '/pc-statistics/composition/:id',
                    name: 'CompositionListStatisticsPC',
                    component: CompositionListStatisticsPC
                }
            ],
        }
    ]
});

router.beforeEach((to, from, next) => {
    if (to.path !== '/login' && !localStorage.token) {
        return next('/login')
    }
    next()
});

export default router
