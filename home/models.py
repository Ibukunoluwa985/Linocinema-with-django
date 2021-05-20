from django.db import models

class SearchManager(models.Model):
    search_queries = models.CharField(max_length=500, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search_queries