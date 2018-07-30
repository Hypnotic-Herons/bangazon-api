from rest_framework import serializers
from api.models import EmployeeTraining

"""
Author: Matthew Kelly
"""


class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = EmployeeTraining
		fields = ('id', 'url', 'training_id', 'employee_id')

