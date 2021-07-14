from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    products = models.ManyToManyField(Product, related_name="collection")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

