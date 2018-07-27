# Author: Deanna Vickers

from rest_framework import viewsets
from api.models import ProductType
from api.serializers import ProductTypeSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    http_method_names = ['get', 'put', 'post', 'delete']