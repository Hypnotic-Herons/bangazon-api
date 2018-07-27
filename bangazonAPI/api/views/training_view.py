from django.shortcuts import render
from rest_framework import viewsets
from api.models import Training
from api.serializers import TrainingSerializer

"""
Author: Matthew Kelly
"""

class TrainingView(viewsets.ModelViewSet):
	queryset = Training.objects.all()
	serializer_class = TrainingSerializer
	http_method_names = ['get', 'put', 'post', 'delete']