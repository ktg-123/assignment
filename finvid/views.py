from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny,]
