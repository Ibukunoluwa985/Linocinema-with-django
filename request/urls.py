from django.urls import path
from . import views

urlpatterns = [
    path("", views.RequestPage.as_view(), name="request_page"),
    path('movie_request/', views.MovieRequest.as_view(), name='movie_request'),
    path('tvshow_request/', views.TvshowRequest.as_view(), name='tvshow_request'),
]