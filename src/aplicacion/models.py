from django.db import models
from cuestionario.models import Respuesta, Pregunta, Cuestionario

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=100, verbose_name='Nombre');
	#Otros detalles (sin importancia por ahora)

	def __str__(self):
		return self.nombre

class Quiz(models.Model):
	cuestionario = models.ForeignKey(Cuestionario,models.CASCADE)
	usuario = models.ForeignKey(Usuario,models.CASCADE)
	fecha = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.usuario.nombre + "_" +self.cuestionario.nombre + "_"+str(self.fecha)

class Answer(models.Model):
	quiz = models.ForeignKey(Quiz,models.CASCADE)
	pregunta = models.ForeignKey(Pregunta,models.CASCADE)
	respuesta = models.ForeignKey(Respuesta,models.CASCADE)

	def __str__(self):
		return self.pregunta.texto+" : "+self.respuesta.texto