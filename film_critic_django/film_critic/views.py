from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Movie, Review
from .forms import ReviewForm, MovieForm

from django.contrib.auth.decorators import login_required

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'film_critic/movie_list.html', {'movies': movies})

def profile(request):
    reviews = Review.objects.all()
    return render(request, 'film_critic/profile.html', {'reviews': reviews})

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'film_critic/movie_detail.html', {'movie': movie})

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'film_critic/movie_form.html', {'form': form})

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

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('movie_list')
    else:
        form = ReviewForm()
    return render(request, 'film_critic/review_form.html', {'form': form})

@login_required
def review_edit(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            movie = form.save()
            return redirect('profile')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'film_critic/review_form.html', {'form': form})

@login_required
def review_delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect('profile')