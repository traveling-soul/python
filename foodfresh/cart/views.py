from django.shortcuts import render
from food.models import GoodsSKU
from django.conf import settings
from django.views.generic.base import View
from django.http import JsonResponse

# Create your views here.


class CartAddView(View):
	def post(self, request):
		user = request.user
		print(user)
		if not user.is_authenticated:
			return JsonResponse({'res': 0, 'errmsg': '请先登录'})

		sku_id = request.POST.get('sku_id')
		count = request.POST.get('count')
		
		if not all([sku_id, count]):
			return JsonResponse({'res': 1, 'errmsg': '数据不完整'})
		
		try:
			count = int(count)
		except Exception as e:
			return JsonResponse({'res': 2, 'errmsg': '商品数目出错了'})

		try:
			sku = GoodsSKU.objects.get(id=sku_id)
		except GoodsSKU.DoesNotExist:
			return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

		conn = settings.REDIS_CONN
		cart_key = 'cart_%d' % user.id
		cart_count = conn.hget(cart_key, sku_id)
		if cart_count:
			count += int(cart_count)

		if count > sku.stock:
			return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})
		
		conn.hset(cart_key, sku_id, count)
		total_count = get_cart_count(user)

		return JsonResponse({'res': 5, 'total_count': total_count, 'message': '添加成功'})


class CartCountView(View):
	def get(self, request):
		total_count = get_cart_count(request.user)
		return JsonResponse({'total_count':total_count})


class CartInfoView(View):
	def get(self, request):
		user = request.user
		conn = settings.REDIS_CONN
		cart_key = 'cart_%d' % user.id
		#{'商品id':商品数量,...}
		cart_dict = conn.hgetall(cart_key)
		print(cart_dict)

		skus = []
		#保存用户购物车中商品的总数目和总价格
		total_count = 0
		total_price = 0
		for sku_id, count in cart_dict.items():
			sku = GoodsSKU.objects.get(id=sku_id)
			amount = sku.price * int(count)
            #动态绑定总价属性、总数目属性
			sku.amount = amount
			sku.count = int(count)
			#添加到列表中
			skus.append(sku)

			#累加计算商品的总数目、总价格
			total_count += int(count)
			total_price += amount

		context = {
			'total_count': total_count,
			'total_price': total_price,
			'skus': skus,
			'title': '购物车'
		}

		return render(request, 'cart.html', context)


class CartUpdateView(View):
	def post(self, request):
		user = request.user
		if not user.is_authenticated:
			return JsonResponse({'res': 0, 'errmsg': '请先登录'})

		#获取数据
		sku_id = request.POST.get('sku_id')
		count = request.POST.get('count')
		print(count)

		#数据校验
		if not all([sku_id, count]):
			return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

		try:
			count = int(count)
		except Exception as e:
			return JsonResponse({'res': 2, 'errmsg': '商品数目出错了'})

		try:
			sku = GoodsSKU.objects.get(id=sku_id)
		except GoodsSKU.DoesNotExist:
			return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

		#更新
		conn = settings.REDIS_CONN
		cart_key = 'cart_%d' % user.id
		if count > sku.stock:
			return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})
		
		conn.hset(cart_key, sku_id, count)
		total_count = get_cart_count(user)
		print(total_count)

		return JsonResponse({'res': 5, 'total_count': total_count, 'message': '更新成功'})


class CartDeleteView(View):
	def post(self, request):
		user = request.user
		if not user.is_authenticated:
			return JsonResponse({'res': 0, 'errmsg': '请先登录'})
	
		sku_id = request.POST.get('sku_id')

		if not sku_id:
			return JsonResponse({'res': 1, 'errmsg': '无效的商品id'})

		try:
			sku = GoodsSKU.objects.get(id=sku_id)
		except GoodsSKU.DoesNotExist:
			return JsonResponse({'res': 2, 'errmsg': '商品不存在'})

		conn = settings.REDIS_CONN
		cart_key = 'cart_%d' % user.id
		conn.hdel(cart_key, sku_id)	
	
		total_count = get_cart_count(user)

		return JsonResponse({'res': 3, 'total_count': total_count, 'message': '删除成功'})


def get_cart_count(user):
	total_count = 0
	if user.is_authenticated:
		conn = settings.REDIS_CONN
		cart_key = 'cart_%d' % user.id
		cart_dict = conn.hgetall(cart_key)\

		for sku_id, count in cart_dict.items():
			total_count += int(count)
	return total_count
