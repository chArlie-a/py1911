<template>
    <div class="usercenter">
        用户中心
        <div v-if="userinfo">
            用户名：{{userinfo.username}}
            <br>
            注册时间：{{userinfo.date_joined|dataFormat}}
            <h2>修改信息</h2>
            <van-field v-model="userinfo.telephone" type="tel" label="手机号" />
            <van-field v-model="userinfo.username" type="username" label="用户名" />
            <van-field v-model="userinfo.password" type="password" label="密码" />
            <van-field v-model="userinfo.email" type="email" label="邮箱" />
            <van-button @click="modify" round block type="info" native-type="submit">
                修改信息
            </van-button>
        </div>
        <van-field
                v-model="verify"
                center
                clearable
                label="短信验证码"
                placeholder="请输入短信验证码"
        >
            <van-button slot="button" size="small" type="primary" @click="sendmsg">发送验证码</van-button>
        </van-field>
    </div>
</template>

<script>
    export default {
        methods:{
            sendmsg(){
                this.$api.sendmsg({
                    telephone:this.telephone
                }).then(res=>{
                    console.log("发送成功")
                }).catch(err=>{
                    console.log("发送失败")
                })

            },
            modify(){
                this.$api.modifyUserInfo({
                    userinfo:this.userinfo
                }).then(res=>{
                    console.log('更改成功',res);
                    this.$toast('更改成功')
                }).catch(err=>{
                    console.log('出错了',err)
                })
            }
        },
        data(){
          return{
              userinfo:null,
          }
        },
        created() {
            this.$api.getUserinfo().then(res => {
                console.log('个人信息', res);
                this.userinfo = res.data;
                this.$jsCookie.set('userinfo', res.data)
            }).catch(err => {
                console.log("出错了",err)
            })
        },
        filters: {
            dataFormat(date) {
                date = new Date(date);
                console.log(date, typeof (date));
                return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
            }
        }
    }
</script>

<style scoped>

</style>