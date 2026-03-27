from django.shortcuts import get_object_or_404, render
from .models import Movie

def lista_movies(request):
    # 1. Le preguntamos a la URL: ¿El usuario escribió algo en la cajita 'q'?
    busqueda = request.GET.get('q') 
    
    if busqueda:
        # 2. Si hay búsqueda, filtramos películas que contengan esa palabra en el título
        # El '__icontains' significa: "busca la palabra sin importar mayúsculas o minúsculas"
        peliculas = Movie.objects.filter(title__icontains=busqueda)
    else:
        # 3. Si no escribió nada (o limpió la búsqueda), mostramos todas
        peliculas = Movie.objects.all()

    # 4. Enviamos el resultado al HTML
    return render(request, 'movies/lista.html', {'movies': peliculas})
# NUEVA FUNCIÓN CONTROLADORA:
def pelicula_detalle(request, pk):
    # 'get_object_or_404' busca la película por su ID. 
    # Si no existe, muestra un error 404 (No encontrado) automáticamente.
    pelicula = get_object_or_404(Movie, pk=pk)
    
    return render(request, 'movies/detalles.html', {'movie': pelicula})