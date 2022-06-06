from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,CreateAPIView,DestroyAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,RetrieveUpdateAPIView


# Create your views here.
def test(request):
	return HttpResponse("Developer")

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post
    serializer_class = PostSerializer
	
class VideoList(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = videoSerializer

class VideoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Video
    serializer_class = videoSerializer