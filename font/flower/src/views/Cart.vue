<template>
	<div class="cart">
		<van-nav-bar class="header"
		  title="购物车"
		  left-arrow
		  @click-left="onClickLeft"
		  @click-right="onClickRight"
		>
		 <van-icon name="search" slot="right" />
		</van-nav-bar>
		<div v-if="state == null">
			<van-cell title="登录后享受更多优惠" is-link value="去登录" to="/mine"/>
		</div>
		
		
		<div class="middle" v-for="(item,index) in this.$store.getters.getGoodList" :key="index">
			<van-card
			  :num="item.num"
			  :price="item.data.Price"
			  :desc="item.data.Instro"
			  :title="item.data.Cpmc"
			  :thumb="item.data.img"
			>
			 <van-stepper @change="change(index,item.num)"  v-model="item.num" slot="bottom" />
			</van-card>
		
		</div>
		<div class="bottom" >
			<van-submit-bar
			  :price="allprice"
			  button-text="提交订单"
			  @submit="onSubmit"
			/>
		</div>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				num:0,
				allprice:0,
				state:localStorage.getItem("login")
			}
		},
		created() {
			this.allPrice();
		},

		methods:{
			onSubmit(){
				if(this.allprice==0){
					this.$toast("请先挑选商品")
				}
				else{
					this.$store.commit("empty");
					this.allprice=0;
					this.$toast("提交成功")
					
				}
			},
			allPrice(){
				let all=0;
				this.$store.getters.getGoodList.forEach(item=>{
					all+=item.num*item.data.Price
				})
				this.allprice=all*100;
				
			},
			change(index,num){
				console.log(num,index);
				this.$store.commit("changeGoodNum",[index,num]);
				this.allPrice();
			},
		
			onClickLeft() {
				this.$router.go(-1);
						
			},
			onClickRight() {
				this.$router.push("/search")
			}
		}
	}
</script>

<style lang="less">
	.van-cell {
	    padding: 10px;
	    font-size: 15px;
	    font-weight: 550;
	}
</style>

<style scoped="scoped" lang="less">
	.cart{
		margin-bottom: 80px;
		position: relative;
	}
</style>
