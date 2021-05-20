from django.urls import path
from . import views

urlpatterns = [
    path('category=<str:category>/', views.CategoriesPage.as_view(), name='categories_page'),
]