from django.conf import settings
from django.db import models

CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('russian', 'RUSSIAN'),
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=False)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
                              verbose_name="фильм",
                              related_name="ratings", blank=True, null=True)

    def __str__(self):
        return str(self.title)


LINK_CHOICES = (
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)


class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie)


class Popularity(models.Model):
    movie_id = models.ForeignKey('Movie', default=' ', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_id


class Comment(models.Model):
    content = models.CharField(max_length=100, default='now')
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, default='now')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name="movie_comment",
                             default='now')