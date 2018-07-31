# Author: Deanna Vickers

from rest_framework import serializers
from api.models import ProductOrderJoin

class ProductOrderJoinSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer for Products and Orders relationships"""
	class Meta:
		model = ProductOrderJoin
		fields = ('id', 'url', 'product_id', 'order_id')