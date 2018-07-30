from django.db import models
from safedelete.models import SafeDeleteModel
from .employee import Employee
from .training import Training

"""
Author: Matthew Kelly
"""

class EmployeeTraining(SafeDeleteModel):
	""" Model represents which Employees are in which Training """

	training_id = models.ForeignKey('Training', on_delete=models.CASCADE)
	employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)

	class Meta:
		db_table = "employee_training"

