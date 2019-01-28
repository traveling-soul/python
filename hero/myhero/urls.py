from . import views
from django.conf.urls import url

urlpatterns= [
    url(r'^index/$', views.index),
    url(r'^book/$', views.book),
    # url(r'^hero/$', views.hero),
    url(r'^hero_list/$', views.HeroListView.as_view()),
    # url(r'^hero_page/(\d+)$', views.hero_page),
    # url(r'^hero_delete/(?P<pk>\d+)/$', views.hero_delete),
    url(r'^hero_delete/(?P<pk>\d+)/$', views.HeroDeleteView.as_view()),
    # url(r'^hero_edit/(\d+)/$', views.hero_edit),
    # url(r'^hero_edit_handler/(\d+)/$', views.hero_edit_handler),
    url(r'^hero_edit/(?P<pk>\d+)$', views.HeroEditView.as_view()),
    # url(r'^hero_add/$', views.hero_add),
    # url(r'^hero_add_handler/$', views.hero_add_handler),
    url(r'^hero_add/$', views.HeroAddView.as_view()),
]