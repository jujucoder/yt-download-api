
from django.shortcuts import render
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import DownloadSerializer
import pytube
from rest_framework.generics import GenericAPIView
import os

# Create your views here.

class VideoDownload(GenericAPIView):
    serializer_class=DownloadSerializer

    def post(self, request, *args, **kwargs):
     link=self.request.data['youtube_link']
     try:
        yt =pytube.YouTube(link)
     except:
        return Response({'link invalid or not found'}, status=status.HTTP_404_NOT_FOUND)  


     video_stream=yt.streams.filter(only_video=True,subtype='mp4').first()
     if video_stream is not None:
        video_stream.download()
        os.rename(video_stream, 'wahala.mp4')
        return Response({'thanks for downloading'},status=status.HTTP_200_OK)
     return Response({'this resoluton is unavailable for this video'},status=status.HTTP_404_NOT_FOUND)    