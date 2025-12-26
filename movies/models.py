from django.db import models


# class Genre(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return self.name or 'Unnamed Genre'

# class Category(models.Model):
#     title = models.CharField(max_length=100 ,null=True, blank=True)

#     def __str__(self):
#         return self.title or 'Unnamed Titile'
    
# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     poster = models.ImageField()
#     year = models.PositiveIntegerField()
#     country = models.CharField(max_length=100)
#     duration = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     genre = models.ManyToManyField(Genre, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.title
