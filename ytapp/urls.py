from django.urls import path
from . import views

urlpatterns=[
    path('',views.VideoDownload.as_view(),name='video-download')
]