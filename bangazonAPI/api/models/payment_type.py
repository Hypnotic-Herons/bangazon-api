from django.db import models
from safedelete.models import SafeDeleteModel
from .customer import Customer
# from .orders import Order



'''
Author: Meghan Debity
'''

class Payment_Type(SafeDeleteModel):
	payment_type = models.CharField(max_length=100)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

	class Meta:
		db_table = "payment type"