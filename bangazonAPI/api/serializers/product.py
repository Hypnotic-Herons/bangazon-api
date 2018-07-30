from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	'''Serializer for products, has FK to product_type & customer
	Author: Levi Schubert
	'''
	class Meta:
		model = Product
		fields = ('id', 'url', 'title', 'description', 'price', 'seller', 'type')