from authApp.models.categories import Categories
from rest_framework import serializers

from authApp.models.product import Products

class CategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categories
		fields = ['model', 'gender', 'shoes']

	def to_representation(self, obj):
		categories	=	Categories.objects.get(id = obj.id)
		shoes 		=	Products.objects.get(id = categories.products_id)
		return {
			'id'	:	categories.id,
			'model'	:	categories.model,
			'gender':	categories.gender,
			shoes : {	
				'id' : shoes.id,
				'brand' : shoes.brand,
			}
		}