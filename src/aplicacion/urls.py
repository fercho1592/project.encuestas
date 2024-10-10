from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^P1/(?P<nombre>[a-zA-Z]+)/$', views.P1, name='p1'),
]
