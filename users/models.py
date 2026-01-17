from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True, null=True, verbose_name='Аватар')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_movies')
    tmdb_id = models.IntegerField()

    class Meta:
        unique_together = ('user', 'tmdb_id')

class ViewedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewed_movies')
    tmdb_id = models.IntegerField()

    class Meta:
        unique_together = ('user', 'tmdb_id')

class PlanMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plan_movies')
    tmdb_id = models.IntegerField()

    class Meta:
        unique_together = ('user', 'tmdb_id')  
