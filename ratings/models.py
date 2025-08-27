from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MOVIE(models.Model):
    movie_id = models.IntegerField(unique=True)
    poster = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    released_year = models.IntegerField()
    ratings = models.FloatField(default=0.0)
    overview = models.TextField()
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class RATING(models.Model):
    rating = models.IntegerField(choices=[(i , i)for i in range(1,6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(MOVIE, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
    
    