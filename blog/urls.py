from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
# from .views import PostList, PostDetail, VideoList, VideoDetail
from . import views
urlpatterns = [
    # path('new_blog',views.new_blog, name='newblog'),
    path('posts', PostList.as_view(),name='posts'),
    path('postdetail/<int:pk>', PostDetail.as_view(),name = 'postdetail'),
    path('videos', VideoList.as_view(),name='videos'),
    path('videodetail/<int:pk>', VideoDetail.as_view(),name='VideoDetail'),
    path('', views.test, name='test')

]
