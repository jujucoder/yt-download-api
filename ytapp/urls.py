from django.urls import path
from . import views

urlpatterns=[
    # path('',views.api_root),
    # path('video-details/',views.VideoDetails.as_view(),name='video-details'),
    path('',views.VideoDownload.as_view(),name='video-download')
]