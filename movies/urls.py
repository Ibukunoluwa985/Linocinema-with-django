from django.urls import path
from . import views

urlpatterns = [
    path("", views.MoviesPage.as_view(), name="movies_page"),
    path('api/', views.movie_list_api, name='movie_list_api'),
    path("<int:pk>/", views.MoviesDetailPage.as_view(), name="movies_detail_page"),
]