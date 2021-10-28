from django.db import models
from .product import Products

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

class Categories(models.Model):
	id = models.AutoField(primary_key=True)
	model = models.CharField("Model", max_length=100)
	gender = models.IntegerField("Gender", choices=GENDER_CHOICES)
	shoes = models.ForeignKey(Products, related_name="shoes", on_delete=models.CASCADE)

	