# Generated by Django 4.2.7 on 2023-11-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='onSale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='salePercentAsDeci',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=4),
            preserve_default=False,
        ),
    ]
