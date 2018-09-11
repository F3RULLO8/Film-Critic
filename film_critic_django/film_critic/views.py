from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Movie, Review
from .forms import ReviewForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'film_critic/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'film_critic/movie_detail.html', {'movie': movie})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('movie_list')
    else:
        form = ReviewForm()
    return render(request, 'film_critic/review_form.html', {'form': form})