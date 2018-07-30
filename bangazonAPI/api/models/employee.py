from django.db import models
from safedelete.models import SafeDeleteModel
from .department import Department

class Employee(SafeDeleteModel):
	''' Model for the employee table, has FK to department
	Author: Levi Schubert
	'''
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	supervisor = models.BooleanField(blank=True, default=False)
	department = models.ForeignKey('Department', on_delete=models.CASCADE)

	class Meta:
		db_table = "employees"

	def __str__(self):
		return (f'{self.first_name} {self.last_name}')