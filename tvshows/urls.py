from django.urls import path
from . import views

urlpatterns = [
    path("", views.TvshowsPage.as_view(), name="tvshows_page"),
    path('api/', views.tvshow_list_api, name='tvshow_list_api'),
    path('season/api/', views.season_list_api, name='season_list_api'),
    path("<int:pk>/", views.TvshowsDetailPage.as_view(), name="tvshows_detail_page"),
]