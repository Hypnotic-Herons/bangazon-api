from rest_framework import serializers
from api.models import Order
from .product import ProductSerializer



class OrderSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Author: Meghan Debity
	Purpose: Serializer for Order table
	'''

	products = ProductSerializer(many=True, read_only=True)

	class Meta:
		model = Order
		fields = ('id', 'url', 'customer_id', 'payment_id', 'products')