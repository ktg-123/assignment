from django.urls import re_path
from .views import VideoList

urlpatterns = [
    re_path(r'', VideoList.as_view(), name='video-list'),
]
