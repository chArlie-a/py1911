<template>
    <div class="login">
        <label for="">用户名：</label> <input type="text" v-model="username">
        <br>
        <label for="">用户名：</label> <input type="text" v-model="password">
        <br>
        <button @click="requestToken">发起请求Token</button>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                username: "charlie",
                password: "123456",
            }
        },
        methods:{
            requestToken() {
            	this.$api.getToken({
            		username: this.username,
            		password: this.password
            	}).then(res => {
            		console.log('得到Token', res)
            		this.$jsCookie.set('refresh',res.data.refresh)
            		this.$jsCookie.set('access',res.data.access)

            	}).catch(err => {
            		console.log('请求token错误', err)
            	})
            }
        }
    }
</script>

<style scoped>

</style>