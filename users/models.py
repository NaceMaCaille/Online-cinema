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


class UserMovie(models.Model):
    STATUS_CHOICES = [
        ('planned', 'В планах'),
        ('favorite', 'Избранное'),
        ('watched', 'Просмотрено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tmdb_id = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('user', 'tmdb_id')