# Author: Deanna Vickers


from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

class ProductType(SafeDeleteModel):
	_safedelete_policy = SOFT_DELETE_CASCADE

	category = models.CharField(max_length=100, default="")
	class Meta:
		db_table = "product_type"

	def __str__(self):
		return self.category