from rest_framework import viewsets
from api.models import Customer
from api.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer = CustomerSerializer
	http_methods = ['get', 'put', 'post']	
	