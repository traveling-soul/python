from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^regist/$', views.regist),
    url(r'^regist_handler/$', views.regist_handler),
    url(r'^check_username/$', views.check_username),
    url(r'^login/$', views.login),
    url(r'^login_handler/$', views.login_handler),
    url(r'^verification_code/$', views.verification_code),
    url(r'^login_out/$', views.login_out),
]