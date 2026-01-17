from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('favorites/remove/<int:tmdb_id>/', views.delete_favorite, name='remove_favorites'),
    path('favorites/add/<int:tmdb_id>/', views.add_favorite, name='add_favorites'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
