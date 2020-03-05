import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 引入请求http模块
// import Axios from 'axios'


// 将Axios注册进VUE的原型  以后项目中就可以使用 this.$http
// Vue.prototype.$http = Axios

import * as api from './api'
Vue.prototype.$api = api

import jsCookie from 'js-cookie'
Vue.prototype.$jsCookie = jsCookie

// 导入vant

import Vant from 'vant';
import 'vant/lib/index.css';
Vue.use(Vant);


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
