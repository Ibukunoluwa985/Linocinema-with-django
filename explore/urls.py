from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExplorePage.as_view(), name="explore_page"),
    path('api/', views.explore_list_api, name='explore_list_api'),
    path('api',  RedirectView.as_view(url='/explore/api/')),
]