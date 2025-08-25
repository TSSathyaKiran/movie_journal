from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MOVIE
# Create your views here.


def home(request):
    pass

def movie_pages_view(request):
    movies = MOVIE.objects.all()
    sort_by = request.GET.get('sort', '-ratings')
    
    if sort_by == 'rating':
        movies = movies.order_by('-ratings')
    elif sort_by == 'released_year':
        movies = movies.order_by('released_year')
    elif sort_by == "title":
        movies = movies.order_by('title')
    else:
        movies = movies.order_by("-ratings")

    paginator = Paginator(movies, 25)
    page_number = request.GET.get('page')
    movies_per_page = paginator.get_page(page_number)
    return render(request, "ratings/list.html", {
        "movies" : movies_per_page,
        })