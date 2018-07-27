from django.db import models
from safedelete.models import SafeDeleteModel

"""
Author: Matthew Kelly
"""


class Training(SafeDeleteModel):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	# date_joined & last_login should be a UNIX timestamp as a string
	start_date = models.CharField(max_length=100)
	end_date = models.CharField(max_length=100)
	max_students = models.CharField(max_length=100)
	class Meta:
		db_table = "training"

	def __str__(self):
		return self.title