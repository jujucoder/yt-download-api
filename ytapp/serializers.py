
from rest_framework import serializers

class DownloadSerializer(serializers.Serializer):
    youtube_link=serializers.CharField(required=True,allow_blank=False,max_length=100)   