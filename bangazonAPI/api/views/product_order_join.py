from rest_framework import viewsets
from api.models import ProductOrderJoin
from api.serializers import ProductOrderJoinSerializer

"""
Author: Deanna Vickers
"""


class ProductOrderJoinViewSet(viewsets.ModelViewSet):
	queryset = ProductOrderJoin.objects.all()
	serializer_class = ProductOrderJoinSerializer
	http_method_names = ['get', 'post', 'delete']
