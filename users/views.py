from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from users.models import UserMovie
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

def get_movie_by_status(user, status):
    tmdb_ids = (
        UserMovie.objects.filter(user=user, status=status).values_list('tmdb_id', flat=True)
    )

    movies = []
    for tmdb_id in tmdb_ids:
        movie = get_movie_detail(tmdb_id)
        movies.append(movie)

    return movies

@login_required
def profile(request):
    context = {
        'title': 'Home - Кабинет',
    }
    return render(request, 'users/profile.html', context)

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Изменить профиль',
        'form': form,
    }

    return render(request, 'users/profile_edit.html', context)

@login_required
def profile_watched(request):
    WATCHED = 'watched'
    context = {
        'watched_movies':get_movie_by_status(
            request.user, WATCHED
        )
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_planned(request):
    PLANNED = 'planned'
    context = {
        'watched_movies':get_movie_by_status(
            request.user, PLANNED
        )
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_favorite(request):
    FAVORITE = 'favorite'
    context = {
        'watched_movies':get_movie_by_status(
            request.user, FAVORITE
        )
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_del(request, tmdb_id):

    UserMovie.objects.filter(user=request.user, tmdb_id=tmdb_id).delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def set_movie_status(request, tmdb_id, status):

    ALLOWED_STATUSES = {'planned', 'favorite', 'watched'}

    if status not in ALLOWED_STATUSES:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    UserMovie.objects.update_or_create(
        user=request.user,
        tmdb_id=tmdb_id,
        defaults={'status': status}
    )

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("movie:index"))