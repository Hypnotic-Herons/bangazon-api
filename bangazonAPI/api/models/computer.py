# Author: Deanna Vickers
# Defining the table structure for product type

from safedelete.models import SafeDeleteModel
from django.db import models

class Computer(SafeDeleteModel):
	"""Define the table for computers - each person has one computer.
    """
	purchase_date = models.CharField(max_length=100)
	ValidationError: ['This field is required.']
	decommission_date = models.CharField(max_length=100, default="")
	employeeID = models.ForeignKey('Employee', on_delete=models.CASCADE)

	class Meta:
		db_table = "computers"