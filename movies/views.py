from rest_framework.response import Response
from .models import Movie, MovieLinks
from rest_framework.views import APIView
from .serializers import MovieListSerializer


class MovieListView(APIView):
    """Вывод списка фильмов"""
    def get_movie_list(self, request):
        movie = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movie, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Вывод фильма"""
    def get_movie_output(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)





