<template>
	<div class="home">
		<img alt="Vue logo" src="../assets/logo.png">
		<!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
		<div class="category">
			<van-cell v-for="(item) in categorys" :title="item.name" is-link :to="'categorys/'+item.id+'/'"/>
		</div>
<!-- 		<div>
			<button @click="requestCategoryList">发起请求商品列表</button>
		</div>
		<div>
			<label for="">创建名：</label> <input type="text" v-model="categoryName">
			<br>
			<button @click="requestCreateCategory">发起创建分类请求</button>
		</div>
		<div>
			<label for="">需要修改的分类id：</label> <input type="text" v-model="newCategoryId">
			<br>
			<label for="">需要修改的分类名字：</label> <input type="text" v-model="newCategoryName">
			<br>
			<button @click="requestModifyCategory">需要修改的分类</button>
		</div>
		<div>
			<label for="">用户名：</label> <input type="text" v-model="username">
			<br>
			<label for="">密 码：</label> <input type="text" v-model="password">
			<br>
			<button @click="requestToken">发起请求Token</button>
		</div> -->
	</div>
</template>

<script>
	// @ is an alias to /src
	import HelloWorld from '@/components/HelloWorld.vue'

	export default {
		name: 'Home',
		data() {
			return {
				// username: "charlie",
				// password: "123456",
				// categoryName: '',
				// newCategoryId:"",
				// newCategoryName:"",
				categorys:[],
			}
		},
		components: {
			// HelloWorld

		},
		created() {
			this.requestCategoryList()
		},
		methods: {
			requestCategoryList() {
				// console.log()
				this.$api.getCategoryList().then(res => {
					console.log('得到列表', res)
					if(res.status==200){
						this.categorys = res.data;
					}
				}).catch(err => {
					console.log('发生错误', err)
				});
			},
			// requestToken() {
			// 	this.$api.getToken({
			// 		username: this.username,
			// 		password: this.password
			// 	}).then(res => {
			// 		console.log('得到Token', res)
			// 		this.$jsCookie.set('refresh',res.data.refresh)
			// 		this.$jsCookie.set('access',res.data.access)

			// 	}).catch(err => {
			// 		console.log('请求token错误', err)
			// 	})
			// },
			// requestCreateCategory() {
			// 	if (this.categoryName != '') {
			// 		this.$api.createCategory({
			// 			name: this.categoryName
			// 		}).then(res => {
			// 			console.log('创建结果', res)
			// 		}).catch(err => {
			// 			console.log('出错了', err)
			// 		})
			// 	} else {
			// 		console.log('必须输入分类名')
			// 	}
			// },
			// requestModifyCategory(){
			// 	if(this.newCategoryId == '' || this.newCategoryName == ''){
			// 		console.log('需要选择分类并且重新给予名字')
			// 	}
			// 	else{
			// 		this.$api.modifyCategory({
			// 			id:this.newCategoryId,
			// 			name:this.newCategoryName
			// 		}).then(res => {
			// 			console.log('修改结果', res)
			// 		}).catch(err => {
			// 			console.log('出错了', err)
			// 		})
			// 	}
			// }

		}
	}
</script>
