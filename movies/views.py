
from rest_framework.response import Response
from .models import Movie, MovieLinks
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer


class MovieListView(APIView):
    """Вывод списка фильмов"""

    def get_movie_list(self, request):
        movie = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movie, many=True)
        return Response(serializer.data)


class MovieDetailView(RetrieveAPIView):
    """Вывод фильма"""
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer



class ReviewCreateView(APIView):
    """Добавление отзыва к фильму"""

    def get_movie_review(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


# class Search(ListView):
#     """Поиск фильмов"""
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Movie.objects.filter(title__icontains=self.request.GET.get("q"))
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["q"] = f'q={self.request.GET.get("q")}&'
#         return context
