<template>
    <div style="height: 100vh;">
        <div>
        </div>
        <div style="position: absolute; bottom:50%;width:100%;">
            <van-panel title="标题" desc="描述信息" status="状态">
                <div slot="header">
                    <h2>请登录</h2>
                </div>
                <van-field
                        v-model="password"
                        type="password"
                        label="密码"
                        placeholder="请输入登陆码"
                        required
                />
                <div slot="footer">
                    <van-button size="large">登陆</van-button>
                </div>
            </van-panel>


        </div>
    </div>
</template>

<script>
    export default {
        name: "LoginView"
    }
</script>

<style scoped>

</style>