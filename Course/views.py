from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
class CourseViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Catagory__name']

class CourseDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Course.objects.get(pk=pk)
        except models.Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = serializers.CourseSerializer(flower)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = serializers.CourseSerializer(flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flower = self.get_object(pk)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)