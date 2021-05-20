from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserInfoPage.as_view(), name='user_info_page'),
    path('login/', views.Login.as_view(), name='user_login'),
    path('register/', views.Register.as_view(), name='user_register'),
    path('logout/', views.Logout.as_view(), name='user_logout'),
    path('disactivate/', views.DisactivateUser.as_view(), name="disactivate_user"),
    path('reactivate/', views.ReactivateUser.as_view(), name="reactivate_user_page"),
    path('delete/', views.DeleteUser.as_view(), name="delete_user"),
    path('first_name/update/', views.UpdateFirstName.as_view(), name="update_first_name"),
    path('last_name/update/', views.UpdateLastName.as_view(), name="update_last_name"),
]