# Author: Deanna Vickers
from rest_framework import viewsets
from api.models import ProductOrderJoin
from api.serializers import ProductOrderJoinSerializer


class ProductOrderJoinViewSet(viewsets.ModelViewSet):
	"""View for the creation of products on orders"""
	queryset = ProductOrderJoin.objects.all()
	serializer_class = ProductOrderJoinSerializer
	http_method_names = ['get', 'post', 'delete']
