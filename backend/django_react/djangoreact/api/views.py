from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ArticlesSerializer
from djangoreact.models import Articles

class ArticlesListView(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class=ArticlesSerializer


class ArticlesDetailView(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class=ArticlesSerializer
