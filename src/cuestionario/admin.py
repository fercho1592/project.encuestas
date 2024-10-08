from django.contrib import admin

# Register your models here.
from .models import Respuesta, Pregunta, Cuestionario

admin.site.register(Respuesta)
admin.site.register(Pregunta)
admin.site.register(Cuestionario)
