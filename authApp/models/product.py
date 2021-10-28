from django.db import models

class Products (models.Model):
	id = models.AutoField(primary_key=True)
	brand = models.CharField('Shoe-Brand', max_length=200)
	name = models.CharField('Name', max_length=100)
	size = models.FloatField('Size', max_length=30)
	