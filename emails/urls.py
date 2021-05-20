from django.urls import path
from . import views

urlpatterns = [
    path('', views.Emails.as_view(), name='emails_page'),
    path('reachout/', views.Reachout.as_view(), name='reachout'),
    path('personal_reachout/', views.PersonalReachout.as_view(), name='personal_reachout'),
    path('personal_fail_reachout/', views.PersonalFailReachout.as_view(), name='personal_fail_reachout'),
]