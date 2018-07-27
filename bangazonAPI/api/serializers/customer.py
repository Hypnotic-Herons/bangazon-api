from rest_framework import serializers
from api.models.customer import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ('id', 'first_name', 'last_name', 'date_joined', 'last_login')

	def create(self, validated_data):
		'''
			Create and return a Customer instance given validated data
		'''
		return Customer.objects.create(**validated_data)

	def update(self, instance, validated_data):
		'''
			Updates and returns a new Customer instance given the validated data
		'''
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.date_joined = validated_data.get('date_joined', instance.date_joined)
		instance.last_login = validated_data.get('last_login', instance.last_login)
		instance.save()
		return instance