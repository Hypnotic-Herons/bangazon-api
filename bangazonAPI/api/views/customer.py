from rest_framework import viewsets
from api.models import Customer
from api.serializers import CustomerSerializer

'''
Author: Levi Schubert
'''


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'put', 'post']
	