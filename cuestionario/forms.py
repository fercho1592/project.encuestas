from django import forms

from .models import Respuesta, Pregunta, Cuestionario

class RespuestaForm(forms.ModelForm):
	class Meta:
		model = Respuesta

		fields = [
			'texto',
		]

		labels = {
			'texto': 'Respuesta',
		}

		widgets = {
			'texto': forms.TextInput(attrs={'class':'form-control'}),
		}

class PreguntaForm(forms.ModelForm):
	class Meta:
		model = Pregunta

		fields = [
			'texto',
			'respuestas',
		]

		labels = {
			'texto':'Pregunta',
			'respuestas':'Respuestas',
		}

		widgets = {
			'texto':forms.TextInput(attrs={'class':'form-control'}),
			'respuestas':forms.Select(attrs={'class':'form-control'}),
		}

class CuestionarioForm(forms.ModelForm):
	class Meta:
		model = Cuestionario

		fields=[
			'nombre',
			'preguntas',
		]

		labels = {
			'nombre':'Cuestionario',
			'preguntas': 'Preguntas',
		}

		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'preguntas': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
		}