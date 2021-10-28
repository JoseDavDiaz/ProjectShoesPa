from authApp.models.product import Products
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = ['brand', 'name', 'size']