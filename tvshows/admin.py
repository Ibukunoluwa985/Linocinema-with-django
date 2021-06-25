from django.contrib import admin
from .models import *

@admin.register(Tvshows)
class TvshowAdmin(admin.ModelAdmin):
    # tvshow display
    list_display = ("title", "id", "genre", "user", "year", "added_on")
    # tvshow filter
    list_filter = ("genre", "language", "year")
    # tvshow search
    search_fields = ("id__startswith", "title__startswith", "language__startswith", "genre__startswith", "year__startswith", "added_on__startswith", )

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    # Season display
    list_display = ("tvshow", "season_number", "episode_number", "added_on")
    # Season search
    search_fields = ("id__startswith", "tvshow__startswith", "added_on__startswith", )

@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    # Subtitle display
    list_display = ("tvshow", "season_number", "episode_number", "added_on")
    # Subtitle search
    search_fields = ("id__startswith", "tvshow__startswith", "added_on__startswith", )