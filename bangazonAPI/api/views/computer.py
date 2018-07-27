# Author: Deanna Vickers

from rest_framework import viewsets
from api.models import Computer
from api.serializers import ComputerSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    http_method_names = ['get', 'put', 'post', 'delete']