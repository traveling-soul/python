from . import views
from django.conf.urls import url


urlpatterns = [
    # url(r'^regist/$', views.regist),
    # url(r'^regist_handler/$', views.regist_handler),
    url(r'^regist/$', views.RegistView.as_view()),
    url(r'^check_username/$', views.check_username),
    # url(r'^login/$', views.login),
    # url(r'^login_handler/$', views.login_handler),
    url(r'^login', views.LoginView.as_view()),
    url(r'^verification_code/$', views.verification_code),
    # url(r'^login_out/$', views.login_out),
    url(r'^log_out/$', views.LogutView.as_view()),
]

