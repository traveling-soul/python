from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from food.models import GoodsSKU
from user.models import Address

# Create your views here.


class OrderPlaceView(View):
	"""提交订单页面显示"""
	def post(self, request):
		user = request.user
		sku_ids = request.POST.getlist('sku_ids')
		print(sku_ids)
		
		if not sku_ids:
			return redirect(reverse('cart:info'))
		
		conn = settings.REDIS_CONN
		cart_key = 'cart_%d' % user.id
		
		skus = []
		total_count = 0
		total_price = 0
		for sku_id in sku_ids:
			sku = GoodsSKU.objects.get(id=sku_id)
			count = conn.hget(cart_key, sku_id)
			amount = sku.price * int(count)
			
			sku.count = int(count)
			sku.amount = amount
			skus.append(sku)

			total_count += int(count)
			total_price += amount

		print(skus)
		#运费
		transit_price = 10

        #实付款
		total_pay = total_price + transit_price
		
		addrs = Address.objects.filter(user=user)

		sku_ids = ','.join(sku_ids)

		context = {
			'skus': skus,
			'total_count': total_count,
			'total_price': total_price,
			'transit_price': transit_price,
			'total_pay': total_pay,
			'addrs': addrs,
			'sku_ids': sku_ids,
			'title': '提交订单'
		}

		return render(request, 'place_order.html', context)
