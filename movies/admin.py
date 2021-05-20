from django.contrib import admin
from .models import *

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    # movies display
    list_display = ("title", "id", "genre", "user", "year", "director", "added_on")
    # movies filter
    list_filter = ("genre", "language", "year", "permission")
    # movies search
    search_fields = ("id__startswith", "title__startswith", "language__startswith", "genre__startswith", "user__startswith", "year__startswith", "added_on__startswith")