# Author: Deanna Vickers


from django.db import models

class ProductType(models.Model):
	category = models.CharField(max_length=100, default="")
	class Meta:
		db_table = "product_type"

	def __str__(self):
		return self.category