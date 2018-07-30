from django.db import models
from safedelete.models import SafeDeleteModel
'''
Author: Levi Schubert
'''

class Customer(SafeDeleteModel):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	# date_joined & last_login should be a UNIX timestamp as a string
	date_joined = models.CharField(max_length=100)
	last_login = models.CharField(max_length=100)

	class Meta:
		db_table = "customers"

	def __str__(self):
		return (f'{self.first_name} {self.last_name}')