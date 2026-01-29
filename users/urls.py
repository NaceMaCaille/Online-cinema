from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('profile/edit-profile/', views.profile_edit, name='edit_profile'),
    path('profile/planned/', views.profile_planned, name='planned_movies'),
    path('profile/favorite/', views.profile_favorite, name='favorite_movies'),
    path('profile/watched/', views.profile_watched, name='watched_movies'),
    path('status/<int:tmdb_id>/', views.profile_del, name='delete_status'),
    path('status/<int:tmdb_id>/<str:status>/', views.set_movie_status, name='set_movie_status'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
