# Author: Deanna Vickers


from django.db import models

class ProductType(models.Model):
	"""Define Product Type table."""
	category = models.CharField(max_length=100, default="")
	class Meta:
		db_table = "product_type"