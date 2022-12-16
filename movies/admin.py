from django.contrib import admin

# Register your models here.
from .models import Movie, MovieLinks, Popularity, Comment

admin.site.register(Movie)
admin.site.register(MovieLinks)
admin.site.register(Popularity)
admin.site.register(Comment)
