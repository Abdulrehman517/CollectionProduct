# Generated by Django 3.2.5 on 2021-07-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0011_auto_20210713_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='collection', to='collection.Product'),
        ),
    ]
