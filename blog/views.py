
from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import BasicAuthentication
from .blog_permissions import IsAuthorOrReadOnly
from .models import Post
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class BlogPagination(PageNumberPagination):
    page_size = 5


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsAuthenticated]
    # pagination_class = BlogPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title']


class BlogList(APIView):
    pass


class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
