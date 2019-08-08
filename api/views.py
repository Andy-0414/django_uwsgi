from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import PostSerializer,PeopleSerializer
from .models import Post,People

# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class PeopleView(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
