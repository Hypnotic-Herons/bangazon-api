from rest_framework import viewsets
from api.models import Employee
from api.serializers import EmployeeSerializer

'''
Author: Levi Schubert
'''


class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	http_method_names = ['get', 'put', 'post']	
	