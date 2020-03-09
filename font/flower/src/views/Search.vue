<template>
	<div>
		<div class="search">
			<div class="header" >
				<van-nav-bar
				  id="searchdiv"
				
				  left-arrow
				  @click-left="onClickLeft"
				  @click-right="onClickRight"
				>
				
				
				<van-search id="searchinput" slot="title" placeholder="请输入搜索关键词" v-model="value"/>
				 
				<div slot="right" class="right">
					搜索
				</div>
				</van-nav-bar>
				
			</div>
			
			<div class="other">
				<img src="" alt="">
				<h3 style="padding: 20px 10px; color: #ED6A0C;">热门搜索</h3>
				<div class="img1">
					<img src="https://img02.hua.com/m/category/Classification/flower.png?v" alt="" style="width: 100%; ">
				</div>
				<div class="searchhot">
						<van-tag class='searchitem' @click="searchHot(item)"  v-for="item in 19" >搜索{{item}}</van-tag>
				</div>
			</div>
			
		</div>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				value:"",

				historySearch: JSON.parse(localStorage.getItem("historySearch"))||[]
			}
		},
		computed:{
			searchHistory(){
				return this.historySearch
			}
		},
		methods:{
			onClickLeft() {
			  this.$router.go(-1)
			},
			onClickRight() {
				if(this.value.length<=0){
					this.$toast("请输入搜索内容")
				}
				else{
					this.historySearch.unshift(this.value);
					localStorage.setItem("historySearch",JSON.stringify(this.historySearch))
					this.$toast(`搜索了${this.value}`);
					this.value=null;
				}
			},
			searchHot(item){
				this.$toast(`搜索了${item}`);
			}
		}
	}
</script>

<style scoped="scoped" long="less">
	*{
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}

	.header{
		#searchdiv{
			background-color: #f2f2f2;
		}
		.van-search .van-cell{
			padding: 0;
		}
	}
	.other{
		display: flex;
		flex-wrap: wrap;
		color: #000000;

	}
	.searchhot{
		padding: 20px 0px;
	}
</style>
<style lang="less">
	.van-tag{
		background-color: #969799;
		margin: 5px;
		padding: 30px;
	}
</style>
