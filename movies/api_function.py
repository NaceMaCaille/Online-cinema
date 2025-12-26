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