from django import forms
from .models import Movie, Review

class ReviewForm(forms.ModelForm):

        class Meta:
            model = Review
            fields = ('movie', 'user', 'description')

class MovieForm(forms.ModelForm):

        class Meta:
            model = Movie
            fields = ('title', 'description', 'img_url')