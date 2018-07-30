from django.db import models
from safedelete.models import SafeDeleteModel
from .department import Department
'''
Author: Levi Schubert
'''

class Employee(SafeDeleteModel):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	supervisor = models.BooleanField(blank=True, default=False)
	department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)

	class Meta:
		db_table = "employees"