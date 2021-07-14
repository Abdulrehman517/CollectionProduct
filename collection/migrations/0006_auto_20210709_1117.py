# Generated by Django 3.2.5 on 2021-07-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_remove_collection_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(related_name='collection', to='collection.Product'),
        ),
    ]
