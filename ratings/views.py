from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MOVIE
# Create your views here.


def home(request):
    pass

def movie_pages_view(request):
    movies = MOVIE.objects.all()
    paginator = Paginator(movies, 25)

    page_number = request.GET.get('page')
    movies_per_page = paginator.get_page(page_number)
    return render(request, "ratings/list.html", {
        "movies" : movies_per_page,
        })