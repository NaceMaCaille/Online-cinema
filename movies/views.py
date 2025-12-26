from django.shortcuts import render

from .api_function import get_popular_movies, get_movie_detail, get_movie_video

def popular_movies(request):
    movies = get_popular_movies()
    print("MOVIES LOADED:", len(movies))  
    return render(request, "movies/index.html", {"movies": movies})

def movie_detail(request, movie_id):
    movies = get_movie_detail(movie_id)
    videos = get_movie_video(movie_id)
    return render(request, "movies/detail.html", {"movies": movies, "videos": videos})

