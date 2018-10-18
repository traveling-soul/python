from django.conf.urls import url
from . import views

app_name = 'food'
urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<goods_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)/$', views.ListView.as_view(), name='list'),
    url(r'^place_order/$', views.place_order),
]
