from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactPage.as_view(), name='contact_page'),
]