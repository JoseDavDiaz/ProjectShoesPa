from django.conf import settings
from rest_framework                               import generics, serializers, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
from rest_framework_simplejwt.backends            import TokenBackend
from authApp.models.categories import Categories

from authApp.serializers.categoriesSerializer import CategoriesSerializer

class CategoriesCreateView (generics.RetrieveAPIView):
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializer
	permissions_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):
		token=request.META.get('HTTP_AUTHORIZATION')[7:]
		tokenBackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
		valid_data=tokenBackend.decode(token,verify=False)


		if valid_data['user_id'] != kwargs['user']:
		    stringResponse = {'detail':'Unauthorized Request'}
		    return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
		return super().get(request, *args, **kwargs)

class ProductCreateView(generics.CreateAPIView):
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializer
	permissions_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):
		token=request.META.get('HTTP_AUTHORIZATION')[7:]
		tokenBackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
		valid_data=tokenBackend.decode(token,verify=False)


		if valid_data['user_id'] != int (request.data['user_id']):
			Stringresponse = {'detail': 'Unathorized request'}
			return Response(Stringresponse, status=status.HTTP_401_UNAUTHORIZED)

class ProductUpdateView():
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializer
	permissions_classes = (IsAuthenticated,)

	def put(self, request, *args, **kwargs):
		token=request.META.get('HTTP_AUTHORIZATION')[7:]
		tokenBackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
		valid_data=tokenBackend.decode(token,verify=False)


		if valid_data['user_id'] != int (request.data['user_id']):
			Stringresponse = {'detail': 'Unathorized request'}
			return Response(Stringresponse, status=status.HTTP_401_UNAUTHORIZED)
		return super().update(request, *args, **kwargs)


	

class ProductDeleteView(generics.DestroyAPIView):
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializer
	permissions_classes = (IsAuthenticated,)

	def delete(self, request, *args, **kwargs):
		token=request.META.get('HTTP_AUTHORIZATION')[7:]
		tokenBackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
		valid_data=tokenBackend.decode(token,verify=False)


		if valid_data['user_id'] != int (request.data['user_id']):
			Stringresponse = {'detail': 'Unathorized request'}
			return Response(Stringresponse, status=status.HTTP_401_UNAUTHORIZED)
		return super().destroy(request, *args, **kwargs)