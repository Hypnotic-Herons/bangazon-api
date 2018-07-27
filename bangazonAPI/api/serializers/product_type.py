# Author: Deanna Vickers


from rest_framework import serializers
from api.models import ProductType

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductType
		fields = "__all__"