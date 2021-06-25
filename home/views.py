from django.views.generic import (View, TemplateView, ListView)
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse, request
from django.contrib import messages
from tvshows.models import Tvshows
from .models import SearchManager
from django.utils import timezone
from movies.models import Movies
from collections import Counter
from django.db.models import Q
from itertools import chain
import datetime, random

class LandingPage(View):
    template_name = template_name = "home/landing_page.html"
    def get(self, request, *args, **kwargs):
        context = {}
        # change values
        movies_random_id = random.sample(list(Movies.objects.values_list("id", flat=True)), 6)
        tvshows_random_id = random.sample(list(Tvshows.objects.values_list("id", flat=True)), 6)
        # change values
        movies_slide_id = random.sample(list(Movies.objects.values_list("id", flat=True)), 2)
        tvshows_slide_id = random.sample(list(Tvshows.objects.values_list("id", flat=True)), 2)
        context['movies'] = Movies.objects.order_by('-id')[:6]
        context['tvshows'] = Tvshows.objects.order_by('-id')[:6]
        context['random_movies'] = Movies.objects.filter(id__in=movies_random_id)
        context['random_tvshows'] = Tvshows.objects.filter(id__in=tvshows_random_id)
        context['slide_movies'] = Movies.objects.filter(id__in=movies_slide_id)
        context['slide_tvshows'] = Tvshows.objects.filter(id__in=tvshows_slide_id)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class SearchAutocomplete(View):
    def get(self, request, *args, **kwargs):
        if 'term' in request.GET:
            query_results = list()
            query_term = request.GET.get('term')
            search_movies = Movies.objects.filter(title__icontains=query_term)
            search_tvshows = Tvshows.objects.filter(title__icontains=query_term)
                                                
            for query in search_movies:
                query_results.append(query.title)
            for query in search_tvshows:
                query_results.append(query.title)

            return JsonResponse(query_results, safe=False)
        return render(request, 'home/landing_page.html')

class Search(ListView):
    model = Movies
    template_name = "home/search_page.html"
    def get_queryset(self):
        query_context = {}
        search_queries = self.request.GET.get('search', '')
        movies = Movies.objects.filter(Q(title__icontains=search_queries) | Q(description__icontains=search_queries))
        tvshows = Tvshows.objects.filter(Q(title__icontains=search_queries) | Q(description__icontains=search_queries))
        user = User.objects.filter(Q(username__icontains=search_queries) | Q(email__icontains=search_queries) | 
                                    Q(first_name__icontains=search_queries) | Q(last_name__icontains=search_queries))

        search_results = list(chain(movies, tvshows, user))

        week_ago = timezone.now() - datetime.timedelta(days=7)
        SearchManager.objects.filter(date_added__lt=week_ago).delete()
        search_query_save = SearchManager.objects.create(search_queries=search_queries)
        search_query_save.save()

        search_manager = SearchManager.objects.all()
        search_manager = [search_manager.values_list('search_queries', flat=True)]

        for i in search_manager:
            count_dict = Counter(i)
            count_dict_values = list(count_dict.values())
            max_value = max(count_dict_values)
            max_search_query = list(count_dict.keys())[list(count_dict.values()).index(max_value)]
            query_context['max_value'] = max(count_dict_values)
            query_context['max_search_query'] = max_search_query

        query_context['search_queries'] = search_queries
        query_context['search_results'] = search_results
        return query_context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_queryset())

class HowTo(View):
    # template_name = "home/how_to.html"
    def get(self, request, *args, **kwargs):
        messages.warning(request, 'Sorry on active doc on this at the moment')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def post(self, request, *args, **kwargs):
        messages.warning(request, 'Sorry on active doc on this at the moment')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class PrivacyPolicy(TemplateView):
    template_name = "home/privacy_policy.html"

class TermsOfService(TemplateView):
    template_name = "home/terms_of_service.html"

# handling page errors
def error_400(request, exception):
    return render(request, 'notifications/error_pages/400.html', status=400)
def error_403(request, exception):
    return render(request, 'notifications/error_pages/403.html', status=403)
def error_404(request, exception):
    return render(request, 'notifications/error_pages/404.html', status=404)
def error_500(request):
    return render(request, 'notifications/error_pages/500.html', status=500)