from rest_framework import serializers
from .models import *

class TvshowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvshows
        fields = '__all__'
        depth = 1

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
        depth = 2

class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = '__all__'
        depth = 2