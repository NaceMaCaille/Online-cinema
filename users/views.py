from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from users.models import FavoriteMovie
from movies.views import get_movie_detail

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('movie:index'))
            
    else:
        form = UserLoginForm

    context = {
        'form': form
    }

    return render(request, 'users/registration_and_login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('movie:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'users/registration_and_login.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    favorites = FavoriteMovie.objects.filter(user=request.user)

    movies = []
    for fav in favorites:
        movie_data = get_movie_detail(fav.tmdb_id)
        movies.append(movie_data)

    context = {
        'title': 'Home - Кабинет',
        "form": form,
        'favorites': movies
    }

    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("movie:index"))

@login_required
def add_favorite(request, tmdb_id):

    FavoriteMovie.objects.get_or_create(user=request.user, tmdb_id=tmdb_id)

    return redirect(request.META.get('HTTP_REFERER','/'))

@login_required
def delete_favorite(request, tmdb_id):

    FavoriteMovie.objects.filter(user=request.user, tmdb_id=tmdb_id).delete()

    return redirect(request.META.get('HTTP_REFERER','/'))