from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_movies, name='lista_movies'),
    
    # NUEVA RUTA: El <int:pk> captura el ID de la película (1, 2, 3...)
    path('pelicula/<int:pk>/', views.pelicula_detalle, name='pelicula_detalle'),
]