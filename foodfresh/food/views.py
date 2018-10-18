from django.shortcuts import render, redirect
from foodfresh.myutil import login_wrapper
from .models import *
from django.conf import settings
from django.views.generic.base import View
from django.core.paginator import Paginator
from cart.views import get_cart_count


# Create your views here.


class IndexView(View):
	def get(self, request):
		user = request.user
		types = GoodsType.objects.all()
		#轮播类
		good_banners = IndexGoodsBanner.objects.all().order_by('index')
		#活动类
		promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

		for type in types:
		    image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
		    title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

		    #动态添加标题和图片属性
		    type.image_banners = image_banners
		    type.title_banners = title_banners

		if user.is_authenticated:
			cart_count = get_cart_count(user)
		else:
			cart_count = 0

		context = {
			'titel':'首页',
			'user':user,
			'types':types,
			'good_banners':good_banners,
			'promotion_banners':promotion_banners,
			'cart_count':cart_count
			}
		return render(request, 'index.html' ,context)



class DetailView(View):
	def get(self, request, goods_id):
		login_name = request.session.get('login_name','')

		try:
			sku = GoodsSKU.objects.get(id=goods_id)
		except GoodsSKU.DoesNotExist:
		    return redirect(reverse('food:index'))

		#新品推荐
		new_skus = GoodsSKU.objects.filter(type=sku.type).exclude(id=goods_id).order_by('-create_time')[:2]

		#获取同一个SPU的其他规格商品，后期拓展
		same_spu_skus = GoodsSKU.objects.filter(goods=sku.goods).exclude(id=goods_id)

		user = request.user
		#购物车
		cart_count = 0
		#如果用户已经登录
		if user.is_authenticated:
			cart_count = get_cart_count(user)			

			#添加用户的历史记录
			conn = settings.REDIS_CONN
			history_key = 'history_%d' % user.id
			#移除列表中的goods_id
			conn.lrem(history_key, 0, goods_id) 
			#把goods_id插入到列表的左侧
			conn.lpush(history_key, goods_id)
		    #只保存用户最新浏览的5条信息
			conn.ltrim(history_key, 0, 4)

		context = {
		    'title': '商品详情', 
		    'login_name':login_name,
		    'sku':sku,
		    'new_skus':new_skus,
            'cart_count': cart_count
		}
		return render(request, 'detail.html', context)


class ListView(View):
    def get(self, request, type_id, page):
        #获取商品的种类信息
        try:
            type = GoodsType.objects.get(id=type_id)
        except GoodsType.DoesNotExist:
            return redirect(reverse('food:index'))

        #获取商品的分类信息
        types = GoodsType.objects.all()
        sort = request.GET.get('sort')
        if sort == 'price':
            skus = GoodsSKU.objects.filter(type=type).order_by('price')
        elif sort == 'hot':
            skus = GoodsSKU.objects.filter(type=type).order_by('-sales')
        else:
            sort = 'default'
            skus = GoodsSKU.objects.filter(type=type).order_by('-id')

        #对数据进行分页
        paginator = Paginator(skus, 1)
        try:
            page = int(page)
        except Exception as e:
            page = 1

        sku_page = paginator.page(page)
		
        #获取第page页的Page实例对象
        num_pages = paginator.num_pages
        if num_pages < 5:
           pages = range(1, num_pages+1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages-4, num_pages+1)
        else:
            pages = range(page-2, page+3)

        #获取新品信息
        new_skus = GoodsSKU.objects.filter(type=type).order_by('-create_time')[:2]

        #获取用户购物车中商品的数目
        cart_count = 0
        context = {
            'title': '商品列表', 
			'type': type,
            'types': types,
            'skus': skus,
            'new_skus': new_skus,
            'cart_count': cart_count,
            'sku_page': sku_page,
            'pages': pages,
            'sort': sort
        }
        return render(request, 'list.html', context)


def place_order(request):
    login_name = request.session.get('login_name', '')
    return render(request, 'place_order.html', {'login_name':login_name})





