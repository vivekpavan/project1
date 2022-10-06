from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import apiSerializer,apiModel

class ApiViewSet(viewsets.ModelViewSet):
    
    queryset = apiModel.objects.all()
    serializer_class = apiSerializer