from authApp.models.product import Products
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = ['brand', 'name', 'size']
	
	def to_representation(self, obj):
		products = Products.objects.get(id = obj.id)
		return {
			'id'	:	products.id,
			'brand'	:	products.brand,
			'name'	:	products.name,
			'size'	:	products.size,
		}

	
