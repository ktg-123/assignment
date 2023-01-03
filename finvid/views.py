from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Video
from .serializers import VideoSerializer

# Create your views here.

class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
