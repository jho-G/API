from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    quesryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer



