<template>
	<div class="page">
		<div class="header">
			<van-nav-bar title="花礼网" left-text="返回" left-arrow @click-left="$router.go(-1)"  @click-right="$router.push('/search')">
			  <van-icon name="search" slot="right" />
			</van-nav-bar>
		</div>
		<div class="middle">
			<img :src="datas.img" alt="">
			<h3>{{datas.Cpmc}}</h3>
			<p><b>{{datas.Instro}}</b></p>
			<div class="bottom">
				
				
				
				<h3>￥{{datas.Price}}</h3>
				<p style="padding: 23px 0 0px; font-size: 14px;">已销售{{datas.Sales}}件</p>
				<p  style="color: #646566; border-top: 1px #F1F1F1 solid; border-bottom: 1px #F1F1F1 solid;"> <b>特别提醒:</b> <span>仅限联邦快递24小时可达地区,为方便物流的跟踪,请务必填写收件地址的正确邮编,以免造成投递失败。</span></p>
				<!-- <s>{{datas.LinePrice}}</s> -->
				<p><b style="line-height: 51px;">选择购买个数：</b> </p>
				<van-stepper style="line-height: 81px;padding: 0px 130px 0 0px;" v-model="buyNum"/>
			</div>
		</div>
		<div class="base">
			<van-goods-action>
			  <van-goods-action-icon icon="chat-o" text="客服" @click="onClickIcon" />
			  <van-goods-action-icon icon="cart-o" @click="$router.push('/cart')" text="购物车" :info="$store.getters.getGoodList.length"/>
			  <van-goods-action-button type="warning" text="加入购物车" @click="addCart" />
			  <van-goods-action-button type="danger" text="立即购买" @click="onClickButton" />
			</van-goods-action>
		</div>
	</div>
</template>

<script>
	import datae from '../detailData.js'
	export default{
		data(){
			return{
				// activeKey: 0,
				datas:null,
				buyNum:1,
				show:false
			}
		},
		created() {
			this.getdata()
		},
		methods: {
		  onClickIcon() {
		    $router.toast('点击图标');
		  },
		  onClickButton() {
		    $router.toast('点击按钮');
		  },
		  addCart(){
		  	this.show=false
			
			this.$toast("加入成功")
			this.$store.commit("addGood",{ItemCode:this.$route.params.ItemCode,data: this.datas,num:this.buyNum})
		  },

		  getdata(){
			  datae.detailData.forEach(item=>{
				   // console.log(item.ItemCode);
				  if(item.ItemCode==this.$route.params.ItemCode){
				  	  this.datas=item
					  console.log(item.ItemCode);
				  }
			  })
		  },
		}
	}
</script>

<style scoped="scoped" lang="less">
	*{
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}
	.page{
		margin-bottom: 80px;
		position: relative;
	}
	.bottom{
		display: flex;
		flex-wrap: wrap;
		text-align: left;
		justify-content: space-between
		
	}
	h3{
		text-align: left;
		font-weight: 600;
		font-size: 30px;
		padding: 10px 10px;
		color: #FF734C
	}
	p{
		padding: 10px 10px;
		margin: 5px;
		text-align: left;
	}
</style>
