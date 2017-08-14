"""Modelos para los Cuestionarios
	Aqui se establecen los modelos 
"""
from django.db import models

class Respuesta(models.Model):
	"""Modelo respuesta

	Este almacena la respuesta
	
	Extends:
		models.Model
	
	Variables:
		texto {string} -- texto de la respuesta
	"""
	texto = models.CharField(max_length=100, verbose_name='Respuesta')


	def __str__(self):
		return self.texto

class Pregunta(models.Model):
	"""[summary]
	
	[description]
	
	Extends:
		models.Model
	
	Variables:
		texto {[type]} -- [description]
		respuestas {[type]} -- [description]
	"""
	texto = models.CharField(max_length=100, verbose_name='Pregunta')
	respuestas = models.ManyToManyField(Respuesta)

	def __str__(self):
		return self.texto

class Cuestionario(models.Model):
	"""[summary]
	
	[description]
	
	Extends:
		models.Model
	
	Variables:
		nombre {[type]} -- [description]
		preguntas {[type]} -- [description]
	"""
	nombre = models.CharField(max_length=50, verbose_name='Cuestionario')
	preguntas = models.ManyToManyField(Pregunta)

	def __str__(self):
		return self.nombre