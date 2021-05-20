from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (ListView)
from tvshows.models import Tvshows
from movies.models import Movies
from itertools import chain

class CategoriesPage(ListView):
    model = Movies
    template_name = "categories/categories_page.html"
    paginate_by = 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['category']
        movies = Movies.objects.filter(genre=category)
        tvshows = Tvshows.objects.filter(genre=category)
        categories = list(chain(movies, tvshows))
        context["category"] = category
        context["categories"] = categories
        return context