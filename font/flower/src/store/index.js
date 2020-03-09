import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	  goodList:[],
  },
  getters:{
	  getGoodList(state){
		  return state.goodList
	  }
  },
  mutations: {
	  empty(state){
		state.goodList=[]
	  },
	  addGood(state,good){
		  let canAdd = true;
		  let index = -1;
		 
		  state.goodList.forEach((item,i)=>{
			  if(item.ItemCode==good.ItemCode){
				  canAdd=false;
				  index = i
			  }
		  })
		  if(canAdd){
			  state.goodList.push(good)
		  }
		  else{
			  state.goodList[index].num+=good.num
		  }
	  },
	  changeGoodNum(state,index_num){
		  console.log(index_num[0],index_num[1]);
		  state.goodList[index_num[0]].num=index_num[1];
	  }
  },
  actions: {
  },
  modules: {
  }
})
