from rest_framework import viewsets
from api.models import Order
from api.serializers import OrderSerializer

'''
Author: Meghan Debity
'''


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	http_method_names = ['get', 'put', 'post', 'delete']