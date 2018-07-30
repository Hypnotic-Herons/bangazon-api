from rest_framework import serializers
from api.models import PaymentType 

'''
Author: Meghan Debity
'''

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = PaymentType
		fields = ('id', 'url', 'customer')