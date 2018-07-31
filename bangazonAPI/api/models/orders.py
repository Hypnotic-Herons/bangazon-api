from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from .customer import Customer
from .payment_type import PaymentType


class Order(SafeDeleteModel):
	'''
	Author: Meghan Debity
	Purpose: Model for Order Table
	'''
	_safedelete_policy = SOFT_DELETE_CASCADE
	order_complete = models.BooleanField(default=False)
	customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
	payment_id = models.ForeignKey('PaymentType', on_delete=models.CASCADE)

	class Meta:
		db_table = "order"
