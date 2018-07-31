# Author: Deanna Vickers
# Setting up the serializer for product type

from rest_framework import serializers
from api.models import ProductOrderJoin

class ProductOrderJoinSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer for Products and Orders relationships"""
	class Meta:
		model = ProductOderJoin
		fields = ('id', 'url', 'product_id', 'order_id')