<template>
    <div style="height: 100vh;">
        <div>
        </div>
        <div style="position: absolute; bottom:50%;width:100%;">
            <van-panel desc="描述信息" status="状态" title="标题">
                <div slot="header">
                    <h2>请登录</h2>
                </div>
                <van-field
                        label="密码"
                        placeholder="请输入登陆码"
                        required
                        type="password"
                        v-model="password"
                />
                <div slot="footer">
                    <van-button @click="loginCxy" size="large">登陆</van-button>
                </div>
            </van-panel>
        </div>
    </div>
</template>

<script>
    export default {
        name: "LoginView",
        data() {
            return {
                password: ''
            }
        },
        methods: {
            alert: function (message) {
                let self = this;
                self.$dialog.alert({
                    title: '登陆失败',
                    message: message
                })
            },
            loginCxy: function () {
                let self = this;
                self.$http
                    .post('/api/token/', {
                        'code': self.password
                    })
                    .then(response => {
                        localStorage['token'] = 'Bearer ' + response.data['access'];
                        this.$http.defaults.headers.common['Authorization'] = 'Bearer ' + response.data['access'];
                        this.$router.push('/')
                    })
                    .catch(function (error) {
                        let message = error.message;
                        if (error.response) {
                            if (error.response.status === '401') {
                                message = '密码错误'
                            }
                            self.alert(message)
                        } else if (error.request) {
                            self.alert(message)
                        } else {
                            self.alert(message)
                        }
                    })
            }
        }
    }
</script>

<style scoped>

</style>