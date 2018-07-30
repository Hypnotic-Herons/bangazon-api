from rest_framework import viewsets
from api.models import Product
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
	'''viewset for products, allows get, post, put, and delete
	Author: Levi Schubert
	'''

	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	http_method_names = ['get', 'post', 'put', 'delete']