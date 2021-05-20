from django.urls import path
from . import views

urlpatterns = [
    path("", views.LandingPage.as_view(), name="landing_page"),
    path("search_autocomplete/", views.SearchAutocomplete.as_view(), name="search_autocomplete"),
    path("search/", views.Search.as_view(), name="search_page"),
    path("how_to/", views.HowTo.as_view(), name="how_to"),
    path("privacy_policy/", views.PrivacyPolicy.as_view(), name="privacy_policy"),
    path("terms_of_service/", views.TermsOfService.as_view(), name="terms_of_service"),
]