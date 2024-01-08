from rest_framework import serializers
from rest_framework.fields import EmailField
from rest_framework.validators import UniqueValidator

from .models import People

class PeopleSerializer(serializers.ModelSerializer):
	"""
	People serializer to accept and validate emails to be saved.
	"""
	
	email = EmailField(required=True, validators=[
		UniqueValidator(queryset=People.objects.all(), message="This email already exists")])
	
	class Meta:
		model = People
		fields = (
			'email',
			'date_created'
		)
