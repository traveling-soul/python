from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'cart'
urlpatterns = [
    url(r'^add/$', views.CartAddView.as_view(), name='add'),
	url(r'^count/$', views.CartCountView.as_view(), name='count'),
	url(r'^info/$', login_required(views.CartInfoView.as_view()), name="info"),
	url(r'^update/$', views.CartUpdateView.as_view(), name='update'),
	url(r'^delete/$', views.CartDeleteView.as_view(), name='delete'),
    url(r'^get_cart_count/$', views.get_cart_count, name='get_cart_count'),
]
