<template>
	<div class="hoe">
		<div class="he">
			<van-nav-bar title="分类" left-arrow @click-left="onClickLeft()"@click-right="onClickRight()" class='din'>
				<van-icon name="search" slot="right" />
			</van-nav-bar>
			
		</div>
		<div class="body">
			<div class='left'>
				<van-sidebar v-model="activeKey"  class='cl'>
					<van-sidebar-item v-for='i in list' :title="i" />
				</van-sidebar>
			</div>
			<div class="right">		
				
					<div v-for="(a,b) in img[activeKey]" class="divk" @click="detail(activeKey,b)">
						<van-card
						  tag="特价"
						  :price='dict[activeKey].Datas.ProductPrices[b].Price'
						  desc="女友/爱人/表白"
						  :title="dict[activeKey].Datas.ProductPrices[b].Cpmc"
						  :origin-price="dict[activeKey].Datas.ProductPrices[b].LinePrice"
						  :thumb="a"
						  class='k1'>
						</van-card>
					</div>
					<p style=" font-size:5px;">亲,到底了,定制可联系客服!</p>
					<br>
				
			</div>
		</div>
	</div>
</template>
<script>
export default {
  name: 'hoe',
  components: {
  },
  created(){this.activeKey=this.$route.params.id},
  data(){return{
	  activeKey:0,
	  list:['鲜花','永生花','蛋糕','礼品','盆栽,'],
	  img:[
		[ "./Buyimg/1.jpg", "./Buyimg/2.jpg", "./Buyimg/3.jpg", "./Buyimg/4.jpg","./Buyimg/5.jpg","./Buyimg/6.jpg", "./Buyimg/7.jpg", "./Buyimg/8.jpg", "./Buyimg/9.jpg","./Buyimg/10.jpg"],  
		[ "./img2/1.jpg","./img2/2.jpg","./img2/3.jpg","./img2/4.jpg","./img2/5.jpg"],
	    [ "./img3/1.jpg","./img3/2.jpg","./img3/4.jpg","./img3/5.jpg","./img3/6.jpg"],
		[ "./img4/1.jpg","./img4/2.jpg","./img4/3.jpg","./img4/4.jpg","./img4/5.jpg","./img4/6.jpg","./img4/7.jpg"],
		[ "./img5/1.jpg","./img5/2.jpg","./img5/3.jpg","./img5/4.jpg","./img5/5.jpg","./img5/6.jpg","./img5/7.jpg"],
	  ],
	  dict:
	  [{"Status":"0","ErrMsg":null,"DataStatus":200,"Datas":{"ProductPrices":[{"ItemCode":"9010966","Price":239,"LinePrice":315,"Cpmc":"一往情深","Instro":"精品玫瑰礼盒:19枝红玫瑰，勿忘我0.1扎","Sales":"7.5万"},{"ItemCode":"9012009","Price":298,"LinePrice":382,"Cpmc":"忘情巴黎","Instro":"33枝红玫瑰","Sales":"6.5万"},{"ItemCode":"9012243","Price":198,"LinePrice":255,"Cpmc":"恋恋情深","Instro":"11枝香槟玫瑰，白色多头百合2枝","Sales":"7.2万"},{"ItemCode":"9012177","Price":539,"LinePrice":766,"Cpmc":"不变的承诺","Instro":"99枝红玫瑰","Sales":"6.2万"},{"ItemCode":"9012154","Price":368,"LinePrice":485,"Cpmc":"甜美公主","Instro":"白玫瑰22枝，粉佳人粉玫瑰14枝，粉色桔梗5枝","Sales":"2.2万"},{"ItemCode":"9012089","Price":389,"LinePrice":479,"Cpmc":"爱在心头","Instro":"玫瑰50枝：戴安娜粉玫瑰19枝，红玫瑰31枝","Sales":"1.9万"},{"ItemCode":"9010011","Price":139,"LinePrice":189,"Cpmc":"一心一意","Instro":"玫瑰11枝，粉色勿忘我0.3扎","Sales":"11.1万"},{"ItemCode":"9010969","Price":248,"LinePrice":331,"Cpmc":"你最珍贵","Instro":"精品玫瑰礼盒:香槟玫瑰19枝，勿忘我适量","Sales":"5.7万"},{"ItemCode":"9012441","Price":198,"LinePrice":256,"Cpmc":" 语笑嫣然","Instro":"粉佳人玫瑰9枝、粉色小菊、洋桔梗、尤加利叶","Sales":"1427"},{"ItemCode":"9010731","Price":196,"LinePrice":281,"Cpmc":"牵手一生","Instro":"红玫瑰19枝","Sales":"6.1万"},{"ItemCode":"9012055","Price":469,"LinePrice":601,"Cpmc":"不变的心","Instro":"戴安娜玫瑰66枝","Sales":"1.1万"},{"ItemCode":"9010917","Price":639,"LinePrice":859,"Cpmc":"永恒的爱情","Instro":"红玫瑰99枝","Sales":"3829"}]},"HuaSessionId":null},
	  {"Status":"0","ErrMsg":null,"DataStatus":200,"Datas":{"ProductPrices":[{"ItemCode":"1073263","Price":398,"LinePrice":498,"Cpmc":"永生花满月艺术台灯/朦胧粉","Instro":"永生花台灯","Sales":"70"},{"ItemCode":"1073247","Price":298,"LinePrice":398,"Cpmc":"花好月圆永生花台灯","Instro":"精选进口奥斯汀永生玫瑰台灯","Sales":"793"},{"ItemCode":"1073186","Price":588,"LinePrice":788,"Cpmc":"我如此爱你-口红款520","Instro":"Dior#520口红(专柜正品)＋进口永生玫瑰礼盒","Sales":"1261"},{"ItemCode":"1073264","Price":298,"LinePrice":398,"Cpmc":"一鹿(路)有你永生花小夜灯","Instro":"永生花礼盒","Sales":"70"},{"ItemCode":"1060030","Price":268,"LinePrice":399,"Cpmc":"美丽无限/三色玫瑰","Instro":"泰国进口保鲜花 三色玫瑰精妙搭配 保质期5年以上","Sales":"958"},{"ItemCode":"1073244","Price":398,"LinePrice":498,"Cpmc":"永生花带灯+蓝牙音箱/浪漫粉","Instro":"看得到的美好，听得到的浪漫！","Sales":"1677"},{"ItemCode":"1073120","Price":368,"LinePrice":468,"Cpmc":"时光的花","Instro":"复古相框 ,进口粉色玫瑰2枝 ,进口紫色玫瑰1枝","Sales":"2141"},{"ItemCode":"1073033","Price":198,"LinePrice":259,"Cpmc":"一生一世","Instro":"厄瓜多尔进口永生红玫1朵，双色永生绣球","Sales":"1.2万"},{"ItemCode":"1073209","Price":298,"LinePrice":499,"Cpmc":"花漾蜜恋·少女粉","Instro":"音乐球永生花礼盒，创意礼物","Sales":"312"},{"ItemCode":"1060022","Price":489,"LinePrice":688,"Cpmc":"斜口瓶花","Instro":"真空保鲜花，彩玫系列，5年不凋谢","Sales":"4793"},{"ItemCode":"1073137","Price":368,"LinePrice":498,"Cpmc":"公主的音乐水晶球·红玫瑰","Instro":"大型水晶音乐球永生花","Sales":"584"},{"ItemCode":"1060002","Price":228,"LinePrice":368,"Cpmc":"我爱你","Instro":"不凋谢的玫瑰 红玫瑰系列 最佳送女友礼物","Sales":"1.4万"}]},"HuaSessionId":null},
	  {"Status":"0","ErrMsg":null,"DataStatus":200,"Datas":{"ProductPrices":[{"ItemCode":"5010041","Price":178,"LinePrice":208,"Cpmc":"陪伴左右","Instro":"2磅(8寸)水果蛋糕","Sales":"5450"},{"ItemCode":"5010042","Price":179,"LinePrice":209,"Cpmc":"鲜果缤纷","Instro":"2磅(8寸)水果蛋糕","Sales":"3185"},{"ItemCode":"5010025","Price":178,"LinePrice":208,"Cpmc":"心之恋曲","Instro":"2磅(8寸)鲜奶水果蛋糕","Sales":"1546"},{"ItemCode":"5010046","Price":179,"LinePrice":209,"Cpmc":"水果盛宴","Instro":"2磅(8寸)水果蛋糕","Sales":"3675"},{"ItemCode":"5010020","Price":168,"LinePrice":178,"Cpmc":"蓝玫瑰鲜奶","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"1.3万"},{"ItemCode":"5010044","Price":179,"LinePrice":209,"Cpmc":"欢声乐语","Instro":"2磅(8寸)水果蛋糕","Sales":"2055"},{"ItemCode":"5010045","Price":179,"LinePrice":209,"Cpmc":"美好回忆","Instro":"2磅(8寸)水果蛋糕","Sales":"1343"},{"ItemCode":"5010034","Price":168,"LinePrice":178,"Cpmc":"幸福时刻","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"6520"},{"ItemCode":"5010027","Price":178,"LinePrice":188,"Cpmc":"我的心属于你","Instro":"8寸(2磅)鲜奶水果蛋糕","Sales":"5213"},{"ItemCode":"5010043","Price":179,"LinePrice":209,"Cpmc":"纯洁挚爱","Instro":"2磅(8寸)水果蛋糕","Sales":"3491"},{"ItemCode":"5010031","Price":168,"LinePrice":178,"Cpmc":"I LOVE YOU","Instro":"8寸(2磅)心形鲜奶蛋糕","Sales":"5943"},{"ItemCode":"5014011","Price":168,"LinePrice":178,"Cpmc":"心相印","Instro":"8寸(2磅)心形粉色鲜奶蛋糕","Sales":"4767"}]},"HuaSessionId":null},
	  {"Status":"0","ErrMsg":null,"DataStatus":200,"Datas":{"ProductPrices":[{"ItemCode":"1076078","Price":1580,"LinePrice":1680,"Cpmc":"Dior烈艳蓝金唇膏烟花限量版套装","Instro":"高订套装饰以璀璨烟花，一套汇集6款明星色号，打造百变妆容 演绎百变魅力","Sales":"81"},{"ItemCode":"1076084","Price":1099,"LinePrice":1199,"Cpmc":"Dior迪奥真我香氛礼盒(圣诞限量版)","Instro":"原产法国真我精选：迪奥真我香氛、迪奥全新真我香调身体乳","Sales":"303"},{"ItemCode":"1087022","Price":228,"LinePrice":368,"Cpmc":"布蕾兔暖水袋","Instro":"寒潮中的法式温暖","Sales":"661"},{"ItemCode":"1076062","Price":198,"LinePrice":298,"Cpmc":"星期耳钉礼盒","Instro":"s925银个性耳钉","Sales":"1194"},{"ItemCode":"1076057","Price":2399,"LinePrice":2480,"Cpmc":"施华洛世奇DAZZLING SWAN手链+项链套装","Instro":"浪漫天鹅  项链+手链套装饰品 镀玫瑰金色","Sales":"35"},{"ItemCode":"1087028","Price":129,"LinePrice":229,"Cpmc":"素乐Line联名暖手宝充电宝-可妮兔","Instro":"USB暖手宝 Line Friends定制款","Sales":"60"},{"ItemCode":"1077011","Price":198,"LinePrice":298,"Cpmc":"woody书灯木质led折叠usb书本灯-时尚版（黑胡桃）","Instro":"","Sales":"193"},{"ItemCode":"1076080","Price":968,"LinePrice":1290,"Cpmc":"施华洛世奇跳动的心项链/镀玫瑰金色","Instro":"SPARKLING DC系列新品项链，专柜正品，全国联保","Sales":"59"},{"ItemCode":"1070072","Price":169,"LinePrice":269,"Cpmc":"MUID化妆镜台灯 / 藕色","Instro":"藕色","Sales":"184"},{"ItemCode":"1076083","Price":259,"LinePrice":359,"Cpmc":"T400双C银项链女纯银锁骨链镶施华洛世奇锆","Instro":"双C系列新品，精美苹果礼盒，s925银项链 ","Sales":"305"},{"ItemCode":"1076082","Price":189,"LinePrice":289,"Cpmc":"生肖鼠项链礼盒","Instro":"s925银本命鼠项链","Sales":"302"},{"ItemCode":"1077022","Price":1099,"LinePrice":1199,"Cpmc":"猫王·乌托邦 复古蓝牙音箱 MW-6","Instro":"猫王乌托邦FM复古蓝牙音箱复古收音机音响（胡桃木）","Sales":"55"}]},"HuaSessionId":null},
	  {"Status":"0","ErrMsg":null,"DataStatus":200,"Datas":{"ProductPrices":[{"ItemCode":"6010603","Price":558,"LinePrice":598,"Cpmc":"蝴蝶兰6株","Instro":"蝴蝶兰-室内盆栽（6株红色一品蝴蝶兰）","Sales":"1459"},{"ItemCode":"6010621","Price":338,"LinePrice":398,"Cpmc":"蝴蝶兰4株","Instro":"蝴蝶兰-室内盆栽（4株紫色一品蝴蝶兰）","Sales":"923"},{"ItemCode":"6010611","Price":498,"LinePrice":560,"Cpmc":"纯洁天使","Instro":"蝴蝶兰（5株白色一品蝴蝶兰）","Sales":"397"},{"ItemCode":"6010612","Price":899,"LinePrice":999,"Cpmc":"十全十美","Instro":"蝴蝶兰- 室内盆栽（10株红色一品蝴蝶兰）。 ","Sales":"1060"},{"ItemCode":"6010605","Price":498,"LinePrice":538,"Cpmc":"蝴蝶兰5株","Instro":"蝴蝶兰- 室内盆栽(紫蝴蝶兰3株、浅粉蝴蝶兰2株)。","Sales":"614"},{"ItemCode":"6010606","Price":452,"LinePrice":498,"Cpmc":"迎福纳祥","Instro":"5株粉红色一品蝴蝶兰。(开花期3个月以上)","Sales":"1423"},{"ItemCode":"6010613","Price":218,"LinePrice":238,"Cpmc":"吉祥如意","Instro":"蝴蝶兰- 室内盆栽（2株紫红色蝴蝶兰）。 ","Sales":"1826"},{"ItemCode":"6010602","Price":658,"LinePrice":698,"Cpmc":"蝴蝶兰7株","Instro":"蝴蝶兰7株- 室内盆栽","Sales":"114"},{"ItemCode":"6010167","Price":69,"LinePrice":169,"Cpmc":"遇见","Instro":"手作景观多肉盆栽","Sales":"269"},{"ItemCode":"6010159","Price":129,"LinePrice":129,"Cpmc":"爱琴海／蓝纹","Instro":"手作景观多肉盆栽","Sales":"39"},{"ItemCode":"6010164","Price":199,"LinePrice":299,"Cpmc":"真心","Instro":"手作景观多肉盆栽","Sales":"128"},{"ItemCode":"6010163","Price":119,"LinePrice":119,"Cpmc":"棉花堡","Instro":"手作景观多肉盆栽","Sales":"38"}]},"HuaSessionId":null},
	  ],
	  }},
  methods:{
  	onClickLeft(){this.$router.go(-1)},
	onClickRight(){this.$router.push('/Sou')},
	sen(a,b){if(a=="product"){this.$router.push(`/About/${b}`)}},
	detail(a,b){this.$router.push(`/About/${a}/${b}`)}
		
	},
}
</script>

<style scoped="scoped" lang="less">
	*{margin: 0;}
	.he{
		position: sticky;
		top: 0;
		 margin: -5px 0;
	}

	.body{
		.left{
			position: absolute;
			top: 40px;
			left: 0px;
			bottom: 40px;
			width: 25%;
			overflow: auto;
			text-align: center;
		}
		.left::-webkit-scrollbar {display:none}
		.right{
			position: absolute;
			top: 40px;
			left: 25%;
			bottom: 40px;			
			overflow: auto;
		}
		.right::-webkit-scrollbar {display:none}
		span{ display:block;  font-size:3px;}
		.divk{width: 100%;}
		.k1{display: block;width: 100%;}	}
</style>
