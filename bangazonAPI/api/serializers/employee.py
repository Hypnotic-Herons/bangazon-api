from rest_framework import serializers
from api.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	'''Serializer for the Employee table, has FK to department
	Author: Levi Schubert
	'''
	class Meta:
		model = Employee
		fields = ('id', 'url', 'first_name', 'last_name', 'supervisor', 'department')

