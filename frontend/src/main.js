import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vant from 'vant';
import 'vant/lib/index.css';
import axios from 'axios'


Vue.config.productionTip = false;
Vue.use(Vant);
Vue.prototype.$http = axios;

axios.defaults.baseURL = 'http://192.168.43.177';
axios.defaults.headers.post['Content-Type'] = 'application/json';

// if (localStorage.token) {
//     axios.defaults.headers.common['Authorization'] = localStorage.token
// }

axios.interceptors.request.use(
    config => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.common['Authorization'] = token;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);


axios.interceptors.response.use(
    response => {
        let data = response.data;
        return data.data
        // return Promise.reject(data)
    }, error => {
        let res = error.response;
        switch (res.status) {
            case 401:
            case 403:
                Vant.$dialog.alert({
                    'title': '未登陆',
                    'message': '请登录'
                });
                router.push('/login/');
                return;
            case 500:
                Vant.$dialog.alert({
                    title: '服务器错误',
                    message: '服务器被吃了⊙﹏⊙∥，请联系管理员'
                });
                return;
            default:
                return Promise.reject(error)
        }
    }
);


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
