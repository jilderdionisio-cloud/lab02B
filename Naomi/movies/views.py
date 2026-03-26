from django.shortcuts import render
from .models import Movie

def lista_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/lista.html', {'movies': movies})