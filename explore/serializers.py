from rest_framework import serializers
from movies.models import *

class ExploreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
        depth = 1