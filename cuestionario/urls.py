from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^respuesta/$', views.NuevaRespuesta, name='nuevaRespuesta'),
    url(r'^respuesta/(?P<pk>[0-9]+)$', views.EditaRespuesta, name='editaRespuesta'),
    url(r'^pregunta/$',views.NuevaPregunta, name="NuevaPregunta"),
    url(r'^pregunta/(?P<pk>[0-9]+)$',views.EditaPregunta, name="EditaPregunta"),
    url(r'^nuevoCuestionario/$',views.NuevoCuestionario, name="nuevoCuestionario"),
    url(r'^(?P<pk>[0-9]+)$',views.EditaCuestionario, name="editaCuestionario"),
]