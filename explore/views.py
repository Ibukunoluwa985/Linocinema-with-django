from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExploreSerializer
from django.views.generic import ListView
from tvshows.models import Tvshows
from movies.models import Movies

class ExplorePage(ListView):
    model = Movies
    context_object_name = "random"
    template_name='explore/explore_list_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movies.objects.order_by('?')[:24]
        context["tvshows"] = Tvshows.objects.order_by('?')[:24]
        return context

# API VIEW
@api_view(['GET'])
def explore_list_api(request, format=None):
    """
    to view movie list api
    """
    shuffle_movies = Movies.objects.all().order_by('?')[:100]
    serializer = ExploreSerializer(shuffle_movies, many=True)
    return Response(serializer.data)