from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
      
class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
