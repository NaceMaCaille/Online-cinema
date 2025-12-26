from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
