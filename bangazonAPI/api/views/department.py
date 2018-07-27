from rest_framework import viewsets
from api.models import Department
from api.serializers import DepartmentSerializer

'''
Author: Matthew Kelly
'''


class DepartmentViewSet(viewsets.ModelViewSet):
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer
	http_method_names = ['get', 'put', 'post']
