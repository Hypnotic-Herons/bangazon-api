from django.db import models
from .product import Product
from .order import Order
from safedelete.models import SafeDeleteModel



class ProductOrderJoin(SafeDeleteModel):
'''
Author: Deanna Vickers
Purpose: To connect products to orders.
'''
	product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
	order_id = models.ForeignKey('Order', on_delete=models.CASCADE)

	class Meta:
		db_table = "products_orders"

