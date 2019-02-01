from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^questioncreate/$', views.QuestionCreate.as_view(), name='QuestionCreate'),
    # url(r'^thanks/$', views.thanks),
    url(r'^thanks/$', views.ThanksView.as_view(), name='ThanksView'),
]