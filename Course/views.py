from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
class CourseViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Catagory__name']