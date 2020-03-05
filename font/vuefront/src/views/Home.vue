<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
        <div class="category">
            <van-cell v-for="item in categorys" :title="item.name" is-link :to="'categorys/'+item.id+'/'"/>
        </div>

        <div>
            <van-field v-model="categoryName" type="tel" label="创建分类名" />
<!--            <br>-->
            <van-button type="primary" @click="requestCreateCategory">创建分类</van-button>

        </div>
<!--        <div>-->
<!--            <button @click="requestCategoryList">发起请求商品列表</button>-->
<!--        </div>-->
<!--        <div>-->
<!--            <label for="">需要修改的分类id：</label> <input type="text" v-model="newCategoryId">-->
<!--            <br>-->
<!--            <label for="">需要修改的分类名字：</label> <input type="text" v-model="newCategoryName">-->
<!--            <br>-->
<!--            <button @click="requestModifyCategory">需要修改的分类</button>-->
<!--        </div>-->
<!--        <div>-->
<!--            <label for="">用户名：</label> <input type="text" v-model="username">-->
<!--            <br>-->
<!--            <label for="">密 码：</label> <input type="text" v-model="password">-->
<!--            <br>-->
<!--        </div>-->
    </div>
</template>

<script>
    // @ is an alias to /src
    import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'Home',
        data() {
            return {
                categorys: [],
                categoryName: '',
                // newCategoryId:"",
                // newCategoryName:"",
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
                    if (res.status == 200) {
                        this.categorys = res.data;
                    }
                }).catch(err => {
                    console.log('发生错误', err)
                });
            },

            requestCreateCategory() {
                if (this.categoryName != '') {
                    this.$api.createCategory({
                        name: this.categoryName
                    }).then(res => {
                        console.log('创建结果', res);
                        this.categorys.push(res.data);
                        // this.categoryName
                    }).catch(err => {
                        console.log('出错了', err)
                    })
                } else {
                    this.$toast("必须输入分类名");
                    console.log('必须输入分类名')
                }
            },
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
