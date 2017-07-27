from django.contrib import admin

# Register your models here.
from .models import Usuario, Quiz, Answer

admin.site.register(Answer)
admin.site.register(Usuario)
admin.site.register(Quiz)
