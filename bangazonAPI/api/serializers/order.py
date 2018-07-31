from rest_framework import serializers
from api.models import Order 



class OrderSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Author: Meghan Debity
	Purpose: Serializer for Order table
	'''

	class Meta:
		model = Order
		fields = ('id', 'url', 'products_on_order', 'customer_id', 'payment_id')