<template>
	<div class="home">
		<!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
		<div class="header">
			<div class="left">
				<img src="/img/分类.png" alt="" @click="goToCategory">
			</div>
			<div class="middle">
				<img src="img/m_hualogo.png" alt="">
			</div>
			<div class="right">
				<img src="/img/客服.png" alt="">
			</div>
		</div>
		<div class="tabs">
			<van-swipe :autoplay="3000" indicator-color="white">
			  <van-swipe-item v-for="(item,index) in carouselimg">
				  <img :src="item" alt="" style="width: 100%;">
			  </van-swipe-item>
			</van-swipe>
		</div>
		<div class="authen">
			<div>
				<img src="/img/对.png" alt="" style="width: 14px;height: 14px;">
				认证龙头企
			</div>
			<div>
				<img src="/img/对.png" alt="" style="width: 14px;height: 14px;">
				15年品
			</div>
			<div>
				<img src="/img/对.png" alt="" style="width: 14px;height: 14px;">
				3小时送
			</div>
			<div>
				<img src="/img/对.png" alt="" style="width: 14px;height: 14px;">
				最近349189好
			</div>	
		</div>
		<div class="cate" style="display: flex; padding: 8px 0;">
			<div v-for="item in cateimg.lbimg" style="width: 20%;">
				<img  @click="goToProductList('$event',1)" :src="item.img" alt="" style="width: 36px;height: 36px;">
				<p>{{item.name}}</p>
			</div>
		</div>
		<div class="modetitle" style="font-size: 18px; line-height: 40px; height: 40px; display: flex;">
			<svg t="1578406766476" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9402" width="25" height="40"><path d="M450.56 128h61.44v768H450.56zM512 128h61.44v768h-61.44z" p-id="9403" fill="#2c2c2c"></path></svg>
			一秒选花
		</div>
		<div class="scene-list" style="display: flex;">
			<div v-for="item in cateimg.rale" style="display: flex; padding: 2px;  border-radius: 15px; position: relative;">
				<img @click="goToProductList('$event',)" :src="item.img" alt="" style="width: 100%; height: 100%;">
				<span class="scene-item-use-title">{{item.name}}</span>
			</div>
		</div>
		<div class="sace-list" style="display: flex;">
			<div v-for="item in cateimg.sacelist" style="margin: 2px; position: relative; display: flex; border-radius: 10px;">
				<img @click="goToProductList('$event',)" :src="item.img" alt="" style=" width: 100%; height: 100%;">
				<span>{{item.name}}</span>
			</div>
		</div>
		<div class="sace-list1" style="display: flex;">
			<div v-for="item in cateimg.sacelist1" style="margin: 2px; position: relative; display: flex; border-radius: 10px;">
				<img @click="goToProductList('$event',3)" :src="item.img" alt="" style=" width: 100%; height: 100%;">
				<span>{{item.name}}</span>
			</div>
		</div>
		<div class="product" style="padding: 0 8px 25px;">
			<h2 style="padding: 20px;">送恋人/爱情鲜花</h2>
			<div v-for="item in cateimg.product" style="display: flex;">
				<div class="left" style="width: 40%; border-radius: 10px;">
					<img  @click=goToDetail(item.ItemCode) :src="item.url" alt="" style="width: 100%;">
				</div>
				<div class="right" style="width: 60%;; padding: 0 20px; text-align: left;">
					<h3 style=" padding: 15px 0px;">{{item.Cpmc}}</h3>
					<p>{{item.Instro}}</p>
					<div style="display: flex; ">
						<div class="left" style="width: 80%; display: flex; flex-wrap: wrap; ">
							<h2 style="color: #ED6A0C;">￥{{item.Price}} </h2><s style="padding: 10px 10px; font-size: 8px;">原价：{{item.LinePrice}}</s>
							<h5>已销售{{item.Sales}}件</h5>
						</div>
						<div class="right" style="width: 20%; line-height: 80px;">
							<img src="/img/购物车.png" alt="" style="width: 80%; vertical-align: middle; margin-left: 10px;">
						</div>
					</div>
				</div>
			</div>
		</div>
		<div>
			<van-button @click="goToProductList('$event',4)" type="default">查看更多</van-button>
		</div>
		
		<!-- <div style="height: 1000px;"></div> -->
		
		
	</div>
</template>

<script>
	// @ is an alias to /src
	// import HelloWorld from '@/components/HelloWorld.vue'
	import data from '@/data.js'
	export default {
		name: 'home',
		components: {
			// HelloWorld
		},
		data() {
			return {
				num:100,
				carouselimg:[
					"/carousel-img/01.jpg",
					"/carousel-img/02.jpg",
					"/carousel-img/03.jpg",
					"/carousel-img/04.jpg"
				],
				cateimg:data
			}
		},
		methods: {
			goToCategory() {
				this.$router.push('/Category')
			},
			goToProductList(e,key=0){
				console.log(key)
				this.$router.push("/category?key="+key)
			},
			goToDetail(item){
				this.$router.push('/detail/'+item)
			}
		}
	}
</script>
<style scoped="scoped" lang="less">
	*{
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}

	p{
		font-size: 14px;
		width:100%;
		white-space:nowrap;
		text-overflow:ellipsis;
		overflow:hidden;
		padding: 8px 0px;
	}
	.home{
		margin-bottom: 80px;
		position: relative;
	}
	.header {
		display: flex;
		line-height: 48px;
		height: 48px;
		background-color: #435448;
		
		.left {
			margin: 0 10px;
			width: 20%;

			img {
				height: 26px;
				vertical-align: middle;
			}
		}

		.middle {
			margin: 0 10px;
			width: 60%;

			img {
				height: 22px;
				vertical-align: middle;
				text-align: center;
			}
		}

		.right {
			margin: 0 10px;
			width: 20%;

			img {
				height: 26px;
				vertical-align: middle;
			}
		}
	}

	.authen{
		font-size: 14px;
		display: flex;
		div{
			padding: 6px;
		}
	}
	
	.scene-item-use-title {
	    position: absolute;
	    bottom: 0.28571429rem;
	    left: 0;
	    right: 0;
	    z-index: 1;
	    color: #fff;
	    text-align: center;
	}
	
	.sace-list{
		span{
			height: 19px;
			position: absolute;
			top: 10px;
			left: 0;
			right: 0;
			z-index: 1;
			text-align: center;
			overflow: hidden;
			color: #000;
			font-size: 14px;
		}
	}
	
	.sace-list1{
		span{
			position: absolute;
		    bottom: 0;
		    left: 0;
		    right: 0;
		    background: rgba(35, 38, 40, 0.8);
		    color: #fff;
		    text-align: center;
		    font-size: 14px;
		    padding: 0.28571429rem 0;
		}
		
	}
</style>
