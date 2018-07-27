from rest_framework import serializers
from api.models import Department

"""
Author: Matthew Kelly
"""

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'
