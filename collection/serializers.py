from .models import Product, Collection
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True, source="products")

    class Meta:
        model = Collection
        fields = ['id', 'name']
