<template>
	<div class="category">
		<div class="header" >
			<van-search placeholder="请输入搜索关键词" @click="goToSearch" />
		</div>
		<div class="con">
			<div class="left">
				<van-sidebar v-model="activeKey">
				  <van-sidebar-item title="鲜花	" />
				  <van-sidebar-item title="永生花" />
				  <van-sidebar-item title="蛋糕" />
				  <van-sidebar-item title="女友最爱" />
				  <van-sidebar-item title="绿植花卉" />
				</van-sidebar>
			</div>
			<div class="right" >
				<div class="category_group" v-for="(item,index) in datas.categorymessage[activeKey]" :key="index">
					<van-card
					  tag="TOP"
					  :price="item.Price"
					  :title="item.Cpmc"
					  :thumb="item.img"
					  :origin-price="item.LinePrice"
					  :thumb-link="'/#/detail/'+item.ItemCode"
					/>
				</div>
			</div>
		</div>
		
		
	</div>
	
</template>

<script>
	import datae from '../data.js'
	export default{
		data(){
			return{
				activeKey: this.$route.query.key?this.$route.query.key:0,
				datas:null
			}
		},
		created() {
			this.datas=datae
			
		},
		methods:{
			goToSearch(){
				this.$router.push('/Search')
			},
			// goToSearch(){
			// 	this.$router.push('/Dateil')
			// }
		}
	}
</script>

<style lang="less">
	.header{
		height: 100%;
	}
	.van-field__control {
		height: 30px;
	}
	.van-search__content{
		border-radius: 20px;
	}
	.van-card__title {
	    max-height: 32px;
	    font-weight: 600;
	    line-height: 20px;
		color: #000000;
	    text-align: left;
	}
	.van-card__title {
	    max-height: 32px;
	    font-weight: 550;
	    line-height: 16px;
	}
	.van-card__bottom, .van-card__desc {
	    line-height: 20px;
		 text-align: left;
	}

	.van-card__price-decimal, .van-card__price-integer {
	    font-family: Avenir-Heavy,PingFang SC,Helvetica Neue,Arial,sans-serif;
		color: red;
	}
	.van-card__price-integer {
	    font-size: 22px;
	    font-weight: 600;
	}
	.van-card__price-currency {
	    color: #E7141A;
	    font-weight: 900;
	}
</style>

<style scoped="scoped" lang="less">
	*{
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}
	.con{
		display: flex;
		position: absolute;
		left: 0;
		top: 50px;
		right: 0;
		bottom: 50px;
		.left{
			overflow-y: auto;
			width: 30%;
		}
		.right{
			overflow-y: auto;
			width: 100%;
		}
		.left::-webkit-scrollbar{
			display: none;
		}
		.right::-webkit-scrollbar{
			display: none;
		}
	}
</style>
