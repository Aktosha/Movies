from django.urls import path
from .views import MovieListView
from . import views

urlpatterns = [
    path('movie/', MovieListView.as_view()),
    path("movie/<int:pk>/", views.MovieDetailView.as_view()),
]
