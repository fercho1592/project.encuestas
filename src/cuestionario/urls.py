from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^respuesta/$', views.NuevaRespuesta, name='nuevaRespuesta'),
    re_path(r'^respuesta/(?P<pk>[0-9]+)$', views.EditaRespuesta, name='editaRespuesta'),
    re_path(r'^pregunta/$',views.NuevaPregunta, name="NuevaPregunta"),
    re_path(r'^pregunta/(?P<pk>[0-9]+)$',views.EditaPregunta, name="EditaPregunta"),
    re_path(r'^nuevoCuestionario/$',views.NuevoCuestionario, name="nuevoCuestionario"),
    re_path(r'^(?P<pk>[0-9]+)$',views.EditaCuestionario, name="editaCuestionario"),
]