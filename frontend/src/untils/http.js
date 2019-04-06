import axios from "axios";
import router from '../router'

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.headers.post['Content-Type'] = 'application/json';

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
        return response
    }, error => {
        let res = error.response;
        if (res) {
            switch (res.status) {
                case 401:
                case 403:
                    router.push('/login/');
                    error.message = '登录失效，请重新登录';
                    break
            }
        } else {
            error.message = '网络连接失败，请检查网络'
        }
        return Promise.reject(error)
    }
);

export default axios