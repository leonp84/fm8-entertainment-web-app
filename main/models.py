from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, blank=False)
    year = models.IntegerField(blank=False)
    category = models.CharField(max_length=50, blank=False)
    rating = models.CharField(max_length=10, blank=False)
    isBookmarked = models.BooleanField(default=False)
    isTrending = models.BooleanField(default=False)

    thumbnail_trending_small = models.CharField(max_length=100, blank=True)
    thumbnail_trending_large = models.CharField(max_length=100, blank=True)

    thumbnail_regular_small = models.CharField(max_length=100, blank=False)
    thumbnail_regular_medium = models.CharField(max_length=100, blank=False)
    thumbnail_regular_large = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title
