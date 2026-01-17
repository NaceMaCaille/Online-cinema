from django.shortcuts import render

from .api_function import get_popular_movies, get_movie_detail, get_movie_video, get_search_movie

def popular_movies(request):
    movies = get_popular_movies()
    print("MOVIES LOADED:", len(movies))  
    return render(request, "movies/index.html", {"movies": movies})

def movie_detail(request, movie_id):
    movies = get_movie_detail(movie_id)
    videos = get_movie_video(movie_id)

    favorite_tmdb_ids = []
    if request.user.is_authenticated:
        favorite_tmdb_ids = list(
            request.user.favorite_movies.values_list('tmdb_id', flat=True)
        )

    return render(request, "movies/detail.html", 
        {"movie": movies, 
        "videos": videos, 
        "favorite_tmdb_ids": favorite_tmdb_ids}
        )

def search_movie(request):
    query = request.GET.get('q','').strip()

    movies = []

    if query:
        data = get_search_movie(query)
        movies = data.get("results", [])

    return render(request, "movies/index.html", {"movies": movies, "query": query})

