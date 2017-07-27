from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^P1/(?P<nombre>[a-zA-Z]+)/$', views.P1, name='p1'),
]
