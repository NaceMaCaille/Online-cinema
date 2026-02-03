from django.shortcuts import render

from .api_function import (get_popular_movies, get_movie_detail,
                            get_movie_video, get_search_movie,
                            discover_movie, get_genres)

from .utils import build_tmdb_filters


def popular_movies(request):
    movies = get_popular_movies()
    print("MOVIES LOADED:", len(movies))  
    return render(request, "movies/index.html", {"movies": movies})

def movie_detail(request, movie_id):
    movies = get_movie_detail(movie_id)
    videos = get_movie_video(movie_id)

    return render(request, "movies/detail.html", 
        {"movie": movies, 
        "videos": videos}
        )

def search_movie(request):
    query = request.GET.get('q', '').strip()

    data = {}
    movies = []

    if query:
        data = get_search_movie(query)
    else:
        # 🎛 ФИЛЬТРЫ
        tmdb_filters = build_tmdb_filters(request)
        data = discover_movie(tmdb_filters)

    movies = data.get('results', [])

    selected_genres = request.GET.getlist('genre')

    context = {
        'movies': movies,
        'query': query,
        'genres': get_genres(),
        'page': data.get('page'),
        'total_pages': data.get('total_pages'),
        'selected_genres': selected_genres
    }

    return render(request, "movies/index.html", context)


# def movie_list(request):
#     tmdb_filters = build_tmdb_filters(request)

#     data = discover_movie(tmdb_filters)

#     context = {
#         'movies': data.get('results', []),
#         'genres': get_genres(),
#         'page': data.get('page'),
#         'total_pages': data.get('total_pages'),
#     }

#     return render(request, 'movies/filter.html', context)
