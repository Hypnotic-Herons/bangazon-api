from rest_framework import serializers
from api.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	'''Serializer for the Customer table
	Author: Levi Schubert
	'''
	class Meta:
		model = Customer
		fields = '__all__'

