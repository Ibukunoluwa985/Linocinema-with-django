from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExploreSerializer
from django.views.generic import ListView
from tvshows.models import Tvshows
from movies.models import Movies
import random

class ExplorePage(ListView):
    model = Movies
    context_object_name = "random"
    template_name='explore/explore_list_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies_random_id = random.sample(list(Movies.objects.values_list("id", flat=True)), 24)
        tvshows_random_id = random.sample(list(Tvshows.objects.values_list("id", flat=True)), 24)
        context["movies"] = Movies.objects.filter(id__in=movies_random_id)
        context["tvshows"] = Tvshows.objects.filter(id__in=tvshows_random_id)
        return context

# API VIEW
@api_view(['GET'])
def explore_list_api(request, format=None):
    """
    to view movie list api
    """
    shuffle_movies = random.sample(list(Movies.objects.values_list("id", flat=True)), 24)
    serializer = ExploreSerializer(shuffle_movies, many=True)
    return Response(serializer.data)