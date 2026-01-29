import requests
from django.conf import settings

def get_popular_movies():
    url = f"{settings.TMDB_BASE_URL}/movie/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU"
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])

def get_movie_detail(movie_id):
    url = f"{settings.TMDB_BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_movie_video(movie_id):
    url = f"{settings.TMDB_BASE_URL}/movie/{movie_id}/video"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU"
    }
    response = requests.get(url, params=params)
    return response.json()

def get_search_movie(movie_name):
    url = f"{settings.TMDB_BASE_URL}/search/movie"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU",
        "query": movie_name
    }
    response = requests.get(url, params=params)
    return response.json()

def discover_movie(params):
    url = f"{settings.TMDB_BASE_URL}/discover/movie"
    default_params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "ru-RU",
        "sort_by": "popularity.desc"
    }
    response = requests.get(url, params={**default_params, **params})
    return response.json()

def get_genres():
    response = requests.get(
        f'{settings.TMDB_BASE_URL}/genre/movie/list',
        params={
            "api_key": settings.TMDB_API_KEY,
            "language": "ru-RU"
        }
    )
    return response.json().get('genres', [])