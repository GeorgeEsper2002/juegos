from django import forms
#from django.core.validators import RegexValidator
class Juegoformulario(forms.Form):
    titulo=forms.CharField() # use esto para que por ej: un juego se llame "age of empires 2"
    tematica=forms.CharField()
    estudio=forms.CharField()
    fecha=forms.DateField()

class UsuarioForm(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()

class Reseña(forms.Form):
    usuario=UsuarioForm()
    texto=forms.CharField()
    opinion=forms.BooleanField()

class Comentario(forms.Form):
    usuario=UsuarioForm()
    juego=forms.CharField()
    texto=forms.CharField()
