from django.urls import path
from movies import views

urlpatterns = [
    path('', views.popular_movies, name='index'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail')
]