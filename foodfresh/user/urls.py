from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^register/$', views.Register.as_view()),
    url(r'^active/(.*)/$', views.ActiveView.as_view()),
    url(r'^check_uname/$', views.check_uname),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^user_response/$', views.user_response),
    url(r'^code_response/$', views.code_response),
    url(r'^verification_code/$', views.verification_code),
    url(r'^info/$', login_required(views.UserInfoView.as_view()), name='info'),
    url(r'^order/$', login_required(views.UserOrderView.as_view()), name='order'),
    url(r'^site/$', login_required(views.UserAddressView.as_view()), name='site'),
    url(r'^edit_site/(\d+)/$', login_required(views.EditAddressView.as_view()), name='edit_site'),
    url(r'^del_site/(\d+)$', views.del_site),
    url(r'^site_response/$', views.site_response),
    url(r'^pwd/$', login_required(views.ChangePwdView.as_view()), name='pwd'),
    url(r'^test/$', views.test),
]
