import Vue from 'vue'
import Router from 'vue-router'
import PagesView from './views/PagesView'
import CompetitionList from "./components/CompetitionList";
import CompositionList from "./components/CompositionList";
import JudgeView from "./views/JudgeView";
import LoginView from "./views/LoginView";
import Rules from "./components/Rules";

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
});

router.beforeEach((to, from, next) => {
    if (to.path !== '/login' && !localStorage.token) {
        return next('/login')
    }
    next()
});

export default router
