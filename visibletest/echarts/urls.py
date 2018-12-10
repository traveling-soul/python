"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/5/6'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/$', views.index),
    url(r'scatter_sales/$', views.scatter_sales),
    url(r'get_scatter/$', views.get_scatter),
    url(r'province_sales/$', views.province_sales),
    url(r'get_province/$', views.get_province),
    url(r'pie_sales/$', views.pie_sales),
    url(r'get_pie/$', views.get_pie),
]