from .models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Collection
        fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'description', 'available', 'collection']

    def create(self, validated_data):
        collection = validated_data.pop('collection')
        product = Product.objects.create(**validated_data)
        for i in collection:
            Collection.objects.filter(id=i['id'])
            product.collection.add(i['id'])
            product.save()
        return product

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.available = validated_data.get('available', instance.available)

        collection_data = validated_data.pop('collection')
        for j in collection_data:
            Collection.objects.filter(id=j['id'])
            instance.collection.add(j['id'])
            instance.save()
        return instance





    # def create(self, validated_data):
    #     collection_data = validated_data.pop('collection')
    #     products = Product.objects.create(**validated_data)
    #     collection = []
    #     for i in collection_data:
    #         collection_id = validated_data.pop('id', None)
    #         collection = Collection.objects.get_or_create(id=collection_id, defaults=i)
    #         collection.append(collection)
    #     products.collection.add(*collection)
    #     return products

    # this is all for creating product data it is not accepting collection data



    # def create(self, validated_data):
    #     collection_data = validated_data.pop('collection')
    #     products = Product.objects.create(**validated_data)
    #     for i in collection_data:
    #         Collection.objects.create(**i, products=products)
    #     return products

    # def update(self, instance, validated_data):
    #
    #     collection = validated_data.pop('collection')
    #
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.available = validated_data.get('available', instance.available)
    #     instance.save()
    #     return instance

    # collections_with_same_product_instance = Collection.objects.filter(products=instance.pk).values_list('id', flat=True)
        # collections_id_pool = []
        # for collection in collection_list:
        #     if "id" in collection.keys():

        #         if Collection.objects.filter(id=collection['id'].exists()):
        #             collection_instance = Collection.objects.get(id=collection['id'])
        #             collection_instance.title = collection.get('title', collection_instance.title)
        #             collection_instance.save()
        #             collections_id_pool.append(collection_instance.id)
        #         else:
        #             continue
        #     else:
        #         collectionss_instance = Collection.objects.create(products=instance, **collection)
        #         collections_id_pool.append(collectionss_instance.id)
        # for collection_id in collections_with_same_product_instance:
        #     if collection_id not in collections_id_pool:
        #         Collection.objects.filter(pk=collection_id).delete()
        #
        # return instance
        #
        #
