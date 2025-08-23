from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MOVIE
# Create your views here.


def home(request):
    pass

def movie_pages_view(request):
    movies = MOVIE.objects.all().order_by()
    sort_by = request.GET.get('sort', 'title')
    
    if sort_by == 'genre':
        movies = movies.order_by('genre')
    elif sort_by == 'released_year':
        movies = movies.order_by('released_year')
    else:
        movies = movies.order_by('title')

    paginator = Paginator(movies, 25)
    page_number = request.GET.get('page')
    movies_per_page = paginator.get_page(page_number)
    return render(request, "ratings/list.html", {
        "movies" : movies_per_page,
        })