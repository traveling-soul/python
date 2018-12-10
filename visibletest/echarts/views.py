import numpy as np
import pandas as pd
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Goods

name_list = list((Goods.objects.values_list('name')))
price_list = list(Goods.objects.values_list('price'))
sale_list = list(Goods.objects.values_list('sales'))
address_list = list(Goods.objects.values_list('address'))

goods = Goods.objects.all()
name_list = []
price_list = []
sale_list = []
address_list = []
for good in goods:
    name_list.append(good.name)
    price_list.append(good.price)
    sale_list.append(good.sales)
    address_list.append(good.address)

# Create your views here.


def index(request):
    return render(request, 'echarts/index.html')


def scatter_sales(request):
    return render(request, "echarts/scatter.html")


def get_scatter(request):
    return JsonResponse({"price_list": price_list, "sale_list": sale_list})


def province_sales(request):
    return render(request, "echarts/province.html")


def get_province(request):
    # my_dict = {}
    n_address = []
    # for address in address_list:
    #     n_address.append(address.split()[0])
    # for i in range(len(n_address)):
    #     if n_address[i] in my_dict:
    #         my_dict[n_address[i]] = my_dict[n_address[i]] + sale_list[i]
    #     else:
    #         my_dict[n_address[i]] = sale_list[i]
    # my_list = list(my_dict.items())
    # # print(my_list)
    # return JsonResponse({"my_list": my_list})

    for address in address_list:
        n_address.append(address.split()[0])
    dataset = pd.DataFrame({'address': n_address, "sale": sale_list})
    data_p = dataset.groupby('address', as_index=False).mean()
    data_p[['sale']] = data_p[['sale']].apply(np.round)
    my_list = pd.DataFrame(data_p).values.tolist()
    return JsonResponse({"my_list": my_list})


def pie_sales(request):
    return render(request, "echarts/pie_sales.html")


def get_pie(request):
    # my_dict = {}
    n_address = []
    # for address in address_list:
    #     n_address.append(address.split()[0])
    # for i in range(len(n_address)):
    #     if n_address[i] in my_dict:
    #         my_dict[n_address[i]] = my_dict[n_address[i]] + sale_list[i]
    #     else:
    #         my_dict[n_address[i]] = sale_list[i]
    # my_list = list(my_dict.items())
    # # print(my_list)
    # return JsonResponse({"my_list": my_list})

    for address in address_list:
        n_address.append(address.split()[0])
    dataset = pd.DataFrame({'address': n_address, "sale": sale_list})
    data_p = dataset.groupby('address', as_index=False).sum()
    my_list = pd.DataFrame(data_p).values.tolist()
    return JsonResponse({"my_list": my_list})



