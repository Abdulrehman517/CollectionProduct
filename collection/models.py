from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    collection = models.ManyToManyField(Collection)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




