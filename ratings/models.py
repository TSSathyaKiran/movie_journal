from django.db import models

# Create your models here.

class MOVIE(models.Model):
    poster = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    released_year = models.IntegerField(max_length=4)
    rating = models.FloatField(default=0.0)
    overview = models.TextField()
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.title