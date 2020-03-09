<template>
  <div class="mine">
	<!-- <div class="header">
		<van-nav-bar
		  title="登录注册"
		  left-text=""
		  right-text="按钮"
		  left-arrow
		  @click-left="onClickLeft"
		  @click-right="onClickRight"
		/>
	</div> -->
<!-- 	<div class="img">
		<img src="/img/m_hualogo.png" alt="" style="width: 80%;">
	</div> -->
	<div v-if="state">
		<div class="userinfo">
			<img src="img/m_hualogo.png" alt="" style="width: 50%; padding: 20px;">
			<h1>用户信息</h1>
			<van-image
			  round
			  width="10rem"
			  height="10rem"
			  src="https://img.yzcdn.cn/vant/cat.jpeg"
			/>
			<h3>您好！亲爱的111</h3>
			<!-- <p>{{userinfo.M_JoinTime}}</p> -->
			<!-- <p>{{userinfo.M_Honor}}</p> -->
			<h5>白金会员</h5>
			
			<div class="SNS">
				<div class="top">
					<van-nav-bar
					  left-text="我的订单"
					  @click-left="onClickLeft"
					  right-text="全部订单"
					  left-arrow
						
					  @click-right="onClickRight"
					/>
					<van-grid>
					  <van-grid-item icon="cash-back-record" text="待付款" />
					  <van-grid-item icon="logistics" text="今日配送" />
					  <van-grid-item icon="chat-o" text="待评价" />
					  <van-grid-item icon="bag-o" text="全部订单" />
					</van-grid>
				</div>
				<!-- <van-divider></van-divider> -->
				<br>
				<div class="bottom" >

				</div>
			</div>
			
	
			<van-button type="primary" @click="loginout">注销</van-button>
			<div style="height: 1000px;;"></div>
		</div>
	</div>
	<div v-else>
		<van-tabs v-model="active">
			<van-tab title="登录">
				<div class="login" style="padding: 20px 0;">
					<img src="img/m_hualogo.png" alt="" style="width: 50%; padding: 40px;">
					
					<div class="loginBox" style="width: 80%; margin: auto;">
						<van-cell-group>
						  <van-field
							v-model="loginusername"
							required
							clearable
							label="用户名"
							placeholder="请输入用户名/邮箱"
						  />
						
						  <van-field
							v-model="loginpassword"
							type="password"
							label="密码"
							placeholder="请输入密码"
							required
						  />
						</van-cell-group>
					</div>
					
					<div class="button" style="padding: 20px;">
						<van-button type="danger" @click="login">登录</van-button>
					</div>
				</div>
			</van-tab>
			<van-tab title="注册">
				<div class="regist">
					<img src="img/m_hualogo.png" alt="" style="width: 50%; padding: 40px;">
					
					<div class="registBox" style="width: 80%; margin: auto;">
						<van-cell-group>
						  <van-field
							v-model="username"
							required
							clearable
							label="用户名"
							placeholder="请输入用户名"
						  />
						
						  <van-field
							v-model="password"
							type="password"
							label="密码"
							placeholder="请输入密码"
							required
						  />
						  
						  <van-field
							v-model="password2"
							type="password"
							label="重复密码"
							placeholder="请再次输入密码"
							required
						  />
						  
						  <van-field
							v-model="email"
							type="email"
							label="邮箱"
							placeholder="请输入邮箱"
							required
						  />
						</van-cell-group>
					</div>
					
					<div class="button" style="padding: 20px;">
						<van-button type="danger" @click="regist">注册</van-button>
					</div>
				</div>
			</van-tab>
		</van-tabs>
	</div>
  
  </div>
</template>

<script>
	// 在当前页面引入cookie
	import Cookie from 'js-cookie'
	
	export default {
		data(){
			return{
				username:"py191101",
				password:"123456789",
				password2:"123456789",
				email:"496575233@qq.com",
				loginusername:"py191101",
				loginpassword:"123456789",
				userinfo:null,
				active:0,
				state:localStorage.getItem("login"),
			}
		},
		// created() {
		// 	this.initUser();
		// },
		
		
		methods:{
			 onClickLeft() {
			   // this.$router.go(-1)
			   this.$router.push('/Cart')
			},
			onClickRight() {
			  // this.$toast('按钮');
			  this.$router.push('/Cart')
			},
			// initUser(){
			// 	// this.$http({
			// 	// 	url:`http://www.520mg.com/member/ajax_login.php`,
			// 	// 	method:"get",
			// 	// 	// 强制上传cookie信息
			// 	// 	withCredentials:true
					
			// 	// }).then(res=>{
			// 		console.log(res.data);
					// this.userinfo = {M_UserName:老子}
			// 	// })
			// },
			loginout(){
				// this.$http({
				// 	url:`http://www.520mg.com/member/index_login.php?dopost=exit`,
				// 	method:'post',
				// 	withCredentials:true
				// }).then(res=>{
				// 	if(res.data.status==1){
						this.$toast("退出成功");
						// this.userinfo=null;
						Cookie.remove("islog")
						localStorage.removeItem("login",true);
						this.$router.go(-1)
					// }
					// else{
					// 	this.$toast("退出失败");
					// }
				// })
			},
			login(){
				console.log(localStorage.setItem("login",true));
				// if(this.loginusername.length<=0||this.loginpassword.length<=0){
				// 	this.$toast("必填项目不能为空");
				// }
				// else{
				// 	this.$http({
				// 		url:`http://www.520mg.com/member/index_login.php?fmdo=login&dopost=login&userid=${this.loginusername}&pwd=${this.loginpassword}`,
				// 		method:"post",
				// 		withCredentials:true
				// 		// data:{
							
				// 		// }
				// 	}).then(res=>{
				// 		console.log(res);
				// 		if(res.data.status==1){
				// 			this.$toast("登录成功")
				// 			Cookie.set("islog",true,{ expires: 7 })
				// 			this.initUser();
				// 		}
				// 		else{
				// 			this.$toast(res.data.msg)
				// 		}
				// 	})
				// }
				this.$toast("登录成功");
				this.$router.go(-1)
			},
			regist(){
				
				if(this.email.length<=0||this.username.length<=0||this.password.length<=0||this.password2.length<=0){
					this.$toast("必填项目不能为空");
				}
				else if(this.password!=this.password2)
				{
					this.$toast("密码必须一致");
				}
				else 
				{
					// this.$toast("注册成功")
					// this.$http({
					// 	// url:`http://www.520mg.com/member/reg_new2.php`,
					// 	//  将post参数以get的形式携带
					// 	url:`http://www.520mg.com/member/reg_new2.php?userid=${this.username}&userpwd=${this.password}&email=${this.email}`,
					// 	method:"post",
					// 	// data:{
					// 	// 	"userid":this.username,
					// 	// 	"userpwd":this.password,
					// 	// 	"email":this.email
					// 	// }
					// }).then(res=>{
					// 	if(res.data.status==1){
							this.$toast("注册成功")
					// 	}
					// 	else{
					// 		this.$toast(res.data.msg)
					// 	}
					// }).catch(err=>{
					// 	console.log("请求出错",err);
					// })
					
				}
			}
		}
	}
	
</script>

<style lang="less">
	.mine{
		input{
			width:100%;
			height: 30px;
			margin: auto;
			padding: 20px;
			// border: 0px solid #FF8C00;
			line-height: 66px;
			border-radius: 50px;
			text-align: center;
		}
		.van-field__label {
			-webkit-box-flex: 0;
			flex: none;
			width: 90px;
			font-size: 18px;
			font-weight: 550;
			margin: auto;
		}
		.van-button--danger {
		    color: #fff;
		    background-color: #FF8C00;
		    border: 1px solid #FF8C00;
		    width: 50%;
		    border-radius: 40px;
		}
		.van-cell {
		    padding: 20px;
		}
		.van-button--primary {
		    color: #fff;
		    background-color: #FF8C00;
		    border: 1px solid #FF8C00;
		}
		.van-button--normal {
		    padding: 0 15px;
		    font-size: 14px;
		    width: 80%;
		}
	}
</style>

<style scoped="scoped" lang="less">
	.van-cell__title, .van-cell__value{
		text-align: center;
		line-height: 64px;
	}

	.van-cell--required::before{
		content: none;
	}
	.SNS{
		padding: 10px 20px;
	}
</style>

<!-- 
跨域： 从一个网站请求另一个网站资源   域名 端口都必须一致
 服务端： 
 客户端：get  jsonp
		post 不支持jsonp   
 
 

localStory 本地存储 没有有效期 永久存储 localStory.setItem(key,value) localStory.get(key) localStory.removeItem(key)

存储cookit  可以设置有效期  每次请求服务器 都会携带cookit信息


 -->