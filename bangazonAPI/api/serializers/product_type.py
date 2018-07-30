# Author: Deanna Vickers
# Setting up the serializer for product type

from rest_framework import serializers
from api.models import ProductType

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer for Product Types"""
	class Meta:
		model = ProductType
		fields = "__all__"