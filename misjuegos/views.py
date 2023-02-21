from django.shortcuts import render
from misjuegos.models import *
from misjuegos.forms import Juegoformulario
# Create your views here.
#usuario,juego,reseña,comentario
def inicio(request):
    return render(request,"misjuegos/inicio.html")

def usuario(request):
    return render(request,"misjuegos/usuario.html")

def juego(request):
    return render(request,"misjuegos/juego.html")

def reseña(request):
    return render(request,"misjuegos/reseña.html")

def comentario(request):
    return render(request,"misjuegos/comentario.html")


#def juegoformulario(request):
#    if request.method=='POST':
#        juego=Juego(request.POST['titulo'],request.POST['tematica'],request.POST['estudio'],request.POST['fecha'])
#        juego.save()
#        return render(render,'misjuegos/inicio.html')
#    return render(request,'misjuegos/juegoformulario.html')

#Desde urls tenes que vincular cada view, y eso vinculado con un form que esta vinculado a un model
#class ProductForm(ModelForm):
#    class Meta:
#        model = Product
#        fields = '__all__'

def juegoformulario(request):
    if request.method=='POST':
        formulario=Juegoformulario(request.POST)
        if formulario.is_valid:
            info=formulario.cleaned_dat
            juego=Juego(nombre=info['titulo'],tema=info['tematica'],est=info['estudio'],fech=info['fecha'])
            juego.save()
            return render(request,'misjuegos/inicio.html')
        else:
            formulario=Juegoformulario()
    return render(request,'misjuegos/juegoformulario.html',{'formulario':formulario})