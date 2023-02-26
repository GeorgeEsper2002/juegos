from django.urls import path
from .views import inicio,usuario,juego,reseña,comentario,juegoformulario,buscarjuego

urlpatterns = [
    path('',inicio,name='inicio'),
    path('usuario/',usuario,name='usuario'),
    path('juego/',juego,name='juego'),
    path('reseña/',reseña,name='reseña'),
    path('comentario/',comentario,name='comentario'),
    path('juegoformulario/',juegoformulario,name='Agregar Juego'),
    path('buscarjuego/',buscarjuego,name="Buscar Juego")
]
