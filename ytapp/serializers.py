
from rest_framework import serializers



class LinkSerializer(serializers.Serializer):
    youtube_link = serializers.CharField(required=True,max_length=200,allow_blank=False)


class DownloadSerializer(serializers.Serializer):
    youtube_link=serializers.CharField(required=True,allow_blank=False,max_length=100)   
    resolution=serializers.IntegerField(required=True) 