from rest_framework import viewsets
from api.models import Employee
from api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
	'''Viewset for the employee table, allows get, put, and post
	Author: Levi Schubert
	'''
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	http_method_names = ['get', 'put', 'post']	
	