from django.shortcuts import render
from .models import MOVIE
# Create your views here.


def home(request):
    pass

def movie_list_view(request):

    movies = MOVIE.objects.all().order_by('ratings')

    return render(request, 'ratings/list.html', {
        'movies' : movies,
        
        })