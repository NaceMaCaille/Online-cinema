from django.urls import path
from movies import views

app_name = 'movie'

urlpatterns = [
    path('search/', views.search_movie, name='search'),
    path('', views.popular_movies, name='index'),
    # path('filter-search/', views.movie_list, name='movies_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
]