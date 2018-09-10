from django.shortcuts import render

# Create your views here.

from .models import Movie, Review

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'film_critic/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'film_critic/movie_detail.html', {'movie': movie})