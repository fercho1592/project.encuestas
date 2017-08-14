from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^rN/$', views.NuevaRespuesta, name='nuevaRespuesta'),
    url(r'^pN/$',views.NuevaPregunta, name="NuevaPregunta"),
    url(r'^nuevoCuestionario/$',views.NuevoCuestionario, name="nuevoCuestionario"),
    
    url(r'^(?P<pk>[0-9]+)$',views.EditaCuestionario, name="editaCuestionario"),
    url(r'^p(?P<pk>[0-9]+)$',views.EditaPregunta, name="EditaPregunta"),
    url(r'^r(?P<pk>[0-9]+)$', views.EditaRespuesta, name='editaRespuesta'),
]