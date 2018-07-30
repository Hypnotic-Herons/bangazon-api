from django.db import models
from safedelete.models import SafeDeleteModel

"""
Author: Matthew Kelly
"""


class Department(SafeDeleteModel):
	name = models.CharField(max_length=100)
	budget = models.CharField(max_length=100)

	class Meta:
		db_table = "department"

	def __str__(self):
		return self.name