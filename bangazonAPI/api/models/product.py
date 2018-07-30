from django.db import models
from safedelete.models import SafeDeleteModel
from api import models

class Product(SafeDeleteModel):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	price = models.FloatField()
	seller = models.ForeignKey('customers', on_delete=models.CASCADE)
	type = 	department = models.ForeignKey('product_type', on_delete=models.CASCADE)

	class meta:
		db_table = "product"

	def __str__(self):
		return (f'{self.title}: {self.price}')
 