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
	
	def get_queryset(self):
		queryset = Customer.objects.all()
		active = self.request.GET.get('active')
		active = active.title() # DO NOT REMOVE THIS LINE! django defaults the query to a lowercase true/false which raises an assertion error
		if active:
			queryset = queryset.filter(active=active)

		return queryset