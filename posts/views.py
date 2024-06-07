from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
#view-level permission for 
from rest_framework import generics #for Creating the Logic for Api Endpoint view
from rest_framework import viewsets #for Creating the viewset for multiple views with the same Logic for Api Endpoint view
from rest_framework.permissions import IsAdminUser #for authorising the userdetail page so only admin has access
from .permissions import IsAuthorOrReadOnly #for creating the permissions for the API
from .models import Post
from .serializers import PostSerializer, UserSerializer

#Api Viewfor EndPoints 
""""
class PostList(generics.ListCreateAPIView):
    permission_classes=(IsAuthorOrReadOnly,)#Setpermission Explicit only admin can View Detail APi Endpoint 
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)#Setpermission Explicit only admin can View Detail APi Endpoint 
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class UserList(generics.ListCreateAPIView):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer

"""



class PostViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
