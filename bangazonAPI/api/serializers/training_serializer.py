from rest_framework import serializers
from api.models import Training
"""
Author: Matthew Kelly
"""

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Training
		fields = '__all__'


