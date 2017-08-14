from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import RespuestaForm, CuestionarioForm, PreguntaForm
from .models import Respuesta, Cuestionario,Pregunta
# Create your views here.

#Ventana principal de la creacion de cuestionarios
#Obtiene los cuestionarios registrados en la base de datos y los pasa a la vista para su despliegue
def index(request):
	cuestionarios = Cuestionario.objects.all()
	return render(request,'cuestionario/index.html',{'cuestionarios':cuestionarios})

#*****************************************************
def NuevaRespuesta(request):
	if request.method != 'POST':
		form = RespuestaForm()
	else:
		form = RespuestaForm(request.POST)
		if form.is_valid():
			form.save()
			form = RespuestaForm()

	return render(request,'cuestionario/respuestaForm.html',{'form':form})

def EditaRespuesta(request, pk):
	r = Respuesta.objects.get(pk=pk)
	if request.method != 'POST':
		form = RespuestaForm(instance=r)
	else:
		form = RespuestaForm(request.POST,instance=r)
		if form.is_valid():
			form.save()

	return render(request,'cuestionario/respuestaForm.html',{'form':form})
#*****************************************************

#Crea un nuevo cuestionario
#Esta vista no se despliega en pantalla, solo guarda la informacion y redirige a edita cuestionario
def NuevoCuestionario(request):
	cues = Cuestionario(nombre = request.POST.get('nombre'))
	cues.save()
	return redirect('/cuestionario/{0}'.format(cues.pk))

#Obtiene y guarda la informacion del cuestionario
#----Falta hacer que obtenga todos los elementos por separado y que cree cada objeto----
#----Checa que si hay un objeto (ya sea pregunta o respuesta) con el mismo texto, que no se escriba en la base de datos-----
def EditaCuestionario(request,pk):
	c = Cuestionario.objects.get(pk=pk)
	preguntas = c.preguntas

	if request.method == 'POST':
		c.nombre = request.POST.get("cuestionario")
		c.save()

	return render(request,'cuestionario/cuestionarioForm.html',{'cuestionario':c, 'preguntas':preguntas})
#*****************************************************

def NuevaPregunta(request):
	preg = Pregunta(texto=request.POST.get('pregunta'))
	preg.save()
	cues = Cuestionario.objects.get(pk=request.POST.get('cuestionario'))
	cues.preguntas.add(preg)

	return redirect('/cuestionario/p{0}'.format(preg.pk))

def EditaPregunta(request,pk):
	p = Pregunta.objects.get(pk=pk)
	rs = p.respuestas.all()

	if request.method == 'POST':
		print("*************************************++")
		p.texto = request.POST.get('pregunta')
		#Compara las preguntas a ver si son las mismas y las que no, las separamos
		#Las que separemos las buscamos en la base de datos y se las asignamos
		#Si no las encuentra crea una nueva y la guarda en la base de datos

		p.save()

	return render(request,'cuestionario/pregunta.html',{'pregunta':p, 'repuestas':rs})