from .serializers import SubtitleSerializer, TvshowsSerializer, SeasonSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (ListView, DetailView)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subtitle, Tvshows, Season
import random

class TvshowsPage(ListView):
    model = Tvshows
    context_object_name = 'tvshows'
    template_name='tvshows/tvshows_list_page.html'
    paginate_by = 18
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tvshows_from_db = Tvshows.objects.order_by('-added_on')
        paginator = Paginator(tvshows_from_db, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            tvshows = paginator.page(page)
        except PageNotAnInteger:
            tvshows = paginator.page(1)
        except EmptyPage:
            tvshows = paginator.page(paginator.num_pages)

        index = tvshows.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index -5 else max_index
        page_range = paginator.page_range[start_index:end_index]
        context["tvshows"] = tvshows
        context["page_range"] = page_range
        return context

class TvshowsDetailPage(DetailView):
    model = Tvshows
    context_object_name = 'tvshow_detail'
    template_name='tvshows/tvshows_detail_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tvshow_user = Tvshows.objects.get(id=self.kwargs['pk'])
        random_id = random.sample(list(Tvshows.objects.values_list("id", flat=True)), 1)
        context['related_tvshows'] = Tvshows.objects.filter(id__in=random_id)
        context["seasons"] = Season.objects.order_by('episode_number')
        context["subtitles"] = Subtitle.objects.order_by('episode_number')
        context['tvshow_count'] = Tvshows.objects.filter(user=tvshow_user.user).count()
        context["tvshow_last"] = Tvshows.objects.filter(user=tvshow_user.user).last()
        return context

# API VIEW
@api_view(['GET'])
def tvshow_list_api(request, format=None):
    """
    to view tvshow list api
    """
    tvshow = Tvshows.objects.order_by('-id')
    serializer = TvshowsSerializer(tvshow, many=True)
    return Response(serializer.data)

# API VIEW
@api_view(['GET'])
def season_list_api(request, format=None):
    """
    to view tvshow season list api
    """
    season = Season.objects.order_by('-id')
    serializer = SeasonSerializer(season, many=True)
    return Response(serializer.data)

# API VIEW
@api_view(['GET'])
def subtitle_list_api(request, format=None):
    """
    to view tvshow subtitle list api
    """
    subtitle = Subtitle.objects.order_by('-id')
    serializer = SubtitleSerializer(subtitle, many=True)
    return Response(serializer.data)