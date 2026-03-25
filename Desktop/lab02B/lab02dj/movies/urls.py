from django.urls import path
from .views import lista_movies

urlpatterns = [
    path('', lista_movies),
]