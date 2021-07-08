from .models import Product,Collection
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer, CollectionSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer