import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Search from '../views/Search.vue'
import Detail from '../views/Detail.vue'
import Mine from '../views/Mine.vue'
import Cart from '../views/Cart.vue'
import Category from '../views/Category.vue'
import ProductList from '../views/Category.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/productlist',
    name: 'productlist',
    component: ProductList
  },
  {
    path: '/detail/:ItemCode',
    name: 'detail',
    component: Detail
  },
  {
    path: '/mine',
    name: 'mine',
    component: Mine,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/category',
    name: 'category',
    component: Category,
	meta:{
		tabbar:true
	}
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  routes,
  scrollBehavior(){
	  return {x:0,y:0}
  }
})

export default router
