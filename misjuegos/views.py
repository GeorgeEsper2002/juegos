from django.shortcuts import render
from misjuegos.models import *
from misjuegos.forms import *
from django.http import HttpResponse
# Create your views here.
#usuario,juego,reseña,comentario
def inicio(request):
    return render(request,"misjuegos/inicio.html")

def usuario(request):
    return render(request,"misjuegos/usuario.html")

def juego(request):
    return render(request,"misjuegos/juego.html")
def juegoformulario(request):
    return render(request,"misjuegos/juegoformulario.html")
def reseña(request):
    return render(request,"misjuegos/reseña.html")

def comentario(request):
    return render(request,"misjuegos/comentario.html")


def juegoformulario(request):
    if request.method == 'POST':
        juego=Juego(titulo=request.POST['titulo'],tematica=request.POST['tematica'],estudio=request.POST['estudio'],fecha=request.POST['fecha'])
        juego.save()
        return render(request,'misjuegos/inicio.html')
    return render(request,'misjuegos/juegoformulario.html')

#Desde urls tenes que vincular cada view, y eso vinculado con un form que esta vinculado a un model
#class ProductForm(ModelForm):
#    class Meta:
#        model = Product
#        fields = '__all__'

#def juegoformulario(request):
#    if request.method=='POST':
#        formulario=Juegoformulario(request.POST)
#        if formulario.is_valid():
#            info=formulario.cleaned_data()
#            juego=Juego(nombre=info['titulo'],tema=info['tematica'],est=info['estudio'],fech=info['fecha'])
#            juego.save()
#            return render(request,'misjuegos/inicio.html')
#        else:
#            formulario=Juegoformulario()
#    return render(request,'misjuegos/juegoformulario.html',{'formulario':formulario})

def buscarjuego(request):
    if request.GET["titulo"]:
        titulo = request.GET['titulo']
        estudio = Juego.objects.filter(estudio__icontains=estudio)
        return render(request, "AppCoder/resultadoBusqueda.html", {"titulo":titulo, "estudio":estudio})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos" 
    return HttpResponse (respuesta)