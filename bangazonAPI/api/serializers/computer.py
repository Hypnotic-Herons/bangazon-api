# Author: Deanna Vickers
# Setting up the serializer for computer instances

from rest_framework import serializers
from api.models import Computer

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Computer
		fields = ('id', 'url', 'purchase_date', 'decommission_date', 'employeeID')