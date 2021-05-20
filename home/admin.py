from django.contrib import admin
from .models import SearchManager

@admin.register(SearchManager)
class SearchManagerAdmin(admin.ModelAdmin):
    list_display = ('search_queries', 'date_added')