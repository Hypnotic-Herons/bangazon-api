# Author: Deanna Vickers
# Defining the table structure for product type

from safedelete.models import SafeDeleteModel
from django.db import models


class ProductType(SafeDeleteModel):
	"""Define Product Type table."""

	category = models.CharField(max_length=100, default="")

	class Meta:
		db_table = "product_type"