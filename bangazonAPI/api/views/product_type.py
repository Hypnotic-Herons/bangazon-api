# Author: Deanna Vickers

from rest_framework import viewsets
from api.models.product_type import ProductType
from api.serializers.product_type import ProductTypeSerializer


class ProductTypeView(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    http_method_names = ['get', 'put', 'post', 'delete']