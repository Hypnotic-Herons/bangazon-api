from django.db import models
from safedelete.models import SafeDeleteModel
from .customer import Customer



'''
Author: Meghan Debity
Purpose: To create and manage the payment type table in the database.
'''

class PaymentType(SafeDeleteModel):
	payment_type = models.CharField(max_length=100)
	account_number = models.CharField(max_length=100)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE)


	class Meta:
		db_table = "payment type"

	def __str__(self):
		return self.account_number