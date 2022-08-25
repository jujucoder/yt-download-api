
from django.shortcuts import render
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import DownloadSerializer, LinkSerializer
from pytube import*
from rest_framework.generics import GenericAPIView

# Create your views here.


# @api_view(['POST'])
# def first(request):
#   if request.method == 'POST':  
#      serializer = LinkSerializer(data=request.data)
#      link=serializer.data['youtube_link']
#      try:
#         video = pytube.YouTube(link)
#      except:
#         return Response({'link invalid or not found'}, status=status.HTTP_400_BAD_REQUEST)   


#      stream = video.streams
#      return Response({stream}, status=status.HTTP_400_BAD_REQUEST)

class VideoDetails(GenericAPIView):
    serializer_class=LinkSerializer

    def post(self, request, *args, **kwargs):
     link=self.request.data['youtube_link']
     try:
        yt =YouTube(link)
     except:
        return Response({'link invalid or not found'}, status=status.HTTP_404_NOT_FOUND)  
     video_name=yt.title
     date_posted=yt.publish_date
     date_posted=date_posted.strftime("%Y-%m-%d %H:%M:%S")
     author=yt.author
     available_resolutions=[]
     video_streams=yt.streams.filter(only_video=True,file_extension='mp4')
     print(video_streams)
     for stream in video_streams:
        available_resolutions.append(stream.resolution)

     return Response({'author':author,'video_name':video_name,'date_posted':date_posted,'available res':available_resolutions}, status=status.HTTP_200_OK)


class VideoDownload(GenericAPIView):
    serializer_class=DownloadSerializer

    def post(self, request, *args, **kwargs):
     link=self.request.data['youtube_link']
     res=self.request.data['resolution']
     res=res+'p'
     try:
        yt =YouTube(link)
     except:
        return Response({'link invalid or not found'}, status=status.HTTP_404_NOT_FOUND)  


     stream=yt.streams.filter(subtype='mp4',resolution=res).first()
     stream2=yt.streams.filter(only_audio=True).first()
     print(stream2)
     print(stream)
     if stream is not None:
        stream.download()
        stream2.download()
        return Response({'thanks for downloading'},status=status.HTTP_200_OK)
     return Response({'this resoluton is unavailable for this video'},status=status.HTTP_404_NOT_FOUND)    



@api_view(['GET'])
def api_root(request):
    return Response()