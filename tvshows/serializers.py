from rest_framework import serializers
from .models import *

class TvshowsSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Tvshows
        fields = '__all__'
        depth = 1

    # def get_image_url(self, obj):
    #     request = self.context.get("request")
    #     return request.build_absolute_uri(obj.image.url)

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