# Generated by Django 4.2.7 on 2023-11-16 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='pricate',
            new_name='price',
        ),
    ]
