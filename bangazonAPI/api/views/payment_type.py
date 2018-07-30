from rest_framework import viewsets
from api.models import PaymentType
from api.serializers import PaymentTypeSerializer

'''
Author: Meghan Debity
'''

class PaymentTypeViewSet(viewsets.ModelViewSet):
	queryset = PaymentType.objects.all()
	serializer_class = PaymentTypeSerializer
	http_method_names = ['get', 'post', 'put', 'delete']
