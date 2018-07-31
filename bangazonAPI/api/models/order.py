from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from .customer import Customer
from .product import Product
from .payment_type import PaymentType
# from .product_order_join import ProductOrderJoin



class Order(SafeDeleteModel):
	'''
	Author: Meghan Debity
	Purpose: Model for Order Table
	'''
	_safedelete_policy = SOFT_DELETE_CASCADE
	customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
	payment_id = models.ForeignKey('PaymentType', on_delete=models.CASCADE, null=True)
	products = models.ManyToManyField(through='ProductOrderJoin', to='Product')

	class Meta:
		db_table = "order"
