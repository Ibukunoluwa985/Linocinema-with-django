from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (ListView, DetailView)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movies

class MoviesPage(ListView):
    model = Movies
    context_object_name = 'movies'
    template_name='movies/movies_list_page.html'
    paginate_by = 18
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies_from_db = Movies.objects.order_by('-added_on')
        paginator = Paginator(movies_from_db, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)

        index = movies.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index -5 else max_index
        page_range = paginator.page_range[start_index:end_index]
        context["movies"] = movies
        context["page_range"] = page_range
        return context

class MoviesDetailPage(DetailView):
    model = Movies
    context_object_name = 'movie_detail'
    template_name='movies/movies_detail_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_user = Movies.objects.get(id=self.kwargs['pk'])
        context['related_movies'] = Movies.objects.order_by('?')
        context['movie_count'] = Movies.objects.filter(user=movie_user.user, permission=1).count()
        context["movie_last"] = Movies.objects.filter(user=movie_user.user, permission=1).last()
        return context

# API VIEW
@api_view(['GET'])
def movie_list_api(request, format=None):
    """
    to view movie list api
    """
    movie = Movies.objects.order_by('-id')
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
    