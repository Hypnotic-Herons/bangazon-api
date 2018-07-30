from rest_framework import serializers
from api.models import Employee
'''
Author: Levi Schubert
'''


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'url', 'first_name', 'last_name', 'supervisor', 'department')

