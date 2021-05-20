from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from user import views as user_views
from django.conf.urls.static import static
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    path('', include('home.urls')),
    path('superadmin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('movies/', include('movies.urls')),
    path('tvshows/', include('tvshows.urls')),
    path('explore/', include('explore.urls')),
    path('request/', include('request.urls')),
    path('contact/', include('contact.urls')),
    path('categories/', include('categories.urls')),
    path('emails/', include('emails.urls')),

    # password reset and blocking some paths
    path('accounts/', user_views.home_redirect, name="home_redirect"),
    path('accounts/login/', user_views.login_redirect, name="login_redirect"),
    path('accounts/logout/', user_views.logout_redirect, name="logout_redirect"),
    path('accounts/password_change/', user_views.home_redirect, name="home_redirect"),
    path('accounts/password_change/done/', user_views.home_redirect, name="home_redirect"),
    path('accounts/', include('django.contrib.auth.urls')),
]

# handling page errors
handler403 = 'home.views.error_403'
handler400 = 'home.views.error_400'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'

# following URL patterns for static and media file
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)