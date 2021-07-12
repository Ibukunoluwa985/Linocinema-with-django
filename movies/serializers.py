from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Movies
        fields = '__all__'
        depth = 1

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)