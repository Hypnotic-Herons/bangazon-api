from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from .product_type import ProductType
from .customer import Customer


class Product(SafeDeleteModel):
	'''Model for the product table has FK to customer and product_type
	Author: Levi Schubert
	'''
	_safedelete_policy = SOFT_DELETE_CASCADE

	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	price = models.FloatField()
	seller = models.ForeignKey('Customer', on_delete=models.CASCADE)
	type = models.ForeignKey('ProductType', on_delete=models.CASCADE)

	class meta:
		db_table = "product"

	def __str__(self):
		return (f'{self.title}: {self.price}')
 