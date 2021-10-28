from authApp.models.categories import Categories
from rest_framework import serializers

class CategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categories
		fields = ['model', 'gender', 'shoes']