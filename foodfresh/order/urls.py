from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'food'
urlpatterns = [
	url(r'place', views.OrderPlaceView.as_view(), name='place'),
]
