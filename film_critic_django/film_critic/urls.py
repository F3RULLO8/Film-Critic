from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:pk>', views.movie_detail, name='movie_detail'),
    path('review/new', views.review_create, name='review_create'),
]