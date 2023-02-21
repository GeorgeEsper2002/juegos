from django import forms

class Juegoformulario(Forms.form):
    titulo=forms.CharField()
    tematica=forms.CharField()
    estudio=forms.CharField()
    fecha=forms.CharField()