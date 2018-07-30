from rest_framework import viewsets
from api.models import Customer
from api.serializers import CustomerSerializer



class CustomerViewSet(viewsets.ModelViewSet):
	'''Viewset for the Customer table, allows get, put, and post
	Author: Levi Schubert
	'''
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	http_method_names = ['get', 'put', 'post']	
	