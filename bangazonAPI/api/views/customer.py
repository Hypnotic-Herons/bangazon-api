from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import CustomerSerializer


class CustomerView(viewsets.ModelViewSet):
	