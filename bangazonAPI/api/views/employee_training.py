from rest_framework import viewsets
from api.models import EmployeeTraining
from api.serializers import EmployeeTrainingSerializer

"""
Author: Matthew Kelly
"""


class EmployeeTrainingViewSet(viewsets.ModelViewSet):
	queryset = EmployeeTraining.objects.all()
	serializer_class = EmployeeTrainingSerializer
	http_method_names = ['get', 'put', 'post', 'delete']
